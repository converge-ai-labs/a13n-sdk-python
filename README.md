# a13n

Python SDK package for a13n Service.

## Status

Async-first, typed resource objects cover all 325 Native HTTP operations in the pinned Service contract: managed Agents and revisions, interaction resources, IAM, configuration, environments, memory, connectivity, content, and observability. The resource layer shares one transport with the retained generated low-level API and existing Web Provider facade.

Bounded conveniences provide Agent start, Run-or-queue submission, exact-Run waiting, explicit successor commands, lazy pagination, binary download contexts, and typed Run SSE. Responses retain HTTP evidence; mutations are never automatically replayed. Python 3.13+ is required. This is source implementation coverage, not a claim about a previously published package or every deployed Service.

Notification WebSocket transport and automatic reconnect/snapshot replacement are **not implemented**. Run SSE attaches once and exposes replay gaps; applications own applied checkpoints and bounded recovery. See the [Python contract](spec/README.md) for precise limits.

## Installation

```bash
uv add a13n
```

```python
import a13n

print(a13n.__version__)
```

## Start work with an Agent

Bindings are local and reusable; only explicit async methods perform I/O. Use the Service base URL (including any deployment prefix), not a URL already ending in `/api/v1`.

```python
from a13n import Client


async def run_agent(base_url: str, token: str, workspace_id: str, request_key: str):
    async with Client(base_url, token) as client:
        agent = client.workspaces(workspace_id).agents("helper")
        run = await agent.start("Summarize the release changes", idempotency_key=request_key)
        # start resolves the Agent selector, then submits once. Keep the receipt
        # identities for later access; another client can bind the same Run.
        assert run.acceptance is not None
        print(run.id, run.acceptance.value.thread_id, run.acceptance.value.session_id)
        snapshot = await run.wait(timeout=120)
        if snapshot.value.status == "completed":
            return snapshot.value.output_text
        # waiting, failed, and cancelled are not successful business outcomes.
        return snapshot.value
```

Supply a stable idempotency key for each intended mutation and retain it when reconciling an uncertain response; do not generate a new key merely because a response was lost. `Agent.start` accepts the complete generated `AgentInput` as well as text. Revision selection, overrides, primary Environment selection, and labels are explicit keyword arguments. `UNSET` inherits Service behavior; `environment=None` explicitly selects no Environment.

## Continue, queue, and control exact Runs

```python
from a13n import Client, Run, text_input
from a13n.generated.models import ThreadRunSubmissionRequest, WaitingRunFeedbackRequest


async def submit(client: Client, thread_id: str, thread_version: int, request_key: str):
    submission = await client.threads(thread_id).submit(
        ThreadRunSubmissionRequest(
            expected_thread_version=thread_version,
            input_=text_input("Continue with the next section"),
        ),
        idempotency_key=request_key,
    )
    if isinstance(submission.resource, Run):
        return await submission.resource.wait(timeout=120)
    # The other branch is a QueuedSubmission, not an accepted Run.
    disposition = await submission.resource.wait(timeout=120)
    return disposition  # .run is present only after actual consumption


async def provide_feedback(client: Client, waiting_run_id: str, body: WaitingRunFeedbackRequest, request_key: str):
    # The application explicitly constructs the complete pending-set resolution.
    original = client.runs(waiting_run_id)
    successor = await original.feedback(body, idempotency_key=request_key)
    assert original.id == waiting_run_id
    return successor
```

`retry`, `fork`, and `continue_` similarly return a **new** Run reference with acceptance evidence. Fork creates a child Thread in the same Session, not a new Session. `interrupt` and `steer` return their own typed receipts. `feedback_receipt`, `retry_receipt`, `fork_receipt`, and `continue_receipt` expose the unwrapped HTTP result when desired. Queue editing, withdrawal, reordering, and explicit consumption are separate resource methods with required version/idempotency inputs. A withdrawn queue entry surfaces the Service's not-found error when read; waiting never consumes input.

No read, wait, stream, or property executes a client tool, approves a request, submits feedback, or follows a future Thread head. Local timeout/cancellation/close never interrupts remote work.

## Observe one Run

```python
async def observe(client: Client, run_id: str, applied_cursor: str | None):
    async with client.runs(run_id).stream(after=applied_cursor) as events:
        async for observation in events:
            # Apply observation.event to your projection first, then persist
            # observation.cursor in your own durable checkpoint transaction.
            yield observation
```

Use the async context manager even when breaking iteration early. Heartbeats are skipped; `StreamObservation.cursor` is distinct from `event.event_id`. EOF does not establish completion. Attachment failures raise `ApiError`; an in-stream gap raises `ReplayGap` with its bounded metadata. Reattach explicitly using the last **applied**, not merely received, cursor. No hidden reconnect or checkpoint persistence occurs.

For display recovery, `run.items.pages()` retains `snapshot_version`, `projection_cursor`, `complete`, `finalized`, and `incomplete_reason`. Replace the covered Item projection before attaching after its projection cursor; do not append a merged snapshot over existing deltas or call it exact event replay. Lifecycle collections (`run.events.list`, `client.workspaces(id).events.pages`) have different sequence/cursor domains and are not SSE.

## Typed management and pagination

