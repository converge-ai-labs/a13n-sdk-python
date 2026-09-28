# Python SDK application guide

Use this SDK to call an existing a13n Service, not to execute an agent inside your Python process. Start with the [README examples](../README.md#submit-and-observe); this guide explains how to integrate those calls into an application. Documentation is maintained as Markdown in this repository, alongside the API it describes.

## Reading map

| Task                                                | Read                                                                                                 |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Install, authenticate and submit your first message | [Quick start](../README.md#installation)                                                             |
| Send structured input and observe a Thread          | [Submission and streaming examples](../README.md#submit-and-observe)                                 |
| Upload or download content                          | [Binary examples](../README.md#resources-and-binary-content)                                         |
| Read and update Memory files                        | [Memory example](../README.md#memory) and [Memory semantics below](#memory-files-records-and-mounts) |
| Find a resource or exact request type               | [API discovery below](#find-an-operation)                                                            |
| Diagnose errors and decide whether to retry         | [Failure handling below](#handle-failures-without-replaying-writes)                                  |
| Change the SDK or run acceptance tests              | [Contributing](../CONTRIBUTING.md)                                                                   |
| Understand design guarantees and the pinned Service | [SDK specification](../spec/README.md) and [contract provenance](../contract/README.md)              |

## Before your first request

You need a Service base URL, an explicit workspace ID or key, and credentials authorized for that workspace. Submission also needs an existing Agent ID with a usable model. Obtain these through your deployment's Console or administrator; constructing a resource reference neither discovers resources nor grants access.

For a released SDK, install `a13n` using your package manager and choose the version appropriate to your deployment. To try this source checkout without depending on registry availability, use `uv add /absolute/path/to/a13n-sdk-python` from your application's directory. Source version `0.0.0` is not a published compatibility guarantee. Python 3.13+ is required.

Pass the Service origin as `base_url`, not a complete operation URL. Load secrets from your application's secret storage rather than copying them into source. `Client(base_url, token)` uses Bearer authentication; omitting the token is public, cookieless access. A workspace key cannot authorize organization administration or session-only account operations. A `403` is not a reason to try an unrelated credential automatically.

For session authentication, explicitly construct `Client.session(...)` with the expected origin, cookies and current CSRF token. `set_csrf_token(...)` updates the proof for later mutations; the SDK does not implement an interactive login manager. Trust private certificate authorities through `ca_bundle`, not by disabling verification.

Reuse a Client within its async lifetime and close it with `async with` or `await client.aclose()`. Keep download and Thread stream context managers open while consuming data. Upload file objects remain yours to close.

## Find an operation

The complete resource tree starts at `client.resources`. `client.workspaces` and `client.organizations` are shortcuts into that tree. Calling a collection with a selector binds locally, for example `client.workspaces(workspace_id).memories(memory_id)`.

| Scope        | Examples                                                                     |
| ------------ | ---------------------------------------------------------------------------- |
| Service      | `client.resources.healthz`, `client.resources.auth`                          |
| Organization | `client.organizations(organization_id).models`, `.memory_providers`          |
| Workspace    | `client.workspaces(workspace_id).agents`, `.threads`, `.memories`, `.assets` |
| Thread       | `workspace.threads(thread_id).inbox_entries`, `.memories`, `.environments`   |
| Run          | `workspace.runs(run_id).items`, `.interrupt()`, `.resume(...)`, `.fork(...)` |

Use IDE completion or the generated [resource definitions](../a13n/generated/resources.py). Request/response models live in [generated models](../a13n/generated/models); exact HTTP operations and schemas are in [the pinned OpenAPI](../contract/openapi.json). These files describe the SDK's snapshot, not whatever a different Service deployment happens to expose.

Ordinary requests return `Result[T]`: read `.value`, `.status`, `.headers`, `.etag` and `.request_id`. Submission helpers return `Submitted`; its original response is `.receipt`. Low-level `Client.execute()` and `Client.stream()` are advanced escape hatches, not necessary fallbacks for missing resource operations.

`list()` reads one page. `pages()` retains page responses; `iter()` yields items. Do not assume every collection is paginated: Run Items is a committed snapshot read through `run.items.get()`.

## Preserve request meaning

Use generated models rather than arbitrary dictionaries. `UNSET` from `a13n.generated.types` omits an optional field, `None` sends JSON null when allowed, and a concrete value sends that value. Null is **not** a universal delete instruction: Service defines each field's meaning. For example, Agent metadata updates keep the existing description when sent null; an empty description is an explicit value.

Read the resource you will edit and pass its ETag through `if_match`. Memory file content uses the file ETag; Thread inbox or mount changes use the Thread ETag. On `412`, inspect the new state and decide how to reconcile your intended change; do not blindly fetch a new ETag and overwrite someone else's update.

Keep one idempotency key per logical submission, fork, resume or upload. Retain the key with your request and receipt before retrying a lost response. A different key is a different operation, not recovery of the first one. SDK mutations are not automatically replayed.

## Acceptance, queue and completion

1. Save the response's Thread and Entry identities. `Submitted.run is None` means retained input, not rejected input.
2. Observe `submitted.entry.wait(timeout=..., poll_interval=...)` when queued. Check `status`: failed or withdrawn is not execution. Consumption and `assigned_run_id` let you decide which Run to observe.
3. Observe that exact Run with `run.wait(...)`, then inspect its status. Waiting, failed and cancelled are valid wait results, not successful completion.
4. Read `run.items.get()` for committed display content and the Run view for durable state.
5. To resume a waiting Run, supply explicit answers. `await run.resume(...)` returns `Resumed`, whose `.run` is the successor and whose `.receipt` retains its HTTP response. Waiting again on the old Run never follows the successor.

Each wait has a local timeout. If a queue-plus-Run workflow needs one total budget, also wrap the workflow in `asyncio.timeout(...)`. Local timeout, cancellation and Client closure do not stop a remote Run or prove that a write rolled back. Use the explicit interrupt operation when remote interruption is intended.

Thread SSE is provisional observation. Apply a `delta` or `boundary` before advancing iteration and persisting its cursor. `changed` requires Thread readback; `reset` and `gap` require the indicated Run's Items. Neither EOF nor reconnection proves completion. Your application owns durable checkpoints and applying readback results. See the [typed stream example](../README.md#provisional-thread-stream).

## Memory files, records and mounts

These are separate surfaces; do not infer one from another:

- `memory.files` stores JSON text addressed by a logical path. Pass the path directly to the resource selector; do not URL-encode it yourself. Replace, move and delete use explicit preconditions.
- `memory.revisions` selects revisions by integer `seq`, not a UUID. Restore undoes that revision's change, rather than blindly copying its post-change content. Undoing creation may return `file: null`. Use the current file's ETag when it exists; omission is only for an absent restore target. Purging history is distinct from deleting file content.
- `memory.records` accesses a configured record provider. List/create/replace/delete/search exist, but item GET and file-style ETags do not. A failed provider write can have an unknown outcome.
- `thread.memories` mounts memories by name with the Thread's ETag. Submission and fork bodies can carry mounts. `RunView.memory_mounts` is the accepted snapshot, not a live view of later Thread edits.
- Organization `memory_providers` configures/tests provider accounts; it is not the file-content API.

## Handle failures without replaying writes

Catch public exceptions from `a13n`, keeping local cancellation separate:

| Evidence                                              | What to do                                                                                        |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `ApiError.status`, `.code`, `.details`, `.request_id` | Branch on structured fields; retain request IDs for server diagnosis.                             |
| `401` / `403`                                         | Check authentication mode, workspace scope, grants and session CSRF.                              |
| `409`                                                 | Inspect the conflict reason, including reused idempotency keys or resource state.                 |
| `412` / `428`                                         | Reconcile stale state or supply the correct resource ETag.                                        |
| `TransportError`                                      | Treat a mutation outcome as unknown until reconciled.                                             |
| `ProtocolError`                                       | Inspect deployment/SDK compatibility and response boundaries; do not retry a write automatically. |
| `TimeoutError` / task cancellation                    | Stop local observation; recover using saved identities and keys.                                  |

Do not log tokens, cookies or complete request/response payloads merely to diagnose a failure. Local generated types do not replace Service authorization or complete request validation.

## Version and validation boundaries

This source snapshot generates every operation in its pinned contract. That does not promise compatibility with every Service version or live-test every endpoint/provider. Use the [contract source record](../contract/source.json) when comparing a deployment, and browse documentation at the tag or commit you actually consume rather than assuming `main` matches an installed release.

The [development and acceptance section](../README.md#development-and-acceptance) separates ordinary local tests from opt-in disposable-Service tests. Neither test success nor a documentation update publishes a package.
