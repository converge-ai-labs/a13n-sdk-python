# Python SDK application guide

Use this SDK to call an existing a13n Service, not to execute an Agent inside your Python process. Start with the [Agent interaction example](../README.md#start-observe-continue). The pinned [OpenAPI](../contract/openapi.json) and [SDK specification](../spec/README.md) are the references for complete advanced operations.

## Prerequisites and authentication

You need the Service base URL, an API key authorized for the intended workspace, and an existing **Agent ID** whose configuration selects a usable **Model key**. Agents and Skills use IDs; only Models support keys. API-key identity implicitly determines workspace: do not prefix ordinary business operations with workspace IDs or attempt an invented discovery flow. The resource reference itself never grants permission. Get credentials and Agent IDs from your administrator or Console.

Load tokens from secret storage and close `Client(base_url, token)` with `async with`. An omitted token uses public cookieless mode. Cookie-based accounts use `Client.session(base_url, origin=..., cookies=..., csrf_token=..., workspace_id=...)`: explicit `workspace_id` is sent as `X-Workspace-ID` only on declared workspace business paths, not on organization/admin/public paths; the caller may supply an explicit operation header. `set_csrf_token` updates later mutation proof. The SDK never logs in, discovers workspaces, or refreshes credentials. `ca_bundle` trusts a private CA without disabling TLS verification.

## Find an operation

`client.agents(id)`, `client.threads(id)` and `client.runs(id)` bind authored interaction handles with no request. `client.resources` exposes the **complete pure schema** tree: `.agents`, `.threads`, `.runs`, `.models(key)`, `.skills(id)`, `.memories(id)`, `.assets(id)`, `.uploads`, `.auth`, `.organizations(id)`, `.workspaces(id)` and all other declared routes. A generated submission returns `Result[wire.Submitted]`, not an Interaction. Administration retaining organization/workspace IDs is not an alternative binding for workspace-scoped business APIs. For exact properties and request models use [generated resources](../a13n/generated/resources.py) and [generated models](../a13n/generated/models); both layers use the same transport.

Ordinary requests return `Result[T]` with `.value`, `.status_code`, `.headers`, `.etag`, `.request_id`, and `.content`. `list()` fetches one page; `pages()` and `iter()` paginate lazily where supported. `Client.execute()` exposes a generated HTTP response, including typed error union; `Client.stream()` is the raw HTTP streaming context. For binary downloads use the declared resource's `get_stream()` and check its status before reading. Keep the response context open while consuming; caller-owned upload streams remain yours to close.

## Structured input, file content, and configured Runs

`Agent.start` and `Agent.send` accept a plain string or a generated `wire.MessagePayload`. Use generated content-part models for structured inputs and asset references rather than undocumented dictionaries. Create an upload with `wire.UploadCreate(file=File(source, file_name=..., mime_type=...))` and an Asset separately; publishing an Asset and accepting a Run are independent Service outcomes.

`Agent.start(..., agent_revision_id=..., session_id=..., delivery=..., options=..., environments=..., memories=..., mcp_headers=..., idempotency_key=...)` exposes the full initial Thread configuration. `Agent.send(thread_id, ..., agent_revision_id=..., delivery=..., options=..., idempotency_key=...)` exposes every Message field. Use `wire.MemoryMount(name="notes", memory_id=..., access=wire.MemoryAccess.READ)` for a Thread's named memory mount. `wire.RunOptionsInput(overrides=wire.AgentOverrideInput(...))` specifies per-Run changes; the Agent's `model` field selects a Model **key**, and `wire.SkillSelection(skill_id=...)` uses a Skill **ID**. Model `extra_body`/`extra_headers` mappings are carried intact. Service replacement rules apply: a Run extra object replaces the inherited Agent object, which replaces the Model default, and `{}` clears it; do not merge these mappings in the client.

Generated optional fields use `UNSET` for omission, `None` for explicit null when allowed, and a concrete value for an explicit setting. Null is not universally a delete instruction. Read the resource before a conditional mutation and use its ETag as `if_match`: Memory file content uses a file ETag, Memory metadata uses a Memory ETag, Thread inbox/mount changes use the Thread ETag. On `412`, inspect and reconcile the new state instead of blindly fetching a new ETag and overwriting someone else's change.

## Finite observation and recovery

`await agent.start(...)` and `await agent.send(thread_id, ...)` return one `Interaction`, which owns an original receipt, Thread, Entry and optional immediately accepted Run reference. `await interaction.result()` requires no streaming or context entry: it polls the Entry until **consumed**, then the exact assigned Run until sealed. Pending/assigned is not incorporation. Failed/withdrawn Entry raises `SubmissionError` with its Entry snapshot. Waiting/failed/cancelled Runs are reported as statuses in a `RunOutcome`; no auto-approval or implicit success.

For provisional events use `async with interaction: async for frame in interaction: ...` and then `await interaction.result()` inside the context. It binds the exact Run after incorporation before yielding frames and filters foreign Runs and unscoped Thread notices. A Run can seal while its SSE socket is idle: iteration ends via independent bounded Run readback, not by waiting for EOF or a terminal frame. Current-Run filtering, retention and gaps mean this is not a lossless transcript. On `gap` or `reset`, read the indicated Run's committed `items.get()`; the SDK does not create a UI reducer or pretend provisional deltas are committed. Application display checkpoints and external effects are yours to own.

A result-only call or a naturally completed context caches its outcome. Closing a context early cancels local observer/reader work; `.result()` will **not** secretly restart after such a close. Use saved IDs, `client.runs(run_id).get()/wait()` or `client.threads(id).inbox_entries(entry_id).get()` for explicit recovery. There is no remote interrupt on close. The generated `client.resources.threads(id).stream` preserves the declared Thread SSE HTTP route. Protocol-level consumers can explicitly construct `ThreadStream(client.resources.threads(id))` for a typed persistent **Thread-wide** parser with applied-cursor acknowledgement and bounded reconnect; this is not another ordinary high-level interaction mode.

To answer a waiting Run, inspect `outcome.pending`, perform any external client-tool work yourself and call `outcome.run.resume([wire.Complete(...)], idempotency_key=...)`; the returned `Resumed.run` is a distinct successor. `run.wait()` always observes its exact ID. `run.interrupt()` is an explicit remote command, not a compensating action automatically issued by timeouts. Fork creates a separate Thread through the declared `wire.Fork` body.

Retain an idempotency key per logical submission, fork, resume, or upload. A different key represents a different operation. HTTP transport failure, timeout or cancellation can leave mutation outcome unknown; never replay writes automatically. Save the identities and key, read back explicitly and reconcile. Re-using a single Client within its async lifetime is cheaper than making a Client per request.

## Memory families and errors

`client.resources.memories` exposes metadata, JSON-text files, integer-sequence revisions and provider-backed records. Paths can contain slashes and Unicode; pass the logical path directly to a resource selector, which encodes it once. File-history restore undoes the recorded change (restoring creation can remove a file). Provider records have their own CRUD/search interface, not file-style ETags. `client.resources.memory_providers` configures provider accounts independently. `RunView.memory_mounts` is the accepted snapshot, not a live view of subsequent Thread edits.

| Failure                                                | Application response                                                        |
| ------------------------------------------------------ | --------------------------------------------------------------------------- |
| `ApiError` (`status`, `code`, `details`, `request_id`) | Branch on structured Service rejection; retain request ID for diagnostics.  |
| `SubmissionError` (`entry_id`, `thread_id`, `entry`)   | The exact Entry failed/was withdrawn, with no successful incorporating Run. |
| `ProtocolError`                                        | Investigate SDK/Service compatibility or malformed required response.       |
| `TransportError`                                       | Read back; mutation outcome may be unknown.                                 |
| `TimeoutError` or task cancellation                    | Local observation ended; remote execution has not been interrupted.         |

Do not log credentials, cookies, complete payloads, or sensitive model output merely to diagnose failure. Tests and generated type coverage do not establish compatibility with arbitrary Service deployments. Compare [pinned source provenance](../contract/source.json) to the deployment, and use [Contributing](../CONTRIBUTING.md) for generation, checks, and opt-in installed-artifact acceptance.
