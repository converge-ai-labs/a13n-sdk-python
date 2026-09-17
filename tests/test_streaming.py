"""Run SSE framing, identity, recovery evidence, and client-owned lifetime."""

import asyncio
import json

import httpx2
import pytest

from a13n import ApiError, Client, ProtocolError, ReplayGap, TransportError


def event_value(**changes):
    return {
        "schema_version": "1",
        "event_id": "rse_" + "a" * 20,
        "event_type": "a13n.item.delta",
        "run_id": "run_1",
        "thread_id": "thread_1",
        "occurred_at": "2026-09-17T00:00:00Z",
        "payload": {"text": "你好"},
        **changes,
    }


def frame(value=None, cursor="100-0", event_type="a13n.item.delta", newline="\n"):
    lines = ([f"id: {cursor}"] if cursor is not None else []) + [
        f"event: {event_type}",
        "data: " + json.dumps(value or event_value(), ensure_ascii=False),
        "",
        "",
    ]
    return newline.join(lines).encode()


class Chunks(httpx2.AsyncByteStream):
    def __init__(self, chunks):
        self.chunks = chunks
        self.closed = False
        self.read = 0

    async def __aiter__(self):
        for chunk in self.chunks:
            self.read += 1
            yield chunk

    async def aclose(self):
        self.closed = True


@pytest.mark.parametrize("newline", ["\n", "\r", "\r\n"])
def test_split_utf8_sse_comments_versions_and_applied_cursor(newline):
    payload = ("\ufeff: heartbeat" + newline * 2).encode() + frame(newline=newline)
    body = Chunks([payload[i : i + 1] for i in range(len(payload))])
    requests = []

    async def handler(request):
        requests.append(request)
        assert request.url.path == "/prefix/api/v1/runs/run_1/stream"
        assert request.headers["accept"] == "text/event-stream"
        assert request.headers["last-event-id"] == "99-0"
        return httpx2.Response(200, stream=body, headers={"content-type": "text/event-stream; charset=utf-8"})

    async def scenario():
        async with Client("http://test/prefix", "secret", transport=httpx2.MockTransport(handler)) as client:
            applied = "99-0"
            async with client.runs("run_1").stream(after=applied) as stream:
                observed = [event async for event in stream]
            assert applied == "99-0"  # Receipt is not local application acknowledgement.
            assert len(observed) == 1
            assert observed[0].cursor == "100-0" and observed[0].event.run_id == "run_1"
            assert observed[0].event.payload.to_dict() == {"text": "你好"}
            assert "你好" not in repr(observed[0])
            assert body.closed and len(requests) == 1

    asyncio.run(scenario())


@pytest.mark.parametrize(
    "value,cursor,kind",
    [
        (event_value(schema_version="future"), "100-0", "a13n.item.delta"),
        (event_value(run_id="other"), "100-0", "a13n.item.delta"),
        (event_value(), "100-0", "a13n.other.type"),
        (event_value(), None, "a13n.item.delta"),
        (event_value(thread_id=None), "100-0", "a13n.item.delta"),
    ],
)
def test_malformed_events_are_not_yielded_or_retried(value, cursor, kind):
    body = Chunks([frame(value, cursor, kind)])

    async def handler(request):
        return httpx2.Response(200, stream=body, headers={"content-type": "text/event-stream"})

    async def scenario():
        async with Client("http://test", "secret", transport=httpx2.MockTransport(handler)) as client:
            with pytest.raises(ProtocolError):
                async with client.runs("run_1").stream() as stream:
                    await anext(stream)
            assert body.closed

    asyncio.run(scenario())


def test_replay_gap_after_attachment_retains_metadata_without_cursor():
    details = {"run_id": "run_1", "requested_cursor": "10-0", "available_floor": "50-0", "high_watermark": "100-0"}
    body = Chunks([frame(details, None, "a13n.service.replay_gap")])

    async def handler(request):
        return httpx2.Response(200, stream=body, headers={"content-type": "text/event-stream"})

    async def scenario():
        async with Client("http://test", "secret", transport=httpx2.MockTransport(handler)) as client:
            with pytest.raises(ReplayGap) as caught:
                async with client.runs("run_1").stream(after="10-0") as stream:
                    await anext(stream)
            assert caught.value.details == details
            assert caught.value.run_id == "run_1" and body.closed

    asyncio.run(scenario())


