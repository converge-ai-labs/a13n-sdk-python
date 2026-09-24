# Observation and Data Access

## Thread SSE

The pinned [Thread stream contract](../contract/semantics/facts-and-delivery.md#the-thread-stream) owns server semantics. The SDK's `thread.stream(after=None, reconnect=True, max_reconnects=5, max_event_bytes=1048576)` is a synchronous, I/O-free factory for one single-use `ThreadStream`. Enter with `async with`, then use `async for frame in stream`; exit or `aclose()` releases the HTTP attachment. Breaking iteration alone does not close the context. One stream supports one active reader. Client close or caller cancellation ends local I/O but not the remote Run.

`ThreadFrame` has `event_type`, immutable `data`, and `cursor: str | None`. Its five event names have distinct roles:

| Frame      | `cursor`       | Caller action                                          |
| ---------- | -------------- | ------------------------------------------------------ |
| `delta`    | Redis entry ID | Apply provisional event and item change                |
| `boundary` | Redis entry ID | Committed display covers the named attempt sequence    |
| `changed`  | `None`         | Re-read the Thread for inbox or pointer changes        |
| `reset`    | `None`         | Discard affected Run output and re-read its items      |
| `gap`      | `None`         | Re-read affected Run items to reconcile skipped deltas |

No Run-level SSE, terminal Run event, notification WebSocket, or implicit projection cache is exposed. A Thread SSE EOF never proves Run completion. An absent cursor on `changed`/`reset`/`gap` is intentional: these frames cannot be used as `Last-Event-ID`. A gap can be followed by connection EOF, so the application must perform explicit readback even if reconnection is enabled.

The read-only `stream.response` describes the latest successful HTTP handshake (status, headers, request ID); `is_closed` and `last_received_cursor` describe local lifecycle and last yielded cursor-bearing frame. Headers do not expose the response body. Framing and decoded payloads have a configured byte bound; malformed or truncated frames raise `ProtocolError`. Heartbeats are ignored.

## Checkpoints and Recovery

1. The application supplies its last *applied* Redis entry ID as `after`; the SDK sends it as `Last-Event-ID`. Starting without `after` follows the Service's default stream behavior.
2. The SDK yields a frame without persisting application progress. The application applies its projection and commits its own checkpoint.
3. When the consumer requests the next frame, the SDK acknowledges the previously yielded cursor-bearing frame **in memory** for reconnect. Yielding, prefetching, heartbeats, and ID-less frames do not advance that acknowledgement.
4. If a frame requires readback, the application fetches exact Run items or the Thread and reconciles explicitly. The SDK never silently resets the cursor or merges a snapshot into event history.

Automatic reconnection is only for this read-only attachment. It retries transient transport/EOF and handshake `429`, `502`, `503`, `504` with bounded exponential jitter and `Retry-After` consideration. It does not replay mutations. The retry budget resets only when a *new cursor-bearing frame* is consumed by the next read; a successful handshake, heartbeat, `changed`, `reset`, `gap`, and EOF do not reset it. Thus repeated gap-only reconnects exhaust the budget rather than looping forever. With reconnection disabled, clean EOF ends iteration; a transport failure is an error. After retry exhaustion the last safe `TransportError` or `ApiError` is raised. Protocol errors and caller cancellation are not retried. Applications needing a total time bound use an outer timeout.

A delivered cursor is not a durable application checkpoint. Background-processing a frame while requesting another can advance the in-memory acknowledgement before that work finishes; applications serialize processing or reattach from their own applied cursor after failure. No exactly-once delivery claim is made.

## Readback and Pagination

- `run.get()` reports authoritative Run state, including `waiting` and `pending`; `run.items.get()` reports retained display (`complete`, `dropped`, `position`, items). A sealed Run and complete display are different evidence. The SDK does not synthesize a finalized projection or inspect a Run to decide SSE completion.
- `collection.list(...)` makes one request; `pages(...)` lazily yields `Result[Page]` with original filters, opaque next cursor, and HTTP evidence. `iter(...)` flattens ordinary page items. Empty pages with next cursors do not end traversal; non-advancing cursors fail explicitly. Pagination does not promise snapshot isolation.
- Binary downloads use generated `get_stream()` response contexts where exported; the caller checks status and consumes chunks before exit. Buffered generated `get()` remains available. Multipart uploads use a caller-owned binary source and leave it open; transport cancellation does not imply rollback of a staged upload or published Asset.

Observation, waiting, and local stream cleanup send no mutation. Explicit Run commands remain separate from the stream and retain their normal Service preconditions and unknown-outcome rules.