```python
from a13n.generated.models import UpdateAgentRequest


async def rename(client: Client, workspace_id: str, agent_key: str):
    agent = client.workspaces(workspace_id).agents(agent_key)
    snapshot = await agent.get()
    if snapshot.etag is None:
        raise RuntimeError("Service omitted the required concurrency evidence")
    return await agent.update(
        body=UpdateAgentRequest(name="Research assistant"),
        if_match=snapshot.etag,
    )


async def discover(client: Client, workspace_id: str):
    async for result in client.workspaces(workspace_id).models.pages(limit=50):
        for model in result.value.items:
            yield model
```

`client.resources` exposes the complete typed management tree, with common interaction collections also available directly on Client. Examples include `client.resources.assets(id).content.get_stream()`, `client.resources.connections(id).get()`, `client.resources.configuration_sessions(id).threads.list()`, and `client.organizations(id).web_providers(id).update(...)`. Collections expose `list`/`create`, identified resources `get`/`update`/`replace`/`delete`, and commands their protocol name where supported. The generated `a13n.generated.resources.OPERATIONS` index maps every pinned operation to its resource method; editors expose concrete signatures rather than `**kwargs` dispatch.

A `Result[T]` preserves `.value`, `.status`, `.headers`, `.content`, `.etag`, and `.request_id`. Page iteration is lazy, retains the full page value, and continues across empty pages when a cursor exists. It does not infer snapshot isolation. Request/resource models live under `a13n.generated.models`; `a13n.Run` is a handle, while `a13n.generated.models.RunResource` is a wire snapshot. Existing root-level Pydantic Web/configuration types are unchanged.

Workspace configuration discovery can include Organization-owned resources. Inspect each value's actual ownership and explicitly bind the owning scope for mutation; a Workspace list does not grant ownership or override semantics. Service enforces authorization on every operation. Failed resource operations raise `ApiError` with status/code/details/request ID/retry guidance; malformed replies raise `ProtocolError`, and transport failures raise `TransportError` without claiming rollback. No mutation is replayed and no stale ETag is silently refreshed.

## Web Provider accounts (compatible facade)

Bind API Key operations with `await client.workspace()`. This reads `/api/v1/auth/context` once and returns Web operations without a Workspace argument. The binding uses the immutable Workspace ID and shares the parent transport and shutdown. The parent client retains explicit `WebProviderScope` operations; Service always enforces the credential boundary.

```python
from a13n import AgentRunOverride, Client, SearchToolConfiguration, ToolSelection, ToolsetSelection


async def accounts(base_url, token):
    async with Client(base_url, token) as client:
        workspace = await client.workspace()
        page = await workspace.web_providers()
        return page.items


inherit = AgentRunOverride().to_wire()  # {}
disable = AgentRunOverride(toolsets={"web": ToolsetSelection(enabled=False)}).to_wire()
replace = AgentRunOverride(
    toolsets={
        "web": ToolsetSelection(
            enabled=True,
            tools={
                "search": ToolSelection(
                    permission="inherit",
                    config=SearchToolConfiguration(provider_id="wprov_example").model_dump(exclude_none=True),
                )
            },
        )
    }
).to_wire()
```

`CreateWebProviderRequest` / `UpdateWebProviderRequest` accept any catalog type key and its schema-defined credential dictionary, including nested JSON objects. Pydantic converts that dictionary to a `WebProviderCredential` that redacts the complete object from ordinary model diagnostics; the client reveals it only while serializing an authorized request. Built-ins use `{"api_key": value}`; an external Provider can define another shape. `test_web_provider` sends one quota-consuming probe only when called. Use `aclose()` or an async context manager to release the transport.

## Generated HTTP operations

```python
from a13n import Client
from a13n.generated.api.identity import get_auth_context


async def context(base_url: str, token: str):
    async with Client(base_url, token) as client:
        return await client.execute(lambda api: get_auth_context.asyncio_detailed(client=api))
```

`Response.parsed` is a typed success/error union; `status_code`, `headers`, and `content` retain HTTP evidence. Models use attrs rather than the Web facade's Pydantic models. Use generated enums when constructing requests; `UNSET` means omitted and `None` means JSON null. `Client.execute` shares authentication, timeout, cancellation, and the existing httpx2 pool; it does not apply the Web facade's 1 MiB response limit or exception mapping.

For uploads, generated methods accept `a13n.generated.types.File` with a caller-owned binary file and stream bounded chunks through the async transport. For downloads, use `async with client.stream(operation.build_request(...)) as response` and iterate `response.aiter_bytes()`. Do not use buffered generated `asyncio_detailed` downloads for large files. Low-level generated synchronous clients are separately owned, not another mode of the async facade.

## Development

This is the independent `converge-ai-labs/a13n-sdk-python` repository. It needs Python 3.13, uv, and Make, not a Service checkout or database.

```bash
make install
make generate         # regenerate only from contract/openapi.json
make generated-check  # compare in a temporary directory; do not refresh output
make check-all        # generation, lint, types, tests, wheel and sdist
```

`contract/source.json` records the source repository, full commit SHA, original paths, and SHA-256 of the vendored inputs. The initial snapshot is copied from the committed pre-extraction Service tree, not from an uncommitted export. `contract/README.md` explains the provenance boundary. Generator tools are pinned in `codegen/generate.py`: openapi-python-client 0.29.1 and Ruff 0.16.3. Language adapters and templates belong here; generation never runs the Service exporter. Commit contract and generated changes together.

See [Contributing](CONTRIBUTING.md) for workflow and [SDK contract](spec/README.md) for ownership and observable behavior.

## License

Licensed under the Apache License 2.0.
