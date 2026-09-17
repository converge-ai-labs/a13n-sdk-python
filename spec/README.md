# a13n Python SDK

## Design Position

The `a13n` Python SDK is a typed client for managed Agents and the public Native Service resources around them. Resource objects are the primary application interface; complete low-level protocol access remains available.

- Python operations and iteration are async-first, with explicit local resource lifetime.
- Service owns durable resources, authorization, acceptance, execution, and protocol semantics.
- Applications own orchestration, business completion, external side effects, and durable application checkpoints.
- The SDK introduces no local Agent engine, hidden current Thread, or business-workflow identity.

These documents define the Python contract, not the implementation status of a release. Package and deployment capability claims require separate implementation and validation evidence.

## Authority

| Concern                                                                   | Owner                                                                                                                                                           |
| ------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Shared SDK experience and domain boundaries                               | [Service SDK Design and Contract Distribution](https://github.com/converge-ai-labs/agent-foundation/blob/main/spec/a13n-service/37-service-sdks-and-clients.md) |
| Session, Thread, Run, and Item meaning                                    | [Platform Interaction Model](https://github.com/converge-ai-labs/agent-foundation/blob/main/spec/interaction-model.md)                                          |
| Declared protocol inputs and source identity                              | [Pinned Service contract](../contract/README.md) and `contract/source.json`                                                                                     |
| Python API, runtime behavior, compatibility, and independent distribution | This specification set                                                                                                                                          |
| Contribution, validation commands, and publication workflow               | [Contributing](../CONTRIBUTING.md)                                                                                                                              |

The SDK consumes public Service protocols. It does not import Service startup, storage, migrations, Worker scheduling, or provider-native execution APIs.

## Specification Catalog

| Document                                                                | Owning contract                                                                                                 |
| ----------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| [00 Overview](00-overview.md)                                           | Architecture, dependency direction, end-to-end flow, and completion boundaries                                  |
| [01 Resources and Client Lifetime](01-resources-and-client-lifetime.md) | Python reference/snapshot roles, `Result[T]`, return contracts, local bindings, and transport ownership         |
| [02 Interaction and Control](02-interaction-and-control.md)             | Typed acceptance, Run/queue waiting, steer/cancel, feedback, continuation, fork, and retry                      |
| [03 Observation and Data Access](03-observation-and-data-access.md)     | `RunStream` interface and lifetime, concurrent control, applied cursors, replay gaps, snapshots, and pagination |
| [04 Resource Management](04-resource-management.md)                     | Management-family coverage, owning scopes, configuration provenance, and independent resource lifecycles        |
| [05 Protocol and Compatibility](05-protocol-and-compatibility.md)       | Wire fidelity, errors, concurrency, idempotency, diagnostics, contract generation, and compatibility axes       |

## Reading Paths

- **Architecture:** 00, then 01 and the relevant domain owner.
- **Managed Agent use:** 01, 02, then 03.
- **Resource administration:** 01, 04, then 05.
- **Protocol integration and compatibility:** 05, then the relevant pinned protocol and domain contract.

## Terminology

- A **reference** binds a resource selector locally; it is not a grant of authority or proof that the resource exists.
- A **snapshot** is an observed representation; it is not a live object mirror.
- A **receipt** records a command's actual disposition; acceptance, execution, application, and external delivery are distinct facts.
- An interaction **Session** is not an IAM authentication session.
- A specification requirement does not imply that every deployed Service exposes the corresponding operation.
