"""One thread's provisional Native SSE tail; readback is always explicit."""

from __future__ import annotations

import asyncio
import json
import random
import re
from abc import ABC, abstractmethod
from collections.abc import AsyncGenerator, AsyncIterator, Callable, Mapping
from contextlib import AbstractAsyncContextManager, aclosing
from dataclasses import dataclass, field
from datetime import UTC, datetime
from email.utils import parsedate_to_datetime
from types import MappingProxyType
from typing import TYPE_CHECKING, Any, Literal, NotRequired, ReadOnly, Self, TypedDict, cast

import httpx2
from pydantic import JsonValue

from ._resources import Resource
from .errors import ApiError, ProtocolError, TransportError
from .generated.api.runs import thread_stream
from .generated.models import ErrorEnvelope
from .generated.types import UNSET

if TYPE_CHECKING:
    from types import TracebackType


_RETRYABLE_STATUS = frozenset({429, 502, 503, 504})
_CURSOR = re.compile(r"[0-9]{1,20}-[0-9]{1,20}\Z")
_POSITION = re.compile(r"(0|[1-9][0-9]{0,19})-(0|[1-9][0-9]{0,19})\Z")
_TYPES = frozenset({"delta", "boundary", "changed", "reset", "gap"})


class BoundaryData(TypedDict):
    run_id: ReadOnly[str]
    attempt: ReadOnly[int]
    sequence: ReadOnly[int]


class RecordSource(TypedDict):
    id: ReadOnly[str]
    sha256: ReadOnly[str]


class FileSource(TypedDict):
    path: ReadOnly[str]
    sha256: ReadOnly[str]
    bytes: ReadOnly[int]
    truncated: NotRequired[ReadOnly[bool]]


class MemorySource(TypedDict):
    kind: ReadOnly[Literal["record", "file"]]
    memory: ReadOnly[str]
    status: ReadOnly[Literal["recalled", "failed", "timeout", "full", "changes", "unchanged", "omitted", "unavailable"]]
    memory_id: NotRequired[ReadOnly[str | None]]
    cursor: NotRequired[ReadOnly[str | None]]
    records: NotRequired[ReadOnly[list[RecordSource]]]
    files: NotRequired[ReadOnly[list[FileSource]]]
    sources_truncated: NotRequired[ReadOnly[bool]]


class ItemRef(TypedDict):
    id: ReadOnly[str]
    kind: ReadOnly[Literal["text_message", "reasoning_message", "tool_call", "observation"]]
    state: ReadOnly[Literal["in_progress", "completed", "interrupted", "failed"]]
    ordinal: NotRequired[ReadOnly[int | None]]
    response_group: NotRequired[ReadOnly[str | None]]
    failure: NotRequired[ReadOnly[Mapping[str, JsonValue] | None]]
    memory_sources: NotRequired[ReadOnly[list[MemorySource] | None]]


class DeltaData(BoundaryData):
    # The envelope is validated; AG-UI event semantics remain application-owned.
    event: ReadOnly[Mapping[str, JsonValue]]
    item: ReadOnly[ItemRef | None]


class ChangedData(TypedDict):
    version: ReadOnly[int]


class RunSignalData(TypedDict):
    run_id: ReadOnly[str]


class GapData(RunSignalData):
    position: NotRequired[ReadOnly[str | None]]


@dataclass(frozen=True, repr=False)
class DeltaFrame:
    data: DeltaData
    cursor: str
    event_type: Literal["delta"] = field(default="delta", init=False)


@dataclass(frozen=True, repr=False)
class BoundaryFrame:
    data: BoundaryData
    cursor: str
    event_type: Literal["boundary"] = field(default="boundary", init=False)


@dataclass(frozen=True, repr=False)
class ChangedFrame:
    data: ChangedData
    cursor: None = field(default=None, init=False)
    event_type: Literal["changed"] = field(default="changed", init=False)


@dataclass(frozen=True, repr=False)
class ResetFrame:
    data: RunSignalData
    cursor: None = field(default=None, init=False)
    event_type: Literal["reset"] = field(default="reset", init=False)


@dataclass(frozen=True, repr=False)
class GapFrame:
    data: GapData
    cursor: None = field(default=None, init=False)
    event_type: Literal["gap"] = field(default="gap", init=False)


