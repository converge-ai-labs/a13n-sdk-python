# Protocol and Compatibility

## Wire Fidelity

The [pinned Native API](../contract/semantics/api.md) and [API conventions](../contract/semantics/api-conventions.md) own paths, schemas, statuses, and security. The SDK retains typed generated attrs models and operations for all exported endpoints. `UNSET` omits a field; `None` sends explicit null where permitted; a supplied value remains distinct from both. Server defaults are not inserted into requests. Binary, empty, JSON-null, and error responses retain their declared forms. Static typing does not claim runtime validation of every JSON Schema keyword.

Pure generated resources return `Result[T]` for every declared operation, including Service Submitted-shaped commands; they do not import authored interaction helpers. `Result[T]` keeps successful typed values plus HTTP status, headers, and original content. Resource calls turn an `ErrorEnvelope` into `ApiError(status, code, message, details, request_id, retry_after)` without leaking credentials or raw payloads in ordinary representations. Missing/malformed required response data raises `ProtocolError` at the generated response parser; invalid local input is not misclassified as a Service response failure. An Entry settling failed/withdrawn raises `SubmissionError` with its exact snapshot rather than returning unrelated Run success. A resource may raise `ValueError` before dispatch, with no implied unknown remote outcome; transport failure after possible dispatch raises `TransportError`, so mutation outcome may be unknown. `Client.execute` retains the generated success/error union and raw HTTP evidence without resource exception mapping. `Client.stream` remains an explicit raw-response context; the generated Thread stream route remains raw protocol access, while explicit `ThreadStream` parses Thread-wide SSE and the primary finite Interaction filters to its incorporating Run.

## Preconditions and Cancellation

Versioned mutations retain required ETags, `If-Match`, expected versions, and caller-supplied idempotency keys. A helper does not generate a new key, silently refresh a conflicting version, retry a mutation, or interpret an error as rollback. An SDK wait timeout raises built-in `TimeoutError`; caller cancellation propagates `asyncio.CancelledError` and issues no compensating command. Readback and a retained idempotency key allow the application to reconcile an unknown outcome.

The primary finite Interaction ends by exact Run readback even with idle SSE and filters foreign Runs. The advanced Thread stream has only five frame names; only `delta` and `boundary` carry resumable Redis entry IDs. `changed`, `reset`, and `gap` have no cursor and require caller-owned reconciliation. Malformed frames are protocol errors. EOF, reconnect, and gap handling follow [Observation](03-observation-and-data-access.md#checkpoints-and-recovery), not a generic HTTP retry policy.

## Contract Inputs and Generation

`contract/source.json` identifies the source repository, exact upstream Service commit, and original paths for the vendored `openapi.json`, `thread-stream.schema.json`, and semantic chapters. Generated bindings and resource navigation are derived locally from those files; generation does not import or execute the Service. Vendored evidence is not mutated by generator adaptations.

Generated session workspace-header routing follows OpenAPI declarations; API keys select an implicit workspace and never require a workspace argument for business resources. Only Models support keys; Agents and Skills use IDs. Model `extra_body`/`extra_headers` retain full mappings and explicit `{}` clearing through generated typed models, without SDK-side inference. The generation adapter removes duplicate FastAPI input/output component titles, maps wildcard binary asset responses to an octet-stream generator media type, supplies `format: binary` for the file part of the multipart upload, and generates one `File` body for equivalent binary media schemas. For multi-media image uploads, `File.mime_type` must explicitly select a declared JPEG, PNG, or WebP type; missing or unsupported media fails locally before dispatch. The original OpenAPI retains the complete media declarations. These compatibility adaptations are reviewable code, not a replacement source pin. Generated coverage, typed bodies, and HTTP behavior are tested independently of regenerated-file byte equality.

## Compatibility Axes

| Identity                    | Meaning                      | Does not imply                   |
| --------------------------- | ---------------------------- | -------------------------------- |
| Python distribution version | SDK API compatibility        | A Service deployment version     |
| Source commit SHA           | Contract provenance          | SDK release readiness            |
| HTTP API version            | Native route protocol        | Thread-stream replay guarantee   |
| Stream schema               | Thread frame shape           | Persisted application checkpoint |
| Resource revision/version   | Domain state and concurrency | SDK release or protocol identity |

This Native migration changes the SDK's public Python surface: old global Run paths, Run SSE/notification helpers, queued-submission receipts, auth-context calls, and duplicate Web DTO façade are not preserved. Generated requests remain available for the pinned Service only; clients targeting the former Service protocol must remain on a compatible previous SDK release. Build and unit tests alone do not prove deployed-provider behavior.

## Conformance Evidence

- Generator/resource tests cover operation navigation and binary/media adaptations against pinned inputs.
- Wire and Client tests cover omission/null, bearer/session authentication, `X-CSRF-Token`, TLS CA configuration, transport closure/cancellation, error envelopes, streaming/binary paths, and caller-owned upload sources.
- Interaction/stream tests cover nullable immediate Run, Entry incorporation and failed/withdrawn dispositions, exact Run identity and deadline, finite cleanup/foreign-Run filtering/idle SSE, five-frame parser, cursor acknowledgement, bounded retries and readback.
- An installed artifact test against an existing disposable HTTPS Service is separate from mock/loopback evidence. External model-provider connectivity is separately labeled when configured and authorized.

[Contributing](../CONTRIBUTING.md) owns validation commands and publication. Publication is not implied by generation, packaging, or local acceptance.
