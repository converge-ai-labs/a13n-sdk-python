import asyncio

import httpx2
import pytest

from a13n import (
    ApiError,
    Client,
    ProtocolError,
    SessionDeltaFrame,
    SessionFrame,
    SessionItemsFrame,
    SessionStream,
    SessionThreadFrame,
    TransportError,
)
from a13n.generated import models as wire
from a13n.session_streaming import _session_frame, _validators
from tests.test_interaction import entry_view, run_view, thread_view
from tests.test_run_items import continuation, display_item
from tests.test_streaming import sse


def session_state() -> dict:
    return {"thread": thread_view(), "current_run": run_view(), "last_run": None, "entries": [entry_view()]}


def session_items() -> dict:
    return {
        "thread_id": "thr_1",
        "run_id": "run_1",
        "first": 1,
        "items": [display_item(1)],
        "continuation": continuation(),
        "complete": False,
    }


def session_delta() -> dict:
    return {
        "thread_id": "thr_1",
        "run_id": "run_1",
        "attempt": 1,
        "sequence": 6,
        "event": {"type": "future-agui-event", "raw": [None, False, 0, {"nested": "value"}]},
        "item": {"id": "itm_1", "kind": "text_message", "state": "in_progress"},
    }


def test_session_four_typed_frames_are_distinct_from_thread_cursor_frames() -> None:
    async def scenario() -> None:
        requests = []
        payloads = {
            "thread": session_state(),
            "items": session_items(),
            "delta": session_delta(),
            "gap": {"thread_id": "thr_1", "run_id": "run_1"},
        }
        data = b": heartbeat\r\n\r\n" + b"event: future\ndata: not-json\nid: ignored\n\n"
        data += b"".join(sse(event, value) for event, value in payloads.items())

        def handle(request: httpx2.Request) -> httpx2.Response:
            requests.append(request)
            return httpx2.Response(
                200, content=data, headers={"Content-Type": "text/event-stream", "X-Request-ID": "req_session"}
            )

        async with Client("https://service.example", "token", transport=httpx2.MockTransport(handle)) as client:
            async with SessionStream(client.api.sessions("ses_1")) as stream:
                assert stream.session.id == "ses_1"
                frames = [frame async for frame in stream]
                assert stream.is_closed
                assert stream.response.request_id == "req_session"
                assert stream.response.status_code == 200
            assert all(isinstance(frame, SessionFrame) for frame in frames)
            assert [frame.event_type for frame in frames] == list(payloads)
            assert all(frame.data.to_dict() == payloads[frame.event_type] for frame in frames[1:])
            assert isinstance(frames[0], SessionThreadFrame) and isinstance(frames[0].data.thread, wire.ThreadView)
            assert isinstance(frames[1], SessionItemsFrame) and frames[1].data.continuation.position.sequence == 5
            assert (
                isinstance(frames[2], SessionDeltaFrame)
                and frames[2].data.event.to_dict()["raw"] == payloads["delta"]["event"]["raw"]
            )
            assert not hasattr(frames[2], "cursor")
            assert not hasattr(stream, "last_received_cursor")
            assert len(requests) == 1 and not requests[0].url.params
            assert requests[0].url.path == "/api/v1/sessions/ses_1/stream"
            assert "Last-Event-ID" not in requests[0].headers
            with pytest.raises(RuntimeError, match="single-use"):
                async with stream:
                    pass

    asyncio.run(scenario())


def test_session_reconnection_is_an_explicit_fresh_instance_without_auto_fetch_or_cursor() -> None:
    async def scenario() -> None:
        seen = []

        def handle(request: httpx2.Request) -> httpx2.Response:
            seen.append(request)
            state = session_state()
            state["thread"]["version"] = len(seen)
            return httpx2.Response(200, content=sse("thread", state), headers={"Content-Type": "text/event-stream"})

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            for version in (1, 2):
                async with SessionStream(client.api.sessions("ses_1")) as stream:
                    frames = [frame async for frame in stream]
                    assert len(frames) == 1 and frames[0].data.thread.version == version
                assert len(seen) == version
        assert all(not request.url.params and "Last-Event-ID" not in request.headers for request in seen)
        assert all(request.url.path.endswith("/sessions/ses_1/stream") for request in seen)

    asyncio.run(scenario())


