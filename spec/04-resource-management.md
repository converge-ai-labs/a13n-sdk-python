# Resource Management

## Scope and Authority

`Client.api` exposes the generated public Native resource hierarchy, not a second handwritten management API. Workspace business collections use flat paths and implicit API-key workspace context; Service and Organization administration retains its declared explicit owner selectors. A resource reference does not gain mutation authority outside its owner; a selector is not evidence of access.

Supported methods come from the pinned OpenAPI operation, not generic active-record CRUD. Collections provide declared one-page reads and lazy pagination; identified resources expose only the generated `get`, `update`, `replace`, `delete`, and named commands that their endpoint supports. Mutations preserve ETags, versions, idempotency keys, and typed bodies. The SDK neither refetches a stale version nor retries an uncertain mutation automatically.

## Management Families

Generated resources cover the exported Service boundary: IAM and organization/workspace administration; Agents and immutable revisions; Models, provider configuration and credentials; Skills, staged uploads, Assets and binary content; Sessions, Threads, inbox Entries, Runs and Attempts; Environments and mounts; Memory; integrations and scheduled work; usage, audit, webhooks, trace projections, Findings and managed analyses. This enumeration does not claim every conceptual domain has a public endpoint: `a13n.generated.resources` and the pinned OpenAPI are the operation inventory.

- Agent selection, immutable revision choice, and a Run's reported executed revision remain separate. A later Agent update does not mutate an accepted Run.
- Model `config.settings` is an open native JSON mapping on both request and readback; generated wrappers preserve nested JSON and omission rather than imposing a parallel settings hierarchy or provider policy. Only Models accept stable keys. Agents and Skills use IDs; removed Service secrets are distinct from retained provider credentials. Credential metadata is not a plaintext secret retrieval mechanism. Authentication Sessions are not interaction Sessions.
- Upload staging and Asset publication are different outcomes; a failed Run does not undo a published Asset. Native upload references use `upl_` plus 32 lowercase hex digits. New bootstrap/change/reset passwords have a Service-owned minimum of eight characters; login, invitation acceptance and current-password fields retain their separate declared constraints. Generated string serialization forwards these fields without implementing a second SDK policy. An immutable content endpoint does not imply replacement authority.
- A Thread inbox Entry is retained intent. An assigned Run is identified only by the Service's `assigned_run_id`; `RunAttempt` diagnostics do not grant Worker or lease control.
- Environment selection and mount effects have their declared lifetimes. Updating a Thread does not retarget an already accepted Run. Client shutdown neither stops nor destroys an Environment.
- Usage and trace observations do not by themselves prove billing settlement, external delivery, or business completion.

## Model Media and Provider Authorization

Generated Model characteristics expose native `image_input`, `video_input`, and `url_input` policies on input and readback. Omitted image policy uses native defaults; null disables automatic preparation. Zero values, false flags and empty URL subtype lists remain explicit. Native Message URL/Asset parts retain order and duplicates through authored and generated entry points. The SDK does not download, resize, split, encode, budget or authorize media.

`client.api.model_providers(id)` exposes `authorization.get()`, `authorize(body=...)`, `authorization.callback(body=...)`, `authorization.delete()` and `models.get()`. These use the ordinary Client auth/Workspace context and preserve returned method, nullable state, status and HTTP evidence. Service authorizes status with `read`, authorization mutations with `write`, and discovery with `run`. Only hosted `browser_callback` start requires an unconfined user login; manual Workspace authorization may use an authorized API key. The SDK applies no blanket session-only restriction, browser flow, callback origin, client identity or credential store. Operator configuration and external issuer exchange remain Service/Harness ownership.

Discovery returns `ProviderModel` choices, preserving the original `slug` and `display_name` wire fields plus optional nullable characteristics. `ProviderType.supports_model_discovery` declares capability across provider types; there is no retained ChatGPT-only model alias.

## Environment Preparation and Skills

`AgentOverride.lazy_environment` and `skill_sync` use the same generated serialization as revision configuration. Omission inherits native policy; permitted null, false and empty values remain explicit. Service defaults to lazy instance readiness. `lazy_environment=False` creates/starts frozen mounts before Harness entry; execution connections remain first-use in both modes. Mount working directories and standalone Environment operations retain Service-owned preparation and provider semantics; the SDK does not construct local providers or choose a project directory.

