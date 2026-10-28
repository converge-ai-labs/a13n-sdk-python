"""Native shared-memory, computer, provider and execution contracts."""

import asyncio
import json

import httpx2
import pytest

from a13n import UNSET, AgentOverride, ApiError, Client, MountCreate, RunOptions, TransportError
from a13n.generated import models as wire
from tests.test_interaction import NOW, run_view, submitted

SPACE = {
    "id": "msp_1",
    "organization_id": "org_1",
    "workspace_id": "ws_1",
    "name": "Notes",
    "description": None,
    "labels": {},
    "enabled": False,
    "organization": {"enabled": False},
    "memory_id": "mem_1",
    "guide": None,
    "always_load": [],
    "file_count": 0,
    "content_bytes": 0,
    "history_bytes": 0,
    "version": 1,
    "created_by_id": "usr_1",
    "updated_by_id": "usr_1",
    "created_at": NOW,
    "updated_at": NOW,
}
REVISION = {
    "id": "rev_1",
    "agent_id": "agt_1",
    "number": 1,
    "config": {"model": "live-model"},
    "digest": "digest",
    "note": None,
    "created_by_id": "usr_1",
    "created_at": NOW,
}
ATTEMPT = {
    "id": "att_1",
    "run_id": "run_1",
    "number": 1,
    "status": "succeeded",
    "start_reason": "initial",
    "replaces_attempt_id": None,
    "worker_build": "build",
    "harness_run_id": None,
    "yield_reason": None,
    "failure": None,
    "created_at": NOW,
    "started_at": None,
    "finished_at": None,
}
MOUNT = {"name": "work", "environment_id": "env_1", "working_directory": None, "permission_ceiling": {"operations": []}}
METRICS = {"time_to_first_chunk_seconds": None, "request_duration_seconds": 0, "output_tokens_per_second": None}
ORGANIZATION = {"pending": False, "processed_seq": 0, "active_run_id": None, "history_gap": False, "due_at": None}


async def added_calls(api):
    """Each callback owns exactly one of the eighteen added HTTP operations."""
    space = api.memory_spaces("msp_1")
    provider = api.environment_providers("prv_1")
    return [
        lambda: provider.delete(if_match='"provider:1"'),
        lambda: provider.references.get(),
        lambda: api.environments("env_1").computer.check(),
        lambda: api.memory_spaces.list(enabled=False, label=["team:one"], limit=1),
        lambda: api.memory_spaces.create(body=wire.MemorySpaceCreate(name="Notes", enabled=False)),
        lambda: space.delete(if_match='"space:1"'),
        lambda: space.get(),
        lambda: space.update(body=wire.MemorySpaceUpdate(guide=None, enabled=False), if_match='"space:1"'),
        lambda: space.organization.get(),
        lambda: space.organizations.list(limit=1),
        lambda: space.organizations.create(),
        lambda: space.sessions.list(limit=1),
        lambda: api.runs.list(limit=1),
        lambda: api.runs("run_1").agent.get(),
        lambda: api.runs("run_1").attempts("att_1").get(),
        lambda: api.runs("run_1").images("img_1").get(),
        lambda: (
            api.threads("thr_1")
            .environments("work")
            .update(body=wire.MountUpdate.from_dict({"permission_ceiling": {"operations": []}}), if_match='"thread:1"')
        ),
        lambda: api.usage.records("mur_1").metrics.get(),
    ]


def response_for(request):
    path = request.url.path
    if request.method == "DELETE":
        return httpx2.Response(204)
    if path.endswith("/references"):
        value = {
            "environment_count": 0,
            "environments": [],
            "template_count": 1,
            "templates": [{"id": "etp_1", "name": "Desktop", "status": "active"}],
        }
    elif path.endswith("/computer/check"):
        value = {
            "status": "unsupported",
            "operations": [],
            "display_count": 0,
            "input_ready": False,
            "observe_ready": False,
        }
    elif path.endswith("/organization") or (path.endswith("/organizations") and request.method == "POST"):
        value = ORGANIZATION
    elif path.endswith(("/sessions", "/organizations", "/runs")):
        value = {"items": [], "next_cursor": None}
    elif path.endswith("/memory-spaces") and request.method == "GET":
        value = {"items": [SPACE], "next_cursor": None}
    elif "/memory-spaces" in path:
        value = SPACE
    elif path.endswith("/agent"):
        value = {"revision": REVISION, "config": {"model": "live-model", "instructions": "Run override"}}
    elif "/attempts/" in path:
        value = ATTEMPT
    elif "/images/" in path:
        return httpx2.Response(200, content=b"\x89PNG\r\n\x00\xff", headers={"Content-Type": "image/png"})
    elif "/environments/work" in path:
        value = MOUNT
    else:
        value = METRICS
    status = (
        202
        if path.endswith("/organizations") and request.method == "POST"
        else 201
        if request.method == "POST" and path.endswith("/memory-spaces")
        else 200
    )
    return httpx2.Response(status, json=value, headers={"ETag": '"native:1"', "X-Request-ID": "req_native"})


