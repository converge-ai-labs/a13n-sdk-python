"""Installed-SDK memory acceptance on an existing disposable HTTPS Service.

Requires the ordinary acceptance environment plus A13N_ORGANIZATION and
A13N_MEMORY_PROVIDER, an accessible mem0_oss provider. Never run on production.
The caller owns fixture lifecycle. No external cloud-provider claim is made.
"""

from __future__ import annotations

import asyncio
import json
import os
from typing import Any
from uuid import uuid4

from a13n import ApiError, Client
from a13n.generated import models as wire


def required(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(f"{name} is required")
    return value


def etag(result: Any) -> str:
    assert result.etag
    return result.etag


async def main() -> None:
    async with Client(
        required("A13N_SERVICE_URL"), required("A13N_API_TOKEN"), ca_bundle=required("A13N_CA_BUNDLE")
    ) as client:
        workspace = client.workspaces(required("A13N_WORKSPACE"))
        organization = client.organizations(required("A13N_ORGANIZATION"))
        provider = organization.memory_providers(required("A13N_MEMORY_PROVIDER"))
        assert (await provider.get()).value.type_ == "mem0_oss"
        assert (await provider.test()).value.status == wire.ProviderTestStatus.SUCCEEDED
        assert required("A13N_MEMORY_PROVIDER") in [p.id async for p in organization.memory_providers.iter()]
        assert (await client.resources.auth.configuration.get()).value.initialized
        assert (await client.resources.healthz.get()).status_code == 200
        assert (await client.resources.readyz.get()).status_code == 200

        key = f"py-memory-{uuid4().hex}"
        created = await workspace.memories.create(body=wire.MemoryCreate(key=key, name=key))
        memory = workspace.memories(created.value.id)
        updated = await memory.update(body=wire.MemoryUpdate(name="SDK file memory"), if_match=etag(created))
        assert updated.value.name == "SDK file memory"
        assert memory.id in [item.id async for item in workspace.memories.iter()]
        path = "projects/计划 #1%.md"
        file = memory.files(path)
        first = await memory.files.create(body=wire.MemoryFileCreate(path=path, content="first"))
        assert (await file.get()).value.content == "first"
        await file.replace(body=wire.MemoryFileReplace(content="second"), if_match=etag(first))
        try:
            await file.replace(body=wire.MemoryFileReplace(content="stale"), if_match=etag(first))
        except ApiError as error:
            assert error.status == 412
        else:
            raise AssertionError("A stale file ETag was accepted")
        revisions = [item async for item in memory.revisions.iter(path=path, limit=1)]
        original = next(item.seq for item in revisions if item.op == wire.MemoryRevisionOp.CREATE)
        assert (await memory.revisions(original).get()).value.content == "first"
        current = await file.get()
        moved_path = "archive/计划.md"
        moved = await memory.files.move(
            body=wire.MemoryFileMove(source=path, destination=moved_path), if_match=etag(current)
        )
        assert moved.value.path == moved_path
        assert [item.path async for item in memory.files.iter(limit=1)] == [moved_path]
        await memory.files(moved_path).delete(if_match=etag(moved))
        changed = next(item.seq for item in revisions if item.op == wire.MemoryRevisionOp.UPDATE)
        restored = await memory.revisions(changed).restore()
        assert restored.value.file is not None and restored.value.file.content == "first"
        # Restore undoes a change: restoring the creation removes the current file.
        undone = await memory.revisions(original).restore(if_match=etag(await file.get()))
        assert undone.value.file is None
        assert (await memory.revisions(changed).restore()).value.file is not None

        mounts = [wire.MemoryMount(name="notes", memory_id=memory.id, access=wire.MemoryAccess.READ)]
        submitted = await workspace.threads.create(
            body=wire.NewThread(
                agent_id=required("A13N_AGENT"),
                memories=mounts,
                payload=wire.MessagePayload(content=[wire.TextPart(type_="text", text="Memory SDK acceptance.")]),
            ),
            idempotency_key=key,
        )
        assert submitted.run is not None
        thread = submitted.thread
        run = submitted.run
        assert (await run.wait(timeout=60, poll_interval=0.1)).value.status == wire.RunStatus.COMPLETED
        state = await thread.get()
        mounted = await thread.memories("notes").update(
            body=wire.MemoryMountUpdate(access=wire.MemoryAccess.WRITE), if_match=etag(state)
        )
        assert (await run.get()).value.memory_mounts[0].access == wire.MemoryAccess.READ
        removed = await thread.memories("notes").delete(if_match=etag(mounted))
        extra = await thread.memories.create(
            body=wire.MemoryMount(name="extra", memory_id=memory.id, access=wire.MemoryAccess.READ),
            if_match=etag(removed),
        )
        assert len((await thread.memories.list()).value.items) == 1
        await thread.memories("extra").delete(if_match=etag(extra))

        record_created = await workspace.memories.create(
            body=wire.MemoryCreate(key=f"{key}-records", name=key, type_="mem0_oss", provider_id=provider.id)
        )
        records_memory = workspace.memories(record_created.value.id)
        record = await records_memory.records.create(body=wire.MemoryRecordText(text="prefers tea"))
        await records_memory.records(record.value.id).replace(body=wire.MemoryRecordText(text="prefers coffee"))
        found = await records_memory.records.search(body=wire.MemoryRecordSearch(query="coffee", limit=3))
        assert any(item.id == record.value.id and item.text == "prefers coffee" for item in found.value.items)
        assert record.value.id in [item.id async for item in records_memory.records.iter(limit=1)]
        await records_memory.records(record.value.id).delete()
        assert not (await records_memory.records.list()).value.items
        await records_memory.delete(if_match=etag(await records_memory.get()))
        assert (await memory.revisions.delete(path=moved_path)).value.purged > 0
        await memory.delete(if_match=etag(await memory.get()))
        print(
            json.dumps(
                {
                    "memory_acceptance": "passed",
                    "sdk": "python",
                    "file_cas": True,
                    "numeric_revision_restore": True,
                    "frozen_run_mounts": True,
                    "record_crud_search": True,
                    "provider_test": "fixture",
                }
            )
        )


if __name__ == "__main__":
    asyncio.run(main())
