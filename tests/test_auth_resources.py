import asyncio

import httpx2
import pytest

from a13n import Client, ProtocolError, Result, TransportError


def test_public_bearer_and_session_authentication_are_isolated() -> None:
    async def scenario() -> None:
        public_requests: list[httpx2.Request] = []

        async def public_handler(request: httpx2.Request) -> httpx2.Response:
            public_requests.append(request)
            return httpx2.Response(200, headers={"Set-Cookie": "session=unexpected; Path=/"})

        async with Client("https://service.example", transport=httpx2.MockTransport(public_handler)) as public:
            for _ in range(2):
                async with public.stream({"method": "GET", "url": "/api/v1/ping"}):
                    pass
            with pytest.raises(RuntimeError, match="session"):
                public.set_csrf_token("proof")
        assert all("authorization" not in request.headers for request in public_requests)
        assert all("cookie" not in request.headers for request in public_requests)

        bearer_requests: list[httpx2.Request] = []

        async def bearer_handler(request: httpx2.Request) -> httpx2.Response:
            bearer_requests.append(request)
            return httpx2.Response(200, headers={"Set-Cookie": "session=unexpected; Path=/"})

        async with Client(
            "https://service.example", "secret-token", transport=httpx2.MockTransport(bearer_handler)
        ) as bearer:
            for _ in range(2):
                async with bearer.stream({"method": "GET", "url": "/api/v1/ping"}):
                    pass
        assert all(request.headers["authorization"] == "Bearer secret-token" for request in bearer_requests)
        assert all("cookie" not in request.headers for request in bearer_requests)

        cookies = httpx2.Cookies()
        cookies.set("custom_session", "signed", domain="service.example", path="/api")
        session_requests: list[httpx2.Request] = []

        async def session_handler(request: httpx2.Request) -> httpx2.Response:
            session_requests.append(request)
            return httpx2.Response(200, headers={"Set-Cookie": "rotated=yes; Path=/api"})

        async with Client.session(
            "https://service.example",
            origin="https://app.example",
            workspace_id="ws_1",
            cookies=cookies,
            csrf_token="proof-1",
            transport=httpx2.MockTransport(session_handler),
        ) as session:
            async with session.stream({"method": "POST", "url": "/api/v1/change"}):
                pass
            session.set_csrf_token(None)
            async with session.stream({"method": "GET", "url": "/api/v1/read"}):
                pass
        first, second = session_requests
        assert "authorization" not in first.headers
        assert first.headers["origin"] == "https://app.example"
        assert first.headers["x-a13n-workspace-id"] == "ws_1"
        assert first.headers["x-a13n-csrf-token"] == "proof-1"
        assert first.headers["cookie"] == "custom_session=signed"
        assert second.headers["cookie"] == "custom_session=signed; rotated=yes"
        assert "x-a13n-csrf-token" not in second.headers

    asyncio.run(scenario())


def test_resource_binding_result_evidence_and_lazy_pages() -> None:
    definition = {
        "type": "search",
        "display_name": "Search",
        "configuration_schema": {},
        "credential_schema": {},
        "credential_required": False,
        "setup_url": "https://example.test/setup",
        "operations": ["search"],
        "supports_restricted_scrape": False,
    }

    async def scenario() -> None:
        requests: list[httpx2.Request] = []

        async def handler(request: httpx2.Request) -> httpx2.Response:
            requests.append(request)
            if request.url.path == "/prefix/api/v1/web-provider-types":
                return httpx2.Response(
                    200,
                    json={"items": [definition]},
                    headers={"ETag": '"types-v1"', "X-Request-ID": "req_types"},
                )
            cursor = request.url.params.get("cursor")
            if cursor is None:
                return httpx2.Response(200, json={"items": [], "next_cursor": "next"})
            return httpx2.Response(200, json={"items": [], "next_cursor": None})

        client = Client("https://service.example/prefix", "token", transport=httpx2.MockTransport(handler))
        agent = client.workspaces("ws_1").agents("helper")
        assert requests == []
        assert agent.id == "helper"
        assert agent.selectors == {"workspace": "ws_1", "agent": "helper"}
        assert agent.client is client

        result = await client.resources.web_provider_types.list()
        assert isinstance(result, Result)
        assert result.status_code == result.status == 200
        assert result.headers["ETag"] == '"types-v1"'
        assert result.etag == '"types-v1"' and result.request_id == "req_types"
        assert result.value.items[0].type_ == "search"
        assert b"Search" in result.content

        pages = client.workspaces("ws_1").agents.pages()
        assert len(requests) == 1
        first = await anext(pages)
        assert first.value.items == [] and first.value.next_cursor == "next"
        second = await anext(pages)
        assert second.value.next_cursor is None
        with pytest.raises(StopAsyncIteration):
            await anext(pages)

        await client.aclose()
        with pytest.raises(TransportError, match="closed"):
            await agent.get()

    asyncio.run(scenario())


