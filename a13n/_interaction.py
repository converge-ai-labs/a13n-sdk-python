"""Bounded interaction helpers over generated Native resources."""

from __future__ import annotations

import asyncio
import math
from collections.abc import AsyncGenerator, Mapping
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Self, cast
from uuid import uuid4

from pydantic import JsonValue

from ._resources import Resource, Result
from ._submission import mutation
from ._values import (
    Answer,
    Approve,
    Deny,
    Failed,
    Failure,
    Input,
    MemoryMount,
    MountCreate,
    Pending,
    Returned,
    RunOptions,
    payload,
)
from .errors import PreviewInterrupted, ProtocolError
from .generated import models as wire
from .generated import resources as protocol
from .generated.types import UNSET, Unset

if TYPE_CHECKING:
    from .client import Client
    from .streaming import ThreadFrame

SEALED_STATUSES = frozenset({"completed", "failed", "cancelled", "waiting"})
SETTLED_ENTRIES = frozenset({"consumed", "failed", "withdrawn"})


@dataclass(frozen=True, repr=False)
class Submitted:
    """A submission may remain queued; only a non-null run was accepted."""

    thread: Thread
    entry: InboxEntry
    run: Run | None
    receipt: Result[wire.Submitted] | None

    async def incorporating_run(self, *, timeout: float = 300, poll_interval: float = 0.5) -> Run:
        """Resolve the exact Run only after this Entry was incorporated."""
        from .errors import ProtocolError, SubmissionError

        entry = await self.entry.wait(timeout=timeout, poll_interval=poll_interval)
        if entry.value.thread_id != self.thread.id or entry.value.id != self.entry.id:
            raise ProtocolError("Entry readback has inconsistent identity")
        if entry.value.status != wire.EntryStatus.CONSUMED:
            raise SubmissionError(self.thread.id, self.entry.id, entry)
        run_id = entry.value.assigned_run_id
        if not run_id:
            raise ProtocolError("Consumed Entry has no assigned Run")
        return Run(self.thread.client, {"run_id": run_id})


