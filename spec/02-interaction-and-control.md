# Interaction and Control

## Inputs and Submission

`workspace.threads.create(body=wire.NewThread(...), idempotency_key=...)` is the complete new-Thread entry point. `thread.inbox_entries.create(body=wire.Message(...), idempotency_key=...)` submits a complete Message. Both return the same bound `Submitted` used by the shortcuts below; all NewThread fields, including memories, environments, MCP headers, and explicit null/omission, stay available without reconstructing references manually. Generated operations returning the Service `Submitted` shape (including Entry edits/withdrawal and Run fork) use this same result. Low-level generated HTTP operations retain the raw wire response.

`Workspace.start(input, *, agent_id, idempotency_key, ...)` creates a Thread and submits its initial inbox Message. `Thread.submit(input, *, agent_id, idempotency_key, ...)` submits to an existing Thread. `input` is a string or generated `MessagePayload`; `text_input` constructs one ordinary `TextPart`. Agent revision, delivery, and Run options remain explicit typed inputs. `UNSET` preserves omission; `None` is explicit null where the schema permits it. No helper infers a current Agent, Thread, Workspace, or Session.

```python
submitted = await client.workspaces(workspace_id).start("Review a change", agent_id=agent_id, idempotency_key=key)
if submitted.run is not None:
    sealed = await submitted.run.wait(timeout=60, poll_interval=0.25)
else:
    entry = await submitted.entry.wait(timeout=60, poll_interval=0.25)
    if entry.value.assigned_run_id is not None:
        run = client.workspaces(workspace_id).runs(entry.value.assigned_run_id)
```

Submission operations return immutable `Submitted(thread: Thread, entry: InboxEntry, run: Run | None, receipt: Result[wire.Submitted])`. The Run is present only when Service accepted it immediately. The full receipt preserves wire status and HTTP evidence; resource references are locally bound only after validating reported identities. A queued Entry is not a Run. No hidden read, queue consumption, execution loop, or automatic mutation retry occurs.

A Thread's inbox has explicit generated operations for listing, reading, editing, withdrawing, and ordering Entry intent where exported. `InboxEntry.wait(timeout=..., poll_interval=...)` performs fresh reads until `consumed`, `failed`, or `withdrawn`. A consumed Entry's `assigned_run_id` identifies its accepted Run; neither waiting nor reordering fabricates one. Native inbox and Thread semantics in the pinned contract own its ordering, delivery, and concurrency rules; the SDK does not impose the old queue-version protocol.

## Exact Run Reads and Waiting

`Run.wait(timeout, poll_interval)` polls one exact Workspace Run; both arguments must be finite and positive, and the entire operation is bounded by `timeout`. It returns `Result[RunView]` on `completed`, `failed`, `cancelled`, or `waiting`. A failed or waiting Run is a successful read of state, not an SDK exception or business success. A timeout or local cancellation does not interrupt remote execution.

`run.items.get()` reads the retained Item snapshot. `run.attempts`, `run.lineage`, and other generated children expose only declared operations; they do not turn a RunAttempt into a new application Run. Run and Item readback remain authoritative for retained state; Thread SSE is provisional observation.

## Control and Successors

| Helper                                                           | Request and result                                   | Boundary                                                               |
| ---------------------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------------------------- |
| `await run.interrupt()`                                          | `Result[RunView]` via the declared interrupt command | Targets this Run; no local stream closure is implied                   |
| `await run.resume(wire.ResumeRequest(...), idempotency_key=key)` | `Resumed(run: Run, receipt: Result[RunView])`        | Eligible waiting Run yields a new Run; source reference is unchanged   |
| `await run.fork(body=wire.Fork(...), idempotency_key=key)`       | `Submitted`                                          | Creates an independent Thread and first Entry, optionally accepted Run |

The generated model defines complete resume answers (`Approve`, `Reject`, or `Complete`); the SDK does not automatically execute client tools or approve pending work. The application reads `RunView.pending`, constructs all required answers, and reconciles its own external side effects. Resume and fork preserve caller-supplied idempotency keys and Service authorization, never read-and-retry on conflict. Interrupt acceptance is not proof every remote process stopped or side effects rolled back.

Do not substitute removed older commands (`steer`, `cancel` with dual versions, `retry`, `continue_from`, `feedback`) for this protocol. A Thread `Message` is an inbox entry under Native ordering; it is not an old queued-submission receipt. The SDK does not invent a Session fork, a generic continuation endpoint, or an Agent-bound `start` shortcut.

## Invariants

1. A submission always identifies its Thread and Entry; an optional Run identifies only immediate Run acceptance.
2. Entry waiting and Run waiting read their bound identities and perform no mutation.
3. Every successor reference remains distinct from its source. Fork does not implicitly create a new Session.
4. Local timeout, cancellation, stream exit, and Client close do not perform remote interrupt or rollback.
5. Application handlers, approval decisions, and business completion remain application-owned.