ThreadFrame = DeltaFrame | BoundaryFrame | ChangedFrame | ResetFrame | GapFrame


@dataclass(frozen=True, repr=False)
class StreamResponse:
    status_code: int
    headers: Mapping[str, str]
    request_id: str | None


async def _lines(response: httpx2.Response, limit: int | None) -> AsyncGenerator[bytes]:
    pending = bytearray()
    skip_lf = False
    async with aclosing(response.aiter_bytes()) as chunks:
        async for chunk in chunks:
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
                if limit is not None and len(pending) > limit:
                    raise ProtocolError("SSE line exceeds the configured bound")
                yield bytes(pending)
                pending.clear()
                start = index + 1
                skip_lf = byte == 13
            pending.extend(chunk[start:])
            if limit is not None and len(pending) > limit:
                raise ProtocolError("SSE line exceeds the configured bound")
        if pending:
            raise ProtocolError("Stream ended with a truncated SSE line")


def _memory_sources(value: Any) -> None:
    """Validate the pinned provenance shape without filling omitted defaults."""
    if value is None:
        return
    if not isinstance(value, list):
        raise ValueError
    for source in value:
        if (
            not isinstance(source, dict)
            or source.keys()
            - {"kind", "memory", "status", "memory_id", "cursor", "records", "files", "sources_truncated"}
            or source.get("kind") not in ("record", "file")
            or not isinstance(source.get("memory"), str)
            or source.get("status")
            not in ("recalled", "failed", "timeout", "full", "changes", "unchanged", "omitted", "unavailable")
        ):
            raise ValueError
        for key in ("memory_id", "cursor"):
            if source.get(key) is not None and not isinstance(source[key], str):
                raise ValueError
        if "sources_truncated" in source and not isinstance(source["sources_truncated"], bool):
            raise ValueError
        records = source.get("records", [])
        files = source.get("files", [])
        if not isinstance(records, list) or not isinstance(files, list):
            raise ValueError
        for record in records:
            if (
                not isinstance(record, dict)
                or record.keys() - {"id", "sha256"}
                or not isinstance(record.get("id"), str)
                or not isinstance(record.get("sha256"), str)
            ):
                raise ValueError
        for file in files:
            if (
                not isinstance(file, dict)
                or file.keys() - {"path", "sha256", "bytes", "truncated"}
                or not isinstance(file.get("path"), str)
                or not isinstance(file.get("sha256"), str)
                or not isinstance(file.get("bytes"), int)
                or isinstance(file["bytes"], bool)
                or file["bytes"] < 0
                or ("truncated" in file and not isinstance(file["truncated"], bool))
            ):
                raise ValueError


def _frame(event_type: str, data: list[str], cursor: str | None) -> ThreadFrame:
    try:
        value = json.loads("\n".join(data))
        if not isinstance(value, dict) or event_type not in _TYPES:
            raise ValueError
        if event_type in {"delta", "boundary"}:
            if cursor is None or not _CURSOR.fullmatch(cursor):
                raise ValueError
            if not isinstance(value.get("run_id"), str) or not value["run_id"]:
                raise ValueError
            if any(
                not isinstance(value.get(key), int) or isinstance(value[key], bool) for key in ("attempt", "sequence")
            ):
                raise ValueError
            if event_type == "boundary":
                return BoundaryFrame(cast("BoundaryData", MappingProxyType(value)), cursor)
            if not isinstance(value.get("event"), dict) or "item" not in value:
                raise ValueError
            item = value["item"]
            if item is not None:
                if (
                    not isinstance(item, dict)
                    or not isinstance(item.get("id"), str)
                    or item.get("kind") not in ("text_message", "reasoning_message", "tool_call", "observation")
                    or item.get("state") not in ("in_progress", "completed", "interrupted", "failed")
                ):
                    raise ValueError
                ordinal = item.get("ordinal")
                if ordinal is not None and (not isinstance(ordinal, int) or isinstance(ordinal, bool) or ordinal < 1):
                    raise ValueError
                response_group = item.get("response_group")
                if response_group is not None and not isinstance(response_group, str):
                    raise ValueError
                failure = item.get("failure")
                if failure is not None and not isinstance(failure, dict):
                    raise ValueError
                _memory_sources(item.get("memory_sources"))
                value["item"] = MappingProxyType(item)
            value["event"] = MappingProxyType(value["event"])
            return DeltaFrame(cast("DeltaData", MappingProxyType(value)), cursor)
        else:
            if cursor is not None:
                raise ValueError
            if event_type == "changed":
                if not isinstance(value.get("version"), int) or isinstance(value["version"], bool):
                    raise ValueError
                return ChangedFrame(cast("ChangedData", MappingProxyType(value)))
            if not isinstance(value.get("run_id"), str) or not value["run_id"]:
                raise ValueError
            if event_type == "gap":
                position = value.get("position")
                if position is not None and (not isinstance(position, str) or not _POSITION.fullmatch(position)):
                    raise ValueError
                return GapFrame(cast("GapData", MappingProxyType(value)))
            return ResetFrame(cast("RunSignalData", MappingProxyType(value)))
    except (ValueError, TypeError):
        raise ProtocolError("Malformed Thread stream frame") from None