@pytest.mark.parametrize("mode", ["bearer", "session"])
def test_eighteen_added_operations_auth_binding_metadata_and_client_lifetime(mode: str) -> None:
    async def scenario():
        requests = []

        def handle(request):
            requests.append(request)
            return response_for(request)

        transport = httpx2.MockTransport(handle)
        client = (
            Client.session(
                "https://service.example",
                origin="https://service.example",
                workspace_id="ws_1",
                csrf_token="proof",
                transport=transport,
            )
            if mode == "session"
            else Client("https://service.example", "token", transport=transport)
        )
        async with client:
            calls = await added_calls(client.api)
            assert not requests
            results = [await call() for call in calls]
            assert results[0].value is None and results[5].value is None
            assert results[1].value.templates[0].id == "etp_1"
            assert results[2].value.input_ready is False and results[2].value.display_count == 0
            assert results[3].value.items[0].content_bytes == 0
            assert results[7].etag == '"native:1"' and results[7].request_id == "req_native"
            assert results[8].value.processed_seq == 0
            assert results[13].value.revision.config.instructions is UNSET
            assert results[13].value.config.instructions == "Run override"
            assert results[14].value.id == "att_1"
            assert results[15].value.payload.read() == b"\x89PNG\r\n\x00\xff"
            assert results[16].value.permission_ceiling.operations == []
            assert results[17].value.request_duration_seconds == 0
            assert results[17].value.time_to_first_chunk_seconds is None
        assert len(requests) == 18
        assert requests[3].url.params["enabled"] == "false"
        assert requests[3].url.params.get_list("label") == ["team:one"]
        assert json.loads(requests[7].content) == {"enabled": False, "guide": None}
        assert json.loads(requests[16].content) == {"permission_ceiling": {"operations": []}}
        for i in [0, 5, 7, 16]:
            assert "if-match" in requests[i].headers
        for request in requests:
            if mode == "session":
                assert request.headers["x-workspace-id"] == "ws_1"
                if request.method != "GET":
                    assert request.headers["x-csrf-token"] == "proof"
            else:
                assert request.headers["authorization"] == "Bearer token"
        with pytest.raises(TransportError, match="closed"):
            await calls[-1]()
        assert len(requests) == 18

    asyncio.run(scenario())


@pytest.mark.parametrize("status,code", [(403, "forbidden"), (409, "conflict"), (412, "precondition_failed")])
def test_added_operations_preserve_native_errors_without_retries(status, code):
    async def scenario():
        requests = []

        def handle(request):
            requests.append(request)
            return httpx2.Response(
                status,
                json={
                    "error": {
                        "code": code,
                        "message": "Native rejection",
                        "details": {"reason": "native", "zero": 0, "flag": False},
                        "request_id": "req_error",
                    }
                },
            )

        async with Client("https://service.example", "token", transport=httpx2.MockTransport(handle)) as client:
            for call in await added_calls(client.api):
                with pytest.raises(ApiError) as error:
                    await call()
                assert error.value.status == status and error.value.code == code
                assert error.value.details == {"reason": "native", "zero": 0, "flag": False}
                assert error.value.request_id == "req_error"
        assert len(requests) == 18

    asyncio.run(scenario())


@pytest.mark.parametrize(
    "media,content", [("image/jpeg", b"\xff\xd8\x00\xff\xd9"), ("image/png", b"\x89PNG\r\n\x00\xff")]
)
def test_retained_image_explicit_buffered_and_streamed_media(media, content):
    async def scenario():
        requests = []

        def handle(request):
            requests.append(request)
            return httpx2.Response(200, content=content, headers={"Content-Type": media, "X-Request-ID": "req_image"})

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            image = client.api.runs("run_1").images("img_1")
            result = await image.get()
            assert result.value.payload.read() == content and result.headers["content-type"] == media
            assert result.request_id == "req_image"
            async with image.get_stream() as response:
                assert response.status_code == 200 and response.headers["content-type"] == media
                assert b"".join([chunk async for chunk in response.aiter_bytes()]) == content
        assert len(requests) == 2

    asyncio.run(scenario())


