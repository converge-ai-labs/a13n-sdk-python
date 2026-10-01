"""Native configuration snapshots and media input cross authored and generated paths."""

import asyncio
import json

import httpx2
import pytest

from a13n import ApiError, Client
from a13n.generated import models as wire
from a13n.generated.types import UNSET
from tests.test_interaction import submitted

CONFIGURATIONS = [
    {},
    {"configuration": None},
    {"configuration": {}},
    {"configuration": {"allowed_hosts": None}},
    {"configuration": {"allowed_hosts": []}},
    {"configuration": {"allowed_hosts": ["EXAMPLE.test.", "regex:^media\\.example\\.test$"]}},
    {"configuration": {"extensions": {}}},
    {
        "configuration": {
            "extensions": {
                "example.policy": {"enabled": False, "count": 0, "items": [], "object": {}, "nested": [None, False]},
                "example.null": None,
            }
        }
    },
]
MEDIA = {
    "content": [
        {"type": "text", "text": "Inspect these in order"},
        {"type": "url", "url": "https://media.example.test/image.png"},
        {"type": "url", "url": "https://media.example.test/video.mp4"},
        {"type": "asset", "asset_id": "ast_1"},
        {"type": "url", "url": "https://media.example.test/image.png"},
    ]
}


@pytest.mark.parametrize("options_json", CONFIGURATIONS)
def test_configuration_and_media_forward_through_start_send_and_message(options_json: dict) -> None:
    async def scenario() -> None:
        options = wire.RunOptionsInput.from_dict(options_json)
        payload = wire.MessagePayload.from_dict(MEDIA)
        assert options.to_dict() == options_json
        assert payload.to_dict() == MEDIA
        requests: list[httpx2.Request] = []

        def handle(request: httpx2.Request) -> httpx2.Response:
            requests.append(request)
            body = json.loads(request.content)
            assert body["options"] == options_json
            assert body["payload"] == MEDIA
            assert "configuration" not in body  # Configuration belongs inside native options.
            return httpx2.Response(201, json=submitted())

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            agent = client.agents("agt_1")
            await agent.start(payload, options=options, idempotency_key="start")
            await agent.send("thr_1", payload, options=options, idempotency_key="send")
            await client.resources.threads("thr_1").inbox_entries.create(
                body=wire.Message(agent_id="agt_1", payload=payload, options=options), idempotency_key="message"
            )
        assert len(requests) == 3

    asyncio.run(scenario())


def test_options_omission_is_not_an_empty_configuration() -> None:
    assert wire.RunOptionsInput().configuration is UNSET
    assert wire.RunConfigurationInput().to_dict() == {}
    assert wire.RunConfigurationOutput.from_dict({"allowed_hosts": [], "extensions": {}}).to_dict() == {
        "allowed_hosts": [],
        "extensions": {},
    }

    async def scenario() -> None:
        def handle(request: httpx2.Request) -> httpx2.Response:
            assert "options" not in json.loads(request.content)
            return httpx2.Response(201, json=submitted())

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            await client.agents("agt_1").start("x", idempotency_key="start")
            await client.agents("agt_1").send("thr_1", "x", idempotency_key="send")

    asyncio.run(scenario())


def test_frozen_configuration_conflict_is_not_rewritten_or_replayed() -> None:
    async def scenario() -> None:
        requests: list[httpx2.Request] = []

        def handle(request: httpx2.Request) -> httpx2.Response:
            requests.append(request)
            assert json.loads(request.content)["options"]["configuration"] == {"allowed_hosts": []}
            return httpx2.Response(
                409,
                json={
                    "error": {
                        "code": "conflict",
                        "message": "Run configuration is frozen",
                        "details": {"reason": "run_configuration_immutable"},
                        "request_id": "req_configuration",
                    }
                },
            )

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            with pytest.raises(ApiError) as error:
                await client.agents("agt_1").send(
                    "thr_1",
                    "x",
                    delivery=wire.Delivery.STEER,
                    options=wire.RunOptionsInput(configuration=wire.RunConfigurationInput(allowed_hosts=[])),
                    idempotency_key="steer",
                )
            assert error.value.code == "conflict" and error.value.status == 409
            assert error.value.details["reason"] == "run_configuration_immutable"
        assert len(requests) == 1

    asyncio.run(scenario())


@pytest.mark.parametrize("model", [wire.HarnessModelCharacteristicsInput, wire.HarnessModelCharacteristicsOutput])
@pytest.mark.parametrize(
    "payload",
    [
        {},
        {"image_input": None},
        {"image_input": {}},
        {
            "image_input": {"max_images": 0, "max_image_bytes": 0, "split_large_images": False, "support_gif": False},
            "video_input": {"max_video_bytes": 0},
            "url_input": {"video": []},
        },
        {"video_input": {"max_video_bytes": 4096}, "url_input": {"video": ["youtube"]}},
    ],
)
def test_model_media_characteristics_roundtrip(model, payload: dict) -> None:
    assert model.from_dict(payload).to_dict() == payload


def test_model_media_policies_reach_native_model_update_without_processing() -> None:
    async def scenario() -> None:
        characteristics = wire.HarnessModelCharacteristicsInput(
            image_input=wire.ImageInputPolicy(max_images=0, split_large_images=False),
            video_input=wire.VideoInputPolicy(max_video_bytes=4096),
            url_input=wire.UrlInputSupportInput(video=[]),
        )
        body = wire.ModelUpdate(
            config=wire.ModelConfigInput(
                model_name="native",
                model_api="native",
                characteristics=characteristics,
            )
        )

        def handle(request: httpx2.Request) -> httpx2.Response:
            assert request.method == "PATCH" and request.url.path == "/api/v1/models/mdl_1"
            assert json.loads(request.content) == body.to_dict()
            assert request.headers["if-match"] == '"mdl:1"'
            return httpx2.Response(
                400,
                json={
                    "error": {
                        "code": "invalid_argument",
                        "message": "Stop at native boundary",
                        "details": {},
                        "request_id": "req_1",
                    }
                },
            )

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            with pytest.raises(ApiError):
                await client.resources.models("mdl_1").update(body=body, if_match='"mdl:1"')

    asyncio.run(scenario())
