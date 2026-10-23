"""Pinned desktop, discovery and latest-generation usage boundaries (mock HTTP)."""

import asyncio
import json

import httpx2
import pytest

from a13n import UNSET, AgentOverride, ApiError, Client, ProtocolError, RunOptions, SessionStream
from a13n.generated import models as wire
from tests.test_interaction import NOW, entry_view, run_view, submitted
from tests.test_session_streaming import session_state
from tests.test_streaming import sse

BROWSER_SESSION = "browser_session_token_1234"
CONTEXT = {
    "run_id": "run_1",
    "record_id": "rec_1",
    "input_tokens": 0,
    "output_tokens": None,
    "context_window_tokens": None,
}


def desktop_view(**changes) -> dict:
    return {
        "id": "dsk_1",
        "run_id": "run_1",
        "tool_call_id": None,
        "cause": "user",
        "environment_id": "env_1",
        "mount": "computer",
        "reason": "Finish sign in",
        "state": "viewing",
        "epoch": 0,
        "controller_id": None,
        "deadline": NOW,
        "lease_expires_at": None,
        "failure": None,
        "outcome": None,
        **changes,
    }


def desktop_wait() -> dict:
    return {
        **run_view(status="waiting"),
        "wait_reason": "desktop_control",
        "pending": {"calls": [], "approvals": [], "desktop_control_id": "dsk_1"},
    }


@pytest.mark.parametrize(
    "value",
    [
        {},
        {"config": {}},
        {"config": {"mode": "proxy"}},
        {
            "config": {
                "mode": "proxy",
                "max_results": 0,
                "max_search_bytes": 0,
                "search_name": "find",
                "call_name": "call",
            }
        },
        {
            "groups": {
                "selected": {
                    "description": "Selected sources",
                    "connections": ["con_" + "a" * 20],
                    "plugins": ["example.tools"],
                    "platform": False,
                }
            }
        },
    ],
)
def test_tool_search_round_trip_uses_one_generated_hierarchy(value: dict) -> None:
    search = wire.ToolSearch.from_dict(value)
    assert search.to_dict() == value
    if "config" in value:
        assert isinstance(search.config, wire.ToolSearchConfig)
    for model in (wire.AgentConfigInput, wire.AgentConfigOutput, wire.AgentOverrideInput, wire.AgentOverrideOutput):
        base = {"model": "model_1"} if model in (wire.AgentConfigInput, wire.AgentConfigOutput) else {}
        assert model.from_dict({**base, "tool_search": value}).to_dict() == {**base, "tool_search": value}
    assert RunOptions(overrides=AgentOverride(tool_search=search)).into_wire().to_dict() == {
        "overrides": {"tool_search": value}
    }


@pytest.mark.parametrize(
    "value",
    [
        {"config": {"mode": "native"}},
        {"config": None},
        {"config": {"mode": "other"}},
        {"config": {"mode": "native", "strategy": "invalid"}},
        {"config": {"mode": "native", "strategy": False}},
        {"config": {"mode": "native", "search_name": "mixed"}},
        {"config": {"mode": "proxy", "strategy": "bm25"}},
        {"config": {"mode": "proxy", "max_results": True}},
        {"groups": None},
        {"groups": {"bad": {"description": ""}}},
        {"groups": {"bad": {"description": "x", "connections": ["invalid"]}}},
        {"groups": {"bad": {"description": "x", "platform": 0}}},
        {"unknown": False},
    ],
)
def test_tool_search_invalid_union_forms_fail_at_model_and_nullable_parent(value: dict) -> None:
    with pytest.raises(ValueError):
        wire.ToolSearch.from_dict(value)
    for model in (wire.AgentConfigInput, wire.AgentConfigOutput, wire.AgentOverrideInput, wire.AgentOverrideOutput):
        with pytest.raises(ValueError):
            base = {"model": "model_1"} if model in (wire.AgentConfigInput, wire.AgentConfigOutput) else {}
            model.from_dict({**base, "tool_search": value})


def test_typed_tool_search_validates_serialization_and_omission_null_empty() -> None:
    assert AgentOverride().to_dict() == {}
    assert AgentOverride(tool_search=None).to_dict() == {"tool_search": None}
    assert wire.ToolSearchConfig(mode="proxy").to_dict() == {"mode": "proxy"}
    search = wire.ToolSearch(config=wire.ToolSearchConfig(mode="proxy"), groups=wire.ToolSearchGroups())
    assert AgentOverride(tool_search=search).to_dict() == {"tool_search": {"config": {"mode": "proxy"}, "groups": {}}}
    invalid = wire.ToolSearchConfig(mode="proxy")
    invalid.mode = "native"  # type: ignore[assignment] -- runtime callers also cross this boundary
    with pytest.raises(ValueError):
        RunOptions(overrides=AgentOverride(tool_search=wire.ToolSearch(config=invalid))).into_wire()
    for model in (wire.AgentConfigInput, wire.AgentConfigOutput, wire.AgentOverrideInput, wire.AgentOverrideOutput):
        base = {"model": "model_1"} if model in (wire.AgentConfigInput, wire.AgentConfigOutput) else {}
        assert model.from_dict(base).to_dict() == base
        assert model.from_dict({**base, "tool_search": None}).to_dict() == {**base, "tool_search": None}


