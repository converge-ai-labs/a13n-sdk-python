# Errors and recovery

A reliable integration distinguishes three questions: did the Service accept my message, did execution finish, and did my application observe the result? A connection failure or timeout may leave the first or third question unanswered. It does not prove that the Agent failed.

The examples below take an open `Client` from the [quick start](../README.md#quick-start).

## Handle Service rejections separately from execution failures

A rejected request raises `ApiError`. A Run that was accepted and later failed returns a `failed` outcome. Keep these paths separate:

```python
from uuid import uuid4

from a13n import ApiError, Client


async def review_with_diagnostics(client: Client, agent_id: str, prompt: str) -> None:
    try:
        interaction = await client.agents(agent_id).start(prompt, idempotency_key=uuid4().hex)
        outcome = await interaction.result()
    except ApiError as error:
        print("Request rejected:", error.status, error.code, error.request_id)
        raise

    if outcome.status == "failed":
        print("Run failed:", outcome.run.id)
        print(outcome.failure.message if outcome.failure else "No failure detail")
    elif outcome.status == "waiting":
        print("Run needs input:", outcome.run.id)
    else:
        print("Run status:", outcome.status)
```

Branch on `status` and `code`, not on the human-readable message. Preserve `request_id` when reporting a Service problem. Avoid logging credentials or entire prompts and responses as part of a generic exception handler.

| Failure                  | Meaning and next step                                                                                 |
| ------------------------ | ----------------------------------------------------------------------------------------------------- |
| `ApiError`               | The Service rejected a request. Inspect status, code, details, and any retry information.             |
| `SubmissionError`        | The submitted inbox Entry settled without incorporation into a Run. Inspect its saved `entry`.        |
| `UnknownOutcomeError`    | A dispatched authored mutation lacks a trustworthy acknowledgement; retain its key and reconcile.     |
| `PreviewInterrupted`     | Provisional text projection stopped; authoritative result and sequential raw access remain available. |
| `TransportError`         | Local transport failed. A write may already have reached the Service. Reconcile before another write. |
| `ProtocolError`          | A response does not meet the SDK's expected protocol. Check the deployment and pinned contract.       |
| `TimeoutError`           | The local observation budget expired. Recover from saved identities.                                  |
| `asyncio.CancelledError` | Your application cancelled its task. Propagate cancellation after local cleanup.                      |

For `401`/`403`, fix credentials, session proof, or permissions rather than retrying unchanged. For `412`, reread and reconcile the conflicting version. For a rate or capacity rejection, respect the Service's retry information and your application's retry policy; the SDK does not automatically replay mutations.

## Save the receipt before waiting

Once submission succeeds, record the IDs your application needs to recover. This function separates submission from observation so the caller can persist a small record first:

```python
from a13n import Client, Interaction


async def submit_for_later(
    client: Client, agent_id: str, prompt: str, request_key: str
) -> tuple[Interaction, dict[str, str]]:
    interaction = await client.agents(agent_id).start(prompt, idempotency_key=request_key)
    record = {
        "agent_id": agent_id,
        "thread_id": interaction.thread.id,
        "entry_id": interaction.entry.id,
        "request_key": request_key,
    }
    return interaction, record
```

Generate and persist `request_key` with your application job **before** calling this helper. After it returns, persist the returned IDs, then call `await interaction.result()`. Persist the original message and options as appropriate for your application's data policy; the key alone is not enough to reconstruct an identical retry.

The initial `.receipt` may contain a provisional Run, but `interaction.run` remains `None` until its Entry is consumed. The Entry ID remains useful in both cases. Do not assume that a Thread's newest Run belongs to your message.

## Recover a queued or interrupted observation

Construct an Interaction from saved IDs without a network request or fabricated receipt. It applies the same consumed-only binding and one deadline as normal submission:

```python
from a13n import Client, RunOutcome


async def recover_submission(client: Client, thread_id: str, entry_id: str) -> RunOutcome:
    recovered = client.threads(thread_id).interaction(entry_id, timeout=300)
    return await recovered.result()
```

`recovered.receipt` is `None`; `.thread` and `.entry` select saved identities. Both result-only and `async with recovered` streaming use the ordinary finite Interaction. A failed/withdrawn Entry raises `SubmissionError`, not an observed Run failure.

An assigned Run can change before the Entry is consumed. Waiting only for a non-null `assigned_run_id`, or following the newest Run on the Thread, can give you another execution's result. Keep the `consumed` check.

If you already saved the final exact Run ID, `await client.runs(run_id).result()` is enough. Use `client.runs(run_id).observe(timeout=300)` when you also want raw or text-preview iteration. Exact Run selection never follows successors. If a waiting Run was resumed, use the returned **successor Interaction**; the previous Run does not become the successor.

## Retry a submission with an unknown outcome

`UnknownOutcomeError` identifies an attempted dispatch without trustworthy acknowledgement, including a malformed accepted receipt. It exposes `idempotency_key`, safe `operation`, known `thread_id`/`run_id`, optional HTTP `evidence`, and the original chained cause. Known Service rejection stays `ApiError`; local pre-dispatch validation and closed-client failures are not unknown outcomes. Native cancellation propagates unchanged.

If the connection fails before a receipt arrives, the Service may still have accepted the write. A new idempotency key would describe a new operation and can duplicate the conversation or message.

Keep one stable key and payload for the original logical operation:

1. Before submission, save the Agent selection, message, options, and key in your application job record.
2. If a receipt arrives, save its Thread and Entry IDs and recover by those identities.
3. If the outcome remains unknown, reconcile the same submission using the **same key and unchanged payload**, according to the Service's idempotency rules.
4. Use a new key only for an intentionally new operation.

A key omitted on start/send/resume/fork is generated once before dispatch; no mutation is automatically retried. A generated key cannot be recovered from a cancelled coroutine that never returns. Persist a caller-selected key and identical logical body first for durable/cancellation-safe work. `A13nError` is the common SDK category; `TimeoutError` and `asyncio.CancelledError` retain their native Python meanings.

Do not turn this into an unbounded automatic retry loop. Some operations do not accept an idempotency key; inspect their responses or resource state instead of assuming they can be replayed safely. For a client tool that changes application data, also reconcile the tool's own side effect before [resuming](waiting-and-tools.md).

## Stop waiting versus stop working

An Interaction's timeout, context exit, or task cancellation closes local observation; none sends a remote interrupt. To deliberately stop a known execution, call `await client.runs(run_id).interrupt()` and inspect the returned state. A queued Entry is not necessarily an executing Run; use its inbox state to decide the appropriate control operation rather than interrupting an unrelated current Run.

After local observation closes before producing an outcome, do not call `result()` repeatedly expecting a fresh observer. Use the saved Entry or Run recovery path above.

## Verify against your own development Service

The repository includes opt-in acceptance scripts for a **disposable HTTPS Service**. They create resources and must not target production:

| Script                          | Coverage                                                                       |
| ------------------------------- | ------------------------------------------------------------------------------ |
| `scripts/service-smoke.py`      | Message interaction, streaming, and file transfer.                             |
| `scripts/service_acceptance.py` | Queued messages, Run controls, ordinal windows, failed/cancelled continuation. |
| `scripts/memory_acceptance.py`  | Memory files and provider-backed records.                                      |

Set `A13N_SERVICE_URL`, `A13N_API_TOKEN`, `A13N_AGENT`, and `A13N_CA_BUNDLE`. Control checks also need `A13N_CLIENT_TOOL_AGENT` and `A13N_FAILURE_PROMPT`. The failure prompt must select a disposable model fixture that fails only for that latest input, so a normal follow-up can succeed; it is not a Service API feature. Missing configuration fails explicitly rather than skipping that scenario. Memory checks need `A13N_MEMORY_PROVIDER` for a configured `mem0_oss` provider. These scripts do not provision the Service, models, or credentials.

See [Contributing](../CONTRIBUTING.md) for local checks. Passing local tests does not establish compatibility with every deployment or model provider; use the [pinned contract](../contract/source.json) when diagnosing version differences.

[Back to the guide](README.md)
