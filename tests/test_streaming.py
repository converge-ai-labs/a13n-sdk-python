import asyncio
import json

import httpx2
import pytest

from a13n import Client, ProtocolError, ThreadFrame, TransportError


def sse(event: str, data: dict, cursor: str | None = None) -> bytes:
    return (
        f"event: {event}\n" + (f"id: {cursor}\n" if cursor is not None else "") + f"data: {json.dumps(data)}\n\n"
    ).encode()


def test_thread_stream_parses_all_five_frames_and_requires_readback() -> None:
    async def scenario() -> None:
        requests: list[httpx2.Request] = []
        stream_data = b"".join(
            [
                sse(
                    "delta",
                    {
                        "run_id": "run_1",
                        "attempt": 1,
                        "sequence": 1,
                        "event": {"type": "TEXT_MESSAGE_CONTENT"},
                        "item": None,
                    },
                    "100-0",
                ),
                sse("boundary", {"run_id": "run_1", "attempt": 1, "sequence": 1}, "101-0"),
                sse("changed", {"version": 2}),
                sse("reset", {"run_id": "run_1"}),
                sse("gap", {"run_id": "run_1"}),
            ]
        )

        def handle(request: httpx2.Request) -> httpx2.Response:
            requests.append(request)
            return httpx2.Response(
                200, content=stream_data, headers={"Content-Type": "text/event-stream", "X-Request-Id": "req_1"}
            )

        async with Client("https://service.example", "secret", transport=httpx2.MockTransport(handle)) as client:
            thread = client.workspaces("ws_1").threads("thr_1")
            stream = thread.stream(reconnect=False)
            assert not requests
            async with stream:
                frames = [frame async for frame in stream]
                assert all(isinstance(frame, ThreadFrame) for frame in frames)
                assert stream.last_received_cursor == "101-0"
                assert stream.response and stream.response.request_id == "req_1"
            assert [frame.event_type for frame in frames] == ["delta", "boundary", "changed", "reset", "gap"]
            assert [frame.cursor for frame in frames] == ["100-0", "101-0", None, None, None]
            assert requests[0].url.path == "/api/v1/workspaces/ws_1/threads/thr_1/stream"
            with pytest.raises(RuntimeError, match="single-use"):
                async with stream:
                    pass

    asyncio.run(scenario())


def test_thread_stream_reconnects_only_after_applied_frame_cursor(monkeypatch: pytest.MonkeyPatch) -> None:
    async def scenario() -> None:
        seen: list[str | None] = []

        def handle(request: httpx2.Request) -> httpx2.Response:
            seen.append(request.headers.get("last-event-id"))
            cursor = "100-0" if len(seen) == 1 else "101-0"
            return httpx2.Response(
                200,
                content=sse("boundary", {"run_id": "run_1", "attempt": 1, "sequence": len(seen)}, cursor),
                headers={"Content-Type": "text/event-stream"},
            )

        monkeypatch.setattr("a13n.streaming.random.uniform", lambda _low, _high: 0)
        async with Client("https://service.example", "token", transport=httpx2.MockTransport(handle)) as client:
            async with client.workspaces("ws_1").threads("thr_1").stream(max_reconnects=1) as stream:
                first = await anext(stream)
                second = await anext(stream)
                assert (first.cursor, second.cursor) == ("100-0", "101-0")
            assert seen == [None, "100-0"]

    asyncio.run(scenario())


@pytest.mark.parametrize("cursor", ["", "1", "bad-id", "1-2\nInjected: evil", "123456789012345678901-0"])
def test_thread_stream_rejects_bad_cursors_before_io(cursor: str) -> None:
    async def scenario() -> None:
        async with Client("https://service.example", "token") as client:
            with pytest.raises(ValueError):
                client.workspaces("ws_1").threads("thr_1").stream(after=cursor)

    asyncio.run(scenario())


