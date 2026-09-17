# Resource Management

## Design Position

Typed resource navigation covers the ordinary Native management operations declared by the SDK's pinned Service contract. Coverage is not limited to the managed-Agent example and does not require a handwritten convenience method for every operation.

This document owns management-family responsibilities and scope distinctions. [Resources and Client Lifetime](01-resources-and-client-lifetime.md) owns the common object model; [Interaction and Control](02-interaction-and-control.md) owns Run and queue commands. Service remains the authority for each domain's lifecycle and authorization.

## Scope and Authority

- A resource binding retains the caller's explicit credential context and selector.
- Workspace and Organization scopes are distinct.
- A Workspace configuration collection can contain Organization-owned values; discovery does not convert their ownership.
- Mutations bind the scope reported by the resource, under current Service authorization.
- A Workspace lookup does not imply permission to manage parent configuration, a same-name override, or inherited write access.
- ETags, resource versions, and command preconditions retain their domain meanings under [Protocol and Compatibility](05-protocol-and-compatibility.md#concurrency-and-idempotency).

## IAM and Ownership

Typed operations cover exported Organizations, Workspaces, Users, Service Accounts, bindings, invitations, credentials, authentication sessions, and security audit resources.

- Credential scope, execution Principal, and resource ownership are separate facts.
- Authentication sessions are not interaction Sessions.
- Credential-bearing input and one-time secret output follow the [diagnostic boundary](05-protocol-and-compatibility.md#diagnostics), not ordinary object logging.
- The SDK exposes public operations only; it does not acquire internal Worker or database authority.

## Agent and Provider Configuration

Typed operations cover exported Agents and revisions, Model Providers and Models, Web Providers, Secrets, and installed plugin selections.

- Mutable authoring resources and immutable execution revisions remain distinct.
- A desired selection does not prove the composition accepted or executed by Service.
- Secret reads expose the authorized metadata surface, not an invented plaintext-retrieval API.
- Provider or plugin discovery does not install executable code or prove runtime readiness.
- Configuration-assistant conversations use their dedicated resources rather than an ordinary business-Agent shortcut.

## Skills, Assets, and Content

Typed operations cover staged Skill uploads, managed Skills, immutable revisions, Assets, and authorized content access.

- Upload staging, validation, and publication retain their separate outcomes.
- Immutable Asset content has no invented replacement operation.
- Publication is independent of later Run acceptance; a failed submission does not hide or roll back an already published resource.
- File transfer and caller-owned source lifetime follow [Observation and Data Access](03-observation-and-data-access.md#binary-transfer).

## Interaction Resources

Sessions, Threads, Runs, RunAttempts, Items, pending actions, and queued submissions retain their Service identities.

- Read-only representations and receipts need not become mutable objects.
- A retained Item is neither a transport event nor complete resumable Harness state.
- Attempt diagnostics do not expose Worker claim, lease, or recovery-control operations.
- Submission and successor behavior is owned by [Interaction and Control](02-interaction-and-control.md), not a second management workflow.

## Environments and Mounts

Typed operations cover exported Environment Providers, template revisions, Environment instances, selections, and mount operations.

- A Thread's mutable default is distinct from a Run's fixed primary selection.
- Omission, explicit no-Environment, selection of an existing Environment, and creation from a template remain different choices.
- Updating a Thread default does not redirect an already accepted Run.
- A live additional mount supplements one Run; it does not replace that Run's fixed primary selection.
- Mount acceptance and current-Attempt application are separate evidence.
- Connection status alone proves neither authorization nor successful mount loading.
- Closing an SDK Client does not stop or destroy an Environment.

## Memory

Typed operations cover exported providers, subjects, scopes, documents, records, and change operations.

- Exact provider and storage scope are preserved in requests and results.
- Committed storage changes do not imply completed indexing or retrieval readiness.
- Read-only search projections do not acquire mutation identity implicitly.

## Connectivity and Schedules

Typed operations cover exported Application accounts, targets, connector/provider resources, Connections, authorization flows, checks, and schedules.

- Authorization completion is distinct from Connection readiness and a successful check.
- Scheduled intent is distinct from acceptance of a particular Run.
- Run acceptance is distinct from successful external delivery.
- Provider-native protocols and background polling engines are not synthesized by the SDK.

## Configuration Assistant

The dedicated configuration surface preserves readiness, authoring Sessions and Threads, drafts, and explicit application of a draft.

- Its Run retains the Service's frozen configuration provenance.
- A null `agent_revision_id` is not replaced with a fabricated ordinary AgentRevision.
- Conversation progress does not implicitly apply a draft to a business Agent.
- Applying a draft remains a separately authorized command with its own outcome.

## Lifecycle and Observability

Typed operations expose exported lifecycle events, Hook subscriptions and deliveries, usage, and trace projections.

- Durable lifecycle facts, Hook delivery attempts, and best-effort telemetry are different evidence.
- A trace or notification does not prove a durable Run transition.
- Available usage observations do not imply complete settlement or billing.
- Stream and collection ordering are owned by [Observation and Data Access](03-observation-and-data-access.md#distinct-observation-surfaces).

## Export Boundary

The pinned protocol defines which operations exist. A conceptual resource role does not authorize the SDK to invent an endpoint.

- Session navigation can use exported Thread and label operations without claiming a single-Session read.
- Item collection access does not imply a generic single-Item endpoint.
- Run fork does not imply a separate Session-fork command.
- Worker internals, operator storage access, and provider-native execution controls remain outside the SDK.

## Invariants

1. Every declared Native management operation has a discoverable typed resource path and retained low-level binding.
2. A Workspace collection preserves each result's actual ownership.
3. Discovery, installation, authorization, readiness, execution, and delivery are not collapsed into one success flag.
4. Immutable content and revisions retain their immutable contract.
5. Environment and configuration choices retain the lifetime at which Service fixes them.
6. Missing public operations are not replaced with different domain effects.
