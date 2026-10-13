# Interaction and Control

## Inputs and Submission

The primary Agent workflow is one finite `Interaction`. `Agent.start(input, *, idempotency_key=None, agent_revision_id=UNSET, session_id=UNSET, delivery=UNSET, options=UNSET, environments=UNSET, memories=UNSET, mcp_headers=UNSET, message_history=UNSET)` creates a Thread and first Message. `Agent.send(thread_id, input, *, idempotency_key=None, agent_revision_id=UNSET, delivery=UNSET, options=UNSET)` continues an explicitly selected Thread as that Agent. No helper infers a current Workspace, Session, Thread or Agent.

`input` is a string or ordered sequence of strings and public `TextPart(text)`, `JsonPart(value)`, `UrlPart(url)` and `AssetPart(asset_id)` values. Constructors own the required discriminators. Common workflow callers do not need generated models. Generated `MessagePayload` remains available for low-level resources, not an alternate authored input shape.

`options` is public `RunOptions(configuration=UNSET, overrides=UNSET, labels=UNSET, max_usage=UNSET)`. Public `MountCreate` and `MemoryMount` represent initial mounts, `mcp_headers` is a native mapping, and all existing submission selectors remain available. No alias duplicates configuration at the top level.

`message_history` is a list of native Pydantic AI model-message JSON objects for a new Thread only. The SDK forwards every object's fields without filtering or Service-policy validation. The Service validates completed text and closed tool exchanges and enforces the 256-message/262144-byte limits. Omission differs from an explicit empty list. Readback preserves native metadata and nested object insertion order, including tool arguments and results; subsequent send, resume and fork do not re-seed history. The SDK adds no Pydantic AI dependency or parallel model-message hierarchy.

