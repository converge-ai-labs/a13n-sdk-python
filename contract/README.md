# Pinned Service contract

Service owns the Native HTTP and streaming contracts. This directory contains immutable engineering inputs selected by `source.json`; the SDK does not independently redefine endpoint semantics. The manifest identifies the upstream repository, full commit SHA, original path for each copied file. Generation and local tests use only these local files and need no upstream checkout or credentials.

The next successful sync selects Service's `proto/a13n-service/openapi.json` and `thread-stream.schema.json`, plus `spec/api-conventions.md` and the Runs, Facts and Delivery, and API owner documents. All selected inputs come from the same recorded Service commit; historical pins may still contain the former notification, Run-stream, fixture, and queued-submission inputs until that sync succeeds. Sync retires only files listed in the prior source manifest that are no longer selected, leaving SDK-local files untouched.

Review source identity, contract changes, generated diffs and local tests together. Updating the contract does not itself publish an SDK, and generating bindings does not establish complete JSON Schema validation or streaming protocol parity.
