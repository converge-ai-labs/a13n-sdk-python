"""Wire regression coverage for the current Service contract."""

import asyncio
import json

import httpx2

from a13n import UNSET, Client, SessionStream
from a13n.generated import models as wire
from tests.test_interaction import run_view
from tests.test_session_streaming import session_state
from tests.test_streaming import sse


def test_app_plugins_get_and_replace_preserve_if_match_and_false():
    async def scenario():
        requests = []

        def respond(request):
            requests.append(request)
            return httpx2.Response(
                200, json={"id": "org_1", "version": 2, "permissions": [], "items": []}, headers={"ETag": '"org_1:2"'}
            )

        async with Client.session(
            "https://service.example",
            origin="https://service.example",
            workspace_id="ws_1",
            csrf_token="proof",
            transport=httpx2.MockTransport(respond),
        ) as client:
            plugins = client.api.organizations("org_1").app_plugins
            result = await plugins.get()
            assert isinstance(result.value, wire.AppPlugins)
            assert result.etag == '"org_1:2"'
            await plugins("app_1").replace(body=wire.AppUpdate(enabled=False), if_match='"org_1:1"')
        assert [(r.method, r.url.path) for r in requests] == [
            ("GET", "/api/v1/organizations/org_1/app-plugins"),
            ("PUT", "/api/v1/organizations/org_1/app-plugins/app_1"),
        ]
        assert all("x-workspace-id" not in request.headers for request in requests)
        assert requests[1].headers["if-match"] == '"org_1:1"'
        assert json.loads(requests[1].content) == {"enabled": False}

    asyncio.run(scenario())


def test_run_finding_analysis_id_absent_null_and_string_round_trip():
    for value in (UNSET, None, "ana_1"):
        raw = run_view(status="completed")
        if value is not UNSET:
            raw["finding_analysis_id"] = value
        parsed = wire.RunView.from_dict(raw)
        if value is UNSET:
            assert parsed.finding_analysis_id is UNSET
        else:
            assert parsed.finding_analysis_id == value
        assert ("finding_analysis_id" in parsed.to_dict()) == (value is not UNSET)
        if value is not UNSET:
            assert parsed.to_dict()["finding_analysis_id"] == value


def test_session_thread_frames_preserve_run_finding_analysis_id_presence():
    async def scenario():
        states = []
        for value in (UNSET, None, "ana_1"):
            state = session_state()
            if value is not UNSET:
                state["current_run"]["finding_analysis_id"] = value
            states.append(state)
        payload = b"".join(sse("thread", state) for state in states)
        transport = httpx2.MockTransport(
            lambda _: httpx2.Response(200, content=payload, headers={"Content-Type": "text/event-stream"})
        )
        async with Client("https://service.example", transport=transport) as client:
            async with SessionStream(client.api.sessions("ses_1")) as stream:
                frames = [frame async for frame in stream]
        for frame, original, value in zip(frames, states, (UNSET, None, "ana_1"), strict=True):
            run = frame.data.current_run
            assert isinstance(run, wire.RunView)
            if value is UNSET:
                assert run.finding_analysis_id is UNSET
            else:
                assert run.finding_analysis_id == value
            serialized = run.to_dict()
            assert ("finding_analysis_id" in serialized) == ("finding_analysis_id" in original["current_run"])
            if value is not UNSET:
                assert serialized["finding_analysis_id"] == value

    asyncio.run(scenario())


def test_fresh_schedule_invocation_retains_initial_resources() -> None:
    from a13n.generated import models as wire

    value = {
        "agent_id": "agt_123",
        "agent_revision_id": None,
        "payload": {"content": [{"type": "text", "text": "hello"}]},
        "browser_binding": {"browser_id": "brw_123", "tab_access": "global"},
        "environments": [{"environment_id": "env_123", "name": "work"}],
        "memories": [{"memory_id": "mem_123", "name": "notes", "access": "read"}],
    }
    for model in (wire.ScheduleInvocationInput, wire.ScheduleInvocationOutput):
        encoded = model.from_dict(value).to_dict()
        assert encoded["browser_binding"] == value["browser_binding"]
        assert encoded["environments"] == value["environments"]
        assert encoded["memories"] == value["memories"]
