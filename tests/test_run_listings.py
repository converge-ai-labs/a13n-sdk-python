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
                    "first_number": 501,
                    "previous_cursor": "newer",
                    "next_cursor": "older" if len(requests) == 1 else None,
                },
            )

        async with Client("https://service.test", transport=httpx2.MockTransport(respond)) as client:
            pages = client.api.threads("thr_1").runs.pages(anchor="run_1", limit=2)
            assert not requests
            page = await anext(pages)
            assert isinstance(page.value, wire.ThreadRunPage)
            assert page.value.total == 10000 and page.value.first_number == 501
            assert page.value.previous_cursor == "newer"
            listed = page.value.items[0]
            assert isinstance(listed, wire.RunListItem)
            assert listed.input_preview.text == "😀" * 200 and listed.input_preview.truncated
            assert not hasattr(listed, "output") and not hasattr(listed, "options")
            assert len(requests) == 1
            await anext(pages)
            assert len(requests) == 2
            await pages.aclose()

    asyncio.run(scenario())
