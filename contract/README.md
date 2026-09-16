# Pinned Service contract

Service owns the Native HTTP and streaming contracts. This directory contains immutable engineering inputs selected by `source.json`; the SDK does not independently redefine endpoint semantics. The manifest identifies the upstream repository, full commit SHA, original path and SHA-256 for each copied file. Generation and local tests use only these local files and need no upstream checkout or credentials.

The snapshot contains Service's `proto/a13n-service/` HTTP schema, streaming schemas and wire fixtures, together with API conventions, Native streaming and queued-submission semantics. All inputs come from the same recorded Service commit. Queued-submission DELETE requires the `expected_version` query parameter and returns an empty 204 response.

Review source identity, contract changes, generated diffs and local tests together. Updating the contract does not itself publish an SDK, and generating bindings does not establish complete JSON Schema validation or streaming protocol parity.
