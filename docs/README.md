# Python application guide

Start with the [quick start](../README.md#quick-start) if you have not connected yet. This guide covers the next steps in an application.

The snippets below belong inside an async function with an open `client`. Examples that continue a conversation use the `agent`, `interaction`, and `outcome` from the quick start. Import the request models when needed:

```python
from uuid import uuid4

from a13n import ApiError, Client
from a13n.generated import models as wire
```

## Handle the result

`await interaction.result()` waits for your message to be processed and returns a `RunOutcome`. Check its status before deciding what to do next:

```python
outcome = await interaction.result()
if outcome.status == wire.RunStatus.COMPLETED:
    messages = await outcome.run.items.get()
    print(messages.value.to_dict())
elif outcome.status == wire.RunStatus.WAITING:
    print("Input needed:", outcome.pending.to_dict() if outcome.pending else None)
else:
    print("Stopped:", outcome.status)
    if outcome.failure is not None:
        print(outcome.failure.to_dict())
```

| Status      | What it means for your application                                               |
| ----------- | -------------------------------------------------------------------------------- |
| `completed` | Execution finished. Read the response and evaluate whether it answers your task. |
| `waiting`   | The Agent needs approval, a human answer, or a client-tool result.               |
| `failed`    | Execution failed. Inspect `outcome.failure`.                                     |
| `cancelled` | Execution was cancelled. It is not a successful reply.                           |

Use `outcome.run.items.get()` for saved messages and tool activity. `outcome.output` holds the Run's output value, which may be structured data or `None`; it is not a replacement for message readback. Saved Items are a bounded display: check `complete`, `dropped`, and content omission/truncation flags when completeness matters.

You can call `result()` without streaming. Once it succeeds, later calls return the cached outcome.

### Handle request errors

Service rejections raise `ApiError`. Keep the request ID when reporting a problem:

```python
try:
    interaction = await agent.start("Review this change.", idempotency_key=uuid4().hex)
except ApiError as error:
    print(error.status, error.code, error.request_id)
    raise
```

| Error                               | What to do                                                                                      |
| ----------------------------------- | ----------------------------------------------------------------------------------------------- |
| `ApiError`                          | Inspect `status`, `code`, and `details`. For `401`/`403`, check the credential and permissions. |
| `SubmissionError`                   | The submitted message failed or was withdrawn. Its `entry` contains the saved state.            |
| `TransportError`                    | The request could not be completed locally. A write may still have reached the Service.         |
| `ProtocolError`                     | Check SDK/Service compatibility and the response reported by the exception.                     |
| `TimeoutError` or task cancellation | Local waiting ended; remote work may still be running.                                          |

Branch on error codes rather than message text. Avoid logging tokens, cookies, or sensitive prompts and responses.

### Set a waiting timeout

```python
outcome = await interaction.result(timeout=60)
```

The default is 300 seconds, with a 0.5-second polling interval. This covers both time in the queue and execution. The Client's `timeout` option is separate: it limits an individual ordinary HTTP request and defaults to 30 seconds.

A timeout does not interrupt the Agent. To stop remote execution intentionally, use `await outcome.run.interrupt()` when you have its Run handle, or `await client.runs(run_id).interrupt()` for a saved Run ID.

## Create an Agent

If your API key permits Agent management, create one using an existing Model key:

```python
created = await client.resources.agents.create(
    body=wire.AgentCreate(
        name="Reviewer",
        config=wire.AgentConfigInput(model="review-model", instructions="Review changes clearly and briefly."),
    )
)
agent = client.agents(created.value.id)
interaction = await agent.start("Review my project plan.", idempotency_key=uuid4().hex)
outcome = await interaction.result()
```

Replace `review-model` with a configured Model key in your workspace. **Models use keys; Agents and Skills use IDs.** `client.agents(id)` only creates a local handle; the first request is made by `start()` or `send()`.

### Override settings for one Run

```python
interaction = await agent.start(
    "Review this document.",
    options=wire.RunOptionsInput(
        overrides=wire.AgentOverrideInput(
            model_settings=wire.AgentOverrideInputModelSettingsType0.from_dict(
                {"extra_body": {"thinking": {"type": "enabled"}}}
            )
        )
    ),
    idempotency_key=uuid4().hex,
)
```

The provider-specific `extra_body` above is an example, not a setting supported by every model. Use values your provider accepts. An explicit `extra_body` or `extra_headers` object **replaces** the inherited object; `{}` clears it.

Other options are available without leaving the Agent workflow:

| Method    | Optional settings                                                                                   |
| --------- | --------------------------------------------------------------------------------------------------- |
| `start()` | `agent_revision_id`, `session_id`, `delivery`, `options`, `environments`, `memories`, `mcp_headers` |
| `send()`  | `agent_revision_id`, `delivery`, `options`                                                          |

`session_id` groups conversations; it does not select a hidden current Thread. Use `wire.SkillSelection(skill_id=...)` when configuring a Skill. Refer to the [generated models](../a13n/generated/models) for the complete typed settings.

## Send files and structured input

Both `start()` and `send()` accept a string or `wire.MessagePayload`. For example:

```python
payload = wire.MessagePayload(content=[wire.TextPart(type_="text", text="Summarize the attached material.")])
interaction = await agent.start(payload, idempotency_key=uuid4().hex)
```

For a local file, upload its bytes and then create an Asset:

```python
from a13n.generated.types import File

with open("report.txt", "rb") as source:
    uploaded = await client.resources.uploads.create(
        body=wire.UploadCreate(file=File(payload=source, file_name="report.txt", mime_type="text/plain")),
        idempotency_key=uuid4().hex,
    )
asset = await client.resources.assets.create(body=wire.AssetCreate(name="report.txt", upload_id=uploaded.value.upload_id))
print(asset.value.id)
```

The SDK leaves caller-owned file streams open; the `with` statement above closes the file. Use the Asset ID in the appropriate generated content-part model for your message. Uploading a file alone does not submit it to an Agent.

For a large download, consume the response inside its context:

```python
async with client.resources.assets(asset.value.id).content.get_stream() as response:
    response.raise_for_status()
    with open("downloaded-report.txt", "wb") as destination:
        async for chunk in response.aiter_bytes():
            destination.write(chunk)
```

This writes progressively, so use a new destination or a temporary file if an interrupted download must not replace existing content.

## Respond to a client-tool request

A client tool runs in your application, not in the Service. When the Agent pauses, inspect the pending requests, carry out the requested work, and send back the result. For **one client-tool completion**, given its `tool_call_id` and your `tool_result`:

```python
resumed = await outcome.run.resume(
    [wire.Complete(action="complete", tool_call_id=tool_call_id, result=tool_result)],
    idempotency_key=uuid4().hex,
)
next_outcome = await resumed.run.wait()
```

Get the ID from `outcome.pending.items`; choose the answer type for the actual request. Approval decisions use `wire.Approve` or `wire.Reject`, not `Complete`. The SDK does not approve requests or execute tools for you.

Resume creates a **new Run**. `resumed.run` observes that successor; waiting on the old Run still reports its original `waiting` state. Forking is also explicit: `run.fork(body=wire.Fork(...), idempotency_key=...)` creates a separate Thread.

## Streaming and recovery

Use the [README streaming example](../README.md#stream-progress) for one message's progress. The loop ends on `completed`, `waiting`, `failed`, or `cancelled`. Its context supports one reader and is single-use.

For a live text preview, inspect delta events. These are provisional; replace the preview from saved Items after the Run finishes or the stream reports a gap:

```python
async with interaction:
    async for frame in interaction:
        if frame.event_type == "delta":
            event = frame.data["event"]
            if event["type"] == "TEXT_MESSAGE_CONTENT":
                print(event["delta"], end="", flush=True)
        elif frame.event_type in {"gap", "reset"}:
            snapshot = await client.runs(frame.data["run_id"]).items.get()
            # Refresh your display from snapshot.value.items.
    outcome = await interaction.result()
```

The stream may omit earlier events due to retention or recovery. It is not a complete transcript, and receiving no frames does not mean the request failed. Use the outcome and saved Items to decide what happened.

### Stop listening without stopping the Agent

Breaking out of the context closes local observation. It does not call `interrupt()`. If you close before the result settles, `result()` on that Interaction will not restart the observation. Recover explicitly using saved IDs instead.

An Interaction exposes:

| Property    | Use                                                                     |
| ----------- | ----------------------------------------------------------------------- |
| `thread.id` | Continue the conversation later.                                        |
| `entry.id`  | Find the submitted message, including while it is queued.               |
| `run`       | The Run in the initial receipt, if immediately accepted; may be `None`. |
| `receipt`   | Original response body, status, headers, and request ID.                |

For a saved Run ID, use `await client.runs(run_id).wait()` or `.get()`. If the message was queued, read its inbox entry first:

```python
entry = await client.resources.threads(thread_id).inbox_entries(entry_id).get()
if entry.value.status == wire.EntryStatus.CONSUMED:
    run_id = entry.value.assigned_run_id
    if run_id is not None:
        recovered = await client.runs(run_id).wait()
```

An assigned Run can change before the Entry is consumed. The Interaction handles this automatically; manual recovery must also wait for `consumed`. It never follows a newer Run just because that Run belongs to the same Thread.

### Retry the same submission safely

Save one idempotency key per logical message, resume, fork, or upload. Reuse the same key and payload when reconciling that same operation; a different key means a new operation. The quick start generates a UUID because every execution of that example starts a new conversation.

After a connection failure, the Service may already have accepted the write. Read back saved identities and reconcile before retrying. The SDK does not automatically replay writes.

## Work with Memory

Use `client.resources.memories` to manage Memory metadata, files, revisions, and provider-backed records.

### Attach an existing Memory

```python
interaction = await agent.start(
    "Use the notes to answer my question.",
    memories=[wire.MemoryMount(name="notes", memory_id=memory_id, access=wire.MemoryAccess.READ)],
    idempotency_key=uuid4().hex,
)
```

Replace `memory_id` with an existing Memory ID. A Run keeps the mount snapshot accepted when it starts; later Thread mount edits do not rewrite that snapshot.

### Edit a file without overwriting someone else's changes

```python
file = client.resources.memories(memory_id).files("notes/project.md")
current = await file.get()
updated = await file.replace(body=wire.MemoryFileReplace(content="Updated project notes."), if_match=current.etag)
```

Pass logical paths directly, including slashes or Unicode; the SDK encodes them. If the Service returns `412`, reread and reconcile the change rather than blindly replacing the ETag and resubmitting.

Use the ETag belonging to the object you are changing:

| Change                         | ETag source         |
| ------------------------------ | ------------------- |
| Memory file content            | The file response   |
| Memory metadata                | The Memory response |
| Thread mounts or inbox changes | The Thread response |

File revisions use integer sequence numbers. Restoring a revision undoes that recorded change; restoring a file's creation can remove it. Provider-backed records have their own CRUD/search operations rather than file-style ETags. Provider accounts are managed through `client.resources.memory_providers`.

## Connection options

### Private certificate authority

Pass your CA bundle without disabling TLS verification:

```python
async with Client(service_url, api_key, ca_bundle="/path/to/ca.pem") as client:
    agents = await client.resources.agents.list(limit=10)
```

### Cookie sessions

For applications that already have a Service login session:

```python
async with Client.session(
    service_url,
    origin=console_origin,
    cookies=session_cookies,
    csrf_token=csrf_token,
    workspace_id=workspace_id,
) as client:
    agents = await client.resources.agents.list(limit=10)
```

Supply the cookies and CSRF token from your login flow. The SDK does not log in or refresh credentials. Use `client.set_csrf_token(...)` when your flow provides a new token.

Unlike API keys, cookie sessions need an explicit workspace selection for workspace resources. The SDK sends it only on the relevant routes; public and organization/admin routes do not receive it. An explicit operation header takes precedence.

`Client(service_url)` without a token is a public, cookieless client. Keep one Client open for related requests and close it with `async with` or `aclose()`.

## Use the resource API

Use the Agent workflow for conversations and `client.resources` for management and lower-level operations. Both share authentication and transport.

```python
page = await client.resources.agents.list(limit=10)
for agent_view in page.value.items:
    print(agent_view.id, agent_view.name)
```

A resource response has `.value` plus HTTP metadata: `.status_code`, `.headers`, `.etag`, `.request_id`, and `.content`. A collection's `list()` fetches one page; its `pages()` and `iter()` helpers traverse supported collections lazily.

Generated request models distinguish **omitted** (`UNSET`) from explicit null (`None`, where supported). Null does not always mean deletion.

For advanced integrations:

- [Generated resources](../a13n/generated/resources.py) and [models](../a13n/generated/models) cover the pinned API, including administration routes with explicit owner IDs.
- Generated Thread creation and inbox submission return `Result[wire.Submitted]`, not an Interaction. `text_input(text)` builds a message payload for these requests.
- `Client.execute()` exposes generated HTTP responses; `Client.stream()` opens a raw response context.
- The generated Thread `stream.get_stream()` opens the declared SSE route. `ThreadStream(client.resources.threads(thread_id))` adds Thread-wide protocol parsing, applied-cursor acknowledgement, and bounded reconnect. This is for protocol consumers, not needed for ordinary Agent interactions.

## Check against your development Service

The repository includes opt-in checks for an existing **disposable HTTPS** Service. They create resources and must not target production:

- `scripts/service-smoke.py`: messages, streaming, and file transfer.
- `scripts/service_acceptance.py`: queued messages and explicit Run controls.
- `scripts/memory_acceptance.py`: Memory files and provider-backed records.

Set `A13N_SERVICE_URL`, `A13N_API_TOKEN`, `A13N_AGENT`, and `A13N_CA_BUNDLE`. The control checks also need `A13N_CLIENT_TOOL_AGENT`; Memory checks need `A13N_MEMORY_PROVIDER` for a configured `mem0_oss` provider. These scripts do not provision the Service or credentials.

See [Contributing](../CONTRIBUTING.md) for generation and local checks. The [SDK specification](../spec/README.md) and [pinned source](../contract/source.json) record compatibility details; test success does not establish compatibility with every Service deployment.