class Interaction:
    """One submission's finite, run-scoped observations and authoritative result.

    Iteration is optional. Closing the local observation never interrupts the Run.
    """

    def __init__(
        self,
        origin: Submitted | Run,
        *,
        thread: Thread | None = None,
        receipt: Result[wire.RunView] | None = None,
        idempotency_key: str | None = None,
        timeout: float = 300,
        poll_interval: float = 0.5,
    ) -> None:
        _validate_wait(timeout, poll_interval)
        self._submitted = origin if isinstance(origin, Submitted) else None
        self.thread = origin.thread if isinstance(origin, Submitted) else thread
        self.entry = origin.entry if isinstance(origin, Submitted) else None
        self.run = None if isinstance(origin, Submitted) else origin
        self.receipt = origin.receipt if isinstance(origin, Submitted) else receipt
        self.idempotency_key = idempotency_key
        self.provenance = (
            "recovered_entry"
            if isinstance(origin, Submitted) and origin.receipt is None
            else "submitted"
            if isinstance(origin, Submitted)
            else "resumed"
            if receipt is not None
            else "exact_run"
        )
        self._timeout = timeout
        self._poll_interval = poll_interval
        self._previewing = False
        self._preview_started = False
        self._preview_error: PreviewInterrupted | None = None
        self._entered = False
        self._closed = False
        self._reading = False
        self._deadline: float | None = None
        self._bound_run: Run | None = self.run
        self._bound_ready = asyncio.Event()
        self._wait_task: asyncio.Task[RunOutcome] | None = None
        self._read_task: asyncio.Future[ThreadFrame] | None = None
        self._frames: AsyncGenerator[ThreadFrame] | None = None
        self._outcome: RunOutcome | None = None

    def _start_observer(self, timeout: float | None, poll_interval: float | None) -> asyncio.Task[RunOutcome]:
        if self._closed:
            raise RuntimeError("Interaction observation closed before an outcome; read the exact Run explicitly")
        if self._wait_task is None:
            self._deadline = asyncio.get_running_loop().time() + (self._timeout if timeout is None else timeout)
            self._wait_task = asyncio.create_task(
                self._observe(self._poll_interval if poll_interval is None else poll_interval)
            )
        return self._wait_task

    async def _observe(self, poll_interval: float) -> RunOutcome:
        from .errors import ProtocolError

        assert self._deadline is not None
        try:
            async with asyncio.timeout_at(self._deadline):
                if self._submitted is not None:
                    run = await self._submitted.incorporating_run(
                        timeout=max(self._deadline - asyncio.get_running_loop().time(), 0.000001),
                        poll_interval=poll_interval,
                    )
                    self.run = self._bound_run = run
                    self._bound_ready.set()
                assert self._bound_run is not None
                while True:
                    evidence = await self._bound_run.get()
                    value = evidence.value
                    if value.id != self._bound_run.id or not value.thread_id or not value.workspace_id:
                        raise ProtocolError("Run readback has inconsistent identity")
                    if self.thread is not None and value.thread_id != self.thread.id:
                        raise ProtocolError("Observed Run belongs to a different Thread")
                    self.thread = Thread(self._bound_run.client, {"thread_id": value.thread_id})
                    self._bound_ready.set()
                    if value.status in SEALED_STATUSES:
                        return RunOutcome(self._bound_run, evidence)
                    await asyncio.sleep(poll_interval)
        finally:
            self._bound_ready.set()  # Also wake context entry on failure/cancellation.

    async def result(self, *, timeout: float | None = None, poll_interval: float | None = None) -> RunOutcome:
        """Share this Interaction's one owned observer; no SSE is opened."""
        _validate_wait(
            self._timeout if timeout is None else timeout,
            self._poll_interval if poll_interval is None else poll_interval,
        )
        if self._outcome is not None:
            return self._outcome
        task = self._start_observer(timeout, poll_interval)
        assert self._deadline is not None
        try:
            async with asyncio.timeout_at(self._deadline):
                outcome = await asyncio.shield(task)
        except (TimeoutError, asyncio.CancelledError):
            await self.aclose()
            raise
        self._outcome = outcome
        return outcome

    async def __aenter__(self) -> Self:
        if self._closed:
            raise RuntimeError("Interaction is closed")
        if self._entered:
            raise RuntimeError("Interaction is single-use")
        self._entered = True
        if self._outcome is not None:
            return self
        task = self._start_observer(None, None)
        assert self._deadline is not None
        try:
            async with asyncio.timeout_at(self._deadline):
                await self._bound_ready.wait()
                if task.done():
                    self._outcome = task.result()
                elif self._bound_run is None:
                    raise RuntimeError("Interaction did not bind an incorporating Run")
        except BaseException:
            await self.aclose()
            raise
        return self

    async def _run_frames(self) -> AsyncGenerator[ThreadFrame]:
        assert self._bound_run is not None and self.thread is not None
        from .streaming import ThreadStream

        async with ThreadStream(self.thread) as stream:
            async for frame in stream:
                # Thread SSE is shared by Runs. Never label another Run's output as ours.
                if frame.event_type != "changed" and frame.data["run_id"] == self._bound_run.id:
                    yield frame

    def __aiter__(self) -> Self:
        return self

    async def __anext__(self) -> ThreadFrame:
        if self._previewing:
            raise RuntimeError("Interaction supports one active raw or text reader")
        return await self._next_frame()

    async def _next_frame(self) -> ThreadFrame:
        if not self._entered:
            raise RuntimeError("Enter the Interaction context before iterating")
        if self._closed:
            raise StopAsyncIteration
        if self._reading:
            raise RuntimeError("Interaction supports one active reader")
        if self._outcome is not None:
            raise StopAsyncIteration
        self._reading = True
        try:
            assert self._wait_task is not None and self._deadline is not None
            if self._wait_task.done():
                self._outcome = self._wait_task.result()
                raise StopAsyncIteration
            if self._frames is None:
                self._frames = self._run_frames()
            self._read_task = asyncio.ensure_future(anext(self._frames))
            async with asyncio.timeout_at(self._deadline):
                done, _ = await asyncio.wait({self._read_task, self._wait_task}, return_when=asyncio.FIRST_COMPLETED)
            if self._wait_task in done:
                self._outcome = self._wait_task.result()
                await self._stop_reader()
                raise StopAsyncIteration
            try:
                return self._read_task.result()
            except StopAsyncIteration:
                # SSE ending does not imply the Run sealed, and must not spin/reconnect here.
                self._outcome = await self._wait_task
                raise StopAsyncIteration from None
        except BaseException:
            await self._stop_reader()
            raise
        finally:
            self._reading = False

    async def text_stream(self) -> AsyncGenerator[str]:
        """Yield provisional root assistant chunks; use the context to own cleanup."""
        if self._preview_error is not None:
            raise self._preview_error
        if self._preview_started or self._reading:
            raise RuntimeError("Interaction supports one preview consumer and no concurrent raw reader")
        from ._preview import TextPreview

        if not self._entered or self._bound_run is None:
            raise RuntimeError("Enter the Interaction context before previewing")
        self._preview_started = self._previewing = True
        projection = TextPreview(self._bound_run.id)
        try:
            while True:
                try:
                    frame = await self._next_frame()
                except StopAsyncIteration:
                    return
                chunk = projection.apply(frame)
                if chunk is not None:
                    yield chunk
        except PreviewInterrupted as error:
            self._preview_error = error
            raise
        except ProtocolError as cause:
            self._preview_error = PreviewInterrupted("protocol", self._bound_run.id)
            raise self._preview_error from cause
        finally:
            self._previewing = False

    async def _stop_reader(self) -> None:
        task, self._read_task = self._read_task, None
        if task is not None:
            if not task.done():
                task.cancel()
            await asyncio.gather(task, return_exceptions=True)
        frames, self._frames = self._frames, None
        if frames is not None:
            await frames.aclose()

    async def aclose(self) -> None:
        if self._closed:
            return
        self._closed = True
        await self._stop_reader()
        task, self._wait_task = self._wait_task, None
        if task is not None:
            if task.done() and not task.cancelled():
                try:
                    self._outcome = task.result()
                except Exception:
                    pass  # Result is reported when awaited; closing only releases local observation.
            else:
                task.cancel()
                await asyncio.gather(task, return_exceptions=True)

    async def __aexit__(self, *_args: object) -> None:
        await self.aclose()