An omitted idempotency key generates one random key before dispatch, exposed as `Interaction.idempotency_key`. Explicit keys remain unchanged. No mutation is automatically replayed. Durable or cancellation-safe callers persist their own key and identical logical body before sending; a generated key is not recoverable from a cancelled coroutine that never returns. [Protocol and Compatibility](05-protocol-and-compatibility.md#preconditions-and-cancellation) owns error and unknown-outcome behavior.

Generated resources use the same transport and retain complete wire models, omission/null fidelity and actual HTTP evidence. Their Submitted-shaped commands return pure `Result[wire.Submitted]` and never bind a workflow or poll.

## Native Run Configuration

`RunConfiguration(allowed_hosts=UNSET, extensions=UNSET)` and `AgentOverride` adapt to the canonical generated Run options. Every existing override is selectable: client_tools, connection_tools, instructions, lazy_environment, media_understanding, model, model_characteristics, model_settings, output_spec, plugins, retries, reviewer, skill_sync, skills, subagents and toolsets. Nested schema objects use native JSON mappings rather than a second generated hierarchy. `UsageLimit(requests)` retains the current usage selection.

`UNSET`, permitted `None` and empty containers stay distinct; no defaults are inserted. An explicit configuration object selects a complete snapshot, including `{}`. `allowed_hosts=None` permits unrestricted native URL access; `allowed_hosts=[]` denies it. Arbitrary namespaced extensions preserve all JSON values, including false, zero, empty arrays/objects and null. The Service normalizes and freezes the accepted snapshot.

The [pinned Run semantics](../contract/semantics/runs.md#run-configuration) own steering, pending edits, next-Run selection and inheritance. Steering and pending edits against an active Run may omit configuration or supply the equal frozen value; a different explicit snapshot raises `run_configuration_immutable`. Next-Run input selects its own snapshot; resume input and inline children inherit the accepted one. The SDK neither compares snapshots nor implements network/media policy.

## Incorporation and Exact Outcomes

A submitted Interaction has validated Thread and Entry handles and an actual `.receipt`; `run` stays `None` until exact Entry consumption. A receipt's provisional Run does not establish incorporation. The observer waits until the Entry is consumed, failed or withdrawn. A failed or withdrawn Entry raises `SubmissionError(thread_id, entry_id, entry)` even if an assignment exists. Assigned may revert to pending. On consumed, `assigned_run_id` binds the exact Run; missing or mismatched identities are protocol errors. No current/latest pointer, auto-resume or successor following is used.

`Interaction.result(timeout=None, poll_interval=None)` works without a context and never opens SSE. The default observation budget is 300 seconds with 0.5-second polling; supplied limits must be finite and positive. First observation fixes one deadline spanning Entry polling, exact Run polling and in-flight SSE/readback. Repeated result/iteration shares the observer and never extends that deadline. Local timeout or cancellation stops observation, not remote execution.

`RunOutcome` exposes `.run`, `.run_id`, `.thread_id`, `.status`, full JSON `.output`, string-only `.text`, public `.pending` and `.failure`. Empty string, false, zero, null and empty containers remain values. `PendingRequest.arguments` and optional presentation are native JSON mappings; approval and call categories remain distinct. `.evidence: Result[RunView]` explicitly retains HTTP metadata and the canonical response. Final text never comes from Items, which are a separate bounded display read.

Completed, failed, cancelled and waiting are observed sealed states, not implicit business success or SDK exceptions. `Run.observe(timeout=300, poll_interval=0.5)` locally constructs the same Interaction for one exact Run; its Thread is resolved by authoritative readback without fabricating an Entry or receipt. `Run.result(...)` delegates to that observer for result-only use. There is no authored Run.wait alias or separate polling kernel.

## Identity Recovery

`Thread.interaction(entry_id, *, idempotency_key=None, timeout=300, poll_interval=0.5)` constructs an Interaction without I/O from saved Thread/Entry IDs. Its receipt is absent; it uses the same consumed-only incorporation, exact Run observer and finite cleanup. Fresh recovery starts a new explicitly bounded local observation, not a mutation or an implicit retry.

`Interaction.provenance` distinguishes submitted Entry, recovered Entry, resumed Run and exact Run selection. Original response evidence is present only when actually received. A resumed or exact-selected Interaction has no fabricated Entry. Reference construction is not proof that a resource exists.

## Finite Observation

`async with interaction` establishes authoritative Run binding before exposing frames. Iteration is optional and uses one pending read on the existing Thread SSE parser. It filters foreign Runs and Thread-only changed signals; delta, boundary, gap and reset for the bound Run remain provisional. Exact Run readback terminates even an idle socket. EOF, retry, a child lifecycle or nested RUN_FINISHED does not seal an Interaction. [Observation](03-observation-and-data-access.md#text-preview) owns the text-preview projection and its limits.

The context is single-use and one reader is active at a time. Normal completion caches the outcome. Context exit or `aclose()` cancels and joins owned reads and observation; without an outcome, result does not silently restart. Breaking a loop alone does not leave the context. Explicit saved identity recovery or Run observation creates a new lifetime. Cleanup sends no remote interrupt, withdrawal or compensating command.

## Control and Successors

`ThreadView.last_run_id` names the most recently sealed Run of any outcome. Its nearest checkpoint supplies history for the next explicit message. Failed/cancelled Runs pause automatic inbox advancement, not explicit Agent.send. Waiting requires explicit resume of the exact idle last Run with all answers. Service alone owns scheduling and admission.

| Helper                                                                                                                                                                            | Result and boundary                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| `await run.interrupt()`                                                                                                                                                           | Native `Result[RunView]`; explicit exact Run command        |
| `await run.resume({id: Approve() or Deny() or Returned(value) or Failed(message)}, input=UNSET, idempotency_key=None)`                                                            | Interaction bound to a distinct authoritative successor Run |
| `await run.fork(input, agent_id=..., options=UNSET, agent_revision_id=UNSET, delivery=UNSET, environments=UNSET, memories=UNSET, fresh_environments=UNSET, idempotency_key=None)` | Interaction for a new Thread and Entry                      |

Resume splits one public answer mapping into both wire maps in one mutation, including empty categories. Service validates exact atomic coverage and matching categories. Returned requires an explicit JSON value; null is a value, not omission. Deny preserves omitted, null and empty reasons. Built-in questions are calls whose returned JSON conforms to Harness UserQuestionAnswers. Optional input uses ordinary public parts in the same mutation; omission leaves the wire field absent, `None` supplies explicit null, and parts supply an ordinary MessagePayload. Input does not fill missing answers or grant approval. No client tool or approval is executed automatically.

The application owns answer drafts, edits and complete-batch submission. Service requires 1–128 combined answers and a canonical body within 262144 bytes; pending-coverage or question-validation failures are known `ApiError` rejections and create no successor. Identical explicit replay under the same key returns the same successor; a changed body conflicts. The SDK sends each invocation once.

The resume receipt identifies a distinct Run with Thread/Workspace identity. Its returned Interaction reuses finite result/raw/text observation, retains the response and key, and never follows later successors. Fork uses the current native wire operation, changes no scheduling semantics and does not implicitly create a Session. Interrupt acceptance is not proof of rolled-back external effects.

## Invariants

1. Submitted Entry identity and provisional Run evidence never substitute for consumption.
2. Exact observation never follows pointers or successors.
3. Output and business completion remain distinct from bounded display and transport delivery.
4. One local observer owns one fixed deadline and joined cleanup.
5. Timeout, cancellation and close send no remote mutation.
6. Human decisions, external side effects, application checkpoints and complete-batch validation retain their existing owners.
