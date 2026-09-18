import asyncio
import importlib.util
from pathlib import Path
from types import SimpleNamespace

import httpx2
import pytest

SCRIPT = Path(__file__).parents[1] / "service_acceptance.py"
SPEC = importlib.util.spec_from_file_location("service_acceptance", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
service_acceptance = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(service_acceptance)


def test_acceptance_identity_mismatch_is_runtime_error() -> None:
    accepted = SimpleNamespace(
        receipt=SimpleNamespace(
            value=SimpleNamespace(run_id="run_wrong", thread_id="thread_1", session_id="session_1")
        ),
        run=SimpleNamespace(id="run_1"),
        thread=SimpleNamespace(id="thread_1"),
        session=SimpleNamespace(id="session_1"),
    )

    with pytest.raises(RuntimeError, match="receipt identities"):
        service_acceptance._accepted_evidence(accepted)


class Chunks(httpx2.AsyncByteStream):
    def __init__(self, chunks: list[bytes]) -> None:
        self.chunks = chunks
        self.closed = False

    async def __aiter__(self):
        for chunk in self.chunks:
            yield chunk

    async def aclose(self) -> None:
        self.closed = True


def test_disconnect_transport_fails_after_one_complete_data_event() -> None:
    body = Chunks(
        [
            b": heartbeat\r\n\r\nid: 1-0\r\nevent: run.accepted\r\n",
            b"data: {}\r\n\r\nid: 2-0\r\nevent: run.completed\r\ndata: {}\r\n\r\n",
        ]
    )

    async def handler(_request: httpx2.Request) -> httpx2.Response:
        return httpx2.Response(200, stream=body, headers={"content-type": "text/event-stream"})

    async def scenario() -> None:
        transport = service_acceptance.DisconnectAfterEventTransport(httpx2.MockTransport(handler))
        request = httpx2.Request("GET", "https://service.example/api/v1/runs/run_1/stream")
        response = await transport.handle_async_request(request)
        iterator = response.stream.__aiter__()
        assert await anext(iterator) == b": heartbeat\r\n\r\n"
        first = await anext(iterator)
        assert first.endswith(b"data: {}\r\n\r\n")
        with pytest.raises(httpx2.ReadError, match="Injected Run SSE disconnect"):
            await anext(iterator)
        assert transport.disconnects == 1
        assert transport.last_event_ids == [None]
        assert body.closed
        await transport.aclose()

    asyncio.run(scenario())
