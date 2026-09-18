# a13n

Typed Python SDK for a13n Service.

The SDK is async-first and keeps Service evidence explicit. Resource references bind locally, `Result[T]` preserves HTTP evidence, managed-Agent helpers return exact accepted or queued identities, and `RunStream` provides bounded resumable SSE observation. Complete generated Native bindings and the existing Web Provider facade remain available.

## Installation

```bash
uv add a13n
```

Python 3.13 or later is required.

## Authentication and lifetime

A Client has one credential mode for its lifetime:

```python
import httpx2

from a13n import Client

public = Client("https://service.example")
bearer = Client("https://service.example", "api-token")
session = Client.session(
    "https://service.example",
    origin="https://app.example",
    workspace_id="ws_example",
    cookies=httpx2.Cookies(),
    csrf_token="explicit-proof",
)
```

Public and Bearer clients never send cookies. Session clients use normal cookie rules, send the configured Origin, and send the optional fixed Workspace boundary on every request. State-changing session requests send the explicitly configured CSRF proof. `session.set_csrf_token(value)` replaces or clears that proof without I/O.

Use an async context manager or `aclose()`. References share their Client's pool and lifetime; closing a reference is neither necessary nor supported.

## Managed Agent flow

Binding performs no I/O. Network work starts only at an awaited operation or entered stream:

```python
from a13n import Client, RunAccepted, SubmissionQueued


async def run_agent(base_url: str, token: str) -> None:
    async with Client(base_url, token) as client:
        agent = client.workspaces("ws_example").agents("support")
        accepted = await agent.start(
            "Summarize the ticket",
            idempotency_key="start-ticket-42",
        )

        sealed = await accepted.run.wait(timeout=60.0, poll_interval=0.5)
        print(sealed.value.status, sealed.value.output_text)

        thread = await accepted.thread.get()
        submission = await accepted.thread.submit(
            "Now draft a reply",
            expected_thread_version=thread.value.version,
            idempotency_key="reply-ticket-42",
        )
        if isinstance(submission, RunAccepted):
            print(submission.run.id)
        elif isinstance(submission, SubmissionQueued):
            disposition = await submission.queued_submission.wait(timeout=30.0, poll_interval=0.5)
            print(disposition.value.state)
```

`RunAccepted` retains the operation-specific receipt plus exact Run, Thread, and Session references. A queued Thread submission returns `SubmissionQueued`; it never fabricates a Run before Service accepts one.

Text helpers construct the ordinary versioned text input. Pass a complete `a13n.generated.models.AgentInput` for structured content. Revision, Environment, labels, execution overrides, versions, and idempotency remain explicit typed inputs. `UNSET`, `None`, and supplied values remain distinct.

## Resumable Run observation and control

`run.stream()` is synchronous and I/O-free. Enter it once, then iterate it directly:

```python
async def observe(run) -> None:
    applied_cursor = await load_checkpoint(run.id)
    async with run.stream(after=applied_cursor) as stream:
        async for observation in stream:
            # Commit the application effect and cursor together when possible.
            async with application_transaction():
                await apply_event(observation.event)
                await save_checkpoint(run.id, observation.cursor)

            if should_redirect(observation.event):
                await stream.steer(
                    "Focus on compatibility",
                    idempotency_key="steer-ticket-42",
                )
```

The default stream retries transient attachment/read failures with bounded jittered backoff and at most five reconnects per no-progress episode. It resumes exclusively after the cursor acknowledged in memory when the caller requests the next observation. That cursor is diagnostic delivery evidence, not a durable application checkpoint.

Load the durable cursor before attaching, and persist it only after the corresponding event effect is durable. A crash before that commit intentionally replays the event, so event application should be idempotent. Do not persist `last_received_cursor` before applying the event: it reports transport delivery and can advance beyond application state.

`stream.steer`, `stream.cancel`, and `stream.wait` delegate to the exact Run and remain usable before entry or after local stream closure while the Client is open. One stream has one active reader. Replay gaps, malformed events, retry exhaustion, and unconfirmed EOF are explicit failures. Local close detaches only; it does not cancel the durable Run.

## Resource management

`client.resources` exposes static typed navigation for every Native management operation in the pinned contract. Common roots are also available directly:

```python
async def inspect_resources(client: Client) -> None:
    agents = await client.workspaces("ws_example").agents.list(limit=50)
    providers = await client.resources.organizations("org_example").model_providers.list()
    environments = await client.workspaces("ws_example").environments.list()
    hooks = await client.workspaces("ws_example").hook_subscriptions.list()

    async for page in client.workspaces("ws_example").skills.pages(limit=25):
        for skill in page.value.items:
            print(skill.key)
```

