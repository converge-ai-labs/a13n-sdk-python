"""One fresh Native Session snapshot connection; reconnection is caller-owned."""

from __future__ import annotations

import asyncio
import json
from collections.abc import AsyncGenerator
from contextlib import aclosing
from dataclasses import dataclass, field
from functools import cache
from importlib.resources import files
from typing import Literal

import httpx2
from jsonschema import Draft202012Validator, ValidationError

from ._resources import Resource
from .errors import ProtocolError, TransportError
from .generated.api.runs import session_stream
from .generated.models import Delta, Gap, OccurrenceEvent, RunSnapshot, ScheduleEvent, ThreadState
from .streaming import _events, _StreamContext


@dataclass(frozen=True, repr=False)
class SessionThreadFrame:
    data: ThreadState
    event_type: Literal["thread"] = field(default="thread", init=False)


@dataclass(frozen=True, repr=False)
class SessionItemsFrame:
    data: RunSnapshot
    event_type: Literal["items"] = field(default="items", init=False)


@dataclass(frozen=True, repr=False)
class SessionDeltaFrame:
    data: Delta
    event_type: Literal["delta"] = field(default="delta", init=False)


@dataclass(frozen=True, repr=False)
class SessionGapFrame:
    data: Gap
    event_type: Literal["gap"] = field(default="gap", init=False)


@dataclass(frozen=True, repr=False)
class SessionScheduleFrame:
    data: ScheduleEvent
    event_type: Literal["schedule"] = field(default="schedule", init=False)


@dataclass(frozen=True, repr=False)
class SessionOccurrenceFrame:
    data: OccurrenceEvent
    event_type: Literal["occurrence"] = field(default="occurrence", init=False)


SessionFrame = (
    SessionThreadFrame
    | SessionItemsFrame
    | SessionDeltaFrame
    | SessionGapFrame
    | SessionScheduleFrame
    | SessionOccurrenceFrame
)
_DEFINITIONS = {
    "thread": "ThreadState",
    "items": "RunSnapshot",
    "delta": "Delta",
    "gap": "Gap",
    "schedule": "ScheduleEvent",
    "occurrence": "OccurrenceEvent",
}


@cache
def _validators() -> dict[str, Draft202012Validator]:
    schema = json.loads(files("a13n.generated").joinpath("session-stream.schema.json").read_bytes())
    return {
        event: Draft202012Validator({"$ref": f"#/$defs/{name}", "$defs": schema["$defs"]})
        for event, name in _DEFINITIONS.items()
    }


def _session_frame(event: str, data: list[str], cursor: str | None) -> SessionFrame | None:
    # Unknown names are ignored before interpreting their data or SSE fields.
    if event not in _DEFINITIONS:
        return None
    try:
        if cursor is not None:
            raise ValueError
        value = json.loads("\n".join(data))
        _validators()[event].validate(value)
        if event == "thread":
            return SessionThreadFrame(ThreadState.from_dict(value))
        if event == "items":
            return SessionItemsFrame(RunSnapshot.from_dict(value))
        if event == "delta":
            return SessionDeltaFrame(Delta.from_dict(value))
        if event == "schedule":
            return SessionScheduleFrame(ScheduleEvent.from_dict(value))
        if event == "occurrence":
            return SessionOccurrenceFrame(OccurrenceEvent.from_dict(value))
        return SessionGapFrame(Gap.from_dict(value))
    except (ValueError, TypeError, KeyError, AttributeError, ValidationError):
        raise ProtocolError("Malformed Session stream frame") from None


async def _session_frames(response: httpx2.Response, limit: int | None) -> AsyncGenerator[SessionFrame]:
    async with aclosing(_events(response, limit)) as events:
        async for event, data, cursor in events:
            frame = _session_frame(event, data, cursor)
            if frame is not None:
                yield frame


class SessionStream(_StreamContext[SessionFrame]):
    """Single-use, single-connection Session SSE reader, without automatic reconnect.

    Each instance starts from a fresh snapshot. On EOF, discard unfinished live
    state before opening another instance. Frames expose no resumable cursor.
    """

    def __init__(self, session: Resource, *, max_event_bytes: int | None = None) -> None:
        # Session snapshots aggregate Items and have no protocol size ceiling.
        # Keep error-body reads bounded independently of the default SSE limit.
        super().__init__(session, max_event_bytes if max_event_bytes is not None else 1_048_576)
        self._session_max_event_bytes = max_event_bytes

    @property
    def session(self) -> Resource:
        return self._resource

    async def _attach_with_recovery(self) -> None:
        request = session_stream.build_request(session_id=self._resource.id)
        try:
            await self._open_attachment(
                request, lambda response, _limit: _session_frames(response, self._session_max_event_bytes)
            )
        except httpx2.HTTPError:
            raise TransportError("Session stream transport failed") from None

    async def __anext__(self) -> SessionFrame:
        if not self._entered:
            raise RuntimeError("SessionStream must be entered before iteration")
        if self._closed:
            raise StopAsyncIteration
        if self._reading:
            raise RuntimeError("SessionStream supports one active reader")
        self._reading = True
        self._active_task = asyncio.current_task()
        self._active_done.clear()
        owner = None
        try:
            owner = self._resource._client._enter_io()
            assert self._iterator is not None
            return await anext(self._iterator)
        except asyncio.CancelledError:
            if self._close_event.is_set():
                raise StopAsyncIteration from None
            await self._finish()
            raise
        except httpx2.HTTPError:
            await self._finish()
            raise TransportError("Session stream transport failed") from None
        except BaseException:
            await self._finish()
            raise
        finally:
            self._resource._client._leave_io(owner)
            self._active_task = None
            self._reading = False
            self._active_done.set()
