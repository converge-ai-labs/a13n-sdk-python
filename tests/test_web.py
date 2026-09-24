"""The generated organization provider resource is the only Web provider owner."""

import asyncio

import httpx2
import pytest

from a13n import ApiError, Client
from a13n.generated import models as wire
from a13n.generated.types import UNSET


def test_provider_credential_omission_and_null_are_distinct() -> None:
    base = {"name": "web", "type_": "search", "workspace_id": "ws_1"}
    omitted = wire.ProviderCreate(**base)
    cleared = wire.ProviderCreate(**base, credential=None)
    assert omitted.credential is UNSET
    assert "credential" not in omitted.to_dict()
    assert cleared.to_dict()["credential"] is None
    assert "private" not in repr(cleared)


def test_web_provider_navigation_is_org_scoped_and_preserves_pagination() -> None:
    async def scenario() -> None:
        visited: list[str] = []

        def handle(request: httpx2.Request) -> httpx2.Response:
            visited.append(str(request.url))
            return httpx2.Response(200, json={"items": [], "next_cursor": None})

        async with Client("https://service.example", "token", transport=httpx2.MockTransport(handle)) as client:
            providers = client.organizations("org_1").web_providers
            assert not visited
            result = await providers.list(workspace_id="ws_1")
            assert result.value.items == []
            assert "/api/v1/organizations/org_1/web-providers" in visited[0]
            assert "workspace_id=ws_1" in visited[0]

    asyncio.run(scenario())


def test_provider_mutations_never_automatically_replay() -> None:
    async def scenario() -> None:
        requests: list[httpx2.Request] = []

        def handle(request: httpx2.Request) -> httpx2.Response:
            requests.append(request)
            return httpx2.Response(
                412,
                json={
                    "error": {
                        "code": "precondition_failed",
                        "message": "stale",
                        "details": {"current_etag": "new"},
                        "request_id": "req_1",
                    }
                },
            )

        async with Client("https://service.example", "token", transport=httpx2.MockTransport(handle)) as client:
            with pytest.raises(ApiError) as error:
                await (
                    client.organizations("org_1")
                    .web_providers("prv_1")
                    .update(body=wire.ProviderUpdate(), if_match='"prv_1:1"')
                )
            assert error.value.details["current_etag"] == "new"
            assert len(requests) == 1
            assert requests[0].headers["if-match"] == '"prv_1:1"'

    asyncio.run(scenario())
