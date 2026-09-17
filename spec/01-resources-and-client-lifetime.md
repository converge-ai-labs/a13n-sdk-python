# Resources and Client Lifetime

## Design Position

Python 3.13+ is async-first. Resource operations use asynchronous methods; streaming and lazy collection traversal use asynchronous iteration. Async-first does not remove an existing synchronous API.

This document owns Python resource roles, local bindings, values, and lifetime. [Interaction and Control](02-interaction-and-control.md) owns command semantics; [Protocol and Compatibility](05-protocol-and-compatibility.md) owns wire and error rules.

## Resource Roles

| Role                        | Responsibility                                                                | Identity boundary                                          |
| --------------------------- | ----------------------------------------------------------------------------- | ---------------------------------------------------------- |
| Client                      | Explicit endpoint, credential, resource access, and local transport ownership | No implicit Agent or Thread                                |
| Agent reference             | Read or manage one managed Agent and start work with an explicit selection    | No hidden current conversation                             |
| Session reference           | Navigate exported interaction-scope operations and Threads                    | Not a continuation state or IAM session                    |
| Thread reference            | Read one continuing history, submit input, and inspect Runs and queued intent | Current Run and selected continuation head remain distinct |
| Run reference               | Read, observe, and explicitly control one exact accepted Run                  | Never rebinds to a successor                               |
| Queued-submission reference | Read, edit, withdraw, or observe one queued intent                            | Not a Run before consumption                               |
| RunAttempt reference        | Read an operational attempt and its diagnostics                               | No Worker control authority                                |
| Collection                  | Discover resources and expose supported collection operations                 | Discovery scope does not imply item ownership              |

Read-only projections and command receipts do not need mutable resource objects. Item access retains the Service's exported collection shape rather than inventing a single-Item endpoint.

## Binding and Navigation

