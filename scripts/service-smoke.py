"""Opt-in HTTP-only integration check against an existing configured Service.

Requires A13N_SERVICE_URL, A13N_API_TOKEN, A13N_WORKSPACE and A13N_AGENT.
Creates a Run and an Asset; retains both for inspection. Never resets Service state.
"""

import asyncio
import json
import os
from io import BytesIO
from uuid import uuid4

from a13n import Client
from a13n.generated.types import File


async def main() -> None:
    key = "sdk-smoke-" + uuid4().hex
    payload = b"Python SDK binary integration\n" * 10000
    async with Client(os.environ["A13N_SERVICE_URL"], os.environ["A13N_API_TOKEN"]) as client:
        workspace = client.workspaces(os.environ["A13N_WORKSPACE"])
        agents = await workspace.agents.list(limit=10)
        models = await workspace.models.list()
        web_types = await client.resources.web_provider_types.list()
        accepted = await workspace.agents(os.environ["A13N_AGENT"]).start(
            "Hello from the Python SDK integration check.", idempotency_key=key + "-start"
        )
        # Detach after applying one event, then resume from that exact SSE cursor.
        async with accepted.run.stream() as first:
            applied = await anext(first)
        events = [applied.event.event_type]
        async with asyncio.timeout(120):
            async with accepted.run.stream(after=applied.cursor) as resumed:
                async for observation in resumed:
                    assert observation.cursor != applied.cursor
                    events.append(observation.event.event_type)
            final = await accepted.run.wait(timeout=30, poll_interval=0.2)
        items = await accepted.run.items.list()
        with BytesIO(payload) as source:
            asset = await workspace.assets.create(
                body=File(payload=source),
                filename="sdk-integration.txt",
                media_type="text/plain",
                idempotency_key=key + "-asset",
            )
            assert not source.closed
        received = bytearray()
        async with client.resources.assets(asset.value.id).content.get_stream() as response:
            assert response.status_code == 200
            async for chunk in response.aiter_bytes():
                received.extend(chunk)
        assert received == payload
        assert final.value.status == "completed", final.value.status
        print(
            json.dumps(
                {
                    "run_id": accepted.run.id,
                    "thread_id": accepted.thread.id,
                    "session_id": accepted.session.id,
                    "status": final.value.status,
                    "event_count": len(events),
                    "resumed_after": applied.cursor,
                    "item_count": len(items.value.items),
                    "items_complete": items.value.complete,
                    "items_finalized": items.value.finalized,
                    "asset_id": asset.value.id,
                    "binary_bytes": len(received),
                    "agents_on_page": len(agents.value.items),
                    "models_on_page": len(models.value.items),
                    "web_provider_types": len(web_types.value.items),
                }
            )
        )


if __name__ == "__main__":
    asyncio.run(main())
