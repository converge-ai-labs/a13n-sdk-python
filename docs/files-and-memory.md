# Files and Memory

Use an Asset to attach a document to a message. Use Memory for reusable notes that an Agent can consult across conversations. They solve different problems: uploading an attachment does not create a Memory, and creating a Memory does not automatically mount it in a conversation.

The examples take an open `Client` from the [quick start](../README.md#quick-start). Your credential must permit the corresponding upload, Asset, or Memory operations.

## Attach a local document

The sequence is upload bytes, create an Asset, then reference its ID in a message. This function carries all three steps through to an outcome:

```python
from pathlib import Path
from uuid import uuid4

from a13n import Client, RunOutcome
from a13n.generated import models as wire
from a13n.generated.types import File


async def summarize_file(client: Client, agent_id: str, path: Path) -> RunOutcome:
    with path.open("rb") as source:
        uploaded = await client.resources.uploads.create(
            body=wire.UploadCreate(file=File(payload=source, file_name=path.name, mime_type="text/plain")),
            idempotency_key=uuid4().hex,
        )
    asset = await client.resources.assets.create(
        body=wire.AssetCreate(name=path.name, upload_id=uploaded.value.upload_id)
    )
    payload = wire.MessagePayload(
        content=[
            wire.TextPart(type_="text", text="Summarize this document and list any open questions."),
            wire.AssetPart(type_="asset", asset_id=asset.value.id),
        ]
    )
    interaction = await client.agents(agent_id).start(payload, idempotency_key=uuid4().hex)
    print("Asset:", asset.value.id, "Thread:", interaction.thread.id)
    return await interaction.result()
```

Call it with a UTF-8 text document such as `Path("report.txt")`. For another file type, set the correct MIME type and ensure your Agent's model/media configuration supports it. Successful storage does not guarantee that every model can interpret the content.

The SDK does not close caller-owned file objects. The `with` block closes this file after upload. In an application, record the returned upload and Asset IDs so a failure in a later step does not make you blindly repeat the whole sequence.

## Download without buffering the whole file

The streaming response must remain open while you consume its bytes:

```python
from pathlib import Path

from a13n import Client


async def download_asset(client: Client, asset_id: str, destination: Path) -> None:
    async with client.resources.assets(asset_id).content.get_stream() as response:
        response.raise_for_status()
        with destination.open("xb") as output:
            async for chunk in response.aiter_bytes():
                output.write(chunk)
    print("Downloaded:", destination)
```

This uses exclusive creation (`xb`) so an existing local file is not overwritten. A failed download may leave a partial new file. For an application that requires atomic replacement, write to a temporary path and rename only after successful completion. Raw streaming responses expose HTTP response handling; call `raise_for_status()` before writing error content into a file.

## Create reusable project notes

A file-backed Memory stores named text files. Create it once, write a guide, and keep the returned ID:

```python
from a13n import Client
from a13n.generated import models as wire


async def create_project_notes(client: Client) -> str:
    created = await client.resources.memories.create(
        body=wire.MemoryCreate(
            name="Project notes",
            guide="Read notes/project.md before answering project questions.",
        )
    )
    memory_id = created.value.id
    note = await client.resources.memories(memory_id).files.create(
        body=wire.MemoryFileCreate(
            path="notes/project.md",
            content="# Project\n\nThe first milestone is a working import pipeline.\n",
        )
    )
    print("Memory:", memory_id, "File:", note.value.path)
    return memory_id
```

Memory creation and file creation are separate requests, not one transaction. If the second fails, you still have the Memory ID and can inspect it before continuing. Do not create a duplicate Memory just because the file write failed.

## Mount notes in a conversation

Give a new conversation a named, read-only mount:

```python
from uuid import uuid4

from a13n import Client, RunOutcome
from a13n.generated import models as wire


async def ask_with_notes(client: Client, agent_id: str, memory_id: str) -> RunOutcome:
    interaction = await client.agents(agent_id).start(
        "Read the project notes and propose the next milestone.",
        memories=[wire.MemoryMount(name="notes", memory_id=memory_id, access=wire.MemoryAccess.READ)],
        idempotency_key=uuid4().hex,
    )
    return await interaction.result()
```

The mount name is the name exposed to the Agent; it is not the Memory's resource ID. Use write access only when the task should allow the Agent to modify that Memory. A Run retains the mount snapshot accepted when it starts: changing a Thread's mounts later does not rewrite the running execution's snapshot.

## Update a note without losing another writer's changes

Read the file, make an application-level edit, and submit the ETag from that read:

```python
from a13n import Client
from a13n.generated import models as wire


async def append_milestone(client: Client, memory_id: str, milestone: str) -> None:
    file = client.resources.memories(memory_id).files("notes/project.md")
    current = await file.get()
    updated = await file.replace(
        body=wire.MemoryFileReplace(content=current.value.content + "\n" + milestone + "\n"),
        if_match=current.etag,
    )
    print("Saved version:", updated.value.version)
```

If someone changed the file in between, the Service returns `412`. Reread, show or merge the concurrent edit, and decide whether to submit again. Merely fetching a new ETag and resending old content would defeat the protection.

Pass logical paths directly, including slashes and Unicode. Do not pre-encode them. Use a file response's ETag for file content, a Memory response's ETag for Memory metadata, and a Thread response's ETag for Thread mount changes.

## Understand revisions before restoring

Memory file revisions use integer sequence numbers, not opaque revision IDs. List them through `client.resources.memories(memory_id).revisions`, inspect a revision's detail, then explicitly choose whether to restore it.

Restoring a revision **undoes that recorded change**; it does not mean “make this revision current.” Undoing a file's creation can remove the file. The restore response is a `MemoryFileState`, whose `file` may therefore be `None`. Account for that before dereferencing a returned file.

Provider-backed records are another Memory surface. They have their own CRUD and search operations rather than file-style ETags, and require a configured provider. Provider accounts are managed through `client.resources.memory_providers`; a local file Memory does not require that integration.

[Back to the guide](README.md) · [Next: connections and authentication](connections.md)
