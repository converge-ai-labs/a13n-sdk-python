"""Opt-in Native HTTPS smoke check against an existing configured Service.

Requires A13N_SERVICE_URL, A13N_API_TOKEN, A13N_AGENT, and A13N_CA_BUNDLE. Creates a Thread and an Asset, retaining both for inspection.
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
        agents = await client.resources.agents.list(limit=10)
        interaction = await client.agents(os.environ["A13N_AGENT"]).start(
            "[slow] [long] Native Python SDK integration check.", idempotency_key=key + "-start"
        )
        frames = 0
        async with asyncio.timeout(120):
            async with interaction:
                async for _frame in interaction:
                    frames += 1
                final = await interaction.result()
        items = await final.run.items.get()
        with BytesIO(payload) as source:
            uploaded = await client.resources.uploads.create(
                body=wire.UploadCreate(
                    file=File(payload=source, file_name="sdk-integration.txt", mime_type="text/plain")
                ),
                idempotency_key=key + "-upload",
            )
            if source.closed:
                raise RuntimeError("SDK closed the caller-owned upload stream")
        asset = await client.resources.assets.create(
            body=wire.AssetCreate(name="sdk-integration.txt", upload_id=uploaded.value.upload_id)
        )
        received = bytearray()
        async with client.resources.assets(asset.value.id).content.get_stream() as response:
            if response.status_code != 200:
                raise RuntimeError(f"Asset read returned {response.status_code}")
            async for chunk in response.aiter_bytes():
                received.extend(chunk)
        if received != payload or final.status != wire.RunStatus.COMPLETED:
            raise RuntimeError("Asset content mismatch or Run did not complete")
        print(
            json.dumps(
                {
                    "run_id": final.run.id,
                    "thread_id": interaction.thread.id,
                    "status": str(final.status),
                    "item_count": len(items.value.items),
                    "items_complete": items.value.complete,
                    "finite_frame_count": frames,
                    "asset_id": asset.value.id,
                    "binary_bytes": len(received),
                    "agents_on_page": len(agents.value.items),
                }
            )
        )


if __name__ == "__main__":
    asyncio.run(main())
