# Resources and Client Lifetime

## Resource Roles

Python 3.13+ SDK calls are async-first. The Client owns one endpoint, credential mode, and transport; references only bind selectors. Binding a resource, reading its identity, or constructing a stream sends no request. An ID is not proof of existence or authority.

- `client.workspaces(workspace_id)` binds a Workspace. Navigation such as `.agents(agent_id)`, `.threads(thread_id)`, `.runs(run_id)`, and `.assets(asset_id)` stays in that Workspace. `client.resources` exposes the full generated resource tree; Organization and Service-level resources retain their own explicit scopes.
- A `Thread` refers to a continuing history and its inbox; a `Run` refers to one exact accepted execution; an `InboxEntry` is submitted intent, not a Run. `Session` groups Threads but is neither an IAM session nor a hidden current conversation. A RunAttempt is operational evidence, not Worker control authority.
- Named child collections expose only declared capabilities. A collection's `list`, `pages`, or `iter` performs requests only on iteration/awaiting; a reference's `get` returns a fresh snapshot, never an implicit cache. There is no dirty tracking or generic `save()`.
- Workspace selectors accept an ID or key. References derived from a receipt bind its canonical Workspace ID after checking identities within that receipt (and the bound Thread ID when present), not by comparing the original Workspace key with a returned ID. This adds no resolution request. They do not follow successors automatically or own a separate transport. Mutable generated model fields are local values; changing them does not write remotely.

## Result and Low-Level Access

Ordinary one-request resource operations return `Result[T]`; submission operations return bound `Submitted` with the complete `Result[wire.Submitted]` at `.receipt`. `Result[T]` exposes `.value`, `.status_code`, case-insensitive `.headers`, original `.content`, `.etag`, and `.request_id`. The envelope is a snapshot, not a second resource. Success may legitimately contain `None` or binary content. HTTP rejection raises `ApiError`; malformed required responses raise `ProtocolError`.

`a13n.generated.models` retains all generated attrs models; `a13n.generated.api` retains typed HTTP operations. `Client.execute` returns the generated `Response` including a typed error union and raw evidence; it does not use resource-level error mapping. `Client.stream(request)` returns a raw response context. `Thread.stream()` is the distinct, parsed domain SSE attachment. There is no duplicate Web/configuration DTO facade or `Representation` type.

## Authentication

```python
Client(base_url, token=None, *, timeout=30, ca_bundle=None, transport=None)
Client.session(base_url, *, origin, cookies=None, csrf_token=None,
               timeout=30, ca_bundle=None, transport=None)
client.set_csrf_token(value)  # Session mode only; no I/O
```

- Supplying a token selects Bearer authentication. A public Client sends no Authorization or cookies. Bearer/public Clients reject incoming cookies; neither silently becomes a session client.
- `Client.session` sends the supplied Origin, owns a copied cookie jar when provided, and sends `X-CSRF-Token` on mutating requests when explicitly configured. It does not log in, infer a cookie name, derive a CSRF proof from cookies, or refresh credentials automatically. Authentication configuration is fixed per Client; applications sequence cookie/proof changes outside concurrent requests.
- `ca_bundle` supplies a CA file to a verifying TLS context, including SSE connections. No certificate-verification bypass is provided. A caller-supplied transport is owned by the Client and must implement its own verification.
- Raw caller-authored headers are explicit low-level inputs, not another managed credential mode. Credential values and response payloads are excluded from ordinary diagnostic `repr`; explicitly requested raw HTTP content remains accessible.

## Lifetime and Cancellation

Use `async with Client(...)` or await `aclose()`. The Client owns its async HTTP pool, supplied transport, and live responses; close is idempotent and final. It cancels outstanding owned I/O and releases active streams. Derived references share the Client but cannot close it. One Client supports concurrent tasks on its owning event loop, not arbitrary cross-loop use.

`ThreadStream` is single-use and an async context manager. Exit releases the local SSE attachment even after an early iteration exit. Breaking `async for` alone does not close the context. A caller-owned upload stream remains open after a request. Local cancellation, timeout, or Client close neither interrupts a remote Run nor withdraws an Entry nor rolls back an accepted mutation; explicit commands are required for remote effects.

## Public Call Shapes

| Call                                                      | Result                                                                   |
| --------------------------------------------------------- | ------------------------------------------------------------------------ |
| `await client.execute(operation)`                         | Generated `Response[T]` with status, raw content and typed success/error |
| `client.stream(request)`                                  | Raw asynchronous response context                                        |
| `await resource.get()` / `await collection.list(...)`     | One typed `Result[T]`                                                    |
| `await workspace.start(...)` / `await thread.submit(...)` | `Submitted` with validated references and receipt                        |
| `thread.stream(...)`                                      | I/O-free `ThreadStream` factory                                          |
| `collection.pages(...)` / `collection.iter(...)`          | Lazy asynchronous traversal                                              |

A collection is not implicitly awaitable or iterable. The caller chooses one-page, page-wise, or item-wise access; pagination does not promise snapshot isolation.