async def _events(response: httpx2.Response, limit: int | None) -> AsyncGenerator[tuple[str, list[str], str | None]]:
    data: list[str] = []
    event_type = ""
    cursor: str | None = None
    size = 0
    first = True
    async with aclosing(_lines(response, limit)) as lines:
        async for raw in lines:
            try:
                line = raw.decode("utf-8")
            except UnicodeError:
                raise ProtocolError("Invalid UTF-8 in SSE stream") from None
            if first:
                line = line.removeprefix("\ufeff")
                first = False
            size += len(raw) + 1
            if limit is not None and size > limit:
                raise ProtocolError("SSE frame exceeds the configured bound")
            if not line:
                if data or event_type or cursor is not None:
                    yield event_type, data, cursor
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
            raise ProtocolError("Stream ended with a truncated SSE frame")


async def _frames(response: httpx2.Response, limit: int) -> AsyncGenerator[ThreadFrame]:
    async with aclosing(_events(response, limit)) as events:
        async for event_type, data, cursor in events:
            yield _frame(event_type, data, cursor)


async def _error(response: httpx2.Response, limit: int) -> ApiError:
    payload = bytearray()
    async with aclosing(response.aiter_bytes()) as chunks:
        async for chunk in chunks:
            payload.extend(chunk)
            if len(payload) > limit:
                raise ProtocolError("Oversized stream error response")
        try:
            parsed = ErrorEnvelope.from_dict(json.loads(payload))
        except (ValueError, TypeError, KeyError, AttributeError):
            raise ProtocolError("Malformed stream error response") from None
        error = parsed.error
        return ApiError(
            response.status_code,
            error.code,
            error.message,
            error.details.to_dict(),
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


class _StreamContext[FrameT](ABC):
    """Shared single-reader transport lifetime, without cursor or reconnect policy."""

    def __init__(self, resource: Resource, max_event_bytes: int) -> None:
        if not isinstance(max_event_bytes, int) or isinstance(max_event_bytes, bool) or max_event_bytes <= 0:
            raise ValueError("max_event_bytes must be a positive integer")
        self._resource = resource
        self._max_event_bytes = max_event_bytes
        self._entered = False
        self._closed = False
        self._reading = False
        self._response: StreamResponse | None = None
        self._context: AbstractAsyncContextManager[httpx2.Response] | None = None
        self._iterator: AsyncIterator[FrameT] | None = None
        self._active_task: asyncio.Task[Any] | None = None
        self._close_event = asyncio.Event()
        self._active_done = asyncio.Event()
        self._active_done.set()

    @property
    def response(self) -> StreamResponse | None:
        return self._response

    @property
    def is_closed(self) -> bool:
        return self._closed

    async def __aenter__(self) -> Self:
        if self._entered or self._closed:
            raise RuntimeError(f"{type(self).__name__} is single-use")
        self._entered = True
        self._active_task = asyncio.current_task()
        self._active_done.clear()
        owner = None
        try:
            owner = self._resource._client._enter_io()
            await self._attach_with_recovery()
        except asyncio.CancelledError:
            if self._close_event.is_set():
                raise RuntimeError("Stream was closed during entry") from None
            await self._finish()
            raise
        except BaseException:
            await self._finish()
            raise
        finally:
            self._resource._client._leave_io(owner)
            self._active_task = None
            self._active_done.set()
        if self._closed:
            raise RuntimeError("Stream was closed during entry")
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

    @abstractmethod
    async def _attach_with_recovery(self) -> None:
        """Open the connection using the concrete protocol's policy."""

    async def _open_attachment(
        self,
        request: dict[str, Any],
        decoder: Callable[[httpx2.Response, int], AsyncIterator[FrameT]],
    ) -> None:
        context = self._resource._client.stream(request)
        try:
            response = await context.__aenter__()
        except httpx2.HTTPError:
            raise TransportError("SSE stream transport failed") from None
        self._context = context
        if not 200 <= response.status_code < 300:
            error = await _error(response, self._max_event_bytes)
            await self._close_attachment()
            raise error
        if response.headers.get("content-type", "").split(";", 1)[0].strip().lower() != "text/event-stream":
            await self._close_attachment()
            raise ProtocolError("SSE stream response is not text/event-stream")
        headers = MappingProxyType(httpx2.Headers(response.headers))
        self._response = StreamResponse(response.status_code, headers, headers.get("x-request-id"))
        self._iterator = decoder(response, self._max_event_bytes)

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


class ThreadStream(_StreamContext[ThreadFrame]):
    """Single-use async context; attach/reconnect never mutates Service state."""

    def __init__(
        self,
        thread: Resource,
        *,
        run: str | None = None,
        position: str | None = None,
        after: str | None = None,
        reconnect: bool = True,
        max_reconnects: int = 5,
        max_event_bytes: int = 1_048_576,
    ) -> None:
        if (run is None) != (position is None):
            raise ValueError("run and position must be supplied together")
        if position is not None and not _POSITION.fullmatch(position):
            raise ValueError("position must be a canonical Native attempt-sequence position")
        if after is not None and not _CURSOR.fullmatch(after):
            raise ValueError("after must be a Native thread-stream entry ID")
        if not isinstance(max_reconnects, int) or isinstance(max_reconnects, bool) or max_reconnects < 0:
            raise ValueError("max_reconnects must be a non-negative integer")
        super().__init__(thread, max_event_bytes)
        self._thread = thread
        self._run = run
        self._position = position
        self._acknowledged_cursor = after
        self._pending_ack: str | None = None
        self._last_received_cursor: str | None = None
        self._reconnect = reconnect and max_reconnects > 0
        self._max_reconnects = max_reconnects
        self._retries = 0

    @property
    def thread(self) -> Resource:
        return self._thread

    @property
    def last_received_cursor(self) -> str | None:
        return self._last_received_cursor

    async def __anext__(self) -> ThreadFrame:
        if not self._entered:
            raise RuntimeError("ThreadStream must be entered before iteration")
        if self._closed:
            raise StopAsyncIteration
        if self._reading:
            raise RuntimeError("ThreadStream supports one active reader")
        self._reading = True
        self._active_task = asyncio.current_task()
        self._active_done.clear()
        if self._pending_ack is not None:
            if self._pending_ack != self._acknowledged_cursor:
                self._retries = 0
            self._acknowledged_cursor = self._pending_ack
            self._pending_ack = None
        owner = None
        try:
            owner = self._thread._client._enter_io()
            while not self._closed:
                assert self._iterator is not None
                try:
                    frame = await anext(self._iterator)
                except StopAsyncIteration:
                    await self._close_attachment()
                    if not self._reconnect:
                        await self._finish()
                        raise
                    await self._recover(TransportError("Thread stream ended; re-read state if needed"))
                    await self._attach_with_recovery()
                    continue
                except ProtocolError:
                    await self._finish()
                    raise
                except httpx2.HTTPError:
                    await self._close_attachment()
                    await self._recover(TransportError("Thread stream transport failed"))
                    await self._attach_with_recovery()
                    continue
                if frame.cursor is not None:
                    self._last_received_cursor = frame.cursor
                    self._pending_ack = frame.cursor
                return frame
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
            self._thread._client._leave_io(owner)
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
                await self._recover(TransportError("Thread stream transport failed"))

    async def _attach(self) -> None:
        request = thread_stream.build_request(
            thread_id=self._thread.id,
            run=self._run if self._run is not None else UNSET,
            position=self._position if self._position is not None else UNSET,
            last_event_id=self._acknowledged_cursor if self._acknowledged_cursor is not None else UNSET,
        )
        await self._open_attachment(request, _frames)

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
