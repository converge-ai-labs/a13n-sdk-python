# Resource Management

## Scope and Authority

`Client.resources` exposes the generated public Native resource hierarchy, not a second handwritten management API. Service and Organization collections and Workspace-scoped collections retain their own ownership boundaries. A resource listed through a Workspace does not gain mutation authority outside its actual owner; a selector is not evidence of access.

Supported methods come from the pinned OpenAPI operation, not generic active-record CRUD. Collections provide declared one-page reads and lazy pagination; identified resources expose only the generated `get`, `update`, `replace`, `delete`, and named commands that their endpoint supports. Mutations preserve ETags, versions, idempotency keys, and typed bodies. The SDK neither refetches a stale version nor retries an uncertain mutation automatically.

## Management Families

Generated resources cover the exported Service boundary: IAM and organization/workspace administration; Agents and immutable revisions; Models, provider configuration and credentials; Skills, staged uploads, Assets and binary content; Sessions, Threads, inbox Entries, Runs and Attempts; Environments and mounts; Memory; integrations and scheduled work; usage, audit, webhooks, and trace projections. This enumeration does not claim every conceptual domain has a public endpoint: `a13n.generated.resources` and the pinned OpenAPI are the operation inventory.

- Agent selection, immutable revision choice, and a Run's reported executed revision remain separate. A later Agent update does not mutate an accepted Run.
- Credential metadata is not a plaintext secret retrieval mechanism. Authentication Sessions are not interaction Sessions.
- Upload staging and Asset publication are different outcomes; a failed Run does not undo a published Asset. An immutable content endpoint does not imply replacement authority.
- A Thread inbox Entry is retained intent. An assigned Run is identified only by the Service's `assigned_run_id`; `RunAttempt` diagnostics do not grant Worker or lease control.
- Environment selection and mount effects have their declared lifetimes. Updating a Thread does not retarget an already accepted Run. Client shutdown neither stops nor destroys an Environment.
- Usage and trace observations do not by themselves prove billing settlement, external delivery, or business completion.

## Missing Operations

The SDK does not synthesize removed legacy auth-context, queued-submission, Run-stream, lifecycle-notification, steer/feedback/retry/continue, or Web-provider DTO façade endpoints. A missing Native command remains unavailable rather than being emulated with a different lifecycle. Complete generated models and low-level operations remain accessible alongside convenience methods; they all use the same Client lifetime and wire serialization.
