# Protocol and Compatibility

## Design Position

The SDK preserves the pinned public Service contract while providing a Python-native interface. Resource convenience does not weaken wire fidelity, authorization, concurrency, or failure evidence.

The [pinned API conventions](../contract/semantics/api-conventions.md) own HTTP semantics. The [specification index](README.md#authority) defines upstream authority; this document owns Python serialization, error mapping, compatibility, and generation guarantees.

## Wire and Type Fidelity

- Ordinary Native operations retain typed request fields, response values, unions, path selectors, and required headers.
- Generated attrs request and response models remain available as the complete wire-model family.
- `UNSET` means omitted; `None` means explicit JSON null where permitted; a supplied value is distinct from both.
- Server defaults are not inserted as client-supplied values.
- Default error responses and fields literally named `default` remain part of the contract.
- Typed unions, decimal values, and opaque identities retain their declared wire behavior.
- Unknown Run status strings remain visible. Closed discriminator tags do not become extensible merely because Run status is extensible.
- Static typing and supported wire validation do not claim runtime enforcement of every JSON Schema keyword.
- Successful JSON null, binary content, and empty responses retain their declared semantics rather than being forced into a non-null JSON object.

The resource interface retains the evidence described by [Resources and Client Lifetime](01-resources-and-client-lifetime.md#values-and-response-evidence).

## Concurrency and Idempotency

- Versioned mutations retain required ETags, `If-Match`, expected versions, and idempotency inputs.
- Independent counters, including Thread `version` and `queue_version`, are not substituted for each other.
- Required idempotency keys are explicit caller inputs; a helper does not generate a new key to retry uncertain intent.
- A concurrency conflict is surfaced with Service evidence rather than silently refreshing a version and overwriting state.
- Mutations are never replayed automatically after a transport failure.
- Reading a newer representation is observation, not permission to repeat a prior mutation under new preconditions.

## Failure Semantics

| Condition                                 | Resource interface                      | Required interpretation                                                                                                      |
| ----------------------------------------- | --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Service rejection                         | `ApiError`                              | Preserve status, safe code/message/details, request ID, and retry guidance                                                   |
| Malformed required success body           | `ProtocolError`                         | Do not fabricate a typed resource or successful receipt                                                                      |
| Transport failure after possible dispatch | `TransportError`                        | The mutation outcome can be unknown                                                                                          |
| Timeout or caller cancellation            | Local operation ends                    | No proof of rollback or remote cancellation                                                                                  |
| Valid null or empty success               | Successful typed result                 | Null is not itself a protocol failure                                                                                        |
| Replay or projection gap                  | Observation-specific error and metadata | Apply the recovery boundary in [Observation and Data Access](03-observation-and-data-access.md#replay-gaps-and-reconnection) |

The retained low-level `Client.execute` surface keeps its generated typed success/error union, status, headers, and content. Resource-level exception mapping and the existing Web facade's response-size bound are not silently imposed on it.

### Python Exceptions and Cancellation

- Local invalid helper arguments, such as a non-positive or non-finite wait budget, raise `ValueError` before dispatch.
- Invalid local lifecycle use, including I/O through a closed Client, repeated stream entry, or concurrent reads of one iterator, raises `RuntimeError` without a remote command.
- Exhaustion uses `StopAsyncIteration`. An in-stream replay gap raises `ReplayGap` with its metadata and closes the attachment; it is neither normal exhaustion nor a checkpoint-bearing domain event.
- An SDK wait deadline raises built-in `TimeoutError`. Cancellation of the caller's task propagates `asyncio.CancelledError`; the SDK does not wrap it as `ApiError`, turn it into successful EOF, or send a compensating interrupt.
- A read of a failed/cancelled/waiting Run is still a successful read of that resource, not an API exception for its execution outcome.
- Stream-control calls use the same exception mapping as their corresponding Run methods. A lost cancel response can have an unknown outcome even though a received successful interrupt receipt establishes durable cancellation.

Applications reconcile unknown outcomes using Service state, retained intent, and idempotency evidence. Retry guidance in an error does not itself authorize automatic mutation replay.

## Diagnostics

- Client, request, response, receipt, and error diagnostics do not expose credentials or input/output payloads through ordinary representation.
- Explicit authorized serialization retains the values required on the wire.
- Secret redaction does not remove safe status, error codes, request IDs, or retry guidance needed for diagnosis.
- Raw response content is explicitly accessible evidence, not material to include automatically in logs.

## Generation and Contract Inputs

- Generation uses the SDK's local pinned protocol inputs and pinned tools.
- `contract/source.json` records the upstream repository, complete Service commit SHA, and original paths of the vendored inputs.
- Generation does not import or execute Service or another SDK repository.
- Generation replaces generator-owned output directly. Correctness is established by type checking and wire, transport, and integration tests, not snapshot checksums or generated-file byte comparisons.
- Mechanical generation and bounded convenience share one wire model and serialization contract.
- Generated bindings cover ordinary Native operations independently of which operations have handwritten helpers.
- Correcting a known export omission requires evidence from the pinned protocol or its owning Service source; it does not authorize inventing behavior from a route name.
- A generator adaptation leaves original vendored evidence intact and states its compatibility effect. Publication still requires the SDK's own compatibility review.

## Compatibility Axes

| Identity                       | Meaning                                      | Does not imply                        |
| ------------------------------ | -------------------------------------------- | ------------------------------------- |
| Python distribution version    | SDK public API and package compatibility     | A Service deployment version          |
| Service source SHA             | Exact provenance of consumed contract inputs | SDK release readiness                 |
| HTTP API version               | Native HTTP protocol boundary                | Streaming schema compatibility        |
| Input or stream schema version | Compatibility of the corresponding envelope  | A package-version increment by itself |
| Resource revision or version   | Domain state and concurrency evidence        | Any of the above protocol identities  |

Contract updates can change generated public types and are reviewed before SDK release. Async-first resource access does not implicitly remove existing synchronous or Web-facade APIs; their preserved surface is owned by [Resources and Client Lifetime](01-resources-and-client-lifetime.md#compatibility).

A shared design requirement and a successful generation run are not proof that a published SDK or deployed Service implements the complete surface. Supported capability claims identify their contract and distribution boundary.

## Conformance Evidence

Validation establishes the relevant contract at distinct levels:

- **Coverage:** every pinned Native operation has typed resource navigation and a low-level binding.
- **Wire behavior:** fixtures preserve omission, null, unions, decimals, extensible status, and declared success/error bodies.
- **Public typing:** positive and negative examples exercise accepted and rejected request shapes, acceptance-union narrowing, the non-awaitable stream factory, and direct asynchronous iteration.
- **Transport:** tests preserve base URL prefixes, escaping, authentication, headers, cancellation, nested I/O ownership, and shutdown.
- **Interaction and observation:** tests establish the invariants in the owning interaction and observation contracts: exact identity forwarding; required cancel versions; acceptance versus steer consumption; independent local close and remote cancel; bounded wait across all sealed states; and queue waiting without consumption.
- **Stream lifecycle:** tests cover failed/cancelled entry, EOF, early context exit, malformed events, replay gaps, one-reader rejection, close during a blocked read, cancellation propagation, control calls during iteration and after closure, and preservation of response metadata without automatic checkpoints.
- **Distribution:** local generation and package checks require no Service checkout. Input updates retain their source attribution for review.
- **Integration:** mock, loopback transport, real Service, and real provider evidence are labeled separately.

Validation commands and publication procedure belong to [Contributing](../CONTRIBUTING.md), not this contract. Formatting or mock tests alone do not prove deployed-provider behavior.

## Invariants

1. Omission and explicit null survive serialization distinctly.
2. Local failure never establishes remote rollback.
3. Mutation preconditions are not silently weakened or replayed.
4. Credentials remain absent from ordinary diagnostic representations.
5. Generation is deterministic from pinned inputs and does not mutate source evidence.
6. SDK, Service, protocol, and resource versions remain separate compatibility axes.
7. Validation claims state which boundary was actually exercised.
