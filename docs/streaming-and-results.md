# Streaming and results

Use `await interaction.result()` for background jobs and request/response applications. Add iteration when a person benefits from seeing progress. Both paths observe the same submission and return the same kind of outcome; you do not need a separate streaming API to start the Agent.

These examples take an open `Client` from the [quick start](../README.md#quick-start).

## Read a finished response

A successful HTTP submission does not mean execution succeeded. Check the outcome and read authoritative output directly, with no additional Items request:

```python
from a13n import RunOutcome


def display_outcome(outcome: RunOutcome) -> None:
    if outcome.status == "completed":
        print(outcome.text if outcome.text is not None else outcome.output)
    elif outcome.status == "waiting":
        print("Input needed:", outcome.pending)
    elif outcome.status == "failed":
        print("Execution failed:", outcome.failure)
    else:
        print("Execution cancelled.")
```

Call `display_outcome(await interaction.result())` inside your async application. A `waiting` outcome needs [an explicit response](waiting-and-tools.md), not another wait on the same Run.

### Messages and structured output are different

`outcome.output` is the full Run output, preserving JSON null, false, zero, empty containers and structured values. `outcome.text` returns it only if it is a string, including an empty string. It never scans Items or coerces structured JSON into chat text. `.run`, `.run_id`, `.thread_id`, `.pending` and `.failure` are direct workflow values; `.evidence` explicitly retains HTTP status, headers, request ID and the native response.

**Advanced display readback:** `outcome.run.items.get()` separately returns saved messages and tool activity. A Run can have null output even when display activity exists; no final output is fabricated from it.

Items are a windowed display, not an unlimited archive. `complete` means the Run is sealed, **not** that the response includes all history. Every Item has a dense 1-based `ordinal`. A default `run.items.get(limit=200)` returns the newest limit plus the entire mutable tail, so it can return more than the requested limit. Check content omission/truncation flags separately; the SDK cannot reconstruct omitted content from progress events.

To read earlier Items, explicitly request `run.items.get(before=first_ordinal, limit=200)`; to read forward, use `after=last_ordinal`. Bounds are exclusive, `before` >= 1, `after` >= 0, and the Service accepts at most 500 as the limit. Do not combine before and after. Each call makes one request; there is no automatic all-history loader. Historical windows have `baseline=False` and null `continuation`, `position`, and `resume_after`, even for a sealed Run. Keep them separate from live recovery coverage.

Only a default read has `baseline=True`: it carries the shared normalization continuation and nullable committed coverage. Generated `DisplayContinuation`, `FragmentState`, `ObserverContinuation`, and `StreamPosition` represent that schema faithfully; they are parser continuation, not execution state. A UI that continues folding needs this state rather than inferring it from Items. The SDK provides no display reducer.

## Add a live text preview

This function prints text deltas while the Agent works, then prints the saved result. It deliberately distinguishes the preview from the saved response instead of concatenating both into one supposedly complete transcript:

```python
from a13n import Client, PreviewInterrupted, RunOutcome


async def stream_answer(client: Client, agent_id: str, prompt: str) -> RunOutcome:
    interaction = await client.agents(agent_id).start(prompt)
    async with interaction:
        try:
            async for chunk in interaction.text_stream():
                print(chunk, end="", flush=True)
        except PreviewInterrupted as error:
            print("Preview stopped:", error.reason)
        outcome = await interaction.result()

    print("Final output:", outcome.output)
    return outcome
```

The loop ends when this execution completes, fails, is cancelled, or pauses for input. It does not wait forever for the underlying connection to close. An execution can finish before you receive any deltas; the result and saved Items still tell you what happened.

`text_stream()` lazily projects the existing finite reader. It emits root assistant string CONTENT only after a trustworthy START, excludes explicit child attribution and `metadata.display: false`, and tracks at most 128 active identities without buffering a transcript. Gap/reset, discontinuous Service per-attempt sequences, missing or ambiguous START, duplicate identity, attempt changes, malformed framing and state exhaustion raise sticky `PreviewInterrupted(reason, run_id)`. The still-open Interaction's outcome observer continues; `result()` remains available, and deliberate sequential raw consumption is allowed after interruption. A second text consumer or concurrent raw/text read is rejected.

The pinned `a13n.stream.fragment` CUSTOM envelope carries slices of an original large CUSTOM event, not standard text-message suffixes. Exact-root fragments conservatively interrupt this preview because it does not assemble their semantics; this is an unsupported-framing limitation, not proof of lost assistant text. Explicit foreign/child/hidden fragments are filtered first. Unknown unframed CUSTOM events are ignored by preview and preserved by raw access. Every exact-Run outer Service sequence is tracked before child/hidden exclusion; after the initial observed coordinate, deltas must remain dense. Late boundaries at or below the received high-water mark are notifications, not resets; a boundary ahead of it interrupts preview. Nested event/source coordinates and foreign Runs do not affect tracking. No baseline repair occurs.

Native AG-UI 1.0 events use camelCase fields such as `messageId`, `toolCallId`, and `subagentRunId`. Inline-child events share the Service Run envelope but retain child attribution; the root-only text preview above deliberately excludes them. To display children, group content by `(subagentRunId, messageId)` rather than flattening it into root text. A nested lifecycle event never replaces the exact Service Run outcome.

Tool results can contain an ordered list of native text/image/audio/video/document parts rather than a string. Preserve their `source` descriptors and duplicates; provider file handles are not downloadable URLs. `CUSTOM` values, including null and unknown names, and authored/generated input metadata remain native JSON. Respect `metadata.display: false` in your presentation. Saved tool Item content uses `result_parts` for structured content and `result` for a string, with the same bounded attribution; use a media-aware renderer rather than string coercion. The SDK neither reconstructs source history nor downloads media for display.

Not every frame is a text token. Tool activity, boundaries, and recovery signals also travel through the stream. For native progress events, use `async for frame in interaction` instead. In a UI, keep provisional preview separate from authoritative final output and advanced saved display. If a `gap` or `reset` arrives, discard assumptions about contiguous deltas; refresh the saved view or mark the preview incomplete until you do.

## Own the observation lifetime

Keep iteration inside `async with interaction`. Leaving the context closes its local reader on completion, exceptions, or early exit. Breaking a loop alone while remaining inside the context does not release it. If abandoning a paused text iterator, call `await preview.aclose()` before sequential raw consumption; use `finally` or context exit to release the Interaction. An Interaction has one reader and one observation lifetime; it is not a broadcast channel for several UI consumers.

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

Most applications should stay with Interaction. Advanced consumers can use the generated `client.api.threads(thread_id).stream.get_stream()` for the raw SSE response, or `ThreadStream` for protocol parsing and reconnect handling. That stream covers the Thread rather than one submitted message and requires explicit event/run and cursor handling. It is not a second high-level conversation mode.

### Resume from a saved display, not only a cursor

A default `RunItems` baseline has two different coordinates; a historical ordinal window supplies neither:

- `position` (`attempt-sequence`) describes the display's coverage. Send it with its **Run ID** as the paired `run` and `position` stream query parameters.
- Optional `resume_after` is a covered Redis entry ID. Pass it as `after` on `ThreadStream` (or `last_event_id` on generated `get_stream()`). It is only a seeking hint, not display coverage.

With the query pair, the Service uses a retained hint for direct seeking only when it matches the claimed Run and attempt, the active execution, and a covered sequence. Absent, expired or incompatible hints fall back to retained replay filtered by position. Absence alone is not a gap. Covered boundaries remain observable; an older-attempt claim receives `reset`. This is not a general rule that one cursor takes precedence over another: the [pinned stream contract](../contract/semantics/facts-and-delivery.md#the-thread-stream) owns the conditions.

After receiving a `GapFrame`, explicitly close the old observation, read that exact Run's Items and build a **new** stream from the returned baseline. For example, call this helper after leaving the stream context that produced `gap`:

```python
from a13n import Client, GapFrame, ThreadStream


async def observe_new_baseline(client: Client, thread_id: str, gap: GapFrame) -> None:
    saved = (await client.runs(gap.data["run_id"]).items.get()).value
    print("Gap target:", gap.data.get("position"), "Saved coverage:", saved.position)
    print("Replace provisional preview with saved Items:", saved.to_dict())
    if not saved.baseline or saved.complete or saved.position is None:
        return  # Terminal baseline, or no committed coverage to claim yet.
    hint = saved.resume_after if isinstance(saved.resume_after, str) else None
    async with ThreadStream(
        client.api.threads(thread_id),
        run=saved.run.id,
        position=saved.position,
        after=hint,
        reconnect=False,
    ) as stream:
        async for frame in stream:
            print(frame.event_type, frame.data)
            if frame.event_type in {"gap", "reset"}:
                break  # Let the application decide whether and when to read again.
```

A gap may name a missing range through `gap.data.get("position")`, or have no known target. A snapshot may still be behind that range; replacing a preview does **not** prove complete recovery. Keep the preview incomplete until your application can establish coverage, and check saved truncation/omission metadata. The SDK supplies neither a UI reducer nor an implicit readback loop.

`ThreadStream` preserves its original query pair on automatic reconnects. Only requesting the next frame acknowledges the previously yielded cursor-bearing frame in memory for `Last-Event-ID`; it does not update the query position. Serialize application processing before requesting the next frame, and explicitly start a new stream after adopting newer coverage. Fixed original coverage can replay already-applied suffix events on reconnect; neither attachment nor a Redis hint proves exactly-once or lossless delivery.

See the [streaming contract](../spec/03-observation-and-data-access.md) before building a protocol-level consumer. Finite Interaction still binds its exact consumed Run without implicitly claiming a display baseline.

## Read a saved display value

Saved Items may expose `content_refs`, mapping content field names to immutable references with media type, byte size, preview and truncation. Load a value explicitly through the same Client:

```python
from a13n import Client
from a13n.generated import models as wire


async def load_saved_text(client: Client, run_id: str) -> None:
    saved = await client.api.runs(run_id).items.get(limit=1)
    for item in saved.value.items:
        refs = item.content_refs
        if isinstance(refs, wire.ItemContentRefs) and "text" in refs.additional_properties:
            ref = refs.additional_properties["text"]
            content = await client.api.runs(run_id).contents(ref.id).get()
            print(content.value.value, content.value.truncated)
```

Each request returns the whole saved value as `RunContent`, including native JSON false, zero, null or empty containers. Service checks the reference belongs to the Run's committed display and returns `Cache-Control: no-store`; superseded, private or other-Run references are `not_found`, and missing/damaged objects are `unavailable`. The value may itself be truncated. Finite observation and bounded text preview do not fetch references or synthesize expanded history.

Retained Computer screenshots use separate opaque image references (`id`, `media_type`, `size_bytes`), not `RunContent` values or inline base64. Read them through `client.api.runs(run_id).images(image_id).get()` or `.get_stream()`; [execution inspection](resources.md#inspect-execution-retained-images-and-timing) shows the buffered call. The original JPEG/PNG bytes and Content-Type are retained. A read captures no new pixels and fails if the image does not belong to the Run's committed history. Neither the stream nor `text_stream()` automatically downloads images.

[Back to the guide](README.md) · [Next: waiting and tools](waiting-and-tools.md)
