import asyncio
from io import BytesIO

import httpx2
import pytest

from a13n import ApiError, Client
from a13n.generated import models as wire
from a13n.generated.types import UNSET, File


def test_generated_history_and_resume_wire_roundtrip() -> None:
    native_history = [
        {"kind": "request", "parts": [{"part_kind": "user-prompt", "content": "Prior"}], "metadata": {"origin": "app"}},
        {"kind": "response", "parts": [{"part_kind": "text", "content": "Seen"}], "model_name": "prior-model"},
    ]
    create = wire.NewThread.from_dict(
        {
            "agent_id": "agt_1",
            "payload": {"content": [{"type": "text", "text": "Now"}]},
            "message_history": native_history,
        }
    )
    assert create.to_dict()["message_history"] == native_history
    assert "message_history" not in wire.NewThread(agent_id="agt_1", payload=create.payload).to_dict()

    batch = {
        "approvals": {"approval_1": {"action": "approve"}},
        "calls": {"call_1": {"status": "returned", "value": {"answers": {"Choose": "A"}}}},
        "input": {"content": [{"type": "asset", "asset_id": "ast_1"}]},
    }
    assert wire.Resume.from_dict(batch).to_dict() == batch
    assert wire.Resume.from_dict({"approvals": {}, "calls": {}}).to_dict() == {"approvals": {}, "calls": {}}
    assert wire.Resume.from_dict({"approvals": {}, "calls": {}, "input": None}).to_dict()["input"] is None


def test_generated_request_omission_and_explicit_null() -> None:
    absent = wire.Message(
        agent_id="agt_1", payload=wire.MessagePayload(content=[wire.TextPart(text="x", type_="text")])
    )
    explicit_null = wire.Message(agent_id="agt_1", payload=absent.payload, agent_revision_id=None)
    assert "agent_revision_id" not in absent.to_dict()
    assert explicit_null.to_dict()["agent_revision_id"] is None
    assert absent.options is UNSET
    assert "secret" not in repr(absent)


@pytest.mark.parametrize("model", [wire.ModelPriceRuleInput, wire.ModelPriceRuleOutput])
def test_model_price_rule_selectors_preserve_omission_null_and_values(
    model: type[wire.ModelPriceRuleInput] | type[wire.ModelPriceRuleOutput],
) -> None:
    absent = model(prices=[], rule_id="default")
    assert absent.max_input_tokens is UNSET
    assert absent.service_tier is UNSET
    assert absent.to_dict() == {"prices": [], "rule_id": "default"}
    for selectors in (
        {"max_input_tokens": None, "service_tier": None},
        {"max_input_tokens": 128_000, "service_tier": "priority"},
    ):
        payload = {**absent.to_dict(), **selectors}
        parsed = model.from_dict(payload)
        assert parsed.max_input_tokens == selectors["max_input_tokens"]
        assert parsed.service_tier == selectors["service_tier"]
        assert parsed.to_dict() == payload


