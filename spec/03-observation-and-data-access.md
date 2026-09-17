# Observation and Data Access

## Design Position

Observation exposes Service evidence without acquiring execution authority. Reading an event, page, or binary stream changes no durable resource and advances no application checkpoint implicitly.

The [pinned streaming semantics](../contract/semantics/native-streaming-and-notifications.md) own delivery protocols. [Resources and Client Lifetime](01-resources-and-client-lifetime.md#client-lifetime) owns local cleanup; [Protocol and Compatibility](05-protocol-and-compatibility.md#failure-semantics) owns transport and API failures.

## Distinct Observation Surfaces

| Surface                             | Evidence                          | Ordering or recovery domain                                |
| ----------------------------------- | --------------------------------- | ---------------------------------------------------------- |
| Run SSE                             | Detailed observations for one Run | Run Stream cursor and bounded replay                       |
| Workspace lifecycle collection      | Durable lifecycle facts           | Opaque collection cursor                                   |
| Run/RunAttempt lifecycle collection | Facts for one resource            | `resource_seq`                                             |
| Item collection                     | Retained semantic display state   | Snapshot version, projection cursor, and coverage metadata |
| Hook delivery                       | Delivery attempts and receipts    | Hook-specific delivery contract                            |
| Notification frames                 | Best-effort resource wake-ups     | No replay cursor                                           |

These surfaces do not share a synthetic event envelope or checkpoint. Their delivery does not establish a stronger completion fact than their owner defines.

## Run SSE Observation

- `Run.stream` returns a concrete `RunStream`: an explicit async context manager and typed async iterator for one exact Run. This logical observation scope can span multiple HTTP attachments through bounded automatic reconnection.
- Each observation preserves the SSE cursor separately from the `RunStreamEvent.event_id`.
- Heartbeats are not yielded as domain observations.
- Invalid framing, malformed payloads, incompatible schema versions, and mismatched Run identity are explicit protocol failures.
- Event buffering is bounded; exceeding a configured bound fails rather than accumulating unbounded data.
- Exiting the scope, including after early iteration exit, releases the streaming response.
- End-of-stream does not prove Run completion.

### RunStream Public Interface

The following conceptual Python interface defines the resource-level stream, not the compatible raw `Client.stream` interface. Control signatures and receipt meanings are owned by [Interaction and Control](02-interaction-and-control.md#steer-and-cancel).

```python
class StreamObservation:
    cursor: str
    event: RunStreamEvent


class StreamResponse:
    status_code: int
    headers: Mapping[str, str]
    request_id: str | None


class RunStream:
    run: Run
    response: StreamResponse | None
    is_closed: bool
    last_received_cursor: str | None

    async def __aenter__(self) -> Self: ...
    async def __aexit__(self, exc_type, exc, traceback) -> None: ...
    def __aiter__(self) -> Self: ...
    async def __anext__(self) -> StreamObservation: ...

    async def steer(self, input: str | AgentInput, *, idempotency_key: str) -> Result[SteerReceipt]: ...

    async def cancel(
        self,
        *,
        expected_run_version: int,
        expected_thread_version: int,
        idempotency_key: str,
    ) -> Result[InterruptReceipt]: ...

    async def wait(self, *, timeout: float, poll_interval: float) -> Result[RunResource]: ...

    async def aclose(self) -> None: ...
```

- `run.stream(*, after: str | None = None, reconnect: bool = True, max_reconnects: int = 5)` is a synchronous, I/O-free factory. `after` is the caller's applied Run Stream cursor and maps to the `Last-Event-ID` header (omitted for `None`); it is not an event ID. Each call creates an independent logical stream. `max_reconnects` is a non-negative integer; zero or `reconnect=False` disables retries.
- `async with run.stream(...) as stream` enters and returns that same object. `async for observation in stream` is the primary consumption form; no redundant `events()` iterator or implicit awaiting of the stream is required.
- `StreamObservation` is read-only and separates its opaque cursor from the generated event envelope. Event payload typing does not exceed what the pin declares; the SDK does not manufacture a closed event-payload union.
- `response` is read-only metadata from the latest successful handshake, initially `None`, replaced on successful reattachment and retained during backoff and after closure. A previously returned `StreamResponse` remains an immutable snapshot. It has case-insensitive headers and no live body reader or buffered copy of the SSE body.
- `last_received_cursor` is initially `None` and advances only when an observation is delivered by `__anext__`, not on prefetch or heartbeats. It is diagnostic delivery evidence, never a saved applied checkpoint.
- `run`, `response`, `is_closed`, and `last_received_cursor` are read-only local properties. No property performs network I/O.

### Logical Stream Lifetime

| State  | Entry / iteration                                                                | Local close                             |
| ------ | -------------------------------------------------------------------------------- | --------------------------------------- |
| New    | Entry attaches with the retry policy; reading before entry raises `RuntimeError` | Closes without sending a request        |
| Open   | One active reader, including any reattachment or backoff it is awaiting          | Releases I/O and ends local observation |
| Closed | Re-entry raises `RuntimeError`; subsequent iteration is exhausted                | Idempotent no-op                        |

- Entry is single-use, including a failed or cancelled entry. A second or concurrent entry fails locally; create another `RunStream` to start a new scope.
- `is_closed` is false while new, attached, or recovering. It becomes true on confirmed stream completion, non-retryable failure, retry exhaustion, caller cancellation of entry/read, explicit `aclose`, or context exit. With reconnection disabled, the first EOF or read failure also closes it.
- Every finished or failed HTTP attachment releases its response before another is opened. Recoverable failure does not exhaust the logical iterator. A final failure raises its typed error on the current entry/read; later reads are exhausted. Normal exhaustion never invents a final Run value.
- `aclose()` can run while entry, a read, or backoff is pending. It releases blocked local I/O and sleeps; a pending read ends with `StopAsyncIteration`, and pending entry fails locally with `RuntimeError`. Independently cancelling the consumer task still propagates `asyncio.CancelledError`, not normal EOF.
- Breaking an `async for` does not by itself exit the surrounding context. Cleanup is guaranteed when that context exits or `aclose()` is awaited; callers must not rely on garbage collection.
- Context exit never suppresses the consumer's exception, drains unread events, waits for Run completion, or sends cancel. Cleanup does not replace an existing consumer exception with a synthetic execution result.
- The parent Client owns the transport. Client closure releases the attachment and rejects further requests, without remote cancellation.

### Commands During Observation

- `steer`, `cancel`, and `wait` delegate to `stream.run`; they do not read from the SSE iterator, acquire its single-reader slot, or require a next event to complete.
- They can run from another task while the one consumer is awaiting an event. Concurrent `__anext__` calls fail locally with `RuntimeError`; the SDK does not broadcast, split, or reorder one attachment among readers.
- Delegated calls are available before entry and after attachment closure while the Client remains open. Stream closure affects attachment I/O, not the exact Run reference or its explicit command authority.
- Successful `cancel` neither calls `aclose` nor drains the stream. Callers can keep reading available evidence or close immediately; neither choice changes the cancellation receipt.
- A command failure is raised to its caller and does not independently close an otherwise healthy stream. Local closure does not cancel an in-flight command; closing the Client can end all its owned I/O with the usual unknown-outcome rules.
- Concurrent command order is Service order, not task creation or event-delivery order. Callers sequence dependent commands explicitly and retain required versions and idempotency keys.
- `wait` performs bounded Run reads independently of the attachment. It neither pumps events nor advances `last_received_cursor`; a sealed read can coexist with unread or incomplete display events.

### Completion and Retained Evidence

`RunStream` exposes remote observation and explicit commands, not an embedded Harness execution. It has no live Agent context, `export_state()`, synthesized usage total, cached successful `result`, or local execution `outcome`. These would imply authority or completeness absent from the Service attachment. Exact Run reads, exported usage resources, and retained Item snapshots remain the corresponding evidence sources.

The representative flow separates acceptance, observation, and durable state:

```python
accepted = await agent.start("Review this change", idempotency_key=start_key)
run = accepted.run

async with run.stream(after=applied_cursor) as stream:
    async for observation in stream:
        await apply_and_checkpoint(observation)
        if should_redirect(observation):
            receipt = await stream.steer("Focus on compatibility", idempotency_key=steer_key)
            steer = run.steers(receipt.value.steer_id)
            break

# Exiting above only detached. This read can also run concurrently with streaming.
sealed = await run.wait(timeout=60.0, poll_interval=0.5)
```

The application supplies the policy, keys, and applied checkpoint in this conceptual flow. Nothing in the stream automatically issues the steer or interprets a sealed waiting Run as business completion.

### Applied Checkpoints

1. The caller attaches using its last completely **applied** cursor, or starts without a cursor.
2. The SDK yields an observation without persisting application progress.
3. The application applies the observation to its own projection.
4. The application commits the corresponding checkpoint under its own durability policy.

Receiving an event is not application acknowledgement. For sequential iteration, requesting the next observation acknowledges the previously yielded observation **in memory** for reconnection. The initial resume position is `after`; prefetch, parsing, yielding, heartbeats, and local closure do not advance it. Concurrent reader rejection occurs before this acknowledgement. A failed next read can therefore resume after the previous observation, but never after an undelivered prefetched event.

This contract assumes processing finishes before the next `__anext__` call, as in the example above. Handing an observation to another task and immediately requesting the next acknowledges delivery, not completion of that background work. Applications needing that pattern must serialize acknowledgement through their consumer or disable automatic reconnection and reattach using their own applied cursor. The SDK persists no checkpoint and promises no exactly-once processing across cancellation, failure, or restart.

### Replay Gaps and Reconnection

- Reconnection is enabled by default and applies only to this read-only SSE scope. It retries transient connection/read failures and handshake statuses `429`, `502`, `503`, and `504`. Other API failures, invalid cursors, malformed/incompatible events, local argument/lifecycle failures, and caller cancellation are not retried. No control command or ordinary resource request is replayed by this policy.
- Each recovery episode permits at most `max_reconnects` additional attachment attempts, including initial-handshake recovery. Delay before retry number `n` is uniformly jittered between half and all of `min(0.5 * 2**(n - 1), 10.0)` seconds. A valid non-negative `Retry-After` delay or HTTP date is honored as a lower bound, capped at 30 seconds; invalid values do not alter backoff. There is no public retry-policy class or custom callback framework.
- The consecutive budget resets only when requesting the next observation acknowledges a newly yielded cursor. Successful handshakes, heartbeats, and empty EOFs do not reset it. Repeated disconnects without observation progress therefore cannot loop indefinitely. Long-running healthy observation has no synthetic total Run deadline; applications can use an explicit outer timeout.
- An exhausted handshake/read failure raises the last `ApiError` or `TransportError` with its safe evidence. Unconfirmed EOF exhaustion raises `TransportError`, not successful completion. Cancellation, Client closure, and local close interrupt both network waits and backoff.
- `409 run_stream_replay_gap` and an in-stream `a13n.service.replay_gap` both raise `ReplayGap` with the available requested cursor, floor, high watermark, and Run identity; attachment errors also retain HTTP evidence. Neither is retried or yielded as a checkpoint-bearing event. Other `409` responses retain normal API error semantics.
- Recovery keeps the exact Run and resumes exclusively after the in-memory acknowledged cursor. A cursor is not an event ID, and reconnection never advances it from network receipt alone.
- The SDK does not reset to the beginning, silently read a snapshot to replace missing history, or describe a merged snapshot as exact replay. Snapshot reconciliation remains an explicit application decision.

### EOF and Completion

- A clean EOF without completion evidence can be a server attachment-lifetime limit; it is eligible for bounded reconnection. With reconnection disabled, clean EOF ends iteration without extra evidence reads or a completion claim; a transport failure is raised immediately. A truncated event is a protocol failure, not clean EOF.
- The pinned Service's terminal Run observations are `run.completed`, `run.failed`, `run.cancelled`, and `run.waiting`. Their Run identity must match the bound Run. Harness/AG-UI completion events and Attempt outcomes are not substitutes.
- After yielding a terminal Run observation, the iterator drains the current attachment through clean EOF before normal exhaustion. A transport failure before EOF still follows bounded recovery. Delivery of the terminal observation does not assert that the retained Item projection is finalized.
- An attachment opened after an already-applied terminal cursor can contain no events. On otherwise unconfirmed clean EOF, the SDK may perform one exact Run read and one Run Item-page read per recovery attempt. Normal exhaustion requires both a sealed Run and a finalized Item projection whose `projection_cursor` equals the acknowledged cursor. A newer or unavailable projection is not proof that unseen stream history was consumed; continue bounded recovery or surface the actual read/gap error. These reads do not replace the application's projection or advance its cursor.
- A Run read alone, including `waiting`, never truncates unread observations or confirms display finalization. The SDK does not keep polling after exhausting the bounded recovery policy.

## Item Snapshot Reconciliation

Item collection results retain:

- `snapshot_version` and `projection_cursor`;
- retained Item and Run identities;
- completeness and finalization flags;
- the reported incomplete reason.

Recovery replaces the display projection covered by the snapshot before attaching after its projection cursor. It does not append a merged snapshot over already applied deltas or claim exact replay of missing events.

Run sealing and display finalization are independent. A sealed Run can still have an incomplete or unfinalized retained display projection, and the SDK preserves that evidence.

## Lazy Pagination

- Each request preserves the original filters, explicit scope, server order, and opaque cursor.
- Iteration is lazy and does not prefetch.
- An empty or short page does not end iteration while a next cursor exists.
- An absent next cursor ends the collection; a repeated or non-advancing cursor is an explicit failure rather than an infinite loop.
- Each yielded page retains its full typed representation and HTTP evidence, including specialized snapshot or retention metadata.
- Pagination does not invent snapshot isolation or flatten every Thread Run into one linear conversation.
- Resource-sequence reads are not relabeled as opaque-cursor pagination.

### Collection Call Shape

- `await collection.list(...)` fetches exactly one typed page as `Result[PageT]`.
- `collection.pages(...)` returns a lazy `AsyncIterator[Result[PageT]]`; creating it sends no request. Each advance fetches only the next required page.
- `collection.iter(...)` is the explicit flattened `AsyncIterator[ItemT]` convenience for ordinary collections. It yields wire values, not live references or mutable active-record objects.
- A collection itself is neither awaitable nor implicitly iterable: the caller chooses one-page, page-wise, or value-wise access and supplies its filters there. No implicit total count, indexing, or network-backed `len()` is provided.
- Each traversal has its own cursor and filter snapshot. Independent traversals do not share progress. One traversal does not support concurrent reader calls or implicit restart after exhaustion.
- Page iteration is canonical when page-level evidence matters. Item snapshots and other specialized projection collections retain their full page representation; ordinary flattened iteration is not a snapshot-reconciliation interface.
- Server-owned resource scope and identity remain available in yielded representations. Creating a mutation reference from a value uses that reported ownership, not merely the collection's discovery scope.

## Binary Transfer

- Large downloads use an explicit streaming response scope with caller-visible status and headers.
- Buffered generated methods remain available but are not advertised as the large-file interface.
- Uploads read caller-owned binary sources in bounded chunks without closing them.
- Upload cancellation releases local transport work; it does not imply rollback of a published resource.
- Asset publication, staged upload completion, and later Run acceptance remain distinct outcomes under [Resource Management](04-resource-management.md#skills-assets-and-content).

## Supported Transport Boundary

This Python contract includes ordinary Native HTTP and Run SSE with bounded automatic reconnection. Notification WebSocket attachment and transparent snapshot replacement are outside this transport surface.

Vendoring a notification schema does not claim an implemented attachment or recovery interface. No detailed Run WebSocket stream is synthesized from best-effort notifications.

## Failure Semantics

| Condition                        | Observable result                              | Caller responsibility                                             |
| -------------------------------- | ---------------------------------------------- | ----------------------------------------------------------------- |
| Attachment API failure           | Typed API error with response evidence         | Reconcile authorization, retention, or requested cursor           |
| Malformed or oversized SSE event | Protocol error                                 | Do not advance an applied checkpoint from the invalid event       |
| In-stream replay gap             | Explicit gap metadata                          | Choose snapshot reconciliation or another supported recovery path |
| EOF or transport loss            | Bounded recovery, exhaustion, or typed failure | Do not infer remote completion from a disconnect alone            |
| Local cancellation               | Local I/O ends                                 | Do not infer a remote interrupt or rollback                       |

## Invariants

1. Attachment, iteration, wait, and local cleanup perform no mutation or client-tool execution; explicit stream control calls retain ordinary Run command semantics.
2. Receiving an event never commits an application checkpoint.
3. SSE cursors, event IDs, lifecycle sequences, and snapshot versions remain distinct.
4. Empty pages with continuation cursors are traversed.
5. Snapshot recovery is not represented as exact replay.
6. Early scope exit releases owned I/O without cancelling a durable Run.
