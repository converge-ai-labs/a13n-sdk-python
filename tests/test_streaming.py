import asyncio
import json

import httpx2
import pytest

from a13n import Client, ReplayGap, RunStream, TransportError

NOW = "2026-09-17T00:00:00Z"


def event_value(*, event_type: str = "a13n.item.delta", run_id: str = "run_1") -> dict:
    return {
        "schema_version": "1",
        "event_id": "rse_" + "a" * 20,
        "event_type": event_type,
        "run_id": run_id,
        "thread_id": "thread_1",
        "occurred_at": NOW,
        "payload": {"text": "hello"},
    }


def frame(*, cursor: str = "100-0", event_type: str = "a13n.item.delta", value: dict | None = None) -> bytes:
    return (
        f"id: {cursor}\nevent: {event_type}\ndata: {json.dumps(value or event_value(event_type=event_type))}\n\n"
    ).encode()


class Chunks(httpx2.AsyncByteStream):
    def __init__(self, chunks: list[bytes]) -> None:
        self.chunks = chunks
        self.closed = False

    async def __aiter__(self):
        for chunk in self.chunks:
            yield chunk

    async def aclose(self) -> None:
        self.closed = True


def test_run_stream_is_io_free_single_use_and_resumes_after_next_read_acknowledgement() -> None:
    first = Chunks([frame(cursor="100-0")])
    second = Chunks([frame(cursor="101-0", event_type="run.completed")])
    requests: list[httpx2.Request] = []
    attachments = 0

    async def handler(request: httpx2.Request) -> httpx2.Response:
        nonlocal attachments
        requests.append(request)
        if request.url.path.endswith("/stream"):
            attachments += 1
            body = first if attachments == 1 else second
            return httpx2.Response(
                200,
                stream=body,
                headers={"content-type": "text/event-stream", "x-request-id": f"req_{attachments}"},
            )
        if request.url.path == "/api/v1/runs/run_1":
            return httpx2.Response(200, json=_run_value("running"))
        if request.url.path.endswith("/items"):
            return httpx2.Response(
                200,
                json={
                    "complete": False,
                    "finalized": False,
                    "incomplete_reason": "running",
                    "items": [],
                    "next_cursor": None,
                    "projection_cursor": None,
                    "snapshot_version": 1,
                },
            )
        raise AssertionError(request.url.path)

    async def scenario() -> None:
        async with Client("https://service.example", "token", transport=httpx2.MockTransport(handler)) as client:
            stream = client.runs("run_1").stream(after="99-0", max_reconnects=1)
            assert isinstance(stream, RunStream)
            assert requests == [] and stream.response is None and not stream.is_closed
            async with stream as entered:
                assert entered is stream
                first_observation = await anext(stream)
                assert first_observation.cursor == "100-0"
                assert stream.last_received_cursor == "100-0"
                second_observation = await anext(stream)
                assert second_observation.cursor == "101-0"
                with pytest.raises(StopAsyncIteration):
                    await anext(stream)
            assert stream.is_closed
            assert stream.response is not None and stream.response.request_id == "req_2"
            stream_requests = [request for request in requests if request.url.path.endswith("/stream")]
            assert stream_requests[0].headers["last-event-id"] == "99-0"
            assert stream_requests[1].headers["last-event-id"] == "100-0"
            with pytest.raises(RuntimeError, match="single-use"):
                await stream.__aenter__()
        assert first.closed and second.closed

    asyncio.run(scenario())


def test_stream_control_is_independent_of_blocked_read_and_local_close() -> None:
    read_started = asyncio.Event()
    release = asyncio.Event()
    body_closed = asyncio.Event()

    class LiveBody(httpx2.AsyncByteStream):
        async def __aiter__(self):
            read_started.set()
            await release.wait()
            yield frame(event_type="run.cancelled")

        async def aclose(self) -> None:
            body_closed.set()
            release.set()

    async def handler(request: httpx2.Request) -> httpx2.Response:
        if request.url.path.endswith("/stream"):
            return httpx2.Response(200, stream=LiveBody(), headers={"content-type": "text/event-stream"})
        if request.url.path.endswith("/steer"):
            return httpx2.Response(
                202,
                json={
                    "accepted_at": NOW,
                    "delivery_sequence": 1,
                    "run_id": "run_1",
                    "session_id": "session_1",
                    "steer_id": "steer_1",
                    "thread_id": "thread_1",
                    "schema_version": "1",
                },
            )
        raise AssertionError(request.url.path)

    async def scenario() -> None:
        async with Client("https://service.example", "token", transport=httpx2.MockTransport(handler)) as client:
            stream = client.runs("run_1").stream(reconnect=False)
            async with stream:
                pending = asyncio.create_task(anext(stream))
                await read_started.wait()
                receipt = await stream.steer("Redirect", idempotency_key="steer-1")
                assert receipt.value.steer_id == "steer_1"
                await stream.aclose()
                with pytest.raises(StopAsyncIteration):
                    await pending
                assert body_closed.is_set()
            receipt = await stream.steer("Again", idempotency_key="steer-2")
            assert receipt.value.delivery_sequence == 1

    asyncio.run(scenario())


