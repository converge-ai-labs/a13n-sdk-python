# Observation and Data Access

## Finite Interaction and Advanced Thread SSE

The [finite Interaction](02-interaction-and-control.md#finite-observation) is the primary observation API: it binds the exact incorporating Run first, filters foreign Run and unscoped signals, and ends when that Run seals. The pinned [Thread stream contract](../contract/semantics/facts-and-delivery.md#the-thread-stream) owns the advanced persistent transport semantics. The generated `client.resources.threads(thread_id).stream` child retains the original SSE HTTP operation. An advanced caller may explicitly construct `ThreadStream(client.resources.threads(thread_id), run=None, position=None, after=None, reconnect=True, max_reconnects=5, max_event_bytes=1048576)` as a single-use, Thread-wide parser. Neither the generated resource nor the ordinary authored Thread injects a persistent high-level `events()` workflow. Enter with `async with`, then use `async for frame in stream`; exit or `aclose()` releases the HTTP attachment. Breaking iteration alone does not close the context. One stream supports one active reader. Client close or caller cancellation ends local I/O but not the remote Run.

`ThreadFrame` is a discriminated union of `DeltaFrame`, `BoundaryFrame`, `ChangedFrame`, `ResetFrame`, and `GapFrame`. Each has a literal `event_type` and read-only typed `data`. Testing `event_type` or the concrete class narrows both payload fields and cursor: `str` for delta/boundary, `None` for the other three. The parser validates these envelope fields (including ItemRef), but the nested AG-UI event is an open JSON object, not a claimed validated AG-UI event union. Read-only payload mappings are shallow; nested arbitrary JSON retains normal JSON values. Its five event names have distinct roles:

| Frame      | `cursor`       | Caller action                                                          |
| ---------- | -------------- | ---------------------------------------------------------------------- |
| `delta`    | Redis entry ID | Apply provisional event and item change                                |
| `boundary` | Redis entry ID | Committed display covers the named attempt sequence                    |
| `changed`  | `None`         | Re-read the Thread for inbox or pointer changes                        |
| `reset`    | `None`         | Discard affected Run output and re-read its items                      |
| `gap`      | `None`         | Read affected Run items; reassess coverage through optional `position` |

No Run-level SSE, terminal Run event, notification WebSocket, or implicit projection cache is exposed. The finite Interaction uses exact Run readback to terminate, not a special SSE frame. A Thread SSE EOF never proves Run completion. An absent cursor on `changed`/`reset`/`gap` is intentional: these frames cannot be used as `Last-Event-ID`. A gap can be followed by connection EOF, so the application must perform explicit readback even if reconnection is enabled.

The read-only `stream.response` describes the latest successful HTTP handshake (status, headers, request ID); `is_closed` and `last_received_cursor` describe local lifecycle and last yielded cursor-bearing frame. Headers do not expose the response body. Framing and decoded payloads have a configured byte bound; malformed or truncated frames raise `ProtocolError`. Heartbeats are ignored.

## Checkpoints and Recovery

1. The application may supply a paired `run` and canonical `position` (`{attempt}-{sequence}`) claiming its existing display coverage. These query values remain unchanged on this stream's reconnects; the SDK never derives or advances coverage from a Redis entry ID. `after` is a separate last *applied* Redis entry ID, sent as `Last-Event-ID`; `RunItems.resume_after` is an optional covered hint for a saved display. With no query pair, existing cursor-only Service behavior remains unchanged.
2. The SDK yields a frame without persisting application progress. The application applies its projection and commits its own checkpoint.
3. When the consumer requests the next frame, the SDK acknowledges the previously yielded cursor-bearing frame **in memory** for reconnect. Yielding, prefetching, heartbeats, and ID-less frames do not advance that acknowledgement.
4. A gap preserves its optional canonical `position`, including explicit null and omission permitted by the current schema. The application fetches exact Run items, checks the saved coverage, and explicitly opens a new `ThreadStream` using that display's paired run/position and available `resume_after`. A readback may lag the hole; a gap is not proof that the returned snapshot heals it. Reset requires discarding superseded attempt output. The SDK never silently reads back, resets coverage, or merges a snapshot into event history.

The pinned Service contract, not a client precedence rule, determines replay. With a run/position pair, direct seeking uses the optional Redis hint only when its Run and attempt match the claim and active execution, and its sequence is covered. Absent, expired or incompatible hints fall back to retained replay filtered by the claimed position; their absence alone does not imply a gap. Covered boundaries remain visible, and an older-attempt claim receives reset. Fixed coverage across SDK reconnects can cause replay of already-applied output beyond that original coverage; an application must reconcile such delivery rather than assume exactly-once events.

Automatic reconnection is only for this read-only attachment. It retries transient transport/EOF and handshake `429`, `502`, `503`, `504` with bounded exponential jitter and `Retry-After` consideration. It does not replay mutations. The retry budget resets only when a *new cursor-bearing frame* is consumed by the next read; a successful handshake, heartbeat, `changed`, `reset`, `gap`, and EOF do not reset it. Thus repeated gap-only reconnects exhaust the budget rather than looping forever. With reconnection disabled, clean EOF ends iteration; a transport failure is an error. After retry exhaustion the last safe `TransportError` or `ApiError` is raised. Protocol errors and caller cancellation are not retried. Applications needing a total time bound use an outer timeout.

A delivered cursor is not a durable application checkpoint. Background-processing a frame while requesting another can advance the in-memory acknowledgement before that work finishes; applications serialize processing or reattach from their own applied cursor after failure. No exactly-once delivery claim is made.

## Readback and Pagination

- `run.get()` reports authoritative Run state, including `waiting` and `pending`; `run.items.get()` reports retained display (`complete`, `dropped`, `position`, optional `resume_after`, items). `position` is coverage, while `resume_after` is a Redis transport hint and is never a replacement for it. A sealed Run and complete display are different evidence. The SDK does not synthesize a finalized projection or inspect a Run to decide SSE completion.
- `collection.list(...)` makes one request; `pages(...)` lazily yields `Result[Page]` with original filters, opaque next cursor, and HTTP evidence. `iter(...)` flattens ordinary page items. Empty pages with next cursors do not end traversal; non-advancing cursors fail explicitly. Pagination does not promise snapshot isolation.
- Binary downloads use generated `get_stream()` response contexts where exported; the caller checks status and consumes chunks before exit. Buffered generated `get()` remains available. Multipart uploads use a caller-owned binary source and leave it open; transport cancellation does not imply rollback of a staged upload or published Asset.

Finite observation, exact waiting, and local stream cleanup send no mutation. Explicit Run commands remain separate from the stream and retain their normal Service preconditions and unknown-outcome rules.