@pytest.mark.parametrize("mode", ["bearer", "session"])
def test_all_nine_operations_share_bound_paths_credentials_evidence_and_one_request(mode: str) -> None:
    async def scenario() -> None:
        requests = []

        def handle(request):
            requests.append(request)
            if request.url.path.endswith("/context"):
                value = CONTEXT
            elif request.url.path.endswith(("/view", "/control")):
                value = {
                    "assistance": desktop_view(),
                    "mode": "view",
                    "password": "one-use",
                    "websocket_url": "wss://desktop.example/socket",
                    "expires_in_seconds": 30,
                }
            else:
                value = desktop_view()
            return httpx2.Response(200, json=value, headers={"X-Request-ID": "req_new", "Cache-Control": "no-store"})

        client = (
            Client.session(
                "https://service.example",
                origin="https://service.example",
                workspace_id="ws_1",
                csrf_token="proof",
                transport=httpx2.MockTransport(handle),
            )
            if mode == "session"
            else Client("https://service.example", "token", transport=httpx2.MockTransport(handle))
        )
        async with client:
            api = client.api
            assistance = api.desktop_assistance("dsk /?#%")
            control = wire.Control(session_id=BROWSER_SESSION, epoch=0)
            assert not requests
            responses = [
                await api.runs("run /?#%").desktop_assistance("call /?#%").get(),
                await api.runs("run /?#%").desktop_control.get(),
                await api.runs("run /?#%").desktop_control.create(
                    body=wire.Request(mount="computer", reason="Finish sign in")
                ),
                await assistance.view(body=control),
                await assistance.request_control(),
                await assistance.control(body=control, renew=False),
                await assistance.disconnect(body=control),
                await assistance.complete(body=wire.Completion(session_id=BROWSER_SESSION, epoch=0)),
                await api.usage.context.get(record_id="rec_1"),
            ]
            assert all(
                result.request_id == "req_new" and result.headers["cache-control"] == "no-store" for result in responses
            )
            assert responses[-1].value.to_dict() == CONTEXT
        assert len(requests) == 9
        assert [request.method for request in requests] == [
            "GET",
            "GET",
            "POST",
            "POST",
            "POST",
            "POST",
            "POST",
            "POST",
            "GET",
        ]
        expected_paths = [
            "/api/v1/runs/run%20%2F%3F%23%25/desktop-assistance/call%20%2F%3F%23%25",
            "/api/v1/runs/run%20%2F%3F%23%25/desktop-control",
            "/api/v1/runs/run%20%2F%3F%23%25/desktop-control",
            *[
                "/api/v1/desktop-assistance/dsk%20%2F%3F%23%25/" + suffix
                for suffix in ["view", "request-control", "control", "disconnect", "complete"]
            ],
            "/api/v1/usage/context",
        ]
        assert [request.url.raw_path.decode().split("?")[0] for request in requests] == expected_paths
        assert dict(requests[5].url.params) == {"renew": "false"}
        assert "renew" not in requests[3].url.params
        assert json.loads(requests[3].content) == {"session_id": BROWSER_SESSION, "epoch": 0}
        for request in requests:
            if mode == "session":
                assert request.headers["x-workspace-id"] == "ws_1"
                assert request.headers["origin"] == "https://service.example"
                if request.method == "POST":
                    assert request.headers["x-csrf-token"] == "proof"
            else:
                assert request.headers["authorization"] == "Bearer token"
                assert "x-workspace-id" not in request.headers

    asyncio.run(scenario())


@pytest.mark.parametrize(
    "model,value",
    [
        (wire.Control, {"session_id": "ses_service", "epoch": 0}),
        (wire.Control, {"session_id": BROWSER_SESSION, "epoch": -1}),
        (wire.Control, {"session_id": BROWSER_SESSION, "epoch": False}),
        (wire.Completion, {"session_id": BROWSER_SESSION, "epoch": 0, "outcome": "other"}),
        (wire.Request, {"mount": "computer", "reason": ""}),
    ],
)
def test_desktop_typed_request_constraints(model, value: dict) -> None:
    with pytest.raises(ValueError):
        model.from_dict(value)