def test_image_stream_exposes_error_response_without_decoding_as_image():
    async def scenario():
        body = {"error": {"code": "not_found", "message": "Not retained", "details": {}, "request_id": "req_image"}}
        async with Client(
            "https://service.example", transport=httpx2.MockTransport(lambda _: httpx2.Response(404, json=body))
        ) as client:
            image = client.api.runs("run_1").images("missing")
            with pytest.raises(ApiError, match="Not retained"):
                await image.get()
            async with image.get_stream() as response:
                assert response.status_code == 404
                assert json.loads(await response.aread()) == body

    asyncio.run(scenario())


@pytest.mark.parametrize(
    "frozen", [{"roots": [], "space_id": None}, {"roots": ["sessions/ses_1", "shared/msp_1"], "space_id": "msp_1"}]
)
def test_run_memory_union_keeps_typed_host_resolved_roots(frozen):
    mount = {"name": "notes", "memory_id": "mem_1", "access": "read", "recall": False}
    value = run_view(status="completed")
    value["memory_mounts"] = [mount, {**mount, **frozen}]
    parsed = wire.RunView.from_dict(value)
    assert isinstance(parsed.memory_mounts[0], wire.MemoryMount)
    resolved = parsed.memory_mounts[1]
    assert isinstance(resolved, wire.FrozenMemoryMount)
    assert resolved.roots == frozen["roots"] and resolved.space_id == frozen["space_id"]
    assert parsed.to_dict()["memory_mounts"] == value["memory_mounts"]
    assert "roots" not in wire.MemoryMount.__annotations__


def test_public_overrides_reject_retired_platform_settings():
    with pytest.raises(TypeError):
        AgentOverride(platform_tools={})
    assert RunOptions(overrides=AgentOverride(builtin_skills=[])).into_wire().to_dict() == {
        "overrides": {"builtin_skills": []}
    }
    assert RunOptions(overrides=AgentOverride(builtin_skills=None)).into_wire().to_dict() == {
        "overrides": {"builtin_skills": None}
    }


def test_authored_mount_permission_ceiling_is_optional_without_injected_defaults():
    async def scenario():
        requests = []

        def handle(request):
            requests.append(request)
            return httpx2.Response(201, json=submitted())

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            await client.agents("agt_1").start(
                "x",
                environments=[
                    MountCreate("work", "env_1"),
                    MountCreate("restricted", "env_2", None, {"operations": []}),
                ],
            )
        assert json.loads(requests[0].content)["environments"] == [
            {"name": "work", "environment_id": "env_1"},
            {
                "name": "restricted",
                "environment_id": "env_2",
                "working_directory": None,
                "permission_ceiling": {"operations": []},
            },
        ]

    asyncio.run(scenario())


@pytest.mark.parametrize("trigger", [{"type": "any_change"}, {"type": "change_count", "count": 1}])
def test_memory_settings_policies_and_native_nulls_round_trip(trigger):
    memory = {"enabled": False, "spaces": [{"name": "notes", "space_id": "msp_1", "access": "read"}]}
    assert wire.SessionMemorySettings.from_dict(memory).to_dict() == memory
    assert wire.SessionCreate.from_dict({"memory": memory, "labels": {}}).to_dict() == {"memory": memory, "labels": {}}
    assert wire.SessionUpdate.from_dict({"memory": memory, "labels": None}).to_dict() == {
        "memory": memory,
        "labels": None,
    }
    policy = {"enabled": False, "check_interval_seconds": 30, "cooldown_seconds": 0, "model": None, "trigger": trigger}
    assert wire.OrganizationPolicy.from_dict(policy).to_dict() == policy
    assert wire.AgentConfigInput.from_dict({"model": "live", "memory": memory}).to_dict() == {
        "model": "live",
        "memory": memory,
    }


