# a13n Python SDK

Async-first Python 3.13+ client for the a13n Native Service. The primary interface is one finite Agent interaction: it accepts text or a structured payload, optionally yields provisional frames for **that interaction's incorporating Run**, and returns its authoritative sealed outcome. The complete pinned OpenAPI is also available through generated typed resources and operations.

```bash
uv add a13n
```

## Start, observe, continue

```python
from a13n import Client
from a13n.generated import models as wire


async def example(base_url: str, api_key: str, agent_id: str) -> None:
    async with Client(base_url, api_key) as client:
        agent = client.agents(agent_id)  # Local binding; Agent IDs, not keys.
        interaction = await agent.start("Summarize this change", idempotency_key="review-001")
        async with interaction:
            async for frame in interaction:
                if frame.event_type == "gap" or frame.event_type == "reset":
                    # Read committed Items for the indicated Run; provisional deltas can be missing.
                    await client.runs(frame.data["run_id"]).items.get()
                elif frame.event_type == "delta":
                    print(frame.data["event"])
            outcome = await interaction.result()
        if outcome.status == wire.RunStatus.COMPLETED:
            print(outcome.output)
        elif outcome.status == wire.RunStatus.WAITING:
            print(outcome.pending)  # Explicit human/client-tool decision required.
        else:
            print(outcome.status, outcome.failure)
        follow_up = await agent.send(interaction.thread.id, "Explain the risks", idempotency_key="review-002")
        next_outcome = await follow_up.result()  # No SSE connection needed.
        print(next_outcome.status)
```

`Agent.start(input, *, idempotency_key, agent_revision_id=..., session_id=..., delivery=..., options=..., environments=..., memories=..., mcp_headers=...)` creates a Thread; `Agent.send(thread_id, input, *, idempotency_key, agent_revision_id=..., delivery=..., options=...)` continues an existing Thread as the selected Agent. Input is text or `wire.MessagePayload`. Use `text_input(text)` to construct a text payload for a generated request. A Thread does not have a permanent Agent. The optional Service interaction Session only groups Threads; it is not a hidden current conversation.

`Interaction.thread`, `.entry`, `.run` (immediate receipt Run or `None`), and `.receipt` expose original identities and HTTP evidence. `result(timeout=300, poll_interval=0.5)` resolves its Entry until **consumed**, then waits for the exact incorporating Run to seal, with one deadline for both phases. A failed or withdrawn Entry raises `SubmissionError` carrying its snapshot. Waiting, failed, and cancelled Runs return `RunOutcome` with `.status`, `.output`, `.pending`, `.failure`, `.run`, and `.snapshot`. Run status is not business success; `Run.items.get()` is committed display readback. Repeated results reuse a completed outcome. Local timeout, cancellation, context exit, and Client close never interrupt a remote Run or replay a mutation. Closing observation before settlement cancels its local observer; a later `.result()` does **not** silently restart it—use the exact Run handle/readback explicitly.

The context is single-use, with one frame reader and one Run observer. It binds the Run after Entry consumption before exposing Run-scoped frames; foreign Run frames and Thread-only change notices are omitted. It ends on exact Run seal even when the SSE socket is idle. The underlying retained Thread stream is provisional and subject to retention, current-Run filtering, reset and gaps; finite iteration is **not** a lossless transcript. `result()` is authoritative and works without entering a context or opening SSE. A context manager is needed for prompt stream cleanup after breaking iteration.

## Authentication

An API key implicitly selects its workspace. There is no workspace selector or discovery call for ordinary Agent, Thread, Model, Skill, Asset, or Memory operations. `Client(base_url, token=None, *, timeout=30, ca_bundle=None, transport=None)` uses Bearer credentials when a token is supplied and a public cookieless transport otherwise. `Client.session(base_url, *, origin, cookies=None, csrf_token=None, workspace_id=None, ...)` supports existing cookie login sessions; set `workspace_id` explicitly when accessing workspace business routes. The session client adds `X-Workspace-ID` only on declared workspace routes, never to public, organization or administration routes; an explicit operation header takes precedence. `set_csrf_token` updates a session's mutation proof. No implicit login, credential refresh, cookie-mode switch, TLS verification bypass, or cross-workspace privilege is provided. Close the Client with `async with` or `aclose()`; it owns its HTTP transport and SSE connections.

## Create an Agent and configure a Run

