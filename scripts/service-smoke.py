"""Opt-in Native HTTPS smoke check against an existing configured Service.

Requires A13N_SERVICE_URL, A13N_API_TOKEN, A13N_WORKSPACE, A13N_AGENT,
and A13N_CA_BUNDLE. Creates a Thread and an Asset, retaining both for inspection.
"""

import asyncio
import json
import os
from io import BytesIO
from uuid import uuid4

from a13n import Client
from a13n.generated import models as wire
from a13n.generated.types import File


async def main() -> None:
    key = "sdk-smoke-" + uuid4().hex
    payload = b"Python SDK binary integration\n" * 10000
    async with Client(
        os.environ["A13N_SERVICE_URL"], os.environ["A13N_API_TOKEN"], ca_bundle=os.environ["A13N_CA_BUNDLE"]
    ) as client:
        workspace = client.workspaces(os.environ["A13N_WORKSPACE"])
        agents = await workspace.agents.list(limit=10)
        submitted = await workspace.start(
            "Native Python SDK integration check.", agent_id=os.environ["A13N_AGENT"], idempotency_key=key + "-start"
        )
        if submitted.run is None:
            raise RuntimeError("New Thread did not return a Run")
        final = await submitted.run.wait(timeout=120, poll_interval=0.2)
        items = await submitted.run.items.get()
        with BytesIO(payload) as source:
            uploaded = await workspace.uploads.create(
                body=wire.UploadCreate(
                    file=File(payload=source, file_name="sdk-integration.txt", mime_type="text/plain")
                ),
                idempotency_key=key + "-upload",
            )
            if source.closed:
                raise RuntimeError("SDK closed the caller-owned upload stream")
        asset = await workspace.assets.create(
            body=wire.AssetCreate(name="sdk-integration.txt", upload_id=uploaded.value.upload_id)
        )
        received = bytearray()
        async with workspace.assets(asset.value.id).content.get_stream() as response:
            if response.status_code != 200:
                raise RuntimeError(f"Asset read returned {response.status_code}")
            async for chunk in response.aiter_bytes():
                received.extend(chunk)
        if received != payload or final.value.status != wire.RunStatus.COMPLETED:
            raise RuntimeError("Asset content mismatch or Run did not complete")
        print(
            json.dumps(
                {
                    "run_id": submitted.run.id,
                    "thread_id": submitted.thread.id,
                    "status": str(final.value.status),
                    "item_count": len(items.value.items),
                    "items_complete": items.value.complete,
                    "asset_id": asset.value.id,
                    "binary_bytes": len(received),
                    "agents_on_page": len(agents.value.items),
                }
            )
        )


if __name__ == "__main__":
    asyncio.run(main())
