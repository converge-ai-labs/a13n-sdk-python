# Resources and Client Lifetime

## Resource Roles

Python 3.13+ SDK calls are async-first. A Client owns one endpoint, credential mode and transport. Binding a reference, reading its ID, or constructing an advanced stream sends no request; an ID is not proof of existence or authority.

- `client.agents(agent_id)` binds an Agent; `client.threads(thread_id)` a continuing history and inbox; `client.runs(run_id)` an exact accepted execution. An `InboxEntry` is retained intent, not a Run. `Session` groups Threads but is neither an IAM session nor a hidden current conversation. A RunAttempt is operational evidence, not Worker control authority.
- `client.resources` exposes the complete pure-schema generated Native hierarchy. Workspace business resources are flat (`client.resources.agents`, `.threads`, `.runs`, `.memories`, `.assets`, `.models`, `.skills`, etc.). Administration retaining explicit organization/workspace IDs is separate. Authored `client.agents`, `.threads`, `.runs` bind workflow handles. Administration uses only `client.resources.organizations` and `client.resources.workspaces`, without duplicate Client shortcuts. Both layers reuse one transport, not duplicate HTTP implementations.
- Named child collections expose only declared capabilities. `list()` fetches one page; `pages()` and `iter()` are lazy. A reference's `get()` returns a fresh snapshot, never an implicit cache; mutable generated model fields are local, not remote updates.
- The generated layer returns `Result[wire.Submitted]` for submission operations without high-level binding. The authored Agent workflow validates canonical Thread, Entry and optional Run identities and binds them on its Interaction receipt. Derived references share the Client and never silently follow successors. No workspace-key lookup or extra resolution request is performed.

## Result and Low-Level Access

Every generated one-request resource operation, including submissions, returns `Result[T]`. Authored Agent interactions expose the original `Result[wire.Submitted]` at `.receipt` alongside bound Thread/Entry/Run handles. `Result[T]` exposes `.value`, `.status_code`, case-insensitive `.headers`, original `.content`, `.etag` and `.request_id`. Success can legitimately contain `None` or binary content. HTTP rejection raises `ApiError`; malformed required responses raise `ProtocolError`.

`a13n.generated.models` retains all generated attrs models; `a13n.generated.api` retains typed HTTP operations. `Client.execute()` returns the generated response including typed errors and raw evidence, without resource error mapping. `Client.stream(request)` returns a raw response context. The generated Thread `stream` child preserves the declared SSE HTTP operation. Explicit `ThreadStream(client.resources.threads(thread_id))` supplies protocol-level parsed Thread-wide SSE for advanced callers without adding another ordinary high-level Thread method. These surfaces use the same transport, serialization and authentication as the primary `Interaction`.

## Authentication

```python
Client(base_url, token=None, *, timeout=30, ca_bundle=None, transport=None)
Client.session(base_url, *, origin, cookies=None, csrf_token=None,
               workspace_id=None, timeout=30, ca_bundle=None, transport=None)
client.set_csrf_token(value)  # Session mode only; no I/O
```

- Supplying an API token selects Bearer authentication and its implicit workspace. A public Client sends neither Authorization nor cookies. Bearer/public Clients reject incoming cookies; neither silently becomes a session client.
- Cookie session clients send Origin and a copied cookie jar. A configured `workspace_id` supplies `X-Workspace-ID` **only** to routes declaring workspace context in the pinned API; it never leaks to organization/admin/public routes. Explicit operation headers take precedence. Mutations send explicitly configured CSRF proof. The SDK does not log in, derive a cookie name or CSRF proof, refresh credentials, or select a workspace by discovery.
- `ca_bundle` supplies a CA file to a verifying TLS context, including SSE. No verification bypass is provided. Caller-supplied transports are owned by the Client and implement their own verification.
- Raw caller-authored headers are explicit advanced inputs. Credentials and payloads are excluded from ordinary diagnostic representations; explicitly requested raw HTTP content remains accessible.

## Lifetime and Cancellation

Use `async with Client(...)` or await `aclose()`. The Client owns its pool, supplied transport and live responses. Close is idempotent and final; it cancels outstanding owned I/O and releases active streams. Derived references share the Client. One Client supports concurrent tasks on its owning event loop, not arbitrary cross-loop use.

`Interaction` is a single-use local async context and finite iterator; its `result()` also works without a context or SSE. Exiting closes its stream and cancels/awaits local observation work. Re-entering after a context is not supported. Closing before settlement does not silently restart observation on a later result call: explicit exact-resource readback is available. Explicit `ThreadStream` remains one single-use advanced context for protocol consumers. Breaking either `async for` alone does not release a context. Caller-owned upload streams remain open. Local cancellation, timeout, and Client close do not interrupt a remote Run, withdraw an Entry, or roll back a mutation.

## Public Call Shapes

| Call                                                                        | Result                                                      |
| --------------------------------------------------------------------------- | ----------------------------------------------------------- |
| `await client.agents(agent_id).start(input, idempotency_key=...)`           | One finite `Interaction` with receipt and Thread            |
| `await client.agents(agent_id).send(thread_id, input, idempotency_key=...)` | One finite continuation `Interaction`                       |
| `await interaction.result()`                                                | Exact authoritative `RunOutcome` without SSE                |
| `async with interaction: async for frame in interaction: ...`               | Finite, run-scoped provisional observation                  |
| `await resource.get()` / `await collection.list(...)`                       | One typed `Result[T]`                                       |
| `await client.resources.threads.create(body=wire.NewThread(...), ...)`      | Pure generated `Result[wire.Submitted]`                     |
| `ThreadStream(client.resources.threads(thread_id), ...)`                    | Explicit advanced Thread-wide parsed SSE context            |
| `await client.execute(operation)` / `client.stream(request)`                | Generated HTTP response / raw asynchronous response context |

A collection is not implicitly awaitable or iterable. Pagination does not promise snapshot isolation.