- Construction and property access are local and perform no I/O.
- A binding retains the explicit Client and resource selector; a key remains a selector until Service resolves it.
- IDs and bindings do not prove existence or grant authority.
- `client.workspaces(id).agents(key)`, `client.threads(id)`, and `client.runs(id)` express the primary Python navigation shape.
- `Client.resources` exposes complete typed management navigation without replacing the compatible Web facade.
- Identified collection children are callable selectors. Collection operations use `list` and `create`; identified resources use `get`, `update`, `replace`, and `delete` where exported.
- Nested collections and named commands remain statically typed and discoverable. Required protocol preconditions remain explicit.
- Mutations address the actual owning scope under [Resource Management](04-resource-management.md#scope-and-authority), not an ownership assumption derived from a list query.

### References and Snapshots

- Public interaction references are named `Agent`, `Session`, `Thread`, `Run`, and `QueuedSubmission`. Their names describe remote resources, not local execution engines.
- A reference's Client, scope, and selector are read-only. Reading or updating a resource returns a new snapshot and never retargets an existing reference.
- `await ref.get()` performs a fresh read where that endpoint exists. There is no implicit cache, property-triggered refresh, or active-record `save()`.
- Mutable fields such as Run status, Thread versions, and Agent current Revision belong to returned representations, not apparently live reference properties.
- Navigation that needs unknown relationship IDs requires a representation or receipt first. A Run bound by ID does not fetch a Thread merely because a property is accessed.
- References have no independent transport context manager or `aclose()`. Closing a reference must not accidentally close the shared Client.
- A reference is not awaitable. Factories bind locally, `await` marks a request or wait, and `async with` marks an owned I/O scope.

## Values and Response Evidence

Resource calls return typed values together with HTTP evidence:

- status and response headers;
- ETag and request ID when supplied;
- the original response content;
- the actual command receipt or resource representation.

`Result[T]` has this conceptual public Python shape; it is not a serialized Service schema:

```python
class Result[T]:
    value: T
    status_code: int
    headers: Mapping[str, str]
    content: bytes
    etag: str | None
    request_id: str | None
```

- The envelope is read-only. `value` is the declared successful representation, receipt, binary value, or `None` for an empty/null success, not an optional parse attempt.
- Header lookup is case-insensitive. `etag` preserves the complete header value, including quoting; absent metadata is `None`.
- A `Result[T]` is a snapshot envelope, not a second durable resource. Generated model mutability does not confer persistence; mutating a local value causes no remote write and does not rewrite original `content`.
- Failure uses the resource exception contract rather than a false-valued envelope. No truthiness, tuple unpacking, or attribute forwarding substitutes for explicit `.value` access.
- Acceptance helpers return a [typed disposition](02-interaction-and-control.md#acceptance-values), containing the full `Result` receipt and its corresponding references. They do not hide the receipt on a mutable Run handle.

Complete request and response models remain available under `a13n.generated.models`. A resource reference and a similarly named wire representation are distinct types. Existing Pydantic Web/configuration models and `Representation` remain compatible; the resource interface does not silently replace them with another model family.

## Client Lifetime

- A Client owns its authenticated asynchronous HTTP pool, including a transport supplied to that Client.
- References derived from the Client share configuration, transport, and lifetime.
- One Client supports concurrent asynchronous requests on its owning event loop, including commands while a stream is open. It does not promise cross-thread or cross-event-loop use.
- `aclose()` is idempotent and final; a closed Client cannot be reopened. Local reference binding and inspection of already returned evidence remain possible after closure, but further I/O fails locally.
- `async with Client(...)` and `aclose()` provide explicit shutdown.
- Closing the Client rejects further owned I/O, cancels active owned transport work, and releases open streaming responses.
- Nested requests inside a streaming scope do not end the outer scope's ownership.
- Separately constructed generated synchronous clients retain a separate lifetime.
- Caller-owned upload sources remain caller-owned and are not closed by the SDK.

Closing, timing out, or cancelling local work does not interrupt a durable Run, consume queued input, delete a resource, or destroy an Environment. Remote effects require an explicit supported command.

## Compatibility

The resource interface preserves these distinct return contracts:

| Call                                                   | Return contract                                                                            | Ownership                                                                                               |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| `await client.execute(...)`                            | Generated `Response[T]`, including its typed success/error union and optional parsed value | Retained low-level HTTP                                                                                 |
| `client.stream(request)`                               | Async context manager yielding raw `httpx2.Response`                                       | Caller handles status and consumes response bytes                                                       |
| `await client.workspace(...)`                          | Existing `WorkspaceClient` discovery result                                                | Compatible Pydantic Web facade and shared Client lifetime                                               |
| Resource `get`, ordinary commands, and one-page `list` | `Result[T]`                                                                                | Typed successful value and original HTTP evidence                                                       |
| `agent.start(...)` and `thread.submit(...)`            | Awaitable typed acceptance/disposition result                                              | Receipt and references; not completion                                                                  |
| `run.stream(...)`                                      | Concrete `RunStream`, without awaiting the factory                                         | Domain SSE attachment under [Observation](03-observation-and-data-access.md#runstream-public-interface) |
| Collection `pages(...)` / `iter(...)`                  | Lazy asynchronous iterators                                                                | Page evidence / explicitly flattened values                                                             |

The existing Pydantic Web facade, its `Representation` values, and independently constructed generated synchronous clients remain available. `Client.stream` is not changed to return `RunStream`, and a `RunStream` does not expose a raw response body for competing consumption.

Operation-specific response bounds and exception behavior are not silently imposed on the retained low-level surface. Detailed error ownership belongs to [Protocol and Compatibility](05-protocol-and-compatibility.md#failure-semantics).

## Invariants

1. Binding a reference sends no request.
2. An existing reference's identity does not change after another command succeeds.
3. A snapshot mutation causes no remote write.
4. All derived references respect the parent Client's closure.
5. Early exit from an observation scope releases its local response lifetime.
6. Local cancellation or shutdown performs no remote lifecycle command.