Service's default skill policy is shared publication (`mode=shared`, `overwrite=true`, `cleanup=false`); opt-in isolated policy uses `mode=isolated`, `cache_count=128`. A Run override replaces the whole block, and omitted members use that mode's native defaults. Shared overwrite/cleanup acts on mutable conventional skill names; isolated packages use digest directories and a soft count budget, with zero disabling trimming. The SDK preserves the policy and performs no publication, cache management or migration.

`AgentOverride.builtin_skills` selects instruction bundles while preserving omission, null and empty selections. Service owns tool admission and authorization; instruction selection grants no authority.

## Computer and Environment Authority

`MountCreate.permission_ceiling` forwards a native JSON permission set; omission preserves the Service's file/execution defaults, not Computer authority. An explicit empty `operations` list remains empty. Thread `environments(name).update(body=MountUpdate(...), if_match=...)` replaces the desired ceiling under the Thread ETag; already accepted Runs retain their frozen ceiling. The SDK neither provisions a desktop nor infers actions from a toolset name.

`client.api.environments(id).computer.check()` is one explicit readiness probe, not startup, screenshot capture or input. Its `checked`, `unsupported` and `not_ready` results preserve exact actions and readiness flags. Provider failures remain errors. Actual Computer use requires the Agent's toolset, explicit mount actions and provider readiness; a check is not a permission grant.

Environment Provider `references.get()` returns counts and bounded reference samples; `delete(if_match=...)` remains a conditional mutation that Service may refuse while referenced. Private provider configuration is write-only at the Service boundary. Public readback is not a credential backup, and the SDK does not recover omitted private values or copy them from request objects into responses.

## Tool Discovery Configuration

Agent revisions and Run overrides expose generated `ToolSearch` with a strict proxy-only `ToolSearchConfig`. Omitted configuration and `{}` use Service defaults; null configuration and retired native strategy fields are invalid. Groups select already admitted Connection, plugin, platform and capability sources. Service owns discovery execution and validation.

Omitted or null `tool_search` retains revision configuration; an explicit block replaces the whole block, without recursive merging. Omitted config/groups retains its native defaults; `groups={}` disables grouping. The SDK preserves omitted members, explicit null and empty maps and adds no provider fallback.

## Desktop Assistance and User Control

The native graph exposes `runs(id).desktop_assistance(call_id).get()`, nullable `runs(id).desktop_control.get()`, and explicit `desktop_control.create(body=Request(...))`. The shared `desktop_assistance(id)` resource exposes `view`, `request_control`, `control`, `disconnect`, and `complete`. Opening user control creates a viewing context, not an execution reservation. Requesting control reserves/suspends under Service authority and may return preparing before a grant. Access requires ordinary workspace/Run access, current execution authority, the frozen mount and matching provider generation; the SDK neither supplies nor bypasses these checks.

`Control` and `Completion` use a 20–72-character browser-session token and a nonnegative epoch. Their `session_id` is not a Service Session resource ID. Metadata `View` contains no access secret; `Access` preserves the no-store WebSocket URL/password and expiry from an explicit grant. Applications keep these short-lived credentials private. Disconnect revokes the caller's browser session without answering a deferred call; completion revokes access, confirms held-input cleanup and persists its outcome. [Interaction control](02-interaction-and-control.md#desktop-waiting-and-control) owns the separate explicit resume boundary.

## Execution Readback and Usage

`client.api.runs.list(...)`, `runs(id).agent.get()` and `runs(id).attempts(attempt_id).get()` retain native scope, paging and HTTP evidence. `RunAgent` separates the frozen revision from the configuration with that Run's override applied. Referenced Models, Connections and templates remain live; the SDK does not fabricate an immutable resolved dependency graph.

`usage.records(record_id).metrics.get()` reads Service-derived request timing. Nullable metrics remain null when unavailable and zero remains a measured zero. `UsageSummary` requires both aggregate `models` and per-Run `runs`; each `ModelUsage` requires nullable first-chunk and output-speed fields. No client-side timestamp formula replaces missing metrics, and usage still does not prove billing settlement.

