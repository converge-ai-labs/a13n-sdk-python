# a13n

Async-first Python SDK for the a13n Native Service. Resource references bind locally; `Result[T]` retains typed values and HTTP evidence. The pinned contract lives under `contract/` with its exact Service commit in `contract/source.json`. Python 3.13 or later is required.

## Installation

```bash
uv add a13n
```

This SDK targets the rewritten Native Service and intentionally does not retain the older global Run/queue/Run-stream API. See [the SDK specification](spec/README.md) for boundaries and [Contributing](CONTRIBUTING.md) for generation and validation.

## Authentication and lifetime

```python
from a13n import Client

async with Client("https://service.example", "api-token", ca_bundle="/path/to/ca.pem") as client:
    workspace = client.workspaces("ws_example")
```

A token selects Bearer authentication; omitting it creates a public, cookieless Client. For cookie sessions, use `Client.session(base_url, origin=..., cookies=..., csrf_token=...)`; mutating requests send `X-CSRF-Token` only when explicitly configured. `ca_bundle` adds a trusted CA without disabling TLS verification. The Client owns its transport and live responses, and `aclose()` or context exit releases them. Local closure does not interrupt remote execution.

## Submit and observe

```python
from a13n import Client
from a13n.generated import models as wire


async def review(base_url: str, token: str, workspace_id: str, agent_id: str) -> None:
    async with Client(base_url, token) as client:
        workspace = client.workspaces(workspace_id)
        submitted = await workspace.start("Review this change", agent_id=agent_id, idempotency_key="review-42")
        if submitted.run is not None:
            result = await submitted.run.wait(timeout=60, poll_interval=0.25)
            if result.value.status == wire.RunStatus.COMPLETED:
                items = await submitted.run.items.get()
                print(len(items.value.items))
        else:
            entry = await submitted.entry.wait(timeout=60, poll_interval=0.25)
            if entry.value.assigned_run_id is not None:
                run = workspace.runs(entry.value.assigned_run_id)
                result = await run.wait(timeout=60, poll_interval=0.25)
```

`Submitted` always contains exact `thread` and inbox `entry` references, plus an optional `run`. A missing Run means retained intent, not failed acceptance or an invented Run. `Thread.submit(text_or_MessagePayload, agent_id=..., idempotency_key=...)` has the same result shape for an existing Thread. The full typed `Submitted` wire receipt remains at `.receipt.value`. Text is converted into an ordinary text part; structured inputs use generated `wire.MessagePayload`.

For a fully configured Thread, use the same bound receipt with the complete generated body:

```python
from a13n import text_input

submitted = await workspace.threads.create(
    body=wire.NewThread(
        agent_id=agent_id,
        payload=text_input("Review this change"),
        memories=[wire.MemoryMount(name="notes", memory_id="mem_example", access=wire.MemoryAccess.READ)],
        environments=[],
        session_id=None,
    ),
    idempotency_key="review-with-memory-42",
)
# submitted.thread.stream(), submitted.entry.wait(), and submitted.run.wait()
# are available just as with workspace.start(). No manual reference reconstruction.
```

### Provisional Thread stream

```python
async with submitted.thread.stream(after=None, max_reconnects=3) as stream:
    async for frame in stream:
        if frame.event_type in {"delta", "boundary"}:
            await apply_and_checkpoint(frame.data, frame.cursor)
        elif frame.event_type == "changed":
            await submitted.thread.get()
        else:  # reset or gap
            affected_run = workspace.runs(frame.data["run_id"])
            await affected_run.items.get()
```

`ThreadFrame` is a typed union: checking `event_type` narrows the data fields and cursor. `delta` and `boundary` have a resumable Redis entry ID at `frame.cursor`; `changed`, `reset`, and `gap` do not. The latter require explicit Thread or Run Item readback. Reconnection is bounded and does not turn EOF into Run completion or persist your application checkpoint. Keep the `async with` scope to release the attachment; early `async for` exit alone does not close it.

`Run.interrupt()` targets one exact Run. `Run.resume(wire.ResumeRequest(...), idempotency_key=...)` returns a new Run reference when eligible; `Run.fork(body=wire.Fork(...), idempotency_key=...)` returns a new `Submitted` Thread/Entry/optional Run. No helper runs client tools, approves actions automatically, or retries uncertain mutations.

