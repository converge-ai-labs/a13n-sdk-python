# Python SDK Contract

## Ownership and supported surface

This repository owns the `a13n` Python distribution, its public Python API, generator adapters, tests, and independent release lifecycle. Service owns authorization, durable state, HTTP semantics, and protocol schemas. Pinned inputs and source identity live in `contract/`; generation does not import or execute Service or another SDK. The shared Service SDK design supplies the domain boundary; this document defines its Python realization.

Python 3.13+ is async-first. Resource objects are the primary interface, backed by the complete pinned Native HTTP bindings. Existing `Client.execute`, `Client.stream`, async `Client.workspace()` discovery, the Pydantic Web facade, and independently constructed generated synchronous clients remain supported. The SDK version, Service source SHA, HTTP API version, and streaming schema versions are distinct identities.

## Objects, values, and lifetime

`Client` owns one authenticated HTTP pool. Its typed collections bind existing Service resources: for example, `client.workspaces(id).agents(key)`, `client.threads(id)`, and `client.runs(id)`. Binding and property access are local, perform no I/O, and confer no authority. A collection is callable when its protocol has an identified child. Resource methods perform explicit asynchronous reads or mutations; there is no hidden current Thread, local Agent engine, or SDK workflow identity.

`Client.resources` exposes the complete management tree; common interaction collections also have direct Client properties. This avoids collisions with the existing Web facade. Management navigation follows Service resource ownership. Collection operations use `list` and `create`; identified resources use `get`, `update`, `replace`, and `delete` where exported. Nested collections and named commands remain discoverable, statically typed attributes. Protocol-specific selectors and required preconditions remain explicit. Organization and Workspace references are distinct: a Workspace list can contain Organization-owned values, but does not turn them into Workspace-owned mutable handles. Bind mutations to the ownership reported by Service rather than inferring ownership from discovery.

HTTP results preserve the typed value, status, headers, ETag, and request ID. Values are snapshots, not live mirrors. Generated attrs models retain omission (`UNSET`), explicit null (`None`), and value distinctions, including within mutation inputs. The existing Pydantic Web models and `Representation` remain separate compatible types. No assignment to a local value persists a remote change. No concurrency conflict is automatically overwritten.

All references share their client's transport and lifetime. Async context management or `aclose()` releases owned connections and cancels owned local I/O. Closing a client, leaving an observer, timing out, or cancelling a coroutine never interrupts a durable Run, consumes queued input, deletes a resource, or destroys an Environment. Caller-owned upload sources are not closed. Separately constructed generated clients retain their separate lifetime.

## Interaction path

An Agent reference can start multiple independent conversations concurrently. `Agent.start` accepts text or the complete versioned `AgentInput`; text is a convenience for the ordinary text content block, not a second input protocol. Execution overrides, Environment choices, revision selection, labels, and idempotency keys remain separate inputs. The Agent selection is resolved by Service; acceptance preserves actual Run, Thread, Session, and configuration provenance. A selection never claims an immutable revision executed before Service reports it.

Starting work returns a reference to the accepted Run with its acceptance evidence. Creating an empty Thread is a separate collection operation. `Thread.submit` returns the actual typed Run-or-queue receipt plus the corresponding Run or queued-submission reference. A queued submission is never assigned a fabricated Run identity. Its `wait` observes disposition and never consumes it; explicit consume remains a mutation on the Thread's queue. Editing, reordering, and withdrawal preserve their required version preconditions.

Run helpers always target the exact bound Run. `wait` polls only that Run, stops on a known sealed state (including waiting for feedback), and has explicit timeout and polling interval. Unknown status strings remain visible and do not count as success. Feedback, retry, continue, and fork are explicit commands and return new Run references with receipts; they never rebind the original object. Run fork preserves the Service-created child Thread in the same Session. Thread current Run, selected continuation head, ancestry, and RunAttempt identity remain distinct.

Reading, waiting, and streaming never execute a client tool, grant approval, send feedback, or advance a Thread. Applications own handler registration, feedback construction, cross-Run loops, side-effect reconciliation, durable checkpoints, and business completion. The SDK does not provide a universal tool/approval workflow. Configuration-assistant entry points use their own exported resources and retain null AgentRevision provenance rather than fabricating a business Agent.

## Observation, pagination, and transfer

Run SSE is a scoped async context manager yielding a typed async iterator. Each observation preserves the SSE cursor separately from the RunStreamEvent identity. Heartbeats are not observations; malformed frames, incompatible schema versions, mismatched Run identity, and replay gaps are explicit failures. The caller supplies the last **applied** cursor when attaching again. Receiving an event never persists or advances an application checkpoint. EOF is not Run completion.

