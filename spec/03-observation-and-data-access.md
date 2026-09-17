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

## Run SSE Attachment

- A Run stream is an explicit async context manager yielding a typed async iterator.
- Each observation preserves the SSE cursor separately from the `RunStreamEvent.event_id`.
- Heartbeats are not yielded as domain observations.
- Invalid framing, malformed payloads, incompatible schema versions, and mismatched Run identity are explicit protocol failures.
- Event buffering is bounded; exceeding a configured bound fails rather than accumulating unbounded data.
- Exiting the scope, including early iteration exit, releases the streaming response.
- End-of-stream does not prove Run completion.

### Applied Checkpoints

1. The caller attaches using its last completely **applied** cursor, or starts without a cursor.
2. The SDK yields an observation without persisting application progress.
3. The application applies the observation to its own projection.
4. The application commits the corresponding checkpoint under its own durability policy.

Receiving an event is not application acknowledgement. The SDK neither persists a cursor automatically nor resumes from the last merely received event.

### Replay Gaps and Reconnection

- An attachment rejected by Service retains the API error and replay-bound metadata.
- A gap reported after attachment is an explicit `ReplayGap` outcome, not a domain observation with an applied cursor.
- Attaching once does not silently enable reconnection.
- The caller can reconnect with its applied cursor and an explicit bounded policy.
- Missing exact history is not described as replayed history after a snapshot read.

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

## Binary Transfer

- Large downloads use an explicit streaming response scope with caller-visible status and headers.
- Buffered generated methods remain available but are not advertised as the large-file interface.
- Uploads read caller-owned binary sources in bounded chunks without closing them.
- Upload cancellation releases local transport work; it does not imply rollback of a published resource.
- Asset publication, staged upload completion, and later Run acceptance remain distinct outcomes under [Resource Management](04-resource-management.md#skills-assets-and-content).

## Supported Transport Boundary

This Python contract includes ordinary Native HTTP and one-attachment Run SSE. Notification WebSocket attachment, automatic reconnection, and transparent snapshot replacement are outside this transport surface.

Vendoring a notification schema does not claim an implemented attachment or recovery interface. No detailed Run WebSocket stream is synthesized from best-effort notifications.

## Failure Semantics

| Condition                        | Observable result                      | Caller responsibility                                             |
| -------------------------------- | -------------------------------------- | ----------------------------------------------------------------- |
| Attachment API failure           | Typed API error with response evidence | Reconcile authorization, retention, or requested cursor           |
| Malformed or oversized SSE event | Protocol error                         | Do not advance an applied checkpoint from the invalid event       |
| In-stream replay gap             | Explicit gap metadata                  | Choose snapshot reconciliation or another supported recovery path |
| EOF or transport loss            | Attachment ends or fails               | Determine Run state separately and choose bounded reconnection    |
| Local cancellation               | Local I/O ends                         | Do not infer a remote interrupt or rollback                       |

## Invariants

1. Observation performs no mutation or client-tool execution.
2. Receiving an event never commits an application checkpoint.
3. SSE cursors, event IDs, lifecycle sequences, and snapshot versions remain distinct.
4. Empty pages with continuation cursors are traversed.
5. Snapshot recovery is not represented as exact replay.
6. Early exit releases owned I/O without cancelling a durable Run.
