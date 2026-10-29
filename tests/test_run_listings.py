import asyncio

import httpx2

from a13n import Client
from a13n.generated import models as wire
from tests.test_interaction import run_view


def test_thread_run_pages_are_lazy_and_only_anchor_the_first_request():
    async def scenario():
        requests = []
        fields = "agent_id agent_revision_id attempts created_at current_attempt_id id lineage max_attempts parent_run_id principal_id sealed_at session_id source_entry_id started_at status thread_id trigger updated_at version wait_reason workspace_id".split()
        original = run_view()
        item = {name: original[name] for name in fields}
        item["input_preview"] = {"text": "😀" * 200, "truncated": True}
        item.update(number=501, cost=None, model_calls=0, unpriced_requests=0)

        def respond(request):
            requests.append(request)
            assert "view" not in request.url.params
            assert request.url.params["limit"] == "2"
            if len(requests) == 1:
                assert request.url.params["anchor"] == "run_1"
                assert "cursor" not in request.url.params
            else:
                assert request.url.params["cursor"] == "older"
                assert "anchor" not in request.url.params
            return httpx2.Response(
                200,
                json={
                    "items": [item],
                    "total": 10000,
                    "previous_cursor": "newer",
                    "next_cursor": "older" if len(requests) == 1 else None,
                },
            )

        async with Client("https://service.test", transport=httpx2.MockTransport(respond)) as client:
            pages = client.api.threads("thr_1").runs.pages(anchor="run_1", limit=2)
            assert not requests
            page = await anext(pages)
            assert isinstance(page.value, wire.ThreadRunPage)
            assert page.value.total == 10000
            assert page.value.previous_cursor == "newer"
            listed = page.value.items[0]
            assert isinstance(listed, wire.ThreadRunItem)
            assert listed.number == 501
            assert listed.cost is None and listed.model_calls == 0 and listed.unpriced_requests == 0
            assert listed.input_preview.text == "😀" * 200 and listed.input_preview.truncated
            assert not hasattr(listed, "output") and not hasattr(listed, "options")
            assert len(requests) == 1
            await anext(pages)
            assert len(requests) == 2
            await pages.aclose()

    asyncio.run(scenario())


def test_metric_sorting_survives_lazy_pagination():
    async def scenario():
        requests = []

        def respond(request):
            requests.append(request)
            assert request.url.params["sort"] == "cost"
            assert request.url.params["direction"] == "asc"
            assert "anchor" not in request.url.params
            if len(requests) % 2 == 0:
                assert request.url.params["cursor"] == "ranked"
            payload = {"items": [], "next_cursor": "ranked" if len(requests) % 2 else None}
            if request.url.path.endswith("/runs"):
                payload.update(total=0, previous_cursor=None)
            return httpx2.Response(200, json=payload)

        async with Client("https://service.test", transport=httpx2.MockTransport(respond)) as client:
            pages = client.api.threads("thr_1").runs.pages(
                sort=wire.ListThreadRunsSortType0.COST, direction=wire.ListThreadRunsDirection.ASC
            )
            assert not requests
            assert len([page async for page in pages]) == 2
            sessions = client.api.sessions.pages(
                sort=wire.ListSessionsSort.COST, direction=wire.ListSessionsDirection.ASC
            )
            assert len(requests) == 2
            assert len([page async for page in sessions]) == 2

    asyncio.run(scenario())


def test_session_cost_preserves_null_zero_and_decimal_precision():
    for cost in (None, "0", "0.1234567890123456789"):
        session = wire.SessionView.from_dict(
            {
                "id": "ses_1",
                "workspace_id": "ws_1",
                "created_by_id": "usr_1",
                "labels": {},
                "last_run_id": None,
                "run_count": 0,
                "cost": cost,
                "unpriced_requests": 2,
                "version": 1,
                "created_at": "2026-10-29T00:00:00Z",
                "updated_at": "2026-10-29T00:00:00Z",
            }
        )
        assert session.cost == cost and session.run_count == 0 and session.unpriced_requests == 2
        assert session.to_dict()["cost"] == cost


def test_agent_summarize_preserves_explicit_false():
    for enabled in (False, True):
        config = wire.AgentConfigInput.from_dict({"model": "test", "summarize": enabled})
        assert config.summarize is enabled
        assert config.to_dict()["summarize"] is enabled