def test_generated_binary_download_is_unbuffered_and_workspace_bound() -> None:
    async def scenario() -> None:
        paths: list[str] = []

        def handle(request: httpx2.Request) -> httpx2.Response:
            paths.append(request.url.path)
            return httpx2.Response(200, content=b"\0zip-binary", headers={"Content-Type": "application/octet-stream"})

        async with Client("https://service.example", "token", transport=httpx2.MockTransport(handle)) as client:
            async with client.resources.assets("ast_1").content.get_stream() as response:
                assert response.status_code == 200
                assert await response.aread() == b"\0zip-binary"
            assert paths == ["/api/v1/assets/ast_1/content"]

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
                await client.resources.uploads.create(
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


def test_generated_thread_sse_exposes_unbuffered_raw_response() -> None:
    class OpenStream(httpx2.AsyncByteStream):
        def __init__(self) -> None:
            self.closed = False

        async def __aiter__(self):
            yield b'event: changed\ndata: {"version": 1}\n\n'
            await asyncio.Event().wait()  # The server does not close after a frame.

        async def aclose(self) -> None:
            self.closed = True

    async def scenario() -> None:
        stream = OpenStream()
        paths: list[str] = []

        def handle(request: httpx2.Request) -> httpx2.Response:
            paths.append(request.url.path)
            assert dict(request.url.params) == {"run": "run_1", "position": "1-3"}
            assert request.headers["last-event-id"] == "1700000000000-0"
            return httpx2.Response(200, stream=stream, headers={"Content-Type": "text/event-stream"})

        async with Client("https://service.example", "token", transport=httpx2.MockTransport(handle)) as client:
            async with asyncio.timeout(0.5):
                async with client.resources.threads("thr_1").stream.get_stream(
                    run="run_1", position="1-3", last_event_id="1700000000000-0"
                ) as response:
                    assert response.status_code == 200
                    assert await anext(response.aiter_bytes()) == b'event: changed\ndata: {"version": 1}\n\n'
            assert stream.closed
        assert paths == ["/api/v1/threads/thr_1/stream"]

    asyncio.run(scenario())


@pytest.mark.parametrize("model", [wire.ModelConfigInput, wire.ModelConfigOutput])
def test_native_model_settings_preserve_arbitrary_json_and_omission(
    model: type[wire.ModelConfigInput] | type[wire.ModelConfigOutput],
) -> None:
    settings = {
        "provider_option": {"flags": [True, False, None], "limit": 0, "ratio": 0.25},
        "seed": None,
        "extra": "value",
    }
    payload = {"model_name": "test", "model_api": "test.model", "settings": settings}
    parsed = model.from_dict(payload)
    assert isinstance(parsed.settings, (wire.ModelConfigInputSettings, wire.ModelConfigOutputSettings))
    assert parsed.settings.to_dict() == settings
    assert parsed.to_dict() == payload
    absent = model(model_name="test", model_api="test.model")
    assert absent.settings is UNSET and "settings" not in absent.to_dict()


def test_model_settings_reach_native_request_without_filtering() -> None:
    import json

    async def scenario() -> None:
        body = wire.ModelCreate(
            config=wire.ModelConfigInput(
                model_name="test",
                model_api="test.model",
                settings=wire.ModelConfigInputSettings.from_dict(
                    {"vendor": {"nested": [None, False, 0]}, "temperature": 0}
                ),
            ),
            name="Configured model",
            provider_id="mpr_1",
        )

        def handle(request: httpx2.Request) -> httpx2.Response:
            assert request.method == "POST" and request.url.path == "/api/v1/models"
            assert json.loads(request.content) == body.to_dict()
            return httpx2.Response(
                400,
                json={
                    "error": {
                        "code": "invalid_argument",
                        "message": "Provider rejected settings",
                        "details": {},
                        "request_id": "req_1",
                    }
                },
            )

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            with pytest.raises(ApiError, match="Provider rejected settings"):
                await client.resources.models.create(body=body)

    asyncio.run(scenario())


def test_native_upload_ids_and_password_fields_are_forwarded_not_revalidated() -> None:
    upload_id = "upl_" + "0123456789abcdef" * 2
    assert wire.AssetCreate(upload_id=upload_id, name="document").to_dict()["upload_id"] == upload_id
    source = {"kind": "upload", "upload_id": upload_id}
    assert wire.UploadSource.from_dict(source).to_dict() == source
    # These generated strings carry Service constraints; the SDK does not own password policy.
    assert wire.BootstrapInput(email="test@example.test", password="example8").to_dict()["password"] == "example8"
    assert wire.PasswordChange(current_password="old", password="example8").to_dict() == {
        "current_password": "old",
        "password": "example8",
    }
    assert wire.PasswordResetConfirm(token="reset-token", password="example8").to_dict()["password"] == "example8"
    assert wire.LoginInput(email="test@example.test", password="old").to_dict()["password"] == "old"
    assert "example8" not in repr(wire.PasswordChange(current_password="old", password="example8"))
