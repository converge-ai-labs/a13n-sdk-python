"""One-attachment Run SSE consumption; applied checkpoints belong to callers."""

import json
from collections.abc import AsyncGenerator, AsyncIterator
from contextlib import asynccontextmanager
from dataclasses import dataclass
from typing import TYPE_CHECKING

import httpx2

from .client import ApiError, ProtocolError, TransportError
from .generated.api.protocol_gateway import get_runs_run_id_stream
from .generated.models import ErrorResponse, RunStreamEvent
from .generated.types import UNSET, Unset

if TYPE_CHECKING:
    from .client import Client


@dataclass(frozen=True, repr=False)
class StreamObservation:
    cursor: str
    event: RunStreamEvent


class ReplayGap(ProtocolError):
    """A live attachment cannot supply the requested exact event history."""

    def __init__(self, run_id: str, details: dict) -> None:
        super().__init__("Run stream replay gap; reconcile current resource state")
        self.run_id = run_id
        self.details = details


async def _lines(response: httpx2.Response, limit: int) -> AsyncIterator[bytes]:
    pending = bytearray()
    skip_lf = False
    async for chunk in response.aiter_bytes():
        # SSE accepts CR, LF and CRLF even when a delimiter is split across reads.
        start = 0
        for index, byte in enumerate(chunk):
            if skip_lf:
                skip_lf = False
                if byte == 10:
                    start = index + 1
                    continue
            if byte not in (10, 13):
                continue
            pending.extend(chunk[start:index])
            if len(pending) > limit:
                raise ProtocolError("SSE line exceeds the configured event bound")
            yield bytes(pending)
            pending.clear()
            start = index + 1
            skip_lf = byte == 13
        pending.extend(chunk[start:])
        if len(pending) > limit:
            raise ProtocolError("SSE line exceeds the configured event bound")
    # An unterminated event is not dispatched. The caller reconnects after its
    # last fully applied event; EOF itself never establishes Run completion.


async def _observations(response: httpx2.Response, run_id: str, limit: int) -> AsyncGenerator[StreamObservation]:
    data: list[str] = []
    event_type = ""
    cursor: str | None = None
    size = 0
    first = True
    async for raw in _lines(response, limit):
        try:
            line = raw.decode("utf-8")
        except UnicodeError:
            raise ProtocolError("Invalid UTF-8 in Run stream") from None
        if first:
            line = line.removeprefix("\ufeff")
            first = False
        size += len(raw) + 1
        if size > limit:
            raise ProtocolError("SSE event exceeds the configured event bound")
        if not line:
            if data:
                try:
                    value = json.loads("\n".join(data))
                    if not isinstance(value, dict):
                        raise ValueError
                    if event_type == "a13n.service.replay_gap":
                        if cursor is not None or value.get("run_id", run_id) != run_id:
                            raise ValueError
                        raise ReplayGap(run_id, value)
                    if not cursor or "\x00" in cursor or value.get("schema_version", "1") != "1":
                        raise ValueError
                    event = RunStreamEvent.from_dict(value)
                    if event.run_id != run_id or event.event_type != event_type:
                        raise ValueError
                    if not all(
                        isinstance(field, str) and field
                        for field in (event.event_id, event.thread_id, event.event_type)
                    ):
                        raise ValueError
                except (ValueError, TypeError, KeyError, AttributeError):
                    raise ProtocolError("Malformed or incompatible Run stream event") from None
                yield StreamObservation(cursor, event)
            data, event_type, cursor, size = [], "", None, 0
            continue
        if line.startswith(":"):
            continue
        field, separator, value = line.partition(":")
        if separator and value.startswith(" "):
            value = value[1:]
        if field == "data":
            data.append(value)
        elif field == "event":
            event_type = value
        elif field == "id":
            cursor = value


@asynccontextmanager
async def run_stream(
    client: "Client", run_id: str, *, after: str | None = None, max_event_bytes: int = 1_048_576
) -> AsyncIterator[AsyncIterator[StreamObservation]]:
    if max_event_bytes <= 0:
        raise ValueError("max_event_bytes must be positive")
    if after is not None and (not after or any(char in after for char in "\r\n\x00")):
        raise ValueError("after must be a nonblank SSE cursor without control delimiters")
    request = get_runs_run_id_stream.build_request(
        run_id=run_id, accept="text/event-stream", last_event_id=after if after is not None else UNSET
    )
    try:
        async with client.stream(request) as response:
            if not 200 <= response.status_code < 300:
                payload = bytearray()
                async for chunk in response.aiter_bytes():
                    payload.extend(chunk)
                    if len(payload) > max_event_bytes:
                        raise ProtocolError("Oversized stream error response")
                try:
                    parsed = ErrorResponse.from_dict(json.loads(payload))
                except (ValueError, TypeError, KeyError, AttributeError):
                    raise ProtocolError("Malformed stream error response") from None
                error = parsed.error
                raise ApiError(
                    response.status_code,
                    error.code,
                    error.message,
                    {} if isinstance(error.details, Unset) or error.details is None else error.details.to_dict(),
                    response.headers.get("x-request-id") or error.request_id,
                    response.headers.get("retry-after"),
                )
            if response.headers.get("content-type", "").split(";", 1)[0].strip().lower() != "text/event-stream":
                raise ProtocolError("Run stream response is not text/event-stream")
            iterator = _observations(response, run_id, max_event_bytes)
            try:
                yield iterator
            finally:
                await iterator.aclose()
    except httpx2.HTTPError:
        raise TransportError("Run stream transport failed; Run outcome is unchanged") from None