Attachments do not silently reconnect. A caller can perform bounded reconnection using its applied cursor and reconcile through typed current-resource reads. In-stream replay gaps retain their bounded metadata and never advance a cursor. Item pages preserve `snapshot_version`, `projection_cursor`, completeness, and finalization metadata. Callers can replace their covered display projection and attach after that cursor; the SDK does not relabel a merged snapshot as exact replay of missing events. Run sealing and display finalization remain different facts.

Lazy page iteration preserves filters, ownership, server order, and opaque cursors, including across empty pages. It stops only on the protocol's absent next cursor, rejects a non-advancing cursor, and does not prefetch. Each yielded page retains HTTP evidence. Resource-sequence collections remain separate from opaque-cursor collections. Detailed Run SSE, durable lifecycle events, Hook delivery, and best-effort notification frames never share a synthetic envelope or checkpoint.

Binary transfer uses explicit streaming response contexts and bounded upload chunks; buffered generated methods remain available but are not advertised as large-file streaming. Publication of an Asset or upload is distinct from Run acceptance. Partial failure does not roll back or hide a successfully published resource. File paths are not silently interpreted as remote Environment paths.

## Management coverage

Typed resource navigation covers every ordinary Native operation in the pinned OpenAPI, not merely the Agent example. Request and response models remain available under `a13n.generated.models` without duplicating their schema in a second model family.

| Family | Required distinction |
| --- | --- |
| IAM, Organizations, Workspaces, principals, bindings, credentials, audit | Credential scope and ownership are explicit; authentication sessions are not interaction Sessions. |
| Agents, revisions, models/providers, Web providers, Secrets, plugins | Discovery is not installation; Secret reads are metadata-only and credential diagnostics remain redacted. |
| Skills, staged uploads, revisions, Assets, content | Staging differs from publication; immutable Asset bodies have no invented replacement API. |
| Sessions, Threads, Runs, attempts, Items, pending actions, queues | Resource identity, selection, acceptance, consumption, and operational attempts remain distinct. |
| Environment providers, templates, instances, mounts | Thread defaults, fixed Run selection, connection status, and accepted/applied mounts are separate. |
| Memory providers, subjects, scopes, documents, changes, records | Exact storage/provider scope is retained; committed changes do not imply index readiness. |
| Application accounts, targets, connectors, Connections, authorization, schedules | Authorization completion, readiness, checks, Run acceptance, and external delivery are separate evidence. |
| Configuration assistant | Readiness, authoring conversations, drafts, and explicit application use the dedicated endpoints. |
| Lifecycle events, Hooks, usage, traces | Best-effort telemetry and delivery observations are not durable Run outcomes or complete billing. |

Missing endpoints remain missing: in particular, the pinned contract does not expose a single-Session read, a generic single-Item read, or a separate Session-fork command. Session navigation uses the exported Thread and label collections. Notification WebSocket transport is not implemented in this supported surface; HTTP coverage does not imply it. The standalone client-frame schema and semantics remain vendored evidence for a future adapter, not a claim of attachment or recovery support. No internal leases, Worker scheduling APIs, or provider-native protocols are added.

## Failure, compatibility, and generation

Resource methods raise `ApiError` for Service failures, retaining status, safe code/message/details, request ID, and retry guidance. Malformed success bodies raise `ProtocolError`. Transport errors report uncertain mutation outcomes; timeouts and cancellation never prove rollback. Mutations are never automatically replayed, and required idempotency keys are supplied explicitly by the caller. Low-level `execute` retains its existing typed success/error union rather than silently adopting resource exceptions.

Diagnostics do not expose credentials or input/output payloads. Wire serialization still carries authorized values. Generated code owns mechanical typed HTTP and resource navigation; handwritten code owns bounded interaction helpers, lifetime, error normalization, pagination, and SSE semantics. Generation is deterministic from local pinned inputs, checks both names and bytes, and never mutates committed output in check mode. Resource coverage is checked independently of convenience coverage. Upstream changes to generated public types require compatibility review before release.

## Acceptance evidence

- Every pinned Native HTTP operation is reachable through typed resource navigation and the retained low-level binding; signatures retain required headers and omission/null semantics.
- Examples and static type checks cover Agent start, Run observation, Run-or-queue submission, explicit feedback successors, and representative owned management resources.
- Transport tests verify path escaping/base prefixes, shared authentication/lifetime, metadata, errors, no mutation replay, cancellation, and streaming cleanup.
- Semantic tests verify exact Run waiting, queue non-consumption, explicit successor identities, empty-page pagination, SSE framing/checkpoints/gaps, and absence of hidden tool or approval execution.
- Provenance, regeneration, lint, type checks, tests, and package builds pass independently of a Service checkout. Mock-transport evidence is labeled as such; real Service/provider verification is reported separately.
