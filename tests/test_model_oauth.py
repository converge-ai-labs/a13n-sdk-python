"""Provider authorization uses generated operations, not a second client auth flow."""

import asyncio
import json

import httpx2
import pytest

from a13n import ApiError, Client
from a13n.generated import models as wire

STATUS = {
    "provider_id": "mpr_1",
    "state": "disconnected",
    "subject": None,
    "client_id": None,
    "email": None,
    "expires_at": None,
    "pending": False,
    "message": None,
}


@pytest.mark.parametrize("session", [False, True])
@pytest.mark.parametrize("method", ["manual_callback", "browser_callback"])
def test_generated_oauth_graph_preserves_scope_status_nullable_data_and_auth(session: bool, method: str) -> None:
    async def scenario() -> None:
        seen: list[tuple[str, str]] = []

        def handle(request: httpx2.Request) -> httpx2.Response:
            path = request.url.path
            seen.append((request.method, path))
            assert request.headers["x-workspace-id"] == "ws_1"
            if session:
                assert "authorization" not in request.headers
                if request.method != "GET":
                    assert request.headers["x-csrf-token"] == "csrf"
            else:
                assert "authorization" in request.headers
                assert "x-csrf-token" not in request.headers
            if path.endswith("/authorize"):
                assert json.loads(request.content) == {"new_registration": False}
                result = {
                    "attempt_id": "attempt_1",
                    "authorization_url": "https://issuer.example/authorize",
                    "expires_at": "2026-10-01T00:10:00Z",
                    "method": method,
                }
            elif path.endswith("/callback"):
                assert json.loads(request.content) == {
                    "attempt_id": "attempt_1",
                    "callback_url": "https://operator.example/custom?code=fixture&state=fixture",
                }
                result = STATUS
            elif request.method == "DELETE":
                result = {"local_tokens_cleared": True, "revocation_confirmed": None}
            elif path.endswith("/models"):
                result = [{"slug": "native-slug", "display_name": "Native model"}]
            else:
                result = STATUS
            return httpx2.Response(200, json=result, headers={"X-Request-Id": "req_oauth", "Cache-Control": "no-store"})

        transport = httpx2.MockTransport(handle)
        client = (
            Client.session(
                "https://service.example", origin="https://service.example", csrf_token="csrf", transport=transport
            )
            if session
            else Client("https://service.example", "fixture-key", transport=transport)
        )
        async with client:
            provider = client.resources.model_providers("mpr_1")
            status = await provider.authorization.get(x_workspace_id="ws_1")
            assert status.value.to_dict() == STATUS
            start = await provider.authorize(
                body=wire.ProviderAuthorizationRequest(new_registration=False), x_workspace_id="ws_1"
            )
            assert start.value.method == method
            assert start.value.authorization_url == "https://issuer.example/authorize"
            callback = await provider.authorization.callback(
                body=wire.AuthorizationCallback(
                    attempt_id=start.value.attempt_id,
                    callback_url="https://operator.example/custom?code=fixture&state=fixture",
                ),
                x_workspace_id="ws_1",
            )
            assert callback.value.to_dict() == STATUS
            models = await provider.models.get(x_workspace_id="ws_1")
            assert [model.to_dict() for model in models.value] == [
                {"slug": "native-slug", "display_name": "Native model"}
            ]
            disconnected = await provider.authorization.delete(x_workspace_id="ws_1")
            assert disconnected.value.local_tokens_cleared is True and disconnected.value.revocation_confirmed is None
            assert all(
                result.status_code == 200 and result.request_id == "req_oauth"
                for result in (status, start, callback, models, disconnected)
            )
            assert start.headers["cache-control"] == "no-store"
        assert seen == [
            ("GET", "/api/v1/model-providers/mpr_1/authorization"),
            ("POST", "/api/v1/model-providers/mpr_1/authorize"),
            ("POST", "/api/v1/model-providers/mpr_1/authorization/callback"),
            ("GET", "/api/v1/model-providers/mpr_1/models"),
            ("DELETE", "/api/v1/model-providers/mpr_1/authorization"),
        ]

    asyncio.run(scenario())


def test_hosted_authorization_denial_is_service_owned_and_not_replayed() -> None:
    async def scenario() -> None:
        seen: list[httpx2.Request] = []

        def handle(request: httpx2.Request) -> httpx2.Response:
            seen.append(request)
            return httpx2.Response(
                403,
                json={
                    "error": {
                        "code": "forbidden",
                        "message": "An unconfined login session is required",
                        "details": {},
                        "request_id": "req_denied",
                    }
                },
            )

        async with Client("https://service.example", "fixture-key", transport=httpx2.MockTransport(handle)) as client:
            with pytest.raises(ApiError) as error:
                await client.resources.model_providers("mpr_1").authorize(body=wire.ProviderAuthorizationRequest())
            assert error.value.status == 403 and error.value.code == "forbidden"
        assert len(seen) == 1  # No fallback login, callback origin rewrite or mutation replay.

    asyncio.run(scenario())
