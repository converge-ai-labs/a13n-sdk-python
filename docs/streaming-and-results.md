# Streaming and results

Use `await interaction.result()` for background jobs and request/response applications. Add iteration when a person benefits from seeing progress. Both paths observe the same submission and return the same kind of outcome; you do not need a separate streaming API to start the Agent.

These examples take an open `Client` from the [quick start](../README.md#quick-start).

## Read a finished response

A successful HTTP submission does not mean execution succeeded. Check the outcome, then read the saved response:

```python
from a13n import RunOutcome
from a13n.generated import models as wire


async def display_outcome(outcome: RunOutcome) -> None:
    if outcome.status == wire.RunStatus.COMPLETED:
        saved = await outcome.run.items.get()
        for item in saved.value.items:
            content = item.content.to_dict()
            if item.kind == "text_message" and content.get("role") == "assistant":
                print(content.get("text", "[message content omitted]"))
        if not saved.value.complete or saved.value.dropped:
            print("This view does not contain every Item.")
    elif outcome.status == wire.RunStatus.WAITING:
        print("Input needed:", outcome.pending.to_dict() if outcome.pending else None)
    elif outcome.status == wire.RunStatus.FAILED:
        print("Execution failed:", outcome.failure.to_dict() if outcome.failure else None)
    else:
        print("Execution cancelled.")
```

Call `await display_outcome(await interaction.result())` inside your async application. A `waiting` outcome needs [an explicit response](waiting-and-tools.md), not another wait on the same Run.

### Messages and structured output are different

`outcome.run.items.get()` returns saved messages and tool activity. `outcome.output` is the Run's output value; it may contain structured output or be `None` even when an ordinary assistant message exists. Do not use `output` as a universal chat-text field.

Items are also a bounded display, not an unlimited archive. Check `complete`, `dropped`, and each content object's omission or truncation flags if your application promises a complete transcript. The SDK cannot reconstruct omitted content from progress events.

## Add a live text preview

This function prints text deltas while the Agent works, then prints the saved result. It deliberately distinguishes the preview from the saved response instead of concatenating both into one supposedly complete transcript:

```python
from uuid import uuid4

from a13n import Client, RunOutcome


async def stream_answer(client: Client, agent_id: str, prompt: str) -> RunOutcome:
    interaction = await client.agents(agent_id).start(prompt, idempotency_key=uuid4().hex)
    async with interaction:
        async for frame in interaction:
            if frame.event_type == "delta":
                event = frame.data["event"]
                if event["type"] == "TEXT_MESSAGE_CONTENT":
                    print(event["delta"], end="", flush=True)
            elif frame.event_type in {"gap", "reset"}:
                print("\n[Preview interrupted; the saved response will follow.]")
        outcome = await interaction.result()

    print("\nSaved result:", outcome.status)
    saved = await outcome.run.items.get()
    print(saved.value.to_dict())
    return outcome
```

The loop ends when this execution completes, fails, is cancelled, or pauses for input. It does not wait forever for the underlying connection to close. An execution can finish before you receive any deltas; the result and saved Items still tell you what happened.

Not every frame is a text token. Tool activity, boundaries, and recovery signals also travel through the stream. In a UI, maintain a provisional preview while streaming and replace it from saved Items at the end. If a `gap` or `reset` arrives, discard assumptions about contiguous deltas; refresh the saved view or mark the preview incomplete until you do.

## Own the observation lifetime

Keep iteration inside `async with interaction`. The context closes its local reader on normal completion, exceptions, or an early `break`. An Interaction has one reader and one observation lifetime; it is not a broadcast channel for several UI consumers.

`result()` is also useful without iteration. It does not open SSE, and a successfully obtained outcome is cached. After normal stream completion, you can still read that outcome. Closing before an outcome is available is different: the closed Interaction will not silently start another observation.

There are two distinct operations:

| Intention                                | Operation                                                           |
| ---------------------------------------- | ------------------------------------------------------------------- |
| Stop displaying progress                 | Leave the Interaction context or call `await interaction.aclose()`. |
| Ask the Service to stop remote execution | Call `await client.runs(run_id).interrupt()` for the exact Run.     |

Cancelling your Python task also does **not** imply remote cancellation. Save the Thread and Entry IDs when a submission returns so another request or process can [recover its exact execution](errors-and-recovery.md#recover-a-queued-or-interrupted-observation).

## Bound how long you wait

For result-only code, set the observation budget on the first call:

```python
from a13n import Interaction, RunOutcome


async def wait_one_minute(interaction: Interaction) -> RunOutcome:
    return await interaction.result(timeout=60, poll_interval=0.5)
```

The default budget is 300 seconds, including time queued before execution. Repeated calls share the first observer's deadline; they do not extend it. Entering the streaming context starts the default observation. Use an outer `asyncio.timeout(...)` if your entire streaming task needs a shorter application deadline.

The Client's `timeout` setting is separate: it limits an ordinary HTTP request and defaults to 30 seconds. Neither limit is a remote execution deadline. Handle a timeout as [an observation or transport problem](errors-and-recovery.md), not evidence that the Agent stopped.

## When you need Thread-wide events

Most applications should stay with Interaction. Advanced consumers can use the generated `client.resources.threads(thread_id).stream.get_stream()` for the raw SSE response, or `ThreadStream` for protocol parsing and reconnect handling. That stream covers the Thread rather than one submitted message and requires explicit event/run and cursor handling. It is not a second high-level conversation mode.

See the [streaming contract](../spec/README.md) before building a protocol-level consumer.

[Back to the guide](README.md) · [Next: waiting and tools](waiting-and-tools.md)