@dataclass(frozen=True, repr=False)
class RunOutcome:
    """An exact sealed Run with retained structured output and HTTP evidence."""

    run: Run
    evidence: Result[wire.RunView]

    @property
    def status(self) -> wire.RunStatus:
        return self.evidence.value.status

    @property
    def output(self) -> JsonValue:
        return cast(JsonValue, self.evidence.value.output)

    @property
    def text(self) -> str | None:
        value = self.output
        return value if isinstance(value, str) else None

    @property
    def thread_id(self) -> str:
        return self.evidence.value.thread_id

    @property
    def run_id(self) -> str:
        return self.run.id

    @property
    def pending(self) -> Pending | None:
        value = self.evidence.value.pending
        return None if value is None else Pending.from_wire(value)

    @property
    def failure(self) -> Failure | None:
        value = self.evidence.value.failure
        return None if value is None else Failure(value.code, value.message)


def _submitted(client: Client, receipt: Result[wire.Submitted], *, thread_id: str | None = None) -> Submitted:
    from .errors import ProtocolError

    value = receipt.value
    thread, entry, run = value.thread, value.entry, value.run
    if (
        not thread.id
        or not entry.id
        or entry.thread_id != thread.id
        or not thread.workspace_id
        or (thread_id is not None and thread.id != thread_id)
    ):
        raise ProtocolError("Submission has inconsistent thread and entry identities")
    if run is not None and (not run.id or run.thread_id != thread.id or run.workspace_id != thread.workspace_id):
        raise ProtocolError("Submission has inconsistent run identity")
    return Submitted(
        Thread(client, {"thread_id": thread.id}),
        InboxEntry(client, {"thread_id": thread.id, "entry_id": entry.id}),
        Run(client, {"run_id": run.id}) if run is not None else None,
        receipt,
    )


def _validate_wait(timeout: float, poll_interval: float) -> None:
    if not math.isfinite(timeout) or timeout <= 0:
        raise ValueError("timeout must be a finite positive number")
    if not math.isfinite(poll_interval) or poll_interval <= 0:
        raise ValueError("poll_interval must be a finite positive number")


def _options(value: RunOptions | Unset) -> wire.RunOptionsInput | Unset:
    return value if isinstance(value, Unset) else value.into_wire()


def _mounts(values: list[MountCreate] | Unset) -> list[wire.MountCreate] | Unset:
    return values if isinstance(values, Unset) else [wire.MountCreate.from_dict(value.to_dict()) for value in values]


