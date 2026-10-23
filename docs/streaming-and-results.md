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

To read earlier Items, explicitly request `run.items.get(before=first_ordinal, limit=200)`; to read forward, use `after=last_ordinal`. Bounds are exclusive, `before` >= 1, `after` >= 0, and the Service accepts at most 500 as the limit. Do not combine before and after. Each call makes one request; there is no automatic all-history loader. Every Items read returns only `run`, `items`, and `complete`; it establishes no stream coverage.

Session `items` frames separately carry normalization continuation. Generated `DisplayContinuation`, `FragmentState`, `ObserverContinuation`, and `StreamPosition` preserve that protocol state. The SDK supplies typed payloads; the application owns presentation and state replacement.

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

### Keep application progress explicit

`ThreadStream` accepts paired `run` and `position` only when your application already owns the corresponding display coverage. Its optional `after` is a separate applied Redis entry ID. Items readback no longer supplies either coordinate. Keep previously applied stream progress explicitly; do not derive positions from ordinals, a Run view, or an Items response.

After a gap, close the old observation and explicitly read the affected Run's Items to replace the provisional preview. This read alone cannot establish seamless replay coverage:

```python
from a13n import Client, GapFrame


async def read_after_gap(client: Client, gap: GapFrame) -> None:
    saved = (await client.runs(gap.data["run_id"]).items.get()).value
    print("Replace preview with saved Items:", saved.to_dict())
    print("Gap target:", gap.data.get("position"))
```

`ThreadStream` preserves its original query pair on automatic reconnects. Requesting the next frame acknowledges the previously yielded cursor-bearing frame in memory for `Last-Event-ID`; it does not update the query position. Serialize application processing before requesting another frame. Fixed original coverage can replay already-applied suffix events, so applications reconcile delivery against their own progress.

## Observe a Session snapshot connection

`SessionStream` is an advanced single-connection reader for the Session's Threads and live output. Each new instance starts with a fresh snapshot. It exposes six distinct frame classes with generated typed data: `SessionThreadFrame`, `SessionItemsFrame`, `SessionDeltaFrame`, `SessionGapFrame`, `SessionScheduleFrame`, and `SessionOccurrenceFrame`. These frames have no cursor; Session connections never send `Last-Event-ID`. Session snapshots have no default frame-size cap; set `max_event_bytes` to a positive integer when your application needs an explicit bound. HTTP error-body reads remain bounded.

```python
from a13n import Client, SessionStream


async def observe_session(client: Client, session_id: str) -> None:
    # Start a fresh display generation here; discard unfinished state left by
    # any earlier connection. This context never reconnects in the background.
    async with SessionStream(client.api.sessions(session_id)) as stream:
        async for frame in stream:
            if frame.event_type == "thread":
                print("Replace Thread and pointed Runs:", frame.data.thread.id, frame.data.entries)
            elif frame.event_type == "items":
                print("Replace Run items from ordinal:", frame.data.run_id, frame.data.first)
                print(frame.data.items, frame.data.continuation, frame.data.complete)
            elif frame.event_type == "delta":
                print("Provisional event:", frame.data.run_id, frame.data.event.to_dict())
            else:
                print("Wait for an items repair for:", frame.data.run_id)
```

A `thread` frame replaces the Thread, its current/last Run views and its ordered open inbox entries. An `items` frame replaces that Run's Items starting at `first`; earlier Items remain final. A `gap` holds that Run's deltas until a later Items base repairs it. Service owns sequencing and bases; the SDK adds no display reducer or fragment assembler. Sealed Runs missed while disconnected are read explicitly through Items. `RunView.display_position` and `ThreadView.message_history` are absent from current readback.

The context boundary is the fresh-snapshot boundary: clean EOF ends iteration, transport failures raise `TransportError`, HTTP refusals retain `ApiError` status/request ID/Retry-After, and invalid known frames raise `ProtocolError` and close the response. Unknown event names are ignored before JSON decoding. Successful handshake metadata is available through `stream.response`. Exit, `aclose()`, cancellation and Client shutdown release local I/O without a remote command. Raw HTTP access remains `client.api.sessions(session_id).stream.get_stream()`.

Applications that reconnect create a new `SessionStream` and replace unfinished display state before consuming its snapshot. The native reconnect policy retries after any connection end except invalid protocol frames and 4xx responses other than 429. Use full jitter below `min(30 seconds, 0.5 seconds * 2**n)`, honor `Retry-After` on 429/503, and reset the consecutive-failure counter only after a connection remains stable for 30 seconds. Keep this policy separate from ThreadStream's applied-cursor retry behavior.

Finite Interaction remains the primary request/response workflow: it binds the consumed Entry's exact Run and terminates on that Run's completion or human wait. Opening a native Session reader does not change that lifecycle.

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
