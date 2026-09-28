import asyncio
import json

import httpx2
import pytest

from a13n import ApiError, Client, ProtocolError, TransportError, text_input
from a13n.generated import models as wire


def test_credentials_scopes_and_csrf_are_explicit() -> None:
    async def scenario() -> None:
        seen: list[tuple[str, str, dict[str, str]]] = []

        def handle(request: httpx2.Request) -> httpx2.Response:
            seen.append((request.method, request.url.path, dict(request.headers)))
            if request.method == "POST":
                return httpx2.Response(
                    400,
                    json={
                        "error": {"code": "invalid_argument", "message": "bad", "details": {}, "request_id": "req_1"}
                    },
                )
            return httpx2.Response(200, json={"items": [], "next_cursor": None}, headers={"ETag": '"ws_1:2"'})

        async with Client("https://service.example", "secret-token", transport=httpx2.MockTransport(handle)) as client:
            result = await client.resources.threads.list()
            assert result.etag == '"ws_1:2"'
            assert result.value.items == []
            with pytest.raises(ApiError) as error:
                await client.resources.threads.create(
                    body=wire.NewThread(agent_id="agt_1", payload=text_input("Hi")), idempotency_key="k"
                )
            assert error.value.status == 400 and error.value.code == "invalid_argument"
        assert seen[0][1] == "/api/v1/threads"
        assert seen[0][2]["authorization"] == "Bearer secret-token"
        assert "cookie" not in seen[0][2]
        assert "secret-token" not in repr(client)

        seen.clear()
        async with Client.session(
            "https://service.example",
            origin="https://service.example",
            csrf_token="csrf",
            transport=httpx2.MockTransport(handle),
        ) as session:
            await session.resources.threads.list()
            with pytest.raises(ApiError):
                await session.resources.threads.create(
                    body=wire.NewThread(agent_id="agt_1", payload=text_input("Hi")), idempotency_key="k"
                )
            session.set_csrf_token("changed")
            await session.resources.threads.list()
        assert "authorization" not in seen[0][2]
        assert seen[0][2]["origin"] == "https://service.example"
        assert "x-workspace-id" not in seen[0][2]
        assert seen[1][2]["x-csrf-token"] == "csrf"

    asyncio.run(scenario())


def test_lazy_pages_and_tenant_binding() -> None:
    async def scenario() -> None:
        visited: list[str] = []

        def handle(request: httpx2.Request) -> httpx2.Response:
            visited.append(str(request.url))
            cursor = request.url.params.get("cursor")
            return httpx2.Response(200, json={"items": [], "next_cursor": "next" if cursor is None else None})

        async with Client("https://service.example", "t", transport=httpx2.MockTransport(handle)) as client:
            collection = client.resources.threads
            assert not visited
            assert client.threads("thr_1").id == "thr_1"
            assert client.runs("run_1").selectors == {"run_id": "run_1"}
            assert client.resources.threads("thr_1").inbox_entries("entry_1").id == "entry_1"
            pages = [page async for page in collection.pages(limit=1)]
            assert len(pages) == 2
            assert "cursor=next" in visited[-1]

    asyncio.run(scenario())


def test_generated_error_envelope_and_unknown_transport_outcome() -> None:
    async def scenario() -> None:
        def failure(request: httpx2.Request) -> httpx2.Response:
            return httpx2.Response(
                412,
                json={
                    "error": {
                        "code": "precondition_failed",
                        "message": "stale",
                        "details": {"current_etag": "etag"},
                        "request_id": "req_1",
                    }
                },
                headers={"X-Request-Id": "req_1"},
            )

        async with Client("https://service.example", "token", transport=httpx2.MockTransport(failure)) as client:
            with pytest.raises(ApiError) as error:
                await client.resources.threads.list()
            assert (error.value.status, error.value.code, error.value.details["current_etag"]) == (
                412,
                "precondition_failed",
                "etag",
            )
            assert "token" not in repr(error.value)

        def disconnect(request: httpx2.Request) -> httpx2.Response:
            raise httpx2.ReadError("disconnect", request=request)

        async with Client("https://service.example", "token", transport=httpx2.MockTransport(disconnect)) as client:
            with pytest.raises(TransportError, match="unknown"):
                await client.resources.threads.list()

    asyncio.run(scenario())


def test_error_does_not_infer_success_from_empty_body() -> None:
    async def scenario() -> None:
        async with Client(
            "https://service.example",
            "token",
            transport=httpx2.MockTransport(lambda _request: httpx2.Response(500, content=b"broken")),
        ) as client:
            with pytest.raises((ProtocolError, json.JSONDecodeError)):
                await client.resources.threads.list()

    asyncio.run(scenario())


def test_session_workspace_context_only_on_declared_workspace_routes() -> None:
    async def scenario() -> None:
        seen: list[tuple[str, str | None]] = []

        def handle(request: httpx2.Request) -> httpx2.Response:
            seen.append((request.url.path, request.headers.get("x-workspace-id")))
            return httpx2.Response(200, json={"items": [], "next_cursor": None})

        async with Client.session(
            "https://service.example",
            origin="https://service.example",
            workspace_id="ws_1",
            transport=httpx2.MockTransport(handle),
        ) as client:
            await client.resources.agents.list()
            await client.resources.memories.list()
            await client.workspaces.list()
            await client.organizations.list()
        assert seen[0] == ("/api/v1/agents", "ws_1")
        assert seen[1] == ("/api/v1/memories", "ws_1")
        assert all(scope is None for _, scope in seen[2:])

    asyncio.run(scenario())


def test_session_workspace_scope_respects_service_base_path_prefix() -> None:
    async def scenario() -> None:
        seen: list[tuple[str, str | None]] = []

        def handle(request: httpx2.Request) -> httpx2.Response:
            seen.append((request.url.path, request.headers.get("x-workspace-id")))
            return httpx2.Response(200, json={"items": [], "next_cursor": None})

        async with Client.session(
            "https://service.example/proxy/native/",
            origin="https://service.example",
            workspace_id="ws_1",
            transport=httpx2.MockTransport(handle),
        ) as client:
            await client.resources.agents.list()
            await client.organizations.list()
        assert seen == [
            ("/proxy/native/api/v1/agents", "ws_1"),
            ("/proxy/native/api/v1/organizations", None),
        ]

    asyncio.run(scenario())
