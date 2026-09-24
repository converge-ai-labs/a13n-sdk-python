"""Bounded conveniences over explicit workspace-scoped Native resources."""

from __future__ import annotations

import asyncio
import math
from dataclasses import dataclass
from typing import TYPE_CHECKING, cast

from ._resources import Resource, Result
from .generated import models as wire
from .generated.types import UNSET, Unset

if TYPE_CHECKING:
    from .generated.resources import InboxEntry, Run, Thread
    from .streaming import ThreadStream

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


@dataclass(frozen=True, repr=False)
class Resumed:
    run: Run
    receipt: Result[wire.RunView]


def _submitted(client: object, workspace_id: str, receipt: Result[wire.Submitted]) -> Submitted:
    from .client import Client, ProtocolError
    from .generated.resources import InboxEntry, Run, Thread

    assert isinstance(client, Client)
    value = receipt.value
    thread, entry, run = value.thread, value.entry, value.run
    if not thread.id or not entry.id or entry.thread_id != thread.id or thread.workspace_id != workspace_id:
        raise ProtocolError("Submission has inconsistent thread and entry identities")
    if run is not None and (not run.id or run.thread_id != thread.id or run.workspace_id != workspace_id):
        raise ProtocolError("Submission has inconsistent run identity")
    selectors = {"workspace_id": workspace_id, "thread_id": thread.id}
    return Submitted(
        Thread(client, selectors),
        InboxEntry(client, {**selectors, "entry_id": entry.id}),
        Run(client, {"workspace_id": workspace_id, "run_id": run.id}) if run is not None else None,
        receipt,
    )


def _validate_wait(timeout: float, poll_interval: float) -> None:
    if not math.isfinite(timeout) or timeout <= 0:
        raise ValueError("timeout must be a finite positive number")
    if not math.isfinite(poll_interval) or poll_interval <= 0:
        raise ValueError("poll_interval must be a finite positive number")


class WorkspaceMethods(Resource):
    async def start(
        self,
        input: str | wire.MessagePayload,
        *,
        agent_id: str,
        idempotency_key: str,
        agent_revision_id: str | Unset | None = UNSET,
        session_id: str | Unset | None = UNSET,
        delivery: wire.Delivery | Unset = UNSET,
        options: wire.RunOptionsInput | Unset = UNSET,
    ) -> Submitted:
        body = wire.NewThread(
            agent_id=agent_id,
            payload=_payload(input),
            agent_revision_id=agent_revision_id,
            session_id=session_id,
            delivery=delivery,
            options=options,
        )
        return _submitted(
            self._client,
            self._bindings["workspace_id"],
            await self.threads.create(body=body, idempotency_key=idempotency_key),  # type: ignore[attr-defined]
        )


class ThreadMethods(Resource):
    async def submit(
        self,
        input: str | wire.MessagePayload,
        *,
        agent_id: str,
        idempotency_key: str,
        agent_revision_id: str | Unset | None = UNSET,
        delivery: wire.Delivery | Unset = UNSET,
        options: wire.RunOptionsInput | Unset = UNSET,
    ) -> Submitted:
        body = wire.Message(
            agent_id=agent_id,
            payload=_payload(input),
            agent_revision_id=agent_revision_id,
            delivery=delivery,
            options=options,
        )
        return _submitted(
            self._client,
            self._bindings["workspace_id"],
            await self.inbox_entries.create(body=body, idempotency_key=idempotency_key),  # type: ignore[attr-defined]
        )

    def stream(
        self,
        *,
        after: str | None = None,
        reconnect: bool = True,
        max_reconnects: int = 5,
        max_event_bytes: int = 1_048_576,
    ) -> ThreadStream:
        from .streaming import ThreadStream

        return ThreadStream(
            cast("Thread", self),
            after=after,
            reconnect=reconnect,
            max_reconnects=max_reconnects,
            max_event_bytes=max_event_bytes,
        )


class RunMethods(Resource):
    async def wait(self, *, timeout: float, poll_interval: float) -> Result[wire.RunView]:
        _validate_wait(timeout, poll_interval)
        async with asyncio.timeout(timeout):
            while True:
                result = await self.get()  # type: ignore[attr-defined]
                if result.value.status in SEALED_STATUSES:
                    return result
                await asyncio.sleep(poll_interval)

    async def interrupt(self) -> Result[wire.RunView]:
        return await self.interrupt_receipt()  # type: ignore[attr-defined]

    async def resume(self, body: wire.ResumeRequest, *, idempotency_key: str) -> Resumed:
        from .client import ProtocolError
        from .generated.resources import Run

        receipt = await self.resume_receipt(body=body, idempotency_key=idempotency_key)  # type: ignore[attr-defined]
        value = receipt.value
        if not value.id or value.id == self.id or value.workspace_id != self._bindings["workspace_id"]:
            raise ProtocolError("Resume did not return a new run in this workspace")
        return Resumed(Run(self._client, {"workspace_id": value.workspace_id, "run_id": value.id}), receipt)

    async def fork(self, body: wire.Fork, *, idempotency_key: str) -> Submitted:
        return _submitted(
            self._client,
            self._bindings["workspace_id"],
            await self.fork_receipt(body=body, idempotency_key=idempotency_key),  # type: ignore[attr-defined]
        )


class InboxEntryMethods(Resource):
    async def wait(self, *, timeout: float, poll_interval: float) -> Result[wire.EntryView]:
        _validate_wait(timeout, poll_interval)
        async with asyncio.timeout(timeout):
            while True:
                snapshot = await self.get()  # type: ignore[attr-defined]
                if snapshot.value.status in SETTLED_ENTRIES:
                    return snapshot
                await asyncio.sleep(poll_interval)