def test_resource_navigation_covers_representative_management_families_without_io() -> None:
    client = Client("https://service.example")
    resources = [
        client.resources.organizations("org").users,
        client.workspaces("ws").agents("agent").revisions,
        client.resources.organizations("org").model_providers,
        client.workspaces("ws").skills,
        client.resources.assets,
        client.resources.environments("env").connection,
        client.workspaces("ws").memory_providers("provider").memories,
        client.workspaces("ws").connections,
        client.resources.application_accounts("account").bot,
        client.resources.application_accounts("account").memory_scopes,
        client.resources.mcp_servers,
        client.workspaces("ws").configuration_sessions,
        client.workspaces("ws").hook_subscriptions,
        client.workspaces("ws").events,
        client.workspaces("ws").traces,
        client.workspaces("ws").toolsets,
    ]
    assert len({type(resource) for resource in resources}) == len(resources)
    asyncio.run(client.aclose())


def test_repeated_pagination_cursor_fails_instead_of_looping() -> None:
    async def handler(_request: httpx2.Request) -> httpx2.Response:
        return httpx2.Response(200, json={"items": [], "next_cursor": "same"})

    async def scenario() -> None:
        async with Client("https://service.example", transport=httpx2.MockTransport(handler)) as client:
            pages = client.workspaces("ws").agents.pages(cursor="same")
            await anext(pages)
            with pytest.raises(ProtocolError, match="repeated"):
                await anext(pages)

    asyncio.run(scenario())


def test_flattened_iteration_is_lazy_and_retains_filters() -> None:
    calls = []

    async def handler(request: httpx2.Request) -> httpx2.Response:
        calls.append(request)
        assert request.url.params["limit"] == "3"
        return httpx2.Response(200, json={"items": [], "next_cursor": "next" if len(calls) == 1 else None})

    async def scenario() -> None:
        async with Client("https://service.example", transport=httpx2.MockTransport(handler)) as client:
            values = client.workspaces("ws").agents.iter(limit=3)
            assert calls == []
            assert [value async for value in values] == []
            assert len(calls) == 2 and calls[1].url.params["cursor"] == "next"

    asyncio.run(scenario())


def test_resource_binary_scope_is_lazy_and_session_authenticated() -> None:
    consumed = []

    class Body(httpx2.AsyncByteStream):
        async def __aiter__(self):
            consumed.append("first")
            yield b"first"
            consumed.append("second")
            yield b"second"

        async def aclose(self):
            consumed.append("closed")

    async def handler(request: httpx2.Request) -> httpx2.Response:
        assert request.url.path == "/api/v1/assets/asset_1/content"
        assert request.headers["X-A13N-Workspace-ID"] == "ws"
        assert request.headers["Origin"] == "https://console.example"
        return httpx2.Response(200, stream=Body(), headers={"Content-Type": "application/octet-stream"})

    async def scenario() -> None:
        async with Client.session(
            "https://service.example",
            origin="https://console.example",
            workspace_id="ws",
            transport=httpx2.MockTransport(handler),
        ) as client:
            async with client.resources.assets("asset_1").content.get_stream() as response:
                assert consumed == []
                assert response.status_code == 200
                async for chunk in response.aiter_bytes():
                    assert chunk == b"first"
                    break
            assert consumed == ["first", "closed"]

    asyncio.run(scenario())


@pytest.mark.parametrize("flatten", [False, True])
@pytest.mark.parametrize("initial", [[], ["env=dev"]])
def test_traversal_snapshots_filters_at_creation_and_between_pages(flatten: bool, initial: list[str]) -> None:
    labels = initial.copy()
    calls = []

    async def handler(request: httpx2.Request) -> httpx2.Response:
        calls.append(request)
        # Simulate caller mutation while a page request is in flight.
        labels[:] = ["env=changed-during-request"]
        return httpx2.Response(
            200, json={"items": [], "next_cursor": "next" if "cursor" not in request.url.params else None}
        )

    async def scenario() -> None:
        async with Client("https://service.example", transport=httpx2.MockTransport(handler)) as client:
            agents = client.workspaces("ws").agents
            first = agents.iter(label=labels) if flatten else agents.pages(label=labels)
            labels[:] = ["env=prod"]
            second = agents.iter(label=labels) if flatten else agents.pages(label=labels)
            labels[:] = ["env=changed-before-read"]
            assert calls == []
            _ = [value async for value in first]
            _ = [value async for value in second]
            assert [request.url.params.get_list("label") for request in calls] == [
                initial,
                initial,
                ["env=prod"],
                ["env=prod"],
            ]
            assert [request.url.params.get("cursor") for request in calls] == [None, "next", None, "next"]

    asyncio.run(scenario())


@pytest.mark.parametrize("flatten", [False, True])
def test_traversal_filter_snapshot_keeps_unset_distinct_from_empty(
    flatten: bool, monkeypatch: pytest.MonkeyPatch
) -> None:
    from a13n.generated.models import AgentCollection
    from a13n.generated.types import UNSET

    received = []

    async def scenario() -> None:
        async with Client("https://service.example") as client:
            agents = client.workspaces("ws").agents

            async def list_page(**kwargs):
                received.append(kwargs["label"])
                return Result(AgentCollection(items=[], next_cursor=None), 200, {}, b"")

            monkeypatch.setattr(agents, "list", list_page)
            unset = agents.iter() if flatten else agents.pages()
            empty = agents.iter(label=[]) if flatten else agents.pages(label=[])
            assert received == []
            _ = [value async for value in unset]
            _ = [value async for value in empty]
            assert received[0] is UNSET
            assert received[1] == []

    asyncio.run(scenario())
