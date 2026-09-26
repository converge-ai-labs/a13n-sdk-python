import asyncio
from io import BytesIO

import httpx2
import pytest

from a13n import ApiError, Client
from a13n.generated import models as wire
from a13n.generated.types import UNSET, File


def test_generated_request_omission_and_explicit_null() -> None:
    absent = wire.Message(
        agent_id="agt_1", payload=wire.MessagePayload(content=[wire.TextPart(text="x", type_="text")])
    )
    explicit_null = wire.Message(agent_id="agt_1", payload=absent.payload, agent_revision_id=None)
    assert "agent_revision_id" not in absent.to_dict()
    assert explicit_null.to_dict()["agent_revision_id"] is None
    assert absent.options is UNSET
    assert "secret" not in repr(absent)


def test_generated_binary_download_is_unbuffered_and_workspace_bound() -> None:
    async def scenario() -> None:
        paths: list[str] = []

        def handle(request: httpx2.Request) -> httpx2.Response:
            paths.append(request.url.path)
            return httpx2.Response(200, content=b"\0zip-binary", headers={"Content-Type": "application/octet-stream"})

        async with Client("https://service.example", "token", transport=httpx2.MockTransport(handle)) as client:
            async with client.workspaces("ws_1").assets("ast_1").content.get_stream() as response:
                assert response.status_code == 200
                assert await response.aread() == b"\0zip-binary"
            assert paths == ["/api/v1/workspaces/ws_1/assets/ast_1/content"]

    asyncio.run(scenario())


def test_generated_upload_accepts_binary_file_part_not_utf8_string() -> None:
    async def scenario() -> None:
        recorded: list[httpx2.Request] = []

        def handle(request: httpx2.Request) -> httpx2.Response:
            recorded.append(request)
            return httpx2.Response(
                400,
                json={
                    "error": {
                        "code": "invalid_argument",
                        "message": "stop after upload",
                        "details": {},
                        "request_id": "req_1",
                    }
                },
            )

        payload = BytesIO(b"\x00\xff" * 32_768)
        async with Client("https://service.example", "token", transport=httpx2.MockTransport(handle)) as client:
            with pytest.raises(ApiError):
                await client.workspaces("ws_1").uploads.create(
                    body=wire.UploadCreate(
                        file=File(payload=payload, file_name="binary.dat", mime_type="application/octet-stream")
                    ),
                    idempotency_key="upload-key",
                )
        assert len(recorded) == 1
        request = recorded[0]
        assert request.headers["idempotency-key"] == "upload-key"
        assert b"\x00\xff" in request.content
        assert request.headers["content-type"].startswith("multipart/form-data; boundary=")
        boundary = request.headers["content-type"].split("boundary=", 1)[1].encode()
        assert request.content.startswith(b"--" + boundary + b"\r\n")
        assert request.content.endswith(b"--" + boundary + b"--\r\n")
        assert b'name="file"' in request.content

    asyncio.run(scenario())


def test_binary_upload_does_not_expose_secret_in_generated_repr() -> None:
    body = wire.UploadCreate(file=File(payload=BytesIO(b"private-upload"), file_name="private.txt"))
    assert "private-upload" not in repr(body)
