"""Canonical native API entry and unchanged authored workflow integration."""

import asyncio

import httpx2
import pytest

from a13n import Client, TransportError
from tests.test_interaction import entry_view, run_view, submitted

FAMILIES = {
    "agents",
    "assets",
    "auth",
    "connections",
    "connector_providers",
    "environment_providers",
    "environment_templates",
    "environments",
    "finding_analyses",
    "findings",
    "invitations",
    "mcp_servers",
    "media_understanding_defaults",
    "memories",
    "memory_providers",
    "memory_spaces",
    "model_catalog",
    "model_providers",
    "models",
    "organizations",
    "provider_types",
    "runs",
    "sessions",
    "skills",
    "subscriptions",
    "threads",
    "toolsets",
    "trace_backend",
    "traces",
    "uploads",
    "usage",
    "users",
    "web_providers",
    "workspaces",
    "healthz",
    "readyz",
}


@pytest.mark.parametrize("mode", ["public", "bearer", "session"])
def test_api_and_authored_workflow_share_transport_credentials_and_final_close(mode: str) -> None:
    async def scenario() -> None:
        requests: list[httpx2.Request] = []

        def handle(request: httpx2.Request) -> httpx2.Response:
            requests.append(request)
            if request.url.path.endswith("/agents"):
                return httpx2.Response(
                    200, json={"items": [], "next_cursor": None}, headers={"X-Request-ID": "req_api"}
                )
            if request.method == "POST":
                return httpx2.Response(201, json=submitted())
            if "/inbox/" in request.url.path:
                return httpx2.Response(200, json={**entry_view(status="consumed"), "assigned_run_id": "run_1"})
            return httpx2.Response(200, json={**run_view(status="completed"), "output": False})

        class Transport(httpx2.MockTransport):
            closed = False

            async def aclose(self) -> None:
                self.closed = True
                await super().aclose()

        transport = Transport(handle)
        if mode == "session":
            client = Client.session(
                "https://service.example",
                origin="https://service.example",
                workspace_id="ws_1",
                csrf_token="proof",
                transport=transport,
            )
        else:
            client = Client("https://service.example", "token" if mode == "bearer" else None, transport=transport)
        async with client:
            api = client.api
            assert not hasattr(client, "resources")
            families = {name for name, value in type(api).__dict__.items() if isinstance(value, property)}
            assert families == FAMILIES
            for family in families:
                assert getattr(api, family).selectors == {}
            generated = api.agents
            authored = client.agents("agt_1")
            assert not requests
            listed = await generated.list(limit=1)
            assert listed.value.items == [] and listed.request_id == "req_api"
            interaction = await authored.start("hello", idempotency_key="saved")
            assert interaction.run is None
            result = await interaction.result(timeout=1, poll_interval=0.001)
            assert result.run_id == "run_1" and result.output is False
        assert transport.closed and len(requests) == 4
        assert [request.url.path for request in requests] == [
            "/api/v1/agents",
            "/api/v1/threads",
            "/api/v1/threads/thr_1/inbox/ent_1",
            "/api/v1/runs/run_1",
        ]
        for request in requests:
            if mode == "bearer":
                assert request.headers["authorization"] == "Bearer token"
                assert "x-workspace-id" not in request.headers
            elif mode == "session":
                assert request.headers["origin"] == "https://service.example"
                assert request.headers["x-workspace-id"] == "ws_1"
                assert "authorization" not in request.headers
                if request.method == "POST":
                    assert request.headers["x-csrf-token"] == "proof"
            else:
                assert "authorization" not in request.headers and "cookie" not in request.headers
        with pytest.raises(TransportError, match="closed"):
            await generated.list()
        with pytest.raises(TransportError, match="closed"):
            await authored.start("closed")
        assert len(requests) == 4

    asyncio.run(scenario())