def test_empty_eof_has_finite_recovery_and_does_not_claim_completion(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("a13n.streaming.random.uniform", lambda _low, _high: 0.0)
    attachments = 0

    async def handler(request: httpx2.Request) -> httpx2.Response:
        nonlocal attachments
        if request.url.path.endswith("/stream"):
            attachments += 1
            return httpx2.Response(200, content=b"", headers={"content-type": "text/event-stream"})
        if request.url.path == "/api/v1/runs/run_1":
            return httpx2.Response(200, json=_run_value("running"))
        if request.url.path.endswith("/items"):
            return httpx2.Response(
                200,
                json={
                    "complete": False,
                    "finalized": False,
                    "incomplete_reason": "running",
                    "items": [],
                    "next_cursor": None,
                    "projection_cursor": None,
                    "snapshot_version": 1,
                },
            )
        raise AssertionError(request.url.path)

    async def scenario() -> None:
        async with Client("https://service.example", "token", transport=httpx2.MockTransport(handler)) as client:
            with pytest.raises(TransportError, match="ended"):
                async with client.runs("run_1").stream(max_reconnects=2) as stream:
                    await anext(stream)
                pytest.fail("unconfirmed EOF must not become success")
        assert attachments == 3

    asyncio.run(scenario())


def test_attachment_replay_gap_is_not_retried() -> None:
    calls = 0

    async def handler(_request: httpx2.Request) -> httpx2.Response:
        nonlocal calls
        calls += 1
        return httpx2.Response(
            409,
            json={
                "error": {
                    "code": "run_stream_replay_gap",
                    "message": "History expired",
                    "details": {
                        "requested_cursor": "10-0",
                        "retained_floor": "50-0",
                        "high_watermark": "100-0",
                    },
                    "request_id": "req_gap",
                }
            },
            headers={"x-request-id": "req_gap"},
        )

    async def scenario() -> None:
        async with Client("https://service.example", "token", transport=httpx2.MockTransport(handler)) as client:
            with pytest.raises(ReplayGap) as caught:
                async with client.runs("run_1").stream(after="10-0"):
                    pass
            assert caught.value.requested_cursor == "10-0"
            assert caught.value.available_floor == "50-0"
            assert caught.value.high_watermark == "100-0"
            assert caught.value.request_id == "req_gap"
        assert calls == 1

    asyncio.run(scenario())


def test_close_before_entry_sends_no_request() -> None:
    calls = 0

    async def handler(_request: httpx2.Request) -> httpx2.Response:
        nonlocal calls
        calls += 1
        return httpx2.Response(500)

    async def scenario() -> None:
        async with Client("https://service.example", transport=httpx2.MockTransport(handler)) as client:
            stream = client.runs("run_1").stream()
            await stream.aclose()
            assert stream.is_closed
            with pytest.raises(RuntimeError):
                await stream.__aenter__()
        assert calls == 0

    asyncio.run(scenario())


def _run_value(status: str) -> dict:
    return {
        "agent_id": "agent_1",
        "agent_revision_id": "revision_1",
        "completed_at": None,
        "created_at": NOW,
        "effective_agent_config_digest": "digest",
        "environment_access": None,
        "environment_id": None,
        "failure": None,
        "id": "run_1",
        "input": None,
        "input_kind": "text",
        "input_text": None,
        "labels": {},
        "lineage_kind": "root",
        "output": None,
        "output_text": None,
        "parent_run_id": None,
        "pending": None,
        "retry_of_run_id": None,
        "sealed_at": None,
        "sealed_state_digest_sha256": None,
        "session_id": "session_1",
        "started_at": NOW,
        "status": status,
        "thread_id": "thread_1",
        "trigger_type": "user",
        "updated_at": NOW,
        "version": 1,
        "wait_reason": None,
        "waiting_at": None,
    }


@pytest.mark.parametrize("stage", ["entry", "backoff"])
def test_close_interrupts_pending_entry(stage: str, monkeypatch: pytest.MonkeyPatch) -> None:
    started = asyncio.Event()
    released = asyncio.Event()
    monkeypatch.setattr("a13n.streaming.random.uniform", lambda _low, _high: 10.0)

    async def handler(_request: httpx2.Request) -> httpx2.Response:
        started.set()
        if stage == "entry":
            await released.wait()
        return httpx2.Response(
            503, json={"error": {"code": "unavailable", "message": "Retry", "request_id": "req_1", "details": {}}}
        )

    async def scenario() -> None:
        async with Client("https://service.example", transport=httpx2.MockTransport(handler)) as client:
            stream = client.runs("run_1").stream()
            entry = asyncio.create_task(stream.__aenter__())
            await started.wait()
            await asyncio.sleep(0)
            await asyncio.wait_for(stream.aclose(), 1)
            with pytest.raises(RuntimeError, match="closed"):
                await entry
            assert stream.is_closed

    asyncio.run(scenario())


def test_read_cancellation_is_not_normal_eof_and_concurrent_reader_is_rejected() -> None:
    started = asyncio.Event()
    released = asyncio.Event()
    body_closed = asyncio.Event()

    class Body(httpx2.AsyncByteStream):
        async def __aiter__(self):
            started.set()
            await released.wait()
            yield frame()

        async def aclose(self):
            body_closed.set()

    async def handler(_request: httpx2.Request) -> httpx2.Response:
        return httpx2.Response(200, stream=Body(), headers={"Content-Type": "text/event-stream"})

    async def scenario() -> None:
        async with Client("https://service.example", transport=httpx2.MockTransport(handler)) as client:
            async with client.runs("run_1").stream() as stream:
                reader = asyncio.create_task(anext(stream))
                await started.wait()
                with pytest.raises(RuntimeError, match="one active reader"):
                    await anext(stream)
                reader.cancel()
                with pytest.raises(asyncio.CancelledError):
                    await reader
                assert stream.is_closed and body_closed.is_set()
                with pytest.raises(StopAsyncIteration):
                    await anext(stream)

    asyncio.run(scenario())


@pytest.mark.parametrize("body", [frame()[:-1], b"data: unfinished", frame(value=event_value(run_id="other"))])
def test_protocol_failure_closes_stream_without_reconnecting(body: bytes) -> None:
    from a13n import ProtocolError

    calls = 0

    async def handler(_request: httpx2.Request) -> httpx2.Response:
        nonlocal calls
        calls += 1
        return httpx2.Response(200, content=body, headers={"content-type": "text/event-stream"})

    async def scenario() -> None:
        async with Client("https://service.example", transport=httpx2.MockTransport(handler)) as client:
            async with client.runs("run_1").stream() as stream:
                with pytest.raises(ProtocolError):
                    await anext(stream)
                assert stream.is_closed and stream.last_received_cursor is None
                with pytest.raises(StopAsyncIteration):
                    await anext(stream)
        assert calls == 1

    asyncio.run(scenario())


def test_in_stream_gap_has_no_checkpoint_or_retry() -> None:
    body = b'event: a13n.service.replay_gap\ndata: {"run_id":"run_1","requested_cursor":"1-0","retained_floor":"9-0","high_watermark":"12-0"}\n\n'

    async def handler(_request: httpx2.Request) -> httpx2.Response:
        return httpx2.Response(200, content=body, headers={"content-type": "text/event-stream"})

    async def scenario() -> None:
        async with Client("https://service.example", transport=httpx2.MockTransport(handler)) as client:
            async with client.runs("run_1").stream(after="1-0") as stream:
                with pytest.raises(ReplayGap) as caught:
                    await anext(stream)
                assert caught.value.requested_cursor == "1-0"
                assert caught.value.available_floor == "9-0"
                assert caught.value.high_watermark == "12-0"
                assert stream.is_closed and stream.last_received_cursor is None

    asyncio.run(scenario())


def test_disabled_reconnection_eof_does_not_read_evidence() -> None:
    calls = []

    async def handler(request: httpx2.Request) -> httpx2.Response:
        calls.append(request.url.path)
        assert request.url.path.endswith("/stream")
        return httpx2.Response(200, content=b"", headers={"Content-Type": "text/event-stream"})

    async def scenario() -> None:
        async with Client("https://service.example", transport=httpx2.MockTransport(handler)) as client:
            async with client.runs("run_1").stream(reconnect=False) as stream:
                assert stream.response is not None
                assert stream.response.headers["Content-Type"] == "text/event-stream"
                with pytest.raises(StopAsyncIteration):
                    await anext(stream)
                assert stream.is_closed
        assert len(calls) == 1

    asyncio.run(scenario())


def test_transient_read_failure_reconnects_after_acknowledged_cursor(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("a13n.streaming.random.uniform", lambda _low, _high: 0.0)
    calls = []

    class Disconnected(httpx2.AsyncByteStream):
        async def __aiter__(self):
            yield frame(cursor="20-0")
            raise httpx2.ReadError("connection lost")

    async def handler(request: httpx2.Request) -> httpx2.Response:
        calls.append(request)
        if len(calls) == 1:
            return httpx2.Response(200, stream=Disconnected(), headers={"content-type": "text/event-stream"})
        assert request.headers["Last-Event-ID"] == "20-0"
        return httpx2.Response(
            200, content=frame(cursor="21-0", event_type="run.completed"), headers={"content-type": "text/event-stream"}
        )

    async def scenario() -> None:
        async with Client("https://service.example", transport=httpx2.MockTransport(handler)) as client:
            async with client.runs("run_1").stream() as stream:
                assert (await anext(stream)).cursor == "20-0"
                assert (await anext(stream)).cursor == "21-0"
                with pytest.raises(StopAsyncIteration):
                    await anext(stream)
        assert len(calls) == 2

    asyncio.run(scenario())


def test_local_close_waits_for_read_only_not_consumer_business_code() -> None:
    reading = asyncio.Event()
    close_finished = asyncio.Event()
    released = asyncio.Event()
    body_closed = asyncio.Event()

    class Body(httpx2.AsyncByteStream):
        async def __aiter__(self):
            reading.set()
            await released.wait()
            yield frame()

        async def aclose(self):
            body_closed.set()

    async def handler(_request: httpx2.Request) -> httpx2.Response:
        return httpx2.Response(200, stream=Body(), headers={"content-type": "text/event-stream"})

    async def scenario() -> None:
        async with Client("https://service.example", transport=httpx2.MockTransport(handler)) as client:
            async with client.runs("run_1").stream() as stream:

                async def consumer() -> None:
                    async for _ in stream:
                        pass
                    await close_finished.wait()

                consumer_task = asyncio.create_task(consumer())
                await reading.wait()
                await asyncio.wait_for(stream.aclose(), 1)
                assert body_closed.is_set() and not consumer_task.done()
                close_finished.set()
                await consumer_task

    asyncio.run(scenario())


def test_client_close_interrupts_logical_stream_backoff(monkeypatch: pytest.MonkeyPatch) -> None:
    backing_off = asyncio.Event()
    calls = 0

    def delay(_low: float, _high: float) -> float:
        backing_off.set()
        return 10.0

    monkeypatch.setattr("a13n.streaming.random.uniform", delay)

    async def handler(_request: httpx2.Request) -> httpx2.Response:
        nonlocal calls
        calls += 1
        return httpx2.Response(
            503, json={"error": {"code": "unavailable", "message": "Retry", "request_id": "req_1", "details": {}}}
        )

    async def scenario() -> None:
        client = Client("https://service.example", transport=httpx2.MockTransport(handler))
        stream = client.runs("run_1").stream()
        entry = asyncio.create_task(stream.__aenter__())
        await backing_off.wait()
        await asyncio.wait_for(client.aclose(), 1)
        with pytest.raises(asyncio.CancelledError):
            await entry
        assert stream.is_closed and calls == 1

    asyncio.run(scenario())


def test_error_body_transport_loss_uses_bounded_recovery(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("a13n.streaming.random.uniform", lambda _low, _high: 0.0)
    calls = 0
    closed = []

    class BrokenError(httpx2.AsyncByteStream):
        async def __aiter__(self):
            yield b'{"error":'
            raise httpx2.ReadError("lost error body")

        async def aclose(self):
            closed.append(True)

    async def handler(_request: httpx2.Request) -> httpx2.Response:
        nonlocal calls
        calls += 1
        return httpx2.Response(503, stream=BrokenError())

    async def scenario() -> None:
        async with Client("https://service.example", transport=httpx2.MockTransport(handler)) as client:
            stream = client.runs("run_1").stream(max_reconnects=2)
            with pytest.raises(TransportError):
                await stream.__aenter__()
            assert stream.is_closed and calls == 3 and len(closed) == 3

    asyncio.run(scenario())


def test_repeated_cursor_does_not_reset_recovery_budget(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("a13n.streaming.random.uniform", lambda _low, _high: 0.0)
    attachments = 0

    class Repeated(httpx2.AsyncByteStream):
        async def __aiter__(self):
            yield frame(cursor="20-0")
            raise httpx2.ReadError("disconnected")

    async def handler(_request: httpx2.Request) -> httpx2.Response:
        nonlocal attachments
        attachments += 1
        return httpx2.Response(200, stream=Repeated(), headers={"content-type": "text/event-stream"})

    async def scenario() -> None:
        async with Client("https://service.example", transport=httpx2.MockTransport(handler)) as client:
            async with client.runs("run_1").stream(max_reconnects=1) as stream:
                await anext(stream)
                await anext(stream)
                with pytest.raises(TransportError):
                    await anext(stream)
                assert stream.is_closed and attachments == 2

    asyncio.run(scenario())


@pytest.mark.parametrize("matching_projection", [True, False])
def test_empty_terminal_attachment_requires_exact_finalized_projection(
    matching_projection: bool, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr("a13n.streaming.random.uniform", lambda _low, _high: 0.0)
    paths = []

    async def handler(request: httpx2.Request) -> httpx2.Response:
        paths.append(request.url.path)
        if request.url.path.endswith("/stream"):
            return httpx2.Response(200, content=b"", headers={"content-type": "text/event-stream"})
        if request.url.path.endswith("/items"):
            return httpx2.Response(
                200,
                json={
                    "complete": True,
                    "finalized": True,
                    "incomplete_reason": None,
                    "items": [],
                    "next_cursor": None,
                    "projection_cursor": "20-0" if matching_projection else "21-0",
                    "snapshot_version": 1,
                },
            )
        return httpx2.Response(200, json=_run_value("completed"))

    async def scenario() -> None:
        async with Client("https://service.example", transport=httpx2.MockTransport(handler)) as client:
            async with client.runs("run_1").stream(after="20-0", max_reconnects=1) as stream:
                with pytest.raises(StopAsyncIteration if matching_projection else TransportError):
                    await anext(stream)
                assert stream.is_closed and stream.last_received_cursor is None
        assert len(paths) == (3 if matching_projection else 6)

    asyncio.run(scenario())


def test_client_close_waits_for_owned_io_not_consumer_business_code() -> None:
    reading = asyncio.Event()
    close_returned = asyncio.Event()
    released = asyncio.Event()
    body_closed = asyncio.Event()
    consumer_cancelled = asyncio.Event()

    class Body(httpx2.AsyncByteStream):
        async def __aiter__(self):
            reading.set()
            await released.wait()
            yield frame()

        async def aclose(self):
            body_closed.set()

    async def handler(_request: httpx2.Request) -> httpx2.Response:
        return httpx2.Response(200, stream=Body(), headers={"content-type": "text/event-stream"})

    async def scenario() -> None:
        client = Client("https://service.example", transport=httpx2.MockTransport(handler))
        stream = client.runs("run_1").stream()

        async def consumer() -> None:
            try:
                async with stream:
                    await anext(stream)
            except asyncio.CancelledError:
                consumer_cancelled.set()
            await close_returned.wait()

        consumer_task = asyncio.create_task(consumer())
        try:
            await reading.wait()
            await asyncio.wait_for(client.aclose(), 1)
            assert consumer_cancelled.is_set()
            assert body_closed.is_set() and stream.is_closed
            assert not consumer_task.done()
            assert not client._tasks
        finally:
            close_returned.set()
            await consumer_task
            await client.aclose()

    asyncio.run(scenario())
