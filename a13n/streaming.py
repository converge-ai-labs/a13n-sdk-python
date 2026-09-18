"""Resumable exact-Run SSE observation with bounded read-only recovery."""

from __future__ import annotations

import asyncio
import json
import random
from collections.abc import AsyncGenerator, AsyncIterator, Mapping
from contextlib import AbstractAsyncContextManager
from dataclasses import dataclass
from datetime import UTC, datetime
from email.utils import parsedate_to_datetime
from types import MappingProxyType
from typing import TYPE_CHECKING, Any, Self

import httpx2

from .client import ApiError, ProtocolError, TransportError
from .generated.api.protocol_gateway import get_runs_run_id_stream
from .generated.models import ErrorResponse, RunStreamEvent
from .generated.types import UNSET, Unset

if TYPE_CHECKING:
    from types import TracebackType

    from ._resources import Result
    from .generated import models as wire
    from .generated.resources import Run

_RETRYABLE_STATUS = frozenset({429, 502, 503, 504})
_TERMINAL_EVENTS = frozenset(
    {
        "run.completed",
        "run.failed",
        "run.cancelled",
        "run.waiting",
    }
)
_SEALED_STATUSES = frozenset({"completed", "failed", "cancelled", "waiting"})


@dataclass(frozen=True, repr=False)
class StreamObservation:
    cursor: str
    event: RunStreamEvent


@dataclass(frozen=True, repr=False)
class StreamResponse:
    status_code: int
    headers: Mapping[str, str]
    request_id: str | None


class ReplayGap(ProtocolError):
    """Exact Run history no longer covers the requested cursor."""

    def __init__(
        self,
        run_id: str,
        *,
        requested_cursor: str | None = None,
        available_floor: str | None = None,
        high_watermark: str | None = None,
        status_code: int | None = None,
        request_id: str | None = None,
    ) -> None:
        super().__init__("Run stream replay gap; reconcile retained state explicitly")
        self.run_id = run_id
        self.requested_cursor = requested_cursor
        self.available_floor = available_floor
        self.high_watermark = high_watermark
        self.status_code = status_code
        self.request_id = request_id


async def _lines(response: httpx2.Response, limit: int) -> AsyncIterator[bytes]:
    pending = bytearray()
    skip_lf = False
    async for chunk in response.aiter_bytes():
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
    if pending:
        raise ProtocolError("Run stream ended with a truncated SSE line")


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
                        raise ReplayGap(
                            run_id,
                            requested_cursor=_optional_string(value, "requested_cursor"),
                            available_floor=_optional_string(value, "retained_floor"),
                            high_watermark=_optional_string(value, "high_watermark"),
                        )
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
                except ReplayGap:
                    raise
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
    if data or event_type or cursor is not None:
        raise ProtocolError("Run stream ended with a truncated SSE event")


def _optional_string(value: Mapping[str, Any], key: str) -> str | None:
    field = value.get(key)
    return field if isinstance(field, str) else None


async def _error(response: httpx2.Response, limit: int) -> ApiError:
    payload = bytearray()
    async for chunk in response.aiter_bytes():
        payload.extend(chunk)
        if len(payload) > limit:
            raise ProtocolError("Oversized stream error response")
    try:
        parsed = ErrorResponse.from_dict(json.loads(payload))
    except (ValueError, TypeError, KeyError, AttributeError):
        raise ProtocolError("Malformed stream error response") from None
    error = parsed.error
    return ApiError(
        response.status_code,
        error.code,
        error.message,
        {} if isinstance(error.details, Unset) or error.details is None else error.details.to_dict(),
        response.headers.get("x-request-id") or error.request_id,
        response.headers.get("retry-after"),
    )


def _retry_after(value: str | None) -> float | None:
    if value is None:
        return None
    try:
        seconds = float(value)
    except ValueError:
        try:
            instant = parsedate_to_datetime(value)
            if instant.tzinfo is None:
                instant = instant.replace(tzinfo=UTC)
            seconds = (instant - datetime.now(UTC)).total_seconds()
        except (TypeError, ValueError, OverflowError):
            return None
    if seconds < 0:
        return None
    return min(seconds, 30.0)