def test_required_nullable_usage_metrics_and_per_run_summary():
    model = {
        "model": None,
        "requests": 0,
        "input_tokens": 0,
        "output_tokens": 0,
        "cache_read_tokens": 0,
        "cache_write_tokens": 0,
        "cost": None,
        "average_time_to_first_chunk_seconds": None,
        "output_tokens_per_second": 0,
    }
    summary = {"models": [model]}
    runs = {
        "items": [{"run_id": "run_1", "thread_id": "thr_1", "run_number": 42, "models": [model]}],
        "next_cursor": None,
    }
    assert wire.UsageSummary.from_dict(summary).to_dict() == summary
    assert wire.RunUsagePage.from_dict(runs).to_dict() == runs
    assert wire.UsageSummary.from_dict({"models": []}).to_dict() == {"models": []}
    assert wire.ModelRequestMetrics.from_dict(METRICS).to_dict() == METRICS
    with pytest.raises(KeyError):
        wire.ModelUsage.from_dict({k: v for k, v in model.items() if k != "average_time_to_first_chunk_seconds"})
    with pytest.raises(KeyError):
        wire.RunUsagePage.from_dict({"items": []})


def test_new_cursor_pages_are_lazy_with_stable_filters():
    async def scenario():
        requests = []

        def handle(request):
            requests.append(request)
            return httpx2.Response(200, json={"items": [], "next_cursor": "next" if len(requests) % 2 else None})

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            labels = ["team:one"]
            pages = client.api.memory_spaces.pages(enabled=False, label=labels, limit=1)
            labels.append("not-in-snapshot")
            assert not requests
            assert len([page async for page in pages]) == 2
            runs = client.api.runs.pages(agent_id="agt_1", thread_id="thr_1", limit=1)
            assert len(requests) == 2
            assert len([page async for page in runs]) == 2
            space = client.api.memory_spaces("msp_1")
            assert len([page async for page in space.organizations.pages(limit=1)]) == 2
            assert len([page async for page in space.sessions.pages(limit=1)]) == 2
        assert requests[1].url.params.get_list("label") == ["team:one"]
        assert requests[1].url.params["enabled"] == "false" and requests[1].url.params["cursor"] == "next"
        assert dict(requests[3].url.params) == {
            "agent_id": "agt_1",
            "thread_id": "thr_1",
            "limit": "1",
            "cursor": "next",
        }

    asyncio.run(scenario())


def test_current_shared_memory_and_execution_guide_functions():
    import re
    from pathlib import Path

    from tests.test_interaction import thread_view

    root = Path(__file__).resolve().parents[1]
    selected = {
        "create_shared_notes_session",
        "restrict_mount",
        "check_desktop",
        "executed_agent",
        "read_retained_image",
        "request_metrics",
    }
    namespace = {}
    for filename in ["files-and-memory.md", "resources.md"]:
        for block in re.findall(r"```python\n(.*?)```", (root / "docs" / filename).read_text(), re.DOTALL):
            if any(f"async def {name}(" in block for name in selected) or "platform_options =" in block:
                exec(compile(block, filename, "exec"), namespace)
    assert selected <= namespace.keys()
    assert namespace["platform_options"].into_wire().to_dict()["overrides"]["builtin_skills"] == ["platform-operations"]

    async def scenario():
        requests = []

        def handle(request):
            requests.append(request)
            if request.url.path.endswith("/sessions"):
                assert json.loads(request.content) == {
                    "memory": {"enabled": True, "spaces": [{"name": "project", "space_id": "msp_1", "access": "read"}]}
                }
                return httpx2.Response(
                    201,
                    json={
                        "id": "ses_1",
                        "workspace_id": "ws_1",
                        "labels": {},
                        "created_by_id": "usr_1",
                        "last_run_id": None,
                        "version": 1,
                        "created_at": NOW,
                        "updated_at": NOW,
                    },
                )
            if request.url.path == "/api/v1/threads/thr_1":
                return httpx2.Response(200, json=thread_view(), headers={"ETag": '"thr:1"'})
            return response_for(request)

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            session = await namespace["create_shared_notes_session"](client)
            assert session.id == "ses_1"
            assert (await namespace["restrict_mount"](client, "thr_1", "work")).permission_ceiling.operations == []
            assert (await namespace["check_desktop"](client, "env_1")).status == wire.ComputerCheckStatus.UNSUPPORTED
            assert (await namespace["executed_agent"](client, "run_1")).config.instructions == "Run override"
            assert await namespace["read_retained_image"](client, "run_1", "img_1") == (
                b"\x89PNG\r\n\x00\xff",
                "image/png",
            )
            assert (await namespace["request_metrics"](client, "mur_1")).time_to_first_chunk_seconds is None
        assert len(requests) == 8
        assert requests[3].headers["if-match"] == '"thr:1"'

    asyncio.run(scenario())
