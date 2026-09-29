# Interaction and Control

## Inputs and Submission

The primary Agent workflow is a finite `Interaction`. `Agent.start(input, *, idempotency_key, agent_revision_id=UNSET, session_id=UNSET, delivery=UNSET, options=UNSET, environments=UNSET, memories=UNSET, mcp_headers=UNSET, message_history=UNSET)` creates a Thread and first Message. `Agent.send(thread_id, input, *, idempotency_key, agent_revision_id=UNSET, delivery=UNSET, options=UNSET)` continues that Thread using the selected Agent; a Thread never infers an Agent from its latest Run. The typed keyword arguments expose every relevant `NewThread`/`Message` option; `input` is plain text or generated `MessagePayload`, and `text_input()` constructs a text part. `UNSET` preserves omission while permitted `None` sends explicit null. No helper invents a current Workspace, Session, Thread or idempotency key.

```python
agent = client.agents(agent_id)
interaction = await agent.start("Review a change", idempotency_key="review-001")
outcome = await interaction.result()  # No SSE connection.
follow_up = await agent.send(interaction.thread.id, "Explain", idempotency_key="review-002")
async with follow_up:
    async for frame in follow_up:
        if frame.event_type == "gap":
            await client.runs(frame.data["run_id"]).items.get()
    next_outcome = await follow_up.result()
```

`message_history` accepts a list of native Pydantic AI model-message JSON objects for a new Thread only. The SDK forwards every object's fields without filtering or applying Service validation; the Service validates completed text and closed tool exchanges and enforces the 256-message/262144-byte limits. Omission differs from an explicit empty list. Thread readback retains the submitted JSON, including native metadata; subsequent `send`, resume and fork do not re-seed it. The SDK adds no Pydantic AI dependency or parallel model-message hierarchy.

Advanced `client.resources.threads.create(body=wire.NewThread(...), idempotency_key=...)` and `client.resources.threads(thread_id).inbox_entries.create(body=wire.Message(...), idempotency_key=...)` expose complete generated bodies and return **pure** `Result[wire.Submitted]`. Entry edits/withdrawals and Run fork using the Service Submitted shape also remain pure generated results. Only the authored Agent workflow binds `Submitted(thread, entry, run | None, receipt: Result[wire.Submitted])`, with validated references and HTTP evidence. `Run.fork(...)` in the authored layer binds its declared successor receipt. An immediately accepted Run does not prove Entry incorporation. A queued Entry is not a Run. No SDK mutation is retried invisibly.

## Incorporation and Exact Outcomes

`Interaction.result(timeout=300, poll_interval=0.5)` works without entering a context. It waits for the Entry to settle as **consumed**, **failed**, or **withdrawn**. A failed or withdrawn Entry raises typed `SubmissionError(thread_id, entry_id, entry)` with a safe summary; the snapshot remains available. Assigned is not settled: the Entry may return to pending before another Run incorporates it. On consumed, the SDK reads `assigned_run_id` and polls that exact Run until sealed, rejecting identity mismatch even if another Run belongs to the same Thread. It does not use current/head/latest Thread pointers, auto-resume a waiting Run or follow a successor.

One deadline bounds Entry polling, Run polling and in-flight reads. Both limits must be finite positive numbers. The authored `Submitted.wait()` owned by an Interaction uses the same incorporation logic; pure generated resources never wait or poll. `Run.wait(timeout=300, poll_interval=0.5)` observes just its own ID and returns a `RunOutcome` on `completed`, `failed`, `cancelled`, or `waiting`. `RunOutcome` is an immutable view of the authoritative response with `.run`, `.snapshot: Result[RunView]`, `.status`, `.output`, `.pending`, `.failure`. A failed or waiting Run is an observed state, not an SDK exception or business success. `run.items.get()` reads committed display separately. Timeouts and cancellation do not interrupt remote execution.

## Finite Observation

`async with interaction` establishes Entry incorporation before exposing any Run-scoped SSE frame. Iteration is optional; a result-only call does not open SSE. The context owns one exact Run observer and one pending read on the existing Thread SSE parser. It filters foreign Runs and Thread-only `changed` signals; `delta`, `boundary`, `gap` and `reset` for its incorporating Run are typed and remain provisional. It finishes when exact Run readback seals even if the SSE socket stays idle. A connection closing, retrying, or reaching EOF does not by itself establish Run completion. Retention/current-Run filtering and gaps may prevent full replay; no lossless transcript or automatic display reducer is promised.

The context is single-use. Normal finite completion caches its outcome; `result()` can be read again without a new request. On early context exit, stream and polling tasks are cancelled/awaited and local state is released; if no outcome was observed, `result()` does not silently restart. The application may explicitly use the saved Run/Entry handles for readback or issue a separate exact Run wait. Exiting/cancelling does not send a remote interrupt, withdraw intent, or undo external effects.

## Control and Successors

| Helper                                                                                            | Request and result                            | Boundary                                                       |
| ------------------------------------------------------------------------------------------------- | --------------------------------------------- | -------------------------------------------------------------- |
| `await run.interrupt()`                                                                           | `Result[RunView]` via declared interrupt      | Exact Run; no implicit stream close                            |
| `await run.resume(approvals={id: wire.Approve(...)}, calls={}, idempotency_key=key, input=UNSET)` | `Resumed(run: Run, receipt: Result[RunView])` | Complete wait batch, optional atomic input; distinct successor |
| `await run.fork(body=wire.Fork(...), idempotency_key=key)`                                        | `Submitted`                                   | New Thread and Entry, optionally accepted Run                  |

`Pending.approvals` and `Pending.calls` have distinct ID sets. Both maps are mandatory even if empty, and the provided IDs must exactly cover their respective pending requests; the Service rejects missing, extra and category-mismatched results atomically. Approval values are generated `Approve`/`Deny`, call values `Returned`/`Failed`; a built-in question is a call whose returned JSON conforms to Harness `UserQuestionAnswers`. The optional `input` is plain text or a generated `MessagePayload` with ordinary parts, passed in the **same** `wire.Resume` request as the complete batch. It does not answer a question or fill missing results. The SDK does not execute client tools, grant approval or reconcile external side effects automatically. Resume and fork preserve caller-supplied idempotency keys and Service authorization without read-and-retry on conflict. Interrupt acceptance is not proof that remote side effects rolled back. A fork does not implicitly create a new Session.

## Invariants

1. A submission always identifies a Thread and Entry; a nullable receipt Run identifies only immediate acceptance.
2. Entry incorporation is immutable and identifies exactly one Run; an assigned Entry alone does not.
3. Every successor reference remains distinct from its source, and exact Run waiting never follows successors.
4. Local timeout, cancellation, stream exit and Client close issue no remote mutation.
5. Application handlers, human decisions, display checkpoints and business completion remain application-owned.
