# Python SDK guide

Build an application around an Agent running on your a13n Service. Start with the [quick start](../README.md#quick-start), then follow the chapters that match your application.

## Build your first workflow

1. **[Agents and conversations](agents-and-conversations.md)** — create an Agent, send structured input, continue a conversation, and choose settings for one execution.
2. **[Streaming and results](streaming-and-results.md)** — display saved responses, add a live preview, handle incomplete streams, and manage observation lifetime.
3. **[Waiting and tools](waiting-and-tools.md)** — present approval requests, define a client tool, return application-owned results, and observe the successor Run.
4. **[Files and Memory](files-and-memory.md)** — attach a local document, download bytes, create reusable project notes, and edit them without losing concurrent changes.

## Integrate with your application

5. **[Connections and authentication](connections.md)** — choose API keys or login sessions, select a workspace, configure private CAs, and own Client lifetime.
6. **[The resource API](resources.md)** — list resources, traverse pages, make conditional edits, inspect response metadata, and preserve omitted/null distinctions.
7. **[Errors and recovery](errors-and-recovery.md)** — distinguish request failures from execution failures, save submission identities, recover queued work, and reconcile an unknown write outcome.

## How to use the examples

The quick start is a complete executable program. Chapter examples are small, typed functions with their own imports. Copy a function into that program and call it inside `main()` while the Client is open. Parameters such as `agent_id`, `model_key`, and `memory_id` represent resources in **your** workspace; the surrounding text explains how to obtain them.

For example, after copying `review_plan()` from the first chapter, replace the quick start's message section with a call to `await review_plan(client, os.environ["A13N_AGENT"], "Your project plan")`. Keep the existing `asyncio.run(main())` at the program boundary; do not start nested event loops.

Most examples generate a fresh idempotency key because each call demonstrates a new operation. Applications that need recovery should persist their key and request before submission, as described in the recovery chapter.

## Find a specific answer

| I want to…                                                  | Read                                                                                       |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Display assistant text rather than an optional output value | [Read a finished response](streaming-and-results.md#read-a-finished-response)              |
| Stop a progress display without cancelling remote work      | [Observation lifetime](streaming-and-results.md#own-the-observation-lifetime)              |
| Approve one requested action, not every pending tool        | [Approval decisions](waiting-and-tools.md#resume-after-an-approval-decision)               |
| Attach a file rather than only upload it                    | [Attach a local document](files-and-memory.md#attach-a-local-document)                     |
| Resolve an edit conflict                                    | [Conditional edits](resources.md#make-a-conditional-edit)                                  |
| Continue after my process restarts                          | [Recover a submission](errors-and-recovery.md#recover-a-queued-or-interrupted-observation) |

## Reference and development

The [generated models](../a13n/generated/models) and [resource methods](../a13n/generated/resources.py) are the complete typed API reference. The [SDK specification](../spec/README.md) explains implementation contracts, and the [pinned Service source](../contract/source.json) records compatibility inputs. These references complement the task guides; you do not need to read the protocol specifications before sending your first message.

See [Contributing](../CONTRIBUTING.md) for development, generation, tests, and packaging. To check a deployment, use the [opt-in acceptance guidance](errors-and-recovery.md#verify-against-your-own-development-service) against a disposable Service, not production.
