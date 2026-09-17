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

## Values and Response Evidence

Resource calls return typed values together with HTTP evidence:

- status and response headers;
- ETag and request ID when supplied;
- the original response content;
- the actual command receipt or resource representation.

A `Result[T]` is a snapshot envelope, not a second durable resource. Mutating a local value does not persist a remote change.

Complete request and response models remain available under `a13n.generated.models`. A resource reference and a similarly named wire representation are distinct types. Existing Pydantic Web/configuration models and `Representation` remain compatible; the resource interface does not silently replace them with another model family.

## Client Lifetime

- A Client owns its authenticated asynchronous HTTP pool, including a transport supplied to that Client.
- References derived from the Client share configuration, transport, and lifetime.
- `async with Client(...)` and `aclose()` provide explicit shutdown.
- Closing the Client rejects further owned I/O, cancels active owned transport work, and releases open streaming responses.
- Nested requests inside a streaming scope do not end the outer scope's ownership.
- Separately constructed generated synchronous clients retain a separate lifetime.
- Caller-owned upload sources remain caller-owned and are not closed by the SDK.

Closing, timing out, or cancelling local work does not interrupt a durable Run, consume queued input, delete a resource, or destroy an Environment. Remote effects require an explicit supported command.

## Compatibility

The resource interface preserves:

- `Client.execute` and its generated response semantics;
- `Client.stream` and caller-visible streaming lifetime;
- asynchronous `Client.workspace()` discovery;
- the existing Pydantic Web facade;
- independently constructed generated synchronous clients.

Operation-specific response bounds and exception behavior are not silently imposed on the retained low-level surface. Detailed error ownership belongs to [Protocol and Compatibility](05-protocol-and-compatibility.md#failure-semantics).

## Invariants

1. Binding a reference sends no request.
2. An existing reference's identity does not change after another command succeeds.
3. A snapshot mutation causes no remote write.
4. All derived references respect the parent Client's closure.
5. Early exit from an observation releases its local response lifetime.
6. Local cancellation or shutdown performs no remote lifecycle command.
