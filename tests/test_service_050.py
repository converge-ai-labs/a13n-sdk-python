"""Native scoped reset and trace search wire boundaries."""

import asyncio
from datetime import UTC, datetime

import httpx2

from a13n import Client
from a13n.generated import models as wire


def test_scoped_reset_and_trace_filters_preserve_wire_values() -> None:
    async def scenario() -> None:
        requests: list[httpx2.Request] = []

        def respond(request: httpx2.Request) -> httpx2.Response:
            requests.append(request)
            if request.method == "POST":
                return httpx2.Response(200, json={"email_queued": False, "reset_url": None})
            return httpx2.Response(
                200, json={"items": [], "next_cursor": None, "total": 0, "collected_at": "2026-01-01T00:00:00Z"}
            )

        async with Client("https://service.example", "test", transport=httpx2.MockTransport(respond)) as client:
            result = await client.api.organizations("org /1").members("user /2").password_reset()
            assert result.value.email_queued is False
            await client.api.traces.search.list(
                started_after=datetime(2026, 1, 1, tzinfo=UTC),
                started_before=datetime(2026, 1, 2, tzinfo=UTC),
                order_by=wire.SearchTracesOrderBy.COST,
                direction=wire.SearchTracesDirection.ASC,
                min_duration_seconds=0,
                max_duration_seconds=10,
                min_cost_usd=0,
                max_cost_usd=1,
            )
        assert len(requests) == 2
        assert requests[0].method == "POST"
        assert requests[0].url.raw_path == b"/api/v1/organizations/org%20%2F1/members/user%20%2F2/password-reset"
        query = requests[1].url.params
        for key, value in {
            "order_by": "cost",
            "direction": "asc",
            "min_duration_seconds": "0",
            "max_duration_seconds": "10",
            "min_cost_usd": "0",
            "max_cost_usd": "1",
        }.items():
            assert query[key] == value

    asyncio.run(scenario())