`usage.context.get(thread_id=..., run_id=..., record_id=...)` forwards selectors for Service's exactly-one validation. Success is `ContextUsage | None`: no completed contribution is HTTP 200 JSON null, not a fabricated empty model. A model requires Run/record identity and nullable `input_tokens`, `output_tokens`, and `context_window_tokens`; zero remains zero. Thread/Run scope selects the latest completed main-agent contribution; record scope reads the exact contribution, including attributed children. Capacity uses current Model configuration and the applicable frozen Run Agent override. This is neither aggregate usage nor pending prompt estimation. The SDK computes no ratio or token total.

## Findings and Message Authors

`client.api.finding_agent()` prepares the ordinary builtin Finding Agent; `preset_kind=finding` distinguishes it from Composer. `client.api.finding_analyses` exposes one-page/lazy reads and explicit keyed creation of an Analysis backed by an ordinary Run. Analysis is diagnostic selection evidence, not a separate execution lifecycle or proof of complete review. `client.api.findings` exposes declared list/create/get/update operations with native category, severity, assessment, evidence, pagination and conditional-update metadata. Service owns evidence authorization and validation; the SDK performs no trace inference or automatic analysis.

`client.api.sessions(id).message_authors.get(entry_id=[...])` submits repeated query IDs and retains each matching entry's original principal ID/submission time and optional current Principal summary. Missing, foreign-session and non-message entries are omitted by Service. This query neither grants directory access nor changes attribution when an Entry is queued, consumed or forked.

## Missing Operations

The SDK does not synthesize removed legacy auth-context, queued-submission, Run-stream, lifecycle-notification, steer/feedback/retry/continue, or Web-provider DTO façade endpoints. A missing Native command remains unavailable rather than being emulated with a different lifecycle. Complete generated models and low-level operations remain accessible alongside convenience methods; they all use the same Client lifetime and wire serialization.

## Memory

Flat workspace `client.api.memories` exposes metadata, file content and history, or provider-backed records. `client.api.memory_providers` retains provider ownership and optional Workspace binding. Generated methods preserve the Service's distinct file and record operations rather than synthesizing common CRUD.

File content is JSON text, not Asset binary transfer. File paths may contain directory separators and Unicode; references encode selectors once. File replacement, deletion and moves require the current file ETag; Memory metadata changes and deletion use the Memory ETag. Revisions bind an integer sequence. Restore undoes that change by writing its previous content; restoring a creation removes the file. It requires the current file ETag when that path exists and may return a null file state. History purge selects a path, not a revision sequence.

Records expose collection reads, creation, POST-body search, replacement and deletion, without an item GET, ETag, or PATCH. A `write_unconfirmed` conflict is an uncertain provider outcome, not permission to replay the mutation. Thread memory mount mutations use the Thread ETag, and their responses retain that ETag. New Thread and Fork bodies accept mounts; the Run view reports the frozen accepted mounts, not later Thread changes. Agent configuration may declare default mounts. Model `extra_body` and `extra_headers` are full generated mappings, preserving `{}` as an explicit clear under the Service's Model/Agent/Run replacement rules; no SDK-side provider inference is performed. The pinned OpenAPI and referenced Service specifications own schemas and validation rules.

### Memory Spaces and Session Selection

`client.api.memory_spaces` exposes Space CRUD, organization status, explicit organization requests, organization Run pages and attached Session pages. A Space owns one managed file Memory; its `memory_id` uses existing file/revision APIs but is not a standalone mount or independently deletable store. Space configuration uses its own ETag. Disabling preserves data and bindings; deletion may be refused while Sessions or unsealed frozen Runs reference it.

Native Agent defaults and Session `memory` settings select named `SpaceBinding` values. Omission retains unresolved/inherited choices; an explicit `spaces` list replaces the selection, including `[]`. First accepted business execution settles unresolved Session fields under Service authority. Later Agent edits and forks do not replace that settled selection. The SDK forwards these native settings without choosing business scopes or running an organization scheduler.

Run readback retains legacy `MemoryMount` and host-resolved `FrozenMemoryMount` values. Presence of `roots` or `space_id` selects the frozen typed value, including empty roots and null Space identity. These host-owned fields are not added to authored `MemoryMount` request constructors. Organization uses ordinary Runs with `purpose=memory_organization`; accepted work is not completed organization. Service owns isolated roots, timing/change triggers, execution authority and failure evidence.
