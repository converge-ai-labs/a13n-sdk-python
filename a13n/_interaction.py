"""Bounded interaction helpers over generated Native resources."""

from __future__ import annotations

import asyncio
import math
from collections.abc import AsyncGenerator, Mapping
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Self, cast

from ._resources import Resource, Result
from .generated import models as wire
from .generated import resources as protocol
from .generated.types import UNSET, Unset

if TYPE_CHECKING:
    from .client import Client
    from .streaming import ThreadFrame

SEALED_STATUSES = frozenset({"completed", "failed", "cancelled", "waiting"})
SETTLED_ENTRIES = frozenset({"consumed", "failed", "withdrawn"})


def text_input(text: str) -> wire.MessagePayload:
    """Build a text part; other structured parts remain available on the wire model."""
    return wire.MessagePayload(content=[wire.TextPart(text=text, type_="text")])


def _payload(value: str | wire.MessagePayload) -> wire.MessagePayload:
    if isinstance(value, str):
        return text_input(value)
    if isinstance(value, wire.MessagePayload):
        return value
    raise ValueError("input must be text or MessagePayload")


@dataclass(frozen=True, repr=False)
class Submitted:
    """A submission may remain queued; only a non-null run was accepted."""

    thread: Thread
    entry: InboxEntry
    run: Run | None
    receipt: Result[wire.Submitted]

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

    async def wait(self, *, timeout: float = 300, poll_interval: float = 0.5) -> RunOutcome:
        """Wait for this Entry's incorporation and then its exact sealed Run."""
        from .errors import ProtocolError

        _validate_wait(timeout, poll_interval)
        async with asyncio.timeout(timeout):
            run = await self.incorporating_run(timeout=timeout, poll_interval=poll_interval)
            outcome = await run.wait(timeout=timeout, poll_interval=poll_interval)
            if outcome.snapshot.value.thread_id != self.thread.id:
                raise ProtocolError("Incorporating Run belongs to a different Thread")
            return outcome


class Interaction:
    """One submission's finite, run-scoped observations and authoritative result.

    Iteration is optional. Closing the local observation never interrupts the Run.
    """

    def __init__(self, submitted: Submitted) -> None:
        self._submitted = submitted
        self.thread = submitted.thread
        self.entry = submitted.entry
        self.run = submitted.run  # Immediate acceptance only; may be absent for a queued Entry.
        self.receipt = submitted.receipt
        self._entered = False
        self._closed = False
        self._reading = False
        self._deadline: float | None = None
        self._bound_run: Run | None = None
        self._bound_ready = asyncio.Event()
        self._wait_task: asyncio.Task[RunOutcome] | None = None
        self._read_task: asyncio.Future[ThreadFrame] | None = None
        self._frames: AsyncGenerator[ThreadFrame] | None = None
        self._outcome: RunOutcome | None = None

    def _start_observer(self, timeout: float, poll_interval: float) -> asyncio.Task[RunOutcome]:
        if self._closed:
            raise RuntimeError("Interaction observation closed before an outcome; read the exact Run explicitly")
        if self._wait_task is None:
            self._deadline = asyncio.get_running_loop().time() + timeout
            self._wait_task = asyncio.create_task(self._observe(poll_interval))
        return self._wait_task

    async def _observe(self, poll_interval: float) -> RunOutcome:
        from .errors import ProtocolError

        assert self._deadline is not None
        try:
            async with asyncio.timeout_at(self._deadline):
                run = await self._submitted.incorporating_run(poll_interval=poll_interval)
                self._bound_run = run
                self._bound_ready.set()
                outcome = await run.wait(poll_interval=poll_interval)
                if outcome.snapshot.value.thread_id != self.thread.id:
                    raise ProtocolError("Incorporating Run belongs to a different Thread")
                return outcome
        finally:
            self._bound_ready.set()  # Also wake context entry on failure/cancellation.

    async def result(self, *, timeout: float = 300, poll_interval: float = 0.5) -> RunOutcome:
        """Share this Interaction's one owned observer; no SSE is opened."""
        _validate_wait(timeout, poll_interval)
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
        task = self._start_observer(300, 0.5)
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
        assert self._bound_run is not None
        from .streaming import ThreadStream

        async with ThreadStream(self.thread) as stream:
            async for frame in stream:
                # Thread SSE is shared by Runs. Never label another Run's output as ours.
                if frame.event_type != "changed" and frame.data["run_id"] == self._bound_run.id:
                    yield frame

    def __aiter__(self) -> Self:
        return self

    async def __anext__(self) -> ThreadFrame:
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
    snapshot: Result[wire.RunView]

    @property
    def status(self) -> wire.RunStatus:
        return self.snapshot.value.status

    @property
    def output(self) -> object:
        return self.snapshot.value.output

    @property
    def pending(self) -> wire.Pending | None:
        return self.snapshot.value.pending

    @property
    def failure(self) -> wire.Failure | None:
        return self.snapshot.value.failure


@dataclass(frozen=True, repr=False)
class Resumed:
    run: Run
    receipt: Result[wire.RunView]


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