The generated tree covers IAM, Agents and immutable revisions, Model and Web Providers, Skills and Assets, Environments and live mounts, Memory, Connections and Bots, bot memory, MCP discovery/configuration, the configuration assistant, Hooks, lifecycle events, and traces. Collections provide one-page `list` operations and lazy `pages` when the protocol uses an opaque cursor. Ordinary collections also offer explicit `iter` traversal of typed wire values; projection snapshots retain page-level coverage instead. Resource methods preserve generated request models, required versions, ETags, and idempotency keys; mutations are never replayed automatically.

Large binary downloads expose generated buffered methods and resource-level `*_stream` methods. Consume streaming responses inside their context. Upload sources remain caller-owned.

## Result and errors

Resource operations return immutable `Result[T]` values:

```python
result = await client.workspaces("ws_example").agents("support").get()
print(result.value, result.status_code, result.etag, result.request_id)
```

`headers` uses case-insensitive lookup. `content` preserves the original successful response bytes. Failures raise:

- `ApiError` for a Service rejection, with safe status/code/message/details and request metadata;
- `ProtocolError` for malformed success/error bodies, incompatible SSE, repeated cursors, and replay gaps through `ReplayGap`;
- `TransportError` when transport failure leaves a mutation outcome potentially unknown;
- built-in `TimeoutError` for SDK wait deadlines and `asyncio.CancelledError` for caller cancellation.

Credential, cookie, proof, and payload values are absent from ordinary SDK diagnostics.

## Generated HTTP operations

Complete wire models live in `a13n.generated.models`. Generated async operations remain accessible through `Client.execute`:

```python
from a13n.generated.api.identity import get_auth_context

response = await client.execute(lambda api: get_auth_context.asyncio_detailed(client=api))
```

`Response.parsed` retains the generated typed success/error union. `Client.stream(operation.build_request(...))` is the raw unbuffered transport surface and is separate from resource-level `RunStream`. Independently constructed generated synchronous clients retain their own transport lifetime.

## Compatible Web Provider facade

The existing Pydantic Web Provider API remains supported. `await client.workspace()` resolves the Bearer credential's Workspace once and returns `WorkspaceClient`; explicit `WebProviderScope` calls remain available. `AgentConfig` and `AgentRunOverride` preserve typed built-in Toolset selections while retaining unrelated configuration fields.

## Development

This independent repository requires Python 3.13, uv, and Make. Ordinary development and packaging do not import or execute Service source.

```bash
make install
make generate
make check-all
```

Generation reads the pinned local contract, emits attrs wire bindings plus static resource navigation, and replaces only generator-owned output. `contract/source.json` records exact Service provenance. See [Contributing](CONTRIBUTING.md) and the [SDK contract](spec/README.md).

### Opt-in Service integration

Both integration scripts use only HTTP and an installed SDK. They never import Service source, provision credentials, reset state, or delete resources. Output contains resource identities and protocol evidence, not credentials or model output.

`scripts/service-smoke.py` is the short management and binary check. Supply `A13N_SERVICE_URL`, `A13N_API_TOKEN`, `A13N_WORKSPACE`, and `A13N_AGENT`. It creates and retains one Run and one Asset, explicitly detaches/resumes Run SSE, waits for completion, and verifies a 300,000-byte upload/download.

`scripts/service_acceptance.py` is the release-readiness path. It additionally requires `A13N_CLIENT_TOOL_AGENT`, an Agent configured to enter client-Tool waiting state. Against the local scripted provider it:

- injects one real HTTP read failure after a complete SSE event and verifies automatic reconnect with the exact applied `Last-Event-ID`, without changing Service state or other connections;
- exercises steer and cancel with current versions;
- observes a queued Thread submission through `consumed` and follows its exact Run identity;
- exercises feedback, retry, continue, and fork while checking receipt Run, Thread, and Session identities;
- records Run sealing separately from retained Item `complete` and `finalized` projection evidence, including explicit `items_unavailable` results.

Run either script with the Python executable from the environment where the artifact is installed. To prove the script is not importing the source tree, copy it to another directory first:

```bash
cp scripts/service_acceptance.py /tmp/a13n-service-acceptance.py
/path/to/installed-venv/bin/python /tmp/a13n-service-acceptance.py
```

For the companion local Service checkout, discover the instance with `make dev-status` and use its documented lifecycle. `make service-dev` is sufficient when Console is unnecessary. Do not assume fixed ports. A local scripted model proves the complete Service transport and state path, not connectivity or behavior of an external cloud provider.

### Package release readiness

Build once, then install the wheel and sdist into separate clean virtual environments. Run import/version checks and the copied HTTP acceptance script from outside the source directory in each environment. Keep these evidence classes distinct:

1. unit/static checks prove deterministic SDK behavior and typing;
2. the local scripted Service proves real HTTP, SSE, control, queue, and successor integration;
3. isolated wheel and sdist environments prove packaged imports and installed execution;
4. external cloud validation proves provider connectivity only when an explicit test configuration, cost authorization, and request budget are available.

A successful build is not a publication. Missing external provider configuration does not invalidate local SDK evidence, but must be reported as untested rather than inferred from the scripted provider.

## License

Licensed under the Apache License 2.0.