@pytest.mark.parametrize("kind", ["context", "desktop"])
@pytest.mark.parametrize("value", [None, {}, False, [], {"run_id": "run_1"}])
def test_nullable_reads_accept_only_null_or_complete_native_model(kind: str, value) -> None:
    async def scenario() -> None:
        requests = []

        def handle(request):
            requests.append(request)
            return httpx2.Response(
                200,
                content=json.dumps(value).encode(),
                headers={"Content-Type": "application/json", "X-Request-ID": "nullable"},
            )

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            resource = client.api.usage.context if kind == "context" else client.api.runs("run_1").desktop_control
            if value is None:
                result = await resource.get()
                assert result.value is None and result.status_code == 200 and result.request_id == "nullable"
            else:
                with pytest.raises(ProtocolError):
                    await resource.get()
        assert len(requests) == 1

    asyncio.run(scenario())


@pytest.mark.parametrize("field", ["input_tokens", "output_tokens", "context_window_tokens", "run_id", "record_id"])
def test_context_required_nullable_fields_and_types(field: str) -> None:
    for value in [{k: v for k, v in CONTEXT.items() if k != field}, {**CONTEXT, field: True}]:
        with pytest.raises(ValueError):
            wire.ContextUsage.from_dict(value)
    assert wire.ContextUsage.from_dict(CONTEXT).to_dict() == CONTEXT


def test_context_selectors_are_forwarded_for_service_validation_and_errors_do_not_retry() -> None:
    async def scenario() -> None:
        requests = []

        def handle(request):
            requests.append(request)
            return httpx2.Response(
                400,
                json={
                    "error": {
                        "code": "invalid_argument",
                        "message": "Exactly one selector",
                        "details": {},
                        "request_id": "invalid",
                    }
                },
            )

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            with pytest.raises(ApiError) as caught:
                await client.api.usage.context.get(thread_id="thr_1", run_id="run_1")
            assert caught.value.status == 400 and caught.value.request_id == "invalid"
        assert len(requests) == 1 and dict(requests[0].url.params) == {"thread_id": "thr_1", "run_id": "run_1"}

    asyncio.run(scenario())


def test_desktop_wait_ends_exact_consumed_entry_interaction_and_explicit_empty_resume() -> None:
    async def scenario() -> None:
        requests = []
        completed = False

        def handle(request):
            nonlocal completed
            requests.append(request)
            path = request.url.path
            if path == "/api/v1/threads":
                return httpx2.Response(201, json=submitted())
            if "/inbox/" in path:
                return httpx2.Response(200, json={**entry_view(status="consumed"), "assigned_run_id": "run_1"})
            if path.endswith("/complete"):
                completed = True
                return httpx2.Response(200, json=desktop_view(state="ready_to_resume", outcome={"status": "completed"}))
            if path.endswith("/resume"):
                assert completed and json.loads(request.content) == {"approvals": {}, "calls": {}}
                return httpx2.Response(201, json=run_view("run_2"))
            assert path == "/api/v1/runs/run_1"
            return httpx2.Response(200, json=desktop_wait())

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            interaction = await client.agents("agt_1").start("hello", idempotency_key="start")
            async with interaction:
                assert [frame async for frame in interaction] == []
                outcome = await interaction.result()
            assert outcome.run_id == "run_1" and outcome.status == "waiting"
            assert outcome.pending is not None and outcome.pending.desktop_control_id == "dsk_1"
            assert outcome.pending.calls == outcome.pending.approvals == ()
            assert outcome.evidence.value.wait_reason == wire.WaitReason.DESKTOP_CONTROL
            assert len(requests) == 3  # No SSE, synthetic answer, control, or successor observation.
            await client.api.desktop_assistance("dsk_1").complete(
                body=wire.Completion(session_id=BROWSER_SESSION, epoch=0)
            )
            assert len(requests) == 4
            successor = await outcome.run.resume({}, idempotency_key="resume")
            assert successor.run is not None and successor.run.id == "run_2"
            assert outcome.run.id == "run_1" and len(requests) == 5

    asyncio.run(scenario())


def test_session_projects_desktop_wait_with_no_cursor_or_automatic_followup() -> None:
    async def scenario() -> None:
        state = session_state()
        state.update(current_run=None, last_run=desktop_wait())
        requests = []

        def handle(request):
            requests.append(request)
            return httpx2.Response(200, content=sse("thread", state), headers={"Content-Type": "text/event-stream"})

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            async with SessionStream(client.api.sessions("ses_1")) as stream:
                frames = [frame async for frame in stream]
            assert len(frames) == 1
            run = frames[0].data.last_run
            assert run is not None and run is not UNSET and run.wait_reason == wire.WaitReason.DESKTOP_CONTROL
            assert run.pending.desktop_control_id == "dsk_1"
        assert len(requests) == 1 and not requests[0].url.params
        assert "Last-Event-ID" not in requests[0].headers

    asyncio.run(scenario())