class RunStream:
    """Single-use async context and iterator for one exact Run."""

    def __init__(
        self,
        run: Run,
        *,
        after: str | None,
        reconnect: bool,
        max_reconnects: int,
        max_event_bytes: int,
    ) -> None:
        if after is not None and (not after or any(char in after for char in "\r\n\x00")):
            raise ValueError("after must be a nonblank SSE cursor without control delimiters")
        if not isinstance(max_reconnects, int) or isinstance(max_reconnects, bool) or max_reconnects < 0:
            raise ValueError("max_reconnects must be a non-negative integer")
        if not isinstance(max_event_bytes, int) or isinstance(max_event_bytes, bool) or max_event_bytes <= 0:
            raise ValueError("max_event_bytes must be a positive integer")
        self._run = run
        self._acknowledged_cursor = after
        self._pending_ack: str | None = None
        self._last_received_cursor: str | None = None
        self._reconnect = reconnect and max_reconnects > 0
        self._max_reconnects = max_reconnects
        self._max_event_bytes = max_event_bytes
        self._retries = 0
        self._entered = False
        self._closed = False
        self._reading = False
        self._terminal_received = False
        self._response: StreamResponse | None = None
        self._context: AbstractAsyncContextManager[httpx2.Response] | None = None
        self._iterator: AsyncIterator[StreamObservation] | None = None
        self._active_task: asyncio.Task[Any] | None = None
        self._close_event = asyncio.Event()
        self._active_done = asyncio.Event()
        self._active_done.set()

    @property
    def run(self) -> Run:
        return self._run

    @property
    def response(self) -> StreamResponse | None:
        return self._response

    @property
    def is_closed(self) -> bool:
        return self._closed

    @property
    def last_received_cursor(self) -> str | None:
        return self._last_received_cursor

    async def __aenter__(self) -> Self:
        if self._entered:
            raise RuntimeError("RunStream is single-use")
        self._entered = True
        self._active_task = asyncio.current_task()
        self._active_done.clear()
        owner = None
        try:
            owner = self._run._client._enter_io()
            await self._attach_with_recovery()
        except asyncio.CancelledError:
            if self._close_event.is_set():
                raise RuntimeError("RunStream was closed during entry") from None
            await self._finish()
            raise
        except BaseException:
            await self._finish()
            raise
        finally:
            self._run._client._leave_io(owner)
            self._active_task = None
            self._active_done.set()
        if self._closed:
            raise RuntimeError("RunStream was closed during entry")
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        await self.aclose()

    def __aiter__(self) -> Self:
        return self

    async def __anext__(self) -> StreamObservation:
        if not self._entered:
            raise RuntimeError("RunStream must be entered before iteration")
        if self._closed:
            raise StopAsyncIteration
        if self._reading:
            raise RuntimeError("RunStream supports one active reader")
        self._reading = True
        self._active_task = asyncio.current_task()
        self._active_done.clear()
        owner = None
        if self._pending_ack is not None:
            if self._pending_ack != self._acknowledged_cursor:
                self._retries = 0
            self._acknowledged_cursor = self._pending_ack
            self._pending_ack = None
        try:
            owner = self._run._client._enter_io()
            while not self._closed:
                assert self._iterator is not None
                try:
                    observation = await anext(self._iterator)
                except StopAsyncIteration:
                    await self._close_attachment()
                    if not self._reconnect or self._terminal_received or await self._confirmed_terminal_projection():
                        await self._finish()
                        raise
                    await self._recover(TransportError("Run stream ended without confirmed completion"))
                    await self._attach_with_recovery()
                    continue
                except ReplayGap:
                    await self._finish()
                    raise
                except ProtocolError:
                    await self._finish()
                    raise
                except httpx2.HTTPError:
                    await self._close_attachment()
                    await self._recover(TransportError("Run stream transport failed; Run outcome is unchanged"))
                    await self._attach_with_recovery()
                    continue
                self._last_received_cursor = observation.cursor
                self._pending_ack = observation.cursor
                if observation.event.event_type in _TERMINAL_EVENTS:
                    self._terminal_received = True
                return observation
            raise StopAsyncIteration
        except asyncio.CancelledError:
            if self._close_event.is_set():
                raise StopAsyncIteration from None
            await self._finish()
            raise
        except BaseException:
            await self._finish()
            raise
        finally:
            self._run._client._leave_io(owner)
            self._active_task = None
            self._reading = False
            self._active_done.set()

    async def _attach_with_recovery(self) -> None:
        while not self._closed:
            try:
                await self._attach()
                return
            except ApiError as error:
                if error.status not in _RETRYABLE_STATUS:
                    raise
                await self._recover(error)
            except TransportError as error:
                await self._recover(error)
            except httpx2.HTTPError:
                await self._recover(TransportError("Run stream transport failed; Run outcome is unchanged"))

    async def _attach(self) -> None:
        request = get_runs_run_id_stream.build_request(
            run_id=self._run.id,
            accept="text/event-stream",
            last_event_id=self._acknowledged_cursor if self._acknowledged_cursor is not None else UNSET,
        )
        context = self._run._client.stream(request)
        try:
            response = await context.__aenter__()
        except httpx2.HTTPError:
            raise TransportError("Run stream transport failed; Run outcome is unchanged") from None
        self._context = context
        if not 200 <= response.status_code < 300:
            error = await _error(response, self._max_event_bytes)
            await self._close_attachment()
            if error.status == 409 and error.code == "run_stream_replay_gap":
                raise ReplayGap(
                    self._run.id,
                    requested_cursor=_optional_string(error.details, "requested_cursor") or self._acknowledged_cursor,
                    available_floor=_optional_string(error.details, "retained_floor"),
                    high_watermark=_optional_string(error.details, "high_watermark"),
                    status_code=error.status,
                    request_id=error.request_id,
                )
            raise error
        if response.headers.get("content-type", "").split(";", 1)[0].strip().lower() != "text/event-stream":
            await self._close_attachment()
            raise ProtocolError("Run stream response is not text/event-stream")
        headers = MappingProxyType(httpx2.Headers(response.headers))
        self._response = StreamResponse(response.status_code, headers, headers.get("x-request-id"))
        self._iterator = _observations(response, self._run.id, self._max_event_bytes)

    async def _recover(self, error: ApiError | TransportError) -> None:
        await self._close_attachment()
        if not self._reconnect or self._retries >= self._max_reconnects:
            await self._finish()
            raise error
        self._retries += 1
        ceiling = min(0.5 * 2 ** (self._retries - 1), 10.0)
        delay = random.uniform(ceiling / 2, ceiling)
        if isinstance(error, ApiError):
            delay = max(delay, _retry_after(error.retry_after) or 0.0)
        try:
            await asyncio.wait_for(self._close_event.wait(), timeout=delay)
        except TimeoutError:
            pass
        if self._closed:
            raise StopAsyncIteration

    async def _confirmed_terminal_projection(self) -> bool:
        run = await self._run.get()
        if run.value.status not in _SEALED_STATUSES:
            return False
        items = await self._run.items.list()
        return (
            items.value.complete
            and items.value.finalized
            and items.value.projection_cursor == self._acknowledged_cursor
        )

    async def _close_attachment(self) -> None:
        iterator, self._iterator = self._iterator, None
        if isinstance(iterator, AsyncGenerator):
            await iterator.aclose()
        context, self._context = self._context, None
        if context is not None:
            await context.__aexit__(None, None, None)

    async def _finish(self) -> None:
        if self._closed:
            return
        self._closed = True
        self._close_event.set()
        await self._close_attachment()

    async def aclose(self) -> None:
        if self._closed:
            return
        self._closed = True
        self._close_event.set()
        active = self._active_task
        if active is not None and active is not asyncio.current_task():
            active.cancel()
            await self._active_done.wait()
        await self._close_attachment()

    async def steer(self, input: str | wire.AgentInput, *, idempotency_key: str) -> Result[wire.SteerReceipt]:
        return await self._run.steer(input, idempotency_key=idempotency_key)

    async def cancel(
        self,
        *,
        expected_run_version: int,
        expected_thread_version: int,
        idempotency_key: str,
    ) -> Result[wire.InterruptReceipt]:
        return await self._run.cancel(
            expected_run_version=expected_run_version,
            expected_thread_version=expected_thread_version,
            idempotency_key=idempotency_key,
        )

    async def wait(self, *, timeout: float, poll_interval: float) -> Result[wire.RunResource]:
        return await self._run.wait(timeout=timeout, poll_interval=poll_interval)