## Resources and binary content

`client.resources` exposes all generated Service, Organization, and Workspace paths. Ordinary resource methods return `Result[T]`; submissions return bound `Submitted` with that evidence at `.receipt`. Both preserve status, headers, ETag, request ID, and content; `a13n.generated.models` and `a13n.generated.api` retain full wire access. Collection `list()` fetches one page; `pages()` and `iter()` traverse lazily. `Client.execute()` preserves the generated low-level HTTP response, and `Client.stream()` exposes a raw response context independently from `Thread.stream()`.

```python
from io import BytesIO
from a13n.generated import models as wire
from a13n.generated.types import File

with BytesIO(b"binary data") as source:
    upload = await workspace.uploads.create(
        body=wire.UploadCreate(file=File(source, file_name="example.bin", mime_type="application/octet-stream")),
        idempotency_key="upload-42",
    )
asset = await workspace.assets.create(body=wire.AssetCreate(name="example.bin", upload_id=upload.value.upload_id))
async with workspace.assets(asset.value.id).content.get_stream() as response:
    if response.status_code != 200:
        raise RuntimeError(f"download failed: {response.status_code}")
    async for chunk in response.aiter_bytes():
        consume(chunk)
```

Image uploads use the same `File` input and require `mime_type="image/png"`, `"image/jpeg"`, or `"image/webp"`, for example `await workspace.icon.replace(body=File(source, mime_type="image/png"), if_match=etag)`. Missing/unsupported image media fails before dispatch rather than silently sending WebP. The SDK does not close caller-owned upload streams. Staging an upload, publishing an Asset, and accepting a Run are separate Service outcomes.

## Memory

```python
created = await workspace.memories.create(body=wire.MemoryCreate(key="notes", name="Notes"))
memory = workspace.memories(created.value.id)
file = await memory.files.create(body=wire.MemoryFileCreate(path="project/notes.md", content="First note"))
await memory.files("project/notes.md").replace(
    body=wire.MemoryFileReplace(content="Updated note"),
    if_match=file.etag,
)
revisions = await memory.revisions.list(path="project/notes.md")
revision = await memory.revisions(revisions.value.items[0].seq).get()
```

File writes use file ETags; Memory metadata uses Memory ETags. History includes integer-sequence readback, restore and path-scoped purge. Provider-backed `memory.records` supports list/create/replace/delete and `search(body=wire.MemoryRecordSearch(query=...))`, but no item GET or conditional version. Uncertain provider writes are never replayed. Thread mounts are available at `thread.memories`; mutations require the **Thread** ETag. `wire.NewThread` and `wire.Fork` accept `memories`; `RunView.memory_mounts` reports the accepted snapshot. Organization `memory_providers` exposes list/create/get/update/test.

This snapshot covers **230 HTTP operations across 154 paths**, including all 29 memory/provider operations and public auth bootstrap. Every operation has a generated resource method and low-level binding; this is structural coverage, not a claim that every endpoint has been exercised against every deployment. There are 47 lazy paginated resource collections and seven binary download stream methods; file memory itself is JSON text.

## Development and acceptance

```bash
make install
make generate
make check-all
make hooks-check
```

`make generate` reads only the pinned local contract. `scripts/service-smoke.py` and `scripts/service_acceptance.py` are opt-in installed-SDK checks against an **existing disposable HTTPS** Service. Supply `A13N_SERVICE_URL`, `A13N_API_TOKEN`, `A13N_WORKSPACE`, `A13N_AGENT`, and `A13N_CA_BUNDLE`; acceptance also needs `A13N_CLIENT_TOOL_AGENT` configured for a client-tool wait. Run a built wheel in a clean virtual environment and invoke the script outside the source tree. Smoke checks a completed Run and multipart upload/streaming download. Acceptance checks Thread SSE reconnect, inbox consumption, interrupt, fork, and pending-action resume. `scripts/memory_acceptance.py` additionally requires `A13N_ORGANIZATION` and `A13N_MEMORY_PROVIDER` (an accessible `mem0_oss` provider) and checks file CAS/history/restore, frozen Run mounts, record CRUD/search, provider testing and health probes. These scripts do not provision credentials, reset Service data, or claim external cloud-provider validation. Success is not publication.

## License

Licensed under Apache-2.0.
