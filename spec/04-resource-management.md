# Resource Management

## Scope and Authority

`Client.resources` exposes the generated public Native resource hierarchy, not a second handwritten management API. Workspace business collections use flat paths and implicit API-key workspace context; Service and Organization administration retains its declared explicit owner selectors. A resource reference does not gain mutation authority outside its owner; a selector is not evidence of access.

Supported methods come from the pinned OpenAPI operation, not generic active-record CRUD. Collections provide declared one-page reads and lazy pagination; identified resources expose only the generated `get`, `update`, `replace`, `delete`, and named commands that their endpoint supports. Mutations preserve ETags, versions, idempotency keys, and typed bodies. The SDK neither refetches a stale version nor retries an uncertain mutation automatically.

## Management Families

Generated resources cover the exported Service boundary: IAM and organization/workspace administration; Agents and immutable revisions; Models, provider configuration and credentials; Skills, staged uploads, Assets and binary content; Sessions, Threads, inbox Entries, Runs and Attempts; Environments and mounts; Memory; integrations and scheduled work; usage, audit, webhooks, and trace projections. This enumeration does not claim every conceptual domain has a public endpoint: `a13n.generated.resources` and the pinned OpenAPI are the operation inventory.

- Agent selection, immutable revision choice, and a Run's reported executed revision remain separate. A later Agent update does not mutate an accepted Run.
- Model `config.settings` is an open native JSON mapping on both request and readback; generated wrappers preserve nested JSON and omission rather than imposing a parallel settings hierarchy or provider policy. Only Models accept stable keys. Agents and Skills use IDs; removed Service secrets are distinct from retained provider credentials. Credential metadata is not a plaintext secret retrieval mechanism. Authentication Sessions are not interaction Sessions.
- Upload staging and Asset publication are different outcomes; a failed Run does not undo a published Asset. Native upload references use `upl_` plus 32 lowercase hex digits. New bootstrap/change/reset passwords have a Service-owned minimum of eight characters; login, invitation acceptance and current-password fields retain their separate declared constraints. Generated string serialization forwards these fields without implementing a second SDK policy. An immutable content endpoint does not imply replacement authority.
- A Thread inbox Entry is retained intent. An assigned Run is identified only by the Service's `assigned_run_id`; `RunAttempt` diagnostics do not grant Worker or lease control.
- Environment selection and mount effects have their declared lifetimes. Updating a Thread does not retarget an already accepted Run. Client shutdown neither stops nor destroys an Environment.
- Usage and trace observations do not by themselves prove billing settlement, external delivery, or business completion.

## Model Media and Provider Authorization

Generated Model characteristics expose native `image_input`, `video_input`, and `url_input` policies on input and readback. Omitted image policy uses native defaults; null disables automatic preparation. Zero values, false flags and empty URL subtype lists remain explicit. Native Message URL/Asset parts retain order and duplicates through authored and generated entry points. The SDK does not download, resize, split, encode, budget or authorize media.

`client.resources.model_providers(id)` exposes `authorization.get()`, `authorize(body=...)`, `authorization.callback(body=...)`, `authorization.delete()` and `models.get()`. These use the ordinary Client auth/Workspace context and preserve returned method, nullable state, status and HTTP evidence. Service authorizes status with `read`, authorization mutations with `write`, and discovery with `run`. Only hosted `browser_callback` start requires an unconfined user login; manual Workspace authorization may use an authorized API key. The SDK applies no blanket session-only restriction, browser flow, callback origin, client identity or credential store. Operator configuration and external issuer exchange remain Service/Harness ownership.

## Missing Operations

The SDK does not synthesize removed legacy auth-context, queued-submission, Run-stream, lifecycle-notification, steer/feedback/retry/continue, or Web-provider DTO façade endpoints. A missing Native command remains unavailable rather than being emulated with a different lifecycle. Complete generated models and low-level operations remain accessible alongside convenience methods; they all use the same Client lifetime and wire serialization.

## Memory

Flat workspace `client.resources.memories` exposes metadata, file content and history, or provider-backed records. `client.resources.memory_providers` retains provider ownership and optional Workspace binding. Generated methods preserve the Service's distinct file and record operations rather than synthesizing common CRUD.

File content is JSON text, not Asset binary transfer. File paths may contain directory separators and Unicode; references encode selectors once. File replacement, deletion and moves require the current file ETag; Memory metadata changes and deletion use the Memory ETag. Revisions bind an integer sequence. Restore undoes that change by writing its previous content; restoring a creation removes the file. It requires the current file ETag when that path exists and may return a null file state. History purge selects a path, not a revision sequence.

Records expose collection reads, creation, POST-body search, replacement and deletion, without an item GET, ETag, or PATCH. A `write_unconfirmed` conflict is an uncertain provider outcome, not permission to replay the mutation. Thread memory mount mutations use the Thread ETag, and their responses retain that ETag. New Thread and Fork bodies accept mounts; the Run view reports the frozen accepted mounts, not later Thread changes. Agent configuration may declare default mounts. Model `extra_body` and `extra_headers` are full generated mappings, preserving `{}` as an explicit clear under the Service's Model/Agent/Run replacement rules; no SDK-side provider inference is performed. The pinned OpenAPI and referenced Service specifications own schemas and validation rules.