def _memories(values: list[MemoryMount] | Unset) -> list[wire.MemoryMount] | Unset:
    return values if isinstance(values, Unset) else [wire.MemoryMount.from_dict(value.to_dict()) for value in values]


def _key(value: str | None) -> str:
    if value is None:
        return str(uuid4())
    if not isinstance(value, str) or not value:
        raise ValueError("idempotency_key must be a nonblank string or None")
    return value


class AgentMethods(Resource):
    async def start(
        self,
        input: Input,
        *,
        idempotency_key: str | None = None,
        agent_revision_id: str | Unset | None = UNSET,
        session_id: str | Unset | None = UNSET,
        session: wire.SessionCreate | Unset | None = UNSET,
        execution: wire.ExecutionOverride | Unset | None = UNSET,
        delivery: wire.Delivery | Unset = UNSET,
        options: RunOptions | Unset = UNSET,
        environments: list[MountCreate] | Unset = UNSET,
        memories: list[MemoryMount] | Unset = UNSET,
        mcp_headers: Mapping[str, Mapping[str, str]] | Unset = UNSET,
        message_history: list[dict[str, Any]] | Unset = UNSET,
    ) -> Interaction:
        """Create one finite interaction. History is imported only for this new Thread."""
        body = wire.NewThread(
            agent_id=self.id,
            payload=payload(input),
            agent_revision_id=agent_revision_id,
            session_id=session_id,
            session=session,
            execution=execution,
            delivery=delivery,
            options=_options(options),
            environments=_mounts(environments),
            memories=_memories(memories),
            mcp_headers=mcp_headers if isinstance(mcp_headers, Unset) else wire.McpHeaders.from_dict(mcp_headers),
            message_history=message_history
            if isinstance(message_history, Unset)
            else [wire.MessageHistoryItem.from_dict(item) for item in message_history],
        )
        key = _key(idempotency_key)
        with mutation(key, "start") as attempt:
            receipt = await self.client.api.threads.create(body=body, idempotency_key=key)
            attempt.evidence = receipt
            return Interaction(_submitted(self.client, receipt), idempotency_key=key)

    async def send(
        self,
        thread_id: str,
        input: Input,
        *,
        idempotency_key: str | None = None,
        agent_revision_id: str | Unset | None = UNSET,
        delivery: wire.Delivery | Unset = UNSET,
        options: RunOptions | Unset = UNSET,
    ) -> Interaction:
        """Submit one Message as this Agent to an explicitly named Thread."""
        resource = self.client.api.threads(thread_id).inbox_entries
        body = wire.Message(
            agent_id=self.id,
            payload=payload(input),
            agent_revision_id=agent_revision_id,
            delivery=delivery,
            options=_options(options),
        )
        key = _key(idempotency_key)
        with mutation(key, "send", thread_id=thread_id) as attempt:
            receipt = await resource.create(body=body, idempotency_key=key)
            attempt.evidence = receipt
            return Interaction(_submitted(self.client, receipt, thread_id=thread_id), idempotency_key=key)