@pytest.mark.parametrize(
    "event,payload,cursor",
    [
        ("thread", {**session_state(), "current_run": {}}, None),
        ("items", {**session_items(), "first": True}, None),
        ("items", {**session_items(), "continuation": {"run_id": "run_1"}}, None),
        ("delta", {**session_delta(), "attempt": True}, None),
        ("delta", {**session_delta(), "event": []}, None),
        ("delta", {**session_delta(), "item": {"id": "i", "kind": "future", "state": "completed"}}, None),
        ("gap", {"run_id": "run_1"}, None),
        ("gap", {"thread_id": "thr_1", "run_id": "run_1"}, "1-0"),
    ],
)
def test_invalid_known_session_frames_fail_and_release_response_without_retry(
    event: str, payload: dict, cursor: str | None
) -> None:
    async def scenario() -> None:
        responses = []

        def handle(_request: httpx2.Request) -> httpx2.Response:
            response = httpx2.Response(
                200, content=sse(event, payload, cursor), headers={"Content-Type": "text/event-stream"}
            )
            responses.append(response)
            return response

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            async with SessionStream(client.api.sessions("ses_1")) as stream:
                with pytest.raises(ProtocolError, match="Session"):
                    await anext(stream)
                assert stream.is_closed
            assert len(responses) == 1 and responses[0].is_closed

    asyncio.run(scenario())


@pytest.mark.parametrize(
    "data",
    [
        b"event: gap\n\n",
        b"event: gap\ndata: {}",
        b"event: gap\ndata: bad\n\n",
        b"event: gap\ndata: \xff\n\n",
        b"data: " + b"x" * 64 + b"\n\n",
    ],
)
def test_session_framing_failures_are_terminal(data: bytes) -> None:
    async def scenario() -> None:
        transport = httpx2.MockTransport(
            lambda _: httpx2.Response(200, content=data, headers={"Content-Type": "text/event-stream"})
        )
        async with Client("https://service.example", transport=transport) as client:
            async with SessionStream(client.api.sessions("ses_1"), max_event_bytes=64) as stream:
                with pytest.raises(ProtocolError):
                    await anext(stream)
                assert stream.is_closed

    asyncio.run(scenario())


@pytest.mark.parametrize("status", [403, 429, 503])
def test_session_http_errors_preserve_metadata_and_do_not_retry(status: int) -> None:
    async def scenario() -> None:
        responses = []

        def handle(_request: httpx2.Request) -> httpx2.Response:
            response = httpx2.Response(
                status,
                json={
                    "error": {
                        "code": "forbidden",
                        "message": "Try later",
                        "details": {"cause": "test"},
                        "request_id": "body",
                    }
                },
                headers={"X-Request-ID": "req_error", "Retry-After": "17"},
            )
            responses.append(response)
            return response

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            with pytest.raises(ApiError) as error:
                async with SessionStream(client.api.sessions("ses_1")):
                    pass
            assert error.value.status == status and error.value.request_id == "req_error"
            assert error.value.retry_after == "17" and error.value.details == {"cause": "test"}
            assert len(responses) == 1 and responses[0].is_closed

    asyncio.run(scenario())


def test_session_transport_error_is_not_retried() -> None:
    async def scenario() -> None:
        calls = 0

        def handle(request: httpx2.Request) -> httpx2.Response:
            nonlocal calls
            calls += 1
            raise httpx2.ConnectError("disconnected", request=request)

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            with pytest.raises(TransportError):
                async with SessionStream(client.api.sessions("ses_1")):
                    pass
        assert calls == 1

    asyncio.run(scenario())