def test_attachment_409_is_api_error_with_gap_evidence():
    async def handler(request):
        return httpx2.Response(
            409,
            json={
                "error": {
                    "code": "run_stream_replay_gap",
                    "message": "History expired",
                    "details": {"available_floor": "50-0"},
                    "request_id": "req",
                }
            },
            headers={"x-request-id": "req"},
        )

    async def scenario():
        async with Client("http://test", "secret", transport=httpx2.MockTransport(handler)) as client:
            with pytest.raises(ApiError) as caught:
                async with client.runs("run_1").stream(after="10-0"):
                    pytest.fail("An unsuccessful attachment must not yield")
            assert caught.value.code == "run_stream_replay_gap" and caught.value.request_id == "req"
            assert caught.value.details == {"available_floor": "50-0"}

    asyncio.run(scenario())


@pytest.mark.parametrize(
    "body_data,limit", [(b"data: " + b"x" * 100, 64), (b"data: x\n" * 30 + b"\n", 100), (b"data: \xff\n\n", 100)]
)
def test_bounded_sse_invalid_utf8_and_oversized_events(body_data, limit):
    body = Chunks([body_data])

    async def handler(request):
        return httpx2.Response(200, stream=body, headers={"content-type": "text/event-stream"})

    async def scenario():
        async with Client("http://test", "secret", transport=httpx2.MockTransport(handler)) as client:
            with pytest.raises(ProtocolError):
                async with client.runs("run_1").stream(max_event_bytes=limit) as stream:
                    await anext(stream)
            assert body.closed

    asyncio.run(scenario())


def test_eof_partial_event_is_not_dispatched_and_early_break_closes():
    bodies = [Chunks([frame()[:-2]]), Chunks([frame(), frame(cursor="101-0")])]

    async def handler(request):
        return httpx2.Response(200, stream=bodies.pop(0), headers={"content-type": "text/event-stream"})

    first, second = bodies

    async def scenario():
        async with Client("http://test", "secret", transport=httpx2.MockTransport(handler)) as client:
            async with client.runs("run_1").stream() as stream:
                assert [item async for item in stream] == []
            assert first.closed
            async with client.runs("run_1").stream() as stream:
                async for item in stream:
                    assert item.cursor == "100-0"
                    break
            assert second.closed and second.read == 1

    asyncio.run(scenario())


def test_client_close_cancels_stream_even_after_nested_http_request():
    entered = asyncio.Event()
    closed = asyncio.Event()
    calls = []

    class LiveBody(httpx2.AsyncByteStream):
        async def __aiter__(self):
            yield frame()
            await asyncio.Event().wait()

        async def aclose(self):
            closed.set()

    async def handler(request):
        calls.append(request)
        if request.url.path.endswith("/stream"):
            return httpx2.Response(200, stream=LiveBody(), headers={"content-type": "text/event-stream"})
        return httpx2.Response(200, json={"items": [], "next_cursor": None})

    async def scenario():
        client = Client("http://test", "secret", transport=httpx2.MockTransport(handler))

        async def observe():
            async with client.runs("run_1").stream() as stream:
                await anext(stream)
                await client.workspaces("ws").agents.list()
                entered.set()
                await anext(stream)

        task = asyncio.create_task(observe())
        await asyncio.wait_for(entered.wait(), 1)
        await client.aclose()
        assert task.cancelled() and closed.is_set()
        assert len(calls) == 2 and not client._tasks
        with pytest.raises(TransportError, match="closed"):
            await client.workspaces("ws").agents.list()

    asyncio.run(scenario())


def test_close_in_current_stream_task_releases_transport_without_remote_mutation():
    body = Chunks([frame()])

    async def handler(request):
        assert request.method == "GET"
        return httpx2.Response(200, stream=body, headers={"content-type": "text/event-stream"})

    async def scenario():
        client = Client("http://test", "secret", transport=httpx2.MockTransport(handler))
        async with client.runs("run_1").stream() as stream:
            await anext(stream)
            await client.aclose()
            assert body.closed
        assert not client._tasks

    asyncio.run(scenario())