class RunMethods(Resource):
    def observe(self, *, timeout: float = 300, poll_interval: float = 0.5) -> Interaction:
        """Select an exact Run locally; its Thread is resolved by authoritative readback."""
        return Interaction(cast("Run", self), timeout=timeout, poll_interval=poll_interval)

    async def result(self, *, timeout: float = 300, poll_interval: float = 0.5) -> RunOutcome:
        async with self.observe(timeout=timeout, poll_interval=poll_interval) as interaction:
            return await interaction.result()

    async def resume(
        self,
        answers: Mapping[str, Answer],
        *,
        idempotency_key: str | None = None,
        input: Input | Unset | None = UNSET,
    ) -> Interaction:
        """Submit all answers and optional input atomically; observe the exact successor."""
        approvals: dict[str, Any] = {}
        calls: dict[str, Any] = {}
        for identifier, answer in answers.items():
            if isinstance(answer, (Approve, Deny)):
                approvals[identifier] = answer.to_dict()
            elif isinstance(answer, (Returned, Failed)):
                calls[identifier] = answer.to_dict()
            else:
                raise TypeError("resume answers must be Approve, Deny, Returned or Failed")
        intent: dict[str, Any] = {"approvals": approvals, "calls": calls}
        if not isinstance(input, Unset):
            intent["input"] = None if input is None else payload(input).to_dict()
        body = wire.Resume.from_dict(intent)
        key = _key(idempotency_key)
        with mutation(key, "resume", run_id=self.id) as attempt:
            receipt = await self.client.api.runs(self.id).resume(body=body, idempotency_key=key)
            attempt.evidence = receipt
            value = receipt.value
            if not value.id or value.id == self.id or not value.workspace_id or not value.thread_id:
                raise ProtocolError("Resume did not return a distinct Run with Thread and Workspace identities")
            return Interaction(
                Run(self.client, {"run_id": value.id}),
                thread=Thread(self.client, {"thread_id": value.thread_id}),
                receipt=receipt,
                idempotency_key=key,
            )

    async def fork(
        self,
        input: Input,
        *,
        agent_id: str,
        idempotency_key: str | None = None,
        agent_revision_id: str | Unset | None = UNSET,
        delivery: wire.Delivery | Unset = UNSET,
        options: RunOptions | Unset = UNSET,
        environments: list[MountCreate] | Unset = UNSET,
        memories: list[MemoryMount] | Unset = UNSET,
        fresh_environments: bool | Unset = UNSET,
    ) -> Interaction:
        body = wire.Fork(
            agent_id=agent_id,
            payload=payload(input),
            agent_revision_id=agent_revision_id,
            delivery=delivery,
            options=_options(options),
            environments=_mounts(environments),
            memories=_memories(memories),
            fresh_environments=fresh_environments,
        )
        key = _key(idempotency_key)
        with mutation(key, "fork", run_id=self.id) as attempt:
            receipt = await self.client.api.runs(self.id).fork(body=body, idempotency_key=key)
            attempt.evidence = receipt
            return Interaction(_submitted(self.client, receipt), idempotency_key=key)


class InboxEntryMethods(Resource):
    async def wait(self, *, timeout: float = 300, poll_interval: float = 0.5) -> Result[wire.EntryView]:
        _validate_wait(timeout, poll_interval)
        async with asyncio.timeout(timeout):
            while True:
                snapshot = await cast("InboxEntry", self).get()
                if snapshot.value.id != self.id or snapshot.value.thread_id != self.selectors["thread_id"]:
                    from .errors import ProtocolError

                    raise ProtocolError("Entry readback has inconsistent identity")
                if snapshot.value.status in SETTLED_ENTRIES:
                    return snapshot
                await asyncio.sleep(poll_interval)


class Agents(Resource):
    """Local Agent-ID binding for the authored finite interaction workflow."""

    def __call__(self, agent_id: str) -> Agent:
        return Agent(self._client, self._bind("agent_id", agent_id))


class Agent(AgentMethods):
    """An Agent selection; management remains on client.api.agents."""


class Threads(Resource):
    def __call__(self, thread_id: str) -> Thread:
        return Thread(self._client, self._bind("thread_id", thread_id))


class Thread(Resource):
    """A continuing Thread identity, not a persistent high-level stream."""

    def interaction(
        self,
        entry_id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float = 300,
        poll_interval: float = 0.5,
    ) -> Interaction:
        entry = InboxEntry(self.client, self._bind("entry_id", entry_id))
        return Interaction(
            Submitted(self, entry, None, None),
            idempotency_key=idempotency_key,
            timeout=timeout,
            poll_interval=poll_interval,
        )

    async def get(self) -> Result[wire.ThreadView]:
        return await self._client.api.threads(self.id).get()


class Runs(Resource):
    def __call__(self, run_id: str) -> Run:
        return Run(self._client, self._bind("run_id", run_id))


class Run(RunMethods):
    """One exact Run; advanced resources remain available at client.api.runs."""

    async def get(self) -> Result[wire.RunView]:
        return await self._client.api.runs(self.id).get()

    @property
    def items(self) -> protocol.RunsRunIdItems:
        return self._client.api.runs(self.id).items

    async def interrupt(self) -> Result[wire.RunView]:
        return await self._client.api.runs(self.id).interrupt()


class InboxEntry(InboxEntryMethods):
    async def get(self) -> Result[wire.EntryView]:
        return await self._client.api.threads(self.selectors["thread_id"]).inbox_entries(self.id).get()
