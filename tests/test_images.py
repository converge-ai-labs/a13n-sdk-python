"""All declared image media types use the same generated request path."""

import asyncio
import importlib
import json
from io import BytesIO
from pathlib import Path

import httpx2
import pytest

from a13n import ApiError, Client, ProtocolError
from a13n.generated.types import File

DOCUMENT = json.loads((Path(__file__).resolve().parents[1] / "contract/openapi.json").read_text())
OPERATIONS = [
    (path, operation)
    for path, operations in DOCUMENT["paths"].items()
    for operation in operations.values()
    if "image/webp" in operation.get("requestBody", {}).get("content", {})
]


def resource(client: Client, path: str):
    if "/agents/" in path:
        return client.resources.agents("agt_1").avatar
    if "/organizations/" in path:
        return client.organizations("org_1").icon
    if "/workspaces/" in path:
        return client.workspaces("ws_1").icon
    return client.resources.users.me.avatar


@pytest.mark.parametrize("path,operation", OPERATIONS)
@pytest.mark.parametrize("mime_type", ["image/jpeg", "image/png", "image/webp"])
def test_image_upload_preserves_explicit_media_and_caller_owned_source(
    path: str, operation: dict, mime_type: str
) -> None:
    async def scenario() -> None:
        payload = b"image-content" * 25000
        source = BytesIO(payload)
        body = File(source, mime_type=mime_type)
        module = importlib.import_module(
            f"a13n.generated.api.{operation['tags'][0]}.{operation['operationId'].replace('__', '_')}"
        )
        selectors = {p["name"]: "example" for p in operation.get("parameters", []) if p["in"] == "path"}
        request = module.build_request(**selectors, body=body)
        assert request["headers"]["Content-Type"] == mime_type
        assert request["content"] is source
        calls = 0

        async def handle(request: httpx2.Request) -> httpx2.Response:
            nonlocal calls
            calls += 1
            assert request.headers["content-type"] == mime_type
            assert await request.aread() == payload
            return httpx2.Response(
                400,
                json={
                    "error": {"code": "invalid_argument", "message": "fixture", "details": {}, "request_id": "req_1"}
                },
            )

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            with pytest.raises(ApiError) as error:
                await resource(client, path).replace(body=body)
            assert error.value.code == "invalid_argument"
        assert calls == 1 and not source.closed

    asyncio.run(scenario())


@pytest.mark.parametrize("mime_type", [None, "application/octet-stream", "image/gif"])
def test_invalid_image_input_is_local_error_not_protocol_failure(mime_type: str | None) -> None:
    async def scenario() -> None:
        def handle(_request: httpx2.Request) -> httpx2.Response:
            pytest.fail("Invalid media must fail before dispatch")

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            with pytest.raises(ValueError, match=r"File\.mime_type"):
                await client.workspaces("ws_1").icon.replace(body=File(BytesIO(b"x"), mime_type=mime_type))

    asyncio.run(scenario())


def test_malformed_response_is_still_a_protocol_error() -> None:
    async def scenario() -> None:
        transport = httpx2.MockTransport(lambda _: httpx2.Response(200, json={}))
        async with Client("https://service.example", transport=transport) as client:
            with pytest.raises(ProtocolError):
                await client.workspaces("ws_1").get()

    asyncio.run(scenario())