```python
from a13n.generated import models as wire

created = await client.resources.agents.create(
    body=wire.AgentCreate(
        name="Reviewer",
        config=wire.AgentConfigInput(model="review-model", instructions="Review carefully"),
    )
)
agent = client.agents(created.value.id)
interaction = await agent.start(
    "Review this document",
    memories=[wire.MemoryMount(name="notes", memory_id="mem_1", access=wire.MemoryAccess.READ)],
    options=wire.RunOptionsInput(
        overrides=wire.AgentOverrideInput(
            model_settings=wire.AgentOverrideInputModelSettingsType0.from_dict(
                {"extra_body": {"thinking": {"type": "enabled"}}}
            )
        )
    ),
    idempotency_key="review-doc-001",
)
outcome = await interaction.result()
```

Only **Models** accept stable keys; Agents and Skills are selected by IDs (`wire.SkillSelection(skill_id=...)`). Model `extra_body` / `extra_headers` are generated mappings. Service merges Model defaults with Agent settings and Run overrides; a supplied extra object **replaces** its inherited object and `{}` clears it. The SDK preserves the full typed mappings and does not independently infer provider policy. Consult the generated models for declared properties and valid values.

For structured input, supply `wire.MessagePayload(content=[...])`. Upload binary files through `client.resources.uploads.create(body=wire.UploadCreate(file=File(source, file_name=..., mime_type=...)), idempotency_key=...)`; publish with `client.resources.assets.create(...)` separately. The SDK leaves caller-owned upload streams open. `get_stream()` on generated binary content resources supports unbuffered downloads; check response status before consuming it.

## Explicit control and advanced API

```python
if outcome.status == wire.RunStatus.WAITING:
    successor = await outcome.run.resume(
        [
            wire.Complete(
                action="complete", tool_call_id=outcome.pending.items[0].tool_call_id, result={"decision": "approved"}
            )
        ],
        idempotency_key="review-approval-001",
    )
    resumed = await successor.run.wait()  # Exact successor; old Run never follows it.
```

`Run.interrupt()` is the explicit remote interrupt. `Run.fork(body=wire.Fork(...), idempotency_key=...)` creates another Thread. No SDK helper auto-approves a pending action or performs client-tool side effects.

`client.resources` is the complete generated resource tree. Authored `client.agents`, `.threads`, and `.runs` bind primary workflow handles; `.organizations` and `.workspaces` expose administration retaining explicit owner selectors. Generated `client.resources.threads.create(body=wire.NewThread(...), idempotency_key=...)` and `client.resources.threads(thread_id).inbox_entries.create(body=wire.Message(...), idempotency_key=...)` return pure `Result[wire.Submitted]`, retaining all raw identities and HTTP evidence without high-level lifecycle helpers. The generated Thread `stream` child exposes its declared HTTP operation; advanced callers who need typed protocol parsing explicitly construct `ThreadStream(client.resources.threads(thread_id))`. This Thread-wide parser is not a second ordinary high-level interaction mode or a guarantee of a complete history. `Client.execute()` returns raw generated typed HTTP responses, `Client.stream()` a raw response context. `Result[T]` exposes `.value`, `.status_code`, `.headers`, `.etag`, `.request_id`, and `.content`; `.pages()` and `.iter()` traverse supported collections lazily. `UNSET` omits a field and `None` sends explicit null where allowed. ETags, version preconditions and caller-supplied idempotency keys are preserved without hidden retries.

Workspace memories are at `client.resources.memories`: file replacement uses a **file** ETag, metadata uses a **Memory** ETag, Thread mount edits use the **Thread** ETag. Provider-backed records are a separate API. `wire.NewThread` / Agent.start accept mounts; an accepted Run freezes its mount snapshot. Provider configuration is under its declared owner (`client.resources.memory_providers`). For complete recipes and recovery semantics see [the application guide](docs/README.md), [SDK specification](spec/README.md), and [pinned contract provenance](contract/source.json).

## Validation and optional live acceptance

```bash
make install
make generate
make check-all
```

Generation reads only the pinned contract, not a live Service. Mock tests and package builds do not prove deployed provider behavior. Installed-SDK scripts `scripts/service-smoke.py` and `scripts/service_acceptance.py` need an **existing disposable HTTPS** Service and `A13N_SERVICE_URL`, `A13N_API_TOKEN`, `A13N_AGENT`, `A13N_CA_BUNDLE`; acceptance also needs `A13N_CLIENT_TOOL_AGENT`. `scripts/memory_acceptance.py` additionally needs an accessible `A13N_MEMORY_PROVIDER` (`mem0_oss`). These checks do not provision credentials or reset Service data; they must not run against production. No publication follows from a successful local test.

Licensed under Apache-2.0.
