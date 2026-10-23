"""Execution choices survive authored and generated request boundaries."""

import asyncio
import json

import httpx2
import pytest

from a13n import UNSET, Client, ExecutionOverride, ProtocolError, RunOptions, ToolExecutionOverride
from a13n.generated import models as wire
from tests.test_interaction import submitted, thread_view


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (UNSET, {}),
        (None, {"execution": None}),
        (ExecutionOverride(), {"execution": {}}),
        (ExecutionOverride(environment=None), {"execution": {"environment": None}}),
        (ExecutionOverride(environment={}), {"execution": {"environment": {}}}),
        (
            ExecutionOverride(
                tools=ToolExecutionOverride(mode="auto", foreground_wait_seconds=0),
                steering="boundary",
                environment={"APP_ENV": "test", "EMPTY": ""},
            ),
            {
                "execution": {
                    "tools": {"mode": "auto", "foreground_wait_seconds": 0},
                    "steering": "boundary",
                    "environment": {"APP_ENV": "test", "EMPTY": ""},
                }
            },
        ),
    ],
)
def test_execution_wire_presence(value, expected) -> None:
    async def scenario() -> None:
        requests = []

        def handle(request: httpx2.Request) -> httpx2.Response:
            body = json.loads(request.content)
            requests.append(body)
            if request.method == "PATCH":
                assert request.headers["if-match"] == '"v1"'
                return httpx2.Response(200, json=thread_view())
            return httpx2.Response(201, json=submitted())

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            await client.agents("agt_1").start("x", execution=value, options=RunOptions(execution=value))
            await client.agents("agt_1").send("thr_1", "x", options=RunOptions(execution=value))
            await client.api.threads("thr_1").update(body=wire.ThreadUpdate.from_dict(expected), if_match='"v1"')
        assert {k: v for k, v in requests[0].items() if k == "execution"} == expected
        assert requests[0]["options"] == expected
        assert "execution" not in requests[1]
        assert requests[1]["options"] == expected
        assert requests[2] == expected

    asyncio.run(scenario())


def test_agent_execution_and_recipe_environment_are_typed() -> None:
    config = wire.AgentConfigInput.from_dict({"model": "test", "execution": {"environment": {"APP_ENV": "agent"}}})
    assert config.execution.environment.to_dict() == {"APP_ENV": "agent"}
    assert RunOptions(
        execution=ExecutionOverride(tools=ToolExecutionOverride(mode="inline"), steering="immediate")
    ).to_dict() == {"execution": {"tools": {"mode": "inline"}, "steering": "immediate"}}


def test_high_level_reads_request_detailed_and_reject_fragments() -> None:
    async def scenario() -> None:
        fragment = {
            "has_more": False,
            "media_type": "text/plain",
            "next_offset": None,
            "offset": 0,
            "source": "output",
            "text": "partial",
            "total_chars": 7,
            "version": "v1",
            "representation": "fragment",
        }

        def handle(request: httpx2.Request) -> httpx2.Response:
            assert request.url.params["view"] == "detailed"
            return httpx2.Response(200, json=fragment)

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            with pytest.raises(ProtocolError):
                await client.runs("run").get()
            with pytest.raises(ProtocolError):
                interaction = client.threads("thread").interaction("entry")
                assert interaction.entry is not None
                await interaction.entry.get()

    asyncio.run(scenario())


def test_native_start_and_mapping_run_execution_remain_supported() -> None:
    async def scenario() -> None:
        requests = []

        def handle(request: httpx2.Request) -> httpx2.Response:
            requests.append(json.loads(request.content))
            return httpx2.Response(201, json=submitted())

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            await client.agents("agt_1").start(
                "x",
                execution=wire.ExecutionOverride.from_dict({"environment": {"MODE": "thread"}}),
                options=RunOptions(execution={"environment": {"MODE": "run", "EMPTY": ""}}),
            )
        assert requests[0]["execution"] == {"environment": {"MODE": "thread"}}
        assert requests[0]["options"]["execution"] == {"environment": {"MODE": "run", "EMPTY": ""}}

    asyncio.run(scenario())
