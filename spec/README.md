# Python SDK Contract

## Ownership

This repository owns the `a13n` Python distribution, its public Python API, generator adapters, tests and independent release lifecycle. Service owns authorization, durable state, HTTP semantics and protocol schemas. Pinned inputs and their source identity live in `contract/`. Neither development nor generation imports or executes the Service or another SDK repository.

The SDK version, Service source SHA and Service wire schema versions are different identities. Changing one does not implicitly advance the others. A reviewed contract update may change generated public types; compatibility is evaluated in the SDK pull request before release.

## HTTP and model boundary

Generated bindings cover the ordinary Native `/api/v1` operations present in the pinned OpenAPI. Typed attrs request and response models preserve unions and distinguish omitted `UNSET` from JSON null. Server defaults are not inserted as client-supplied values. Default error responses and fields literally named `default` remain part of the contract.

The async `Client` owns the httpx2 pool and shares it with generated calls through `execute`. Workspace bindings share parent transport and lifetime; discovering a Workspace ID never grants authority beyond the Service credential. The Web convenience facade retains its Pydantic models and bounded response/error mapping. Generated responses retain their own typed success/error union, status, headers and raw content; they do not inherit that facade's response-size limit or exception mapping. Separately constructed generated synchronous clients have a separate lifetime.

Uploads read caller-owned binary files in bounded chunks without closing the source. Streaming downloads retain a caller-visible response lifetime; cancellation and client close release owned transport work. Buffered generated download methods remain available but are not the large-file streaming interface.

## Failure and diagnostics

Mutations are not automatically replayed after transport failure. A timeout or cancellation after possible dispatch does not prove that Service rolled back the operation; callers reconcile uncertain effects with Service state. Credential-bearing request, response and client diagnostics do not reveal secret payloads; authorized wire serialization retains them.

Unknown Run status strings are preserved. This does not open closed discriminator tags or promise validation of every JSON Schema keyword. Generated ordinary HTTP bindings do not implement Run SSE or notification WebSocket recovery.

## Verifiable invariants

- Every pinned Native HTTP operation has a generated binding.
- Regeneration uses pinned tools and local inputs only; check mode never replaces committed output.
- Provenance hashes match the vendored input bytes.
- Wire fixtures retain omission, null, typed union, decimal and extensible-status behavior.
- Generated transport calls preserve base URL prefixes, authentication, response headers, cancellation and shutdown.
- Negative type tests reject incorrectly typed public request fields.