class AgentMethods(Resource):
    async def start(
        self,
        input: str | wire.MessagePayload,
        *,
        idempotency_key: str,
        agent_revision_id: str | Unset | None = UNSET,
        session_id: str | Unset | None = UNSET,
        delivery: wire.Delivery | Unset = UNSET,
        options: wire.RunOptionsInput | Unset = UNSET,
        environments: list[wire.MountCreate] | Unset = UNSET,
        memories: list[wire.MemoryMount] | Unset = UNSET,
        mcp_headers: wire.McpHeaders | Unset = UNSET,
        message_history: list[dict[str, Any]] | Unset = UNSET,
    ) -> Interaction:
        """Create a finite interaction with this Agent; import native model history only here."""
        history: list[wire.MessageHistoryItem] | Unset = UNSET
        if not isinstance(message_history, Unset):
            history = [wire.MessageHistoryItem.from_dict(item) for item in message_history]
        body = wire.NewThread(
            agent_id=self.id,
            payload=_payload(input),
            agent_revision_id=agent_revision_id,
            session_id=session_id,
            delivery=delivery,
            options=options,
            environments=environments,
            memories=memories,
            mcp_headers=mcp_headers,
            message_history=history,
        )
        client = cast("Agent", self).client
        receipt = await client.resources.threads.create(body=body, idempotency_key=idempotency_key)
        return Interaction(_submitted(client, receipt))

    async def send(
        self,
        thread_id: str,
        input: str | wire.MessagePayload,
        *,
        idempotency_key: str,
        agent_revision_id: str | Unset | None = UNSET,
        delivery: wire.Delivery | Unset = UNSET,
        options: wire.RunOptionsInput | Unset = UNSET,
    ) -> Interaction:
        """Submit one Message as this Agent to an explicitly named Thread."""
        body = wire.Message(
            agent_id=self.id,
            payload=_payload(input),
            agent_revision_id=agent_revision_id,
            delivery=delivery,
            options=options,
        )
        client = cast("Agent", self).client
        receipt = await client.resources.threads(thread_id).inbox_entries.create(
            body=body, idempotency_key=idempotency_key
        )
        return Interaction(_submitted(client, receipt, thread_id=thread_id))


class RunMethods(Resource):
    async def wait(self, *, timeout: float = 300, poll_interval: float = 0.5) -> RunOutcome:
        from .errors import ProtocolError

        _validate_wait(timeout, poll_interval)
        async with asyncio.timeout(timeout):
            while True:
                result = await cast("Run", self).get()
                if result.value.id != self.id:
                    raise ProtocolError("Run readback has inconsistent identity")
                if result.value.status in SEALED_STATUSES:
                    return RunOutcome(cast("Run", self), result)
                await asyncio.sleep(poll_interval)

    async def resume(
        self,
        *,
        approvals: Mapping[str, wire.Approve | wire.Deny],
        calls: Mapping[str, wire.Returned | wire.Failed],
        idempotency_key: str,
        input: str | wire.MessagePayload | Unset = UNSET,
    ) -> Resumed:
        """Submit a complete wait-result batch and optional input as one immutable intent."""
        from .errors import ProtocolError

        body = wire.Resume(approvals=wire.ResumeApprovals(), calls=wire.ResumeCalls())
        body.approvals.additional_properties = dict(approvals)
        body.calls.additional_properties = dict(calls)
        if not isinstance(input, Unset):
            body.input_ = _payload(input)
        receipt = await self._client.resources.runs(self.id).resume(body=body, idempotency_key=idempotency_key)
        value = receipt.value
        if not value.id or value.id == self.id or not value.workspace_id:
            raise ProtocolError("Resume did not return a new run with a workspace identity")
        return Resumed(Run(self._client, {"run_id": value.id}), receipt)

    async def fork(self, *, body: wire.Fork, idempotency_key: str) -> Submitted:
        receipt = await self._client.resources.runs(self.id).fork(body=body, idempotency_key=idempotency_key)
        return _submitted(self._client, receipt)


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
    """An Agent selection; management remains on client.resources.agents."""


class Threads(Resource):
    def __call__(self, thread_id: str) -> Thread:
        return Thread(self._client, self._bind("thread_id", thread_id))


class Thread(Resource):
    """A continuing Thread identity, not a persistent high-level stream."""

    async def get(self) -> Result[wire.ThreadView]:
        return await self._client.resources.threads(self.id).get()


class Runs(Resource):
    def __call__(self, run_id: str) -> Run:
        return Run(self._client, self._bind("run_id", run_id))


class Run(RunMethods):
    """One exact Run; advanced resources remain available at client.resources.runs."""

    async def get(self) -> Result[wire.RunView]:
        return await self._client.resources.runs(self.id).get()

    @property
    def items(self) -> protocol.RunsRunIdItems:
        return self._client.resources.runs(self.id).items

    async def interrupt(self) -> Result[wire.RunView]:
        return await self._client.resources.runs(self.id).interrupt()


class InboxEntry(InboxEntryMethods):
    async def get(self) -> Result[wire.EntryView]:
        return await self._client.resources.threads(self.selectors["thread_id"]).inbox_entries(self.id).get()
