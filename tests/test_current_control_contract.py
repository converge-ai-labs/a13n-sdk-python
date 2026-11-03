"""Regression coverage for current control models and historical pending evidence."""

import httpx2

from a13n import UNSET
from a13n._values import Pending
from a13n.generated import models as wire
from a13n.generated.api.browsers import browser_viewer
from a13n.generated.api.environments import open_desktop_viewer
from a13n.generated.client import Client
from tests.test_interaction import run_view


def test_current_and_historical_pending_remain_distinct() -> None:
    current = {"approvals": [], "calls": []}
    historical = {**current, "desktop_control_id": "dsk_1"}
    for value, kind in ((current, wire.Pending), (historical, wire.HistoricalDesktopPending)):
        raw = {**run_view(status="waiting"), "pending": value}
        parsed = wire.RunView.from_dict(raw)
        assert isinstance(parsed.pending, kind)
        assert parsed.pending.to_dict() == value
        pending = Pending.from_wire(parsed.pending)
        assert pending.desktop_control_id == ("dsk_1" if kind is wire.HistoricalDesktopPending else UNSET)


def test_browser_and_desktop_models_and_viewer_responses_are_distinct() -> None:
    request = {"thread_id": "thr_1", "lease_seconds": 30}
    for model in (wire.Takeover, wire.DesktopTakeover):
        assert model.from_dict(request).to_dict() == request
    assert wire.Takeover is not wire.DesktopTakeover

    browser = {"url": "wss://browser.example", "expires_at": "2026-11-03T06:00:00+00:00", "episode": 1}
    desktop = {
        "websocket_url": "wss://desktop.example",
        "expires_at": "2026-11-03T06:00:00+00:00",
        "episode": 2,
        "generation": 3,
        "mode": "control",
        "password": "secret",
    }
    client = Client(base_url="https://service.example")
    b = browser_viewer._parse_response(client=client, response=httpx2.Response(200, json=browser))
    d = open_desktop_viewer._parse_response(client=client, response=httpx2.Response(200, json=desktop))
    assert isinstance(b, wire.Viewer) and b.to_dict() == browser
    assert isinstance(d, wire.DesktopViewer) and d.to_dict() == desktop


def test_browser_takeover_request_and_response() -> None:
    import asyncio
    import json

    from a13n import Client as PublicClient
    from tests.test_interaction import NOW

    browser = {
        "control": "human",
        "control_expires_at": None,
        "created_at": NOW,
        "delete_after_seconds": None,
        "episode": 1,
        "expires_at": None,
        "failure": None,
        "generation": 1,
        "id": "brw_1",
        "idle_seconds": None,
        "name": "browser",
        "organization_id": "org_1",
        "provider_id": None,
        "source": "managed",
        "status": "ready",
        "stop_after_seconds": None,
        "updated_at": NOW,
        "version": 2,
        "workspace_id": "ws_1",
    }
    seen = []

    def handle(request):
        seen.append(request)
        return httpx2.Response(200, json=browser)

    async def scenario() -> None:
        async with PublicClient("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            result = await client.api.browsers("brw /?#%").takeover(
                body=wire.Takeover(thread_id="thr_1", lease_seconds=30), if_match='"brw:1"'
            )
            assert isinstance(result.value, wire.Browser)
            assert result.value.id == "brw_1"
        assert len(seen) == 1
        assert seen[0].url.raw_path.decode() == "/api/v1/browsers/brw%20%2F%3F%23%25/takeover"
        assert seen[0].headers["if-match"] == '"brw:1"'
        assert json.loads(seen[0].content) == {"thread_id": "thr_1", "lease_seconds": 30}

    asyncio.run(scenario())


def test_browser_viewer_request_and_response() -> None:
    import asyncio

    from a13n import Client as PublicClient

    viewer = {"url": "wss://browser.example", "expires_at": "2026-11-03T06:00:00+00:00", "episode": 1}
    seen = []

    def handle(request):
        seen.append(request)
        return httpx2.Response(200, json=viewer)

    async def scenario() -> None:
        async with PublicClient("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            result = await client.api.browsers("brw /?#%").viewer(x_workspace_id="ws_1")
            assert isinstance(result.value, wire.Viewer)
            assert result.value.to_dict() == viewer
        assert len(seen) == 1
        assert seen[0].method == "POST"
        assert seen[0].url.raw_path.decode() == "/api/v1/browsers/brw%20%2F%3F%23%25/viewer"
        assert seen[0].headers["x-workspace-id"] == "ws_1"

    asyncio.run(scenario())
