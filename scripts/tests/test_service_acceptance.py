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


def test_native_configuration_acceptance_uses_real_generated_forwarding_locally() -> None:
    import json

    from a13n import Client
    from tests.test_interaction import entry_view, run_view, submitted

    async def scenario() -> None:
        configurations: dict[str, dict] = {}
        posts: list[dict] = []

        def handle(request: httpx2.Request) -> httpx2.Response:
            if request.method == "POST":
                body = json.loads(request.content)
                posts.append(body)
                run_id = f"run_{len(posts)}"
                configurations[run_id] = body["options"]["configuration"]
                receipt = submitted()
                receipt["run"]["id"] = run_id
                return httpx2.Response(201, json=receipt)
            if request.url.path.endswith("/inbox/ent_1"):
                entry = entry_view(status="consumed")
                entry["assigned_run_id"] = f"run_{len(posts)}"
                return httpx2.Response(200, json=entry)
            run_id = request.url.path.rsplit("/", 1)[-1]
            view = run_view(run_id=run_id, status="completed")
            view["options"] = {"configuration": configurations[run_id]}
            return httpx2.Response(200, json=view)

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            evidence = await service_acceptance._configuration_acceptance(client, "agt_1")
        assert evidence["snapshot_readback"] is True
        assert posts[1]["delivery"] == "next_run"
        assert configurations["run_1"] != configurations["run_2"]
        assert configurations["run_1"]["extensions"]["sdk.acceptance"]["enabled"] is False

    asyncio.run(scenario())


def test_acceptance_rejects_lost_or_changed_configuration_readback() -> None:
    from a13n.generated import models as wire
    from tests.test_interaction import run_view

    expected = service_acceptance._configuration("readback")
    with pytest.raises(RuntimeError, match="configuration snapshot"):
        service_acceptance._assert_configuration(wire.RunView.from_dict(run_view()), expected)
    changed = run_view()
    changed["options"] = {"configuration": {"allowed_hosts": [], "extensions": {}}}
    with pytest.raises(RuntimeError, match="configuration snapshot"):
        service_acceptance._assert_configuration(wire.RunView.from_dict(changed), expected)


def test_acceptance_identity_mismatch_is_runtime_error() -> None:
    submitted = SimpleNamespace(
        receipt=SimpleNamespace(
            value=SimpleNamespace(
                thread=SimpleNamespace(id="thr_wrong"), entry=SimpleNamespace(id="ent_1", thread_id="thr_1"), run=None
            )
        ),
        thread=SimpleNamespace(id="thr_1"),
        entry=SimpleNamespace(id="ent_1"),
        run=None,
    )
    with pytest.raises(RuntimeError, match="receipt identities"):
        service_acceptance._submission_evidence(submitted)


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
            b": heartbeat\r\n\r\nid: 1-0\r\nevent: boundary\r\n",
            b'data: {"run_id":"run_1"}\r\n\r\nid: 2-0\r\nevent: delta\r\ndata: {}\r\n\r\n',
        ]
    )

    async def handler(_request: httpx2.Request) -> httpx2.Response:
        return httpx2.Response(200, stream=body, headers={"content-type": "text/event-stream"})

    async def scenario() -> None:
        transport = service_acceptance.DisconnectAfterEventTransport(httpx2.MockTransport(handler))
        request = httpx2.Request("GET", "https://service.example/api/v1/workspaces/ws_1/threads/thr_1/stream")
        response = await transport.handle_async_request(request)
        iterator = response.stream.__aiter__()
        assert await anext(iterator) == b": heartbeat\r\n\r\n"
        first = await anext(iterator)
        assert first.endswith(b'data: {"run_id":"run_1"}\r\n\r\n')
        with pytest.raises(httpx2.ReadError, match="Injected Thread SSE disconnect"):
            await anext(iterator)
        assert transport.disconnects == 1
        assert transport.last_event_ids == [None]
        assert body.closed
        await transport.aclose()

    asyncio.run(scenario())