@pytest.mark.parametrize(
    "data",
    [
        sse("gap", {"run_id": "run_1"}, "100-0"),
        sse("delta", {"run_id": "run_1", "attempt": 1, "sequence": 1, "event": {}, "item": None}),
        b"event: boundary\ndata: not-json\n\n",
    ],
)
def test_malformed_frame_is_not_silent_recovery(data: bytes) -> None:
    async def scenario() -> None:
        transport = httpx2.MockTransport(
            lambda _request: httpx2.Response(200, content=data, headers={"Content-Type": "text/event-stream"})
        )
        async with Client("https://service.example", "token", transport=transport) as client:
            async with client.workspaces("ws_1").threads("thr_1").stream(reconnect=False) as stream:
                with pytest.raises(ProtocolError):
                    await anext(stream)

    asyncio.run(scenario())


def test_gap_only_attachments_do_not_reset_retry_budget(monkeypatch: pytest.MonkeyPatch) -> None:
    async def scenario() -> None:
        count = 0

        def handle(_request: httpx2.Request) -> httpx2.Response:
            nonlocal count
            count += 1
            return httpx2.Response(
                200, content=sse("gap", {"run_id": "run_1"}), headers={"Content-Type": "text/event-stream"}
            )

        monkeypatch.setattr("a13n.streaming.random.uniform", lambda _low, _high: 0)
        async with Client("https://service.example", "token", transport=httpx2.MockTransport(handle)) as client:
            async with client.workspaces("ws_1").threads("thr_1").stream(max_reconnects=2) as stream:
                for _ in range(3):
                    assert (await anext(stream)).event_type == "gap"
                with pytest.raises(TransportError):
                    await anext(stream)
            assert count == 3

    asyncio.run(scenario())


def test_bounded_eof_recovery_does_not_claim_run_completion(monkeypatch: pytest.MonkeyPatch) -> None:
    async def scenario() -> None:
        count = 0

        def handle(_request: httpx2.Request) -> httpx2.Response:
            nonlocal count
            count += 1
            return httpx2.Response(200, content=b"", headers={"Content-Type": "text/event-stream"})

        monkeypatch.setattr("a13n.streaming.random.uniform", lambda _low, _high: 0)
        async with Client("https://service.example", "token", transport=httpx2.MockTransport(handle)) as client:
            async with client.workspaces("ws_1").threads("thr_1").stream(max_reconnects=1) as stream:
                with pytest.raises(TransportError):
                    await anext(stream)
            assert count == 2

    asyncio.run(scenario())


@pytest.mark.parametrize(
    "event,data,cursor",
    [
        ("changed", {"version": True}, None),
        ("boundary", {"run_id": "r", "attempt": True, "sequence": 1}, "1-0"),
        ("delta", {"run_id": "r", "attempt": 1, "sequence": 1, "event": {}, "item": {}}, "1-0"),
        (
            "delta",
            {
                "run_id": "r",
                "attempt": 1,
                "sequence": 1,
                "event": {},
                "item": {"id": "i", "kind": "invalid", "state": "completed"},
            },
            "1-0",
        ),
    ],
)
def test_typed_frame_fields_are_validated(event: str, data: dict, cursor: str | None) -> None:
    from a13n.streaming import _frame

    with pytest.raises(ProtocolError):
        _frame(event, [json.dumps(data)], cursor)


def test_delta_exposes_readonly_typed_envelope_without_claiming_agui_validation() -> None:
    from a13n import DeltaFrame
    from a13n.streaming import _frame

    frame = _frame(
        "delta",
        [
            json.dumps(
                {
                    "run_id": "run_1",
                    "attempt": 2,
                    "sequence": 3,
                    "event": {"future_event": {"value": True}},
                    "item": {"id": "item_1", "kind": "tool_call", "state": "in_progress"},
                }
            )
        ],
        "100-0",
    )
    assert isinstance(frame, DeltaFrame)
    assert frame.data["attempt"] == 2
    assert frame.data["item"] is not None and frame.data["item"]["id"] == "item_1"
    assert frame.data["event"]["future_event"] == {"value": True}
    with pytest.raises(TypeError):
        frame.data["sequence"] = 4  # type: ignore[reportTypedDictNotRequiredAccess, reportTypedDictReadOnlyAccess]