@pytest.mark.parametrize("stop", ["local", "cancel", "client"])
def test_session_blocked_read_cleanup_is_local_and_releases_owned_transport(stop: str) -> None:
    async def scenario() -> None:
        reading = asyncio.Event()
        released = asyncio.Event()
        calls = []

        class Body(httpx2.AsyncByteStream):
            async def __aiter__(self):
                reading.set()
                await asyncio.Event().wait()
                yield b""

            async def aclose(self):
                released.set()

        def handle(request: httpx2.Request) -> httpx2.Response:
            calls.append(request)
            return httpx2.Response(200, stream=Body(), headers={"Content-Type": "text/event-stream"})

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            async with SessionStream(client.api.sessions("ses_1")) as stream:
                reader = asyncio.create_task(anext(stream))
                await reading.wait()
                if stop == "local":
                    await asyncio.wait_for(stream.aclose(), 1)
                    with pytest.raises(StopAsyncIteration):
                        await reader
                else:
                    if stop == "cancel":
                        reader.cancel()
                    else:
                        await asyncio.wait_for(client.aclose(), 1)
                    with pytest.raises(asyncio.CancelledError):
                        await reader
                assert stream.is_closed and released.is_set()
        assert len(calls) == 1 and calls[0].method == "GET"

    asyncio.run(scenario())


@pytest.mark.parametrize("limit", [None, 1_048_576])
def test_session_large_snapshot_has_no_default_cap_and_explicit_limit_closes(limit: int | None) -> None:
    async def scenario() -> None:
        snapshot = session_items()
        snapshot["items"] = [display_item(index) for index in range(1, 41)]
        for item in snapshot["items"]:
            item["content"]["text"] = "x" * 32_000
        data = sse("items", snapshot)
        assert len(data) > 1_048_576
        responses = []

        def handle(_request: httpx2.Request) -> httpx2.Response:
            response = httpx2.Response(200, content=data, headers={"Content-Type": "text/event-stream"})
            responses.append(response)
            return response

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            options = {} if limit is None else {"max_event_bytes": limit}
            async with SessionStream(client.api.sessions("ses_1"), **options) as stream:
                if limit is None:
                    frame = await anext(stream)
                    assert isinstance(frame, SessionItemsFrame)
                    assert len(frame.data.items) == 40
                    assert frame.data.items[-1].content.to_dict()["text"] == "x" * 32_000
                else:
                    with pytest.raises(ProtocolError, match="bound"):
                        await anext(stream)
                    assert stream.is_closed
            assert len(responses) == 1 and responses[0].is_closed

    asyncio.run(scenario())


def test_session_close_before_entry_does_not_open_a_connection() -> None:
    async def scenario() -> None:
        requests = []

        def handle(request: httpx2.Request) -> httpx2.Response:
            requests.append(request)
            return httpx2.Response(200, content=b"", headers={"Content-Type": "text/event-stream"})

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            stream = SessionStream(client.api.sessions("ses_1"))
            await stream.aclose()
            with pytest.raises(RuntimeError, match="single-use"):
                async with stream:
                    pass
            assert stream.is_closed and not requests
            assert not client._streams

    asyncio.run(scenario())


def test_session_error_body_disconnect_is_transport_error_and_releases_response() -> None:
    async def scenario() -> None:
        responses = []
        released = asyncio.Event()

        class Body(httpx2.AsyncByteStream):
            async def __aiter__(self):
                yield b'{"error":'
                raise httpx2.ReadError("error body disconnected")

            async def aclose(self):
                released.set()

        def handle(_request: httpx2.Request) -> httpx2.Response:
            response = httpx2.Response(503, stream=Body())
            responses.append(response)
            return response

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            stream = SessionStream(client.api.sessions("ses_1"))
            with pytest.raises(TransportError):
                async with stream:
                    pass
            assert stream.is_closed and released.is_set()
            assert len(responses) == 1 and responses[0].is_closed
            assert not client._streams

    asyncio.run(scenario())


def test_session_validator_is_cached_and_unknown_events_ignore_payload() -> None:
    assert _validators() is _validators()
    assert _session_frame("future", ["invalid-json"], "not-a-cursor") is None
