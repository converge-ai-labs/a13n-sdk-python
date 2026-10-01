# The resource API

The Agent workflow is designed for conversations. `client.resources` is the complete, generated API for management and lower-level operations: Agents, Models, Skills, files, Memory, Threads, and administration. Both use the same Client and credentials.

Use this chapter when you need to list or edit resources, inspect HTTP metadata, or work with a Service operation that is not part of `start()` / `send()`.

## Find a resource and inspect its response

Generated collection methods return a typed value together with the HTTP evidence for that request:

```python
from a13n import Client


async def find_agents(client: Client, query: str) -> None:
    response = await client.resources.agents.list(q=query, limit=10)
    for agent in response.value.items:
        print(agent.id, agent.name)
    print("HTTP status:", response.status_code)
    print("Request ID:", response.request_id)
    print("More available:", response.value.next_cursor is not None)
```

A `Result[T]` exposes:

| Property      | Purpose                                                                            |
| ------------- | ---------------------------------------------------------------------------------- |
| `value`       | Parsed model, page, or operation result.                                           |
| `status_code` | Actual successful HTTP status, including distinctions such as creation and replay. |
| `headers`     | Response headers when you need protocol metadata.                                  |
| `etag`        | Version token for operations that support conditional changes.                     |
| `request_id`  | Correlate a request with Service diagnostics.                                      |
| `content`     | Response bytes retained by an ordinary buffered request.                           |

Use generated model attributes in your application. Call `to_dict()` when serializing or inspecting their wire representation. Do not print entire responses in production logs if they may contain sensitive content.

## Traverse more than one page

`list()` performs one request. `iter()` yields individual resources, fetching additional pages only as you consume them:

```python
from a13n import Client


async def print_agent_directory(client: Client) -> None:
    async for agent in client.resources.agents.iter(limit=50):
        print(agent.id, agent.name)
```

Here `limit=50` is the page size, not a cap of fifty total results. Break the loop if your application only needs the first match. If you need page metadata, use `pages()` instead:

```python
from a13n import Client


async def inspect_agent_pages(client: Client) -> None:
    async for page in client.resources.agents.pages(limit=50):
        print("Page request:", page.request_id, "Items:", len(page.value.items))
```

Cursor pagination is not a transaction across the entire collection. If your application needs a durable export, account for concurrent changes and the Service's retention rules rather than assuming page traversal freezes the dataset.

## Make a conditional edit

Suppose your application lets a user rename an Agent. Read the resource before editing and pass that response's ETag:

```python
from a13n import Client
from a13n.generated import models as wire


async def rename_agent(client: Client, agent_id: str, name: str) -> None:
    resource = client.resources.agents(agent_id)
    current = await resource.get()
    updated = await resource.update(body=wire.AgentUpdate(name=name), if_match=current.etag)
    print("Renamed:", updated.value.name, "ETag:", updated.etag)
```

A `412` means the version you edited is no longer current. Return that conflict to the user or reconcile the new value with their edit. Do not silently read another ETag and force the old change through.

ETags belong to particular resources. An Agent ETag is not interchangeable with a Thread or Memory-file ETag. [Memory editing](files-and-memory.md#update-a-note-without-losing-another-writers-changes) uses the same pattern at the file boundary.

## Omitted, null, and empty values

Generated requests preserve distinctions that matter to partial updates:

- Leaving a field at `UNSET` omits it from the request.
- `None` sends JSON `null` when the field permits it. Its meaning is defined by that operation, not by a universal “delete” rule.
- An empty object or list is an explicit value, not omission.

You can inspect the difference locally without sending a request:

```python
from a13n.generated import models as wire

unchanged = wire.AgentUpdate()
explicit_null = wire.AgentUpdate(description=None)
empty_text = wire.AgentUpdate(description="")

print(unchanged.to_dict())  # {}
print(explicit_null.to_dict())  # {"description": None}
print(empty_text.to_dict())  # {"description": ""}
```

Do not remove `None` from a request dictionary simply to make it look cleaner; that can change its semantics. Likewise, avoid replacing every omitted field with `None` when mapping an application form into a generated model.

For arbitrary object fields, generated models provide `from_dict()`. For example, setting a Run override's `extra_body` to `{}` explicitly clears the inherited object:

```python
from a13n.generated import models as wire

settings = wire.AgentOverrideInputModelSettingsType0.from_dict({"extra_body": {}})
options = wire.RunOptionsInput(overrides=wire.AgentOverrideInput(model_settings=settings))
print(options.to_dict())
```

An explicit `extra_body` or `extra_headers` object replaces the inherited object; it is not recursively merged. Keep provider-specific keys within those provider-specific settings rather than adding unsupported top-level fields.

## Forward native Model settings

A Model's `config.settings` is an open native JSON object, not a second SDK-defined hierarchy. Use the generated mapping wrapper to preserve provider-specific JSON values:

```python
from a13n.generated import models as wire


def model_config(model_api: str, model_name: str) -> wire.ModelConfigInput:
    return wire.ModelConfigInput(
        model_api=model_api,
        model_name=model_name,
        settings=wire.ModelConfigInputSettings.from_dict({"seed": 42, "timeout": 30}),
    )
```

Use this config with `wire.ModelCreate` or `wire.ModelUpdate`. Supported native keys and conflict resolution with explicit config fields belong to the Service and installed provider. Nested objects, arrays, booleans, numbers and null values are forwarded unchanged and retained in Model readback. Omitting `settings` differs from explicitly supplying `{}`; the SDK does not fill provider defaults or validate provider policy.

## Forward image and video policy

Media preparation belongs to Service/Harness, not Model settings or SDK processing. Set native characteristics on a Model config:

```python
from a13n.generated import models as wire

config = wire.ModelConfigInput(
    model_api="your-installed-api",
    model_name="your-model",
    characteristics=wire.HarnessModelCharacteristicsInput(
        image_input=wire.ImageInputPolicy(max_images=4, split_large_images=False),
        video_input=wire.VideoInputPolicy(max_video_bytes=8_000_000),
        url_input=wire.UrlInputSupportInput(video=[wire.VideoUrlType.YOUTUBE]),
    ),
)
```

Use it in `wire.ModelCreate` or `wire.ModelUpdate`. Omitted `image_input` uses native defaults; `image_input=None` disables automatic preparation. Zero limits, false flags and `video=[]` remain explicit values. The Service enforces byte budgets, URL support, host restrictions and TLS; the SDK does not inspect or transform media.

## Select a native Run configuration

Pass configuration through existing typed `options` on `start()` and `send()`; generated `wire.Message` uses the same shape:

```python
from a13n import Client
from a13n.generated import models as wire


async def restricted_input(client: Client, agent_id: str) -> None:
    options = wire.RunOptionsInput(
        configuration=wire.RunConfigurationInput(
            allowed_hosts=["media.example.test"],
            extensions=wire.RunConfigurationInputExtensions.from_dict(
                {"example.policy": {"enabled": False, "limits": [], "note": None}}
            ),
        )
    )
    payload = wire.MessagePayload(
        content=[
            wire.TextPart(type_="text", text="Describe this image and video."),
            wire.UrlPart(type_="url", url="https://media.example.test/image.png"),
            wire.UrlPart(type_="url", url="https://media.example.test/video.mp4"),
        ]
    )
    interaction = await client.agents(agent_id).start(payload, options=options, idempotency_key="media-001")
    outcome = await interaction.result()
    print(outcome.snapshot.value.options.configuration)
```

An explicit configuration object is a complete snapshot, not a merge with hidden SDK defaults or revision overrides. `configuration=UNSET` omits it, `configuration=None` sends null, and `wire.RunConfigurationInput()` sends `{}`. Omission/null select the native default for a new Run and retain the accepted snapshot when steering. `allowed_hosts=None` is unrestricted; `allowed_hosts=[]` denies every native URL destination. Extensions are arbitrary namespaced JSON, not SDK policy.

The Service normalizes/freezes the accepted configuration. Steering and pending edits against an active Run may omit it or match the frozen value; a different explicit snapshot returns `409 conflict` with reason `run_configuration_immutable`. The SDK does not auto-queue or retry that request. `delivery=wire.Delivery.NEXT_RUN` selects a new snapshot, while resume successors and inline children inherit their source's configuration.

## Model Provider authorization and discovery

Use the generated Provider graph with an existing Client:

```python
from a13n import Client
from a13n.generated import models as wire


async def begin_provider_authorization(client: Client, provider_id: str, workspace_id: str) -> wire.AuthorizationStart:
    provider = client.resources.model_providers(provider_id)
    await provider.authorization.get(x_workspace_id=workspace_id)
    started = await provider.authorize(
        body=wire.ProviderAuthorizationRequest(new_registration=False), x_workspace_id=workspace_id
    )
    return started.value  # Hand the returned URL/method to your application's authorized user; do not log it.


async def complete_manual_authorization(
    client: Client, provider_id: str, workspace_id: str, attempt_id: str, callback_url: str
) -> None:
    await client.resources.model_providers(provider_id).authorization.callback(
        body=wire.AuthorizationCallback(attempt_id=attempt_id, callback_url=callback_url),
        x_workspace_id=workspace_id,
    )


async def discover_provider_models(client: Client, provider_id: str, workspace_id: str) -> list[wire.ChatGPTModel]:
    return (await client.resources.model_providers(provider_id).models.get(x_workspace_id=workspace_id)).value
```

Follow the returned `method`: `manual_callback` accepts a pasted callback through `authorization.callback`; `browser_callback` uses the operator-configured hosted flow and status polling. Do not hardcode callback origins, client identity or port, print callback codes, or store Provider tokens. Starting hosted browser authorization requires an unconfined user login, but manual Workspace authorization can use an authorized API key. Service permissions are `read` for status, `write` for authorize/callback/disconnect, and `run` for discovery; the SDK does not replace these checks. OAuth is workspace-shared Provider state, not a personal Connection or a new Client credential.

`await provider.authorization.delete(...)` clears local Provider tokens and reports external revocation separately through nullable `revocation_confirmed`. Treat unknown exchange/revocation outcomes as reported facts, not permission to replay mutations. Hosted callback setup and issuer approval are operator responsibilities.

## Choose the right level

| Task                                               | Preferred entry point                                                  |
| -------------------------------------------------- | ---------------------------------------------------------------------- |
| Start or continue a conversation                   | `client.agents(id).start(...)` / `.send(...)`                          |
| Wait for a known execution or resume a waiting one | `client.runs(id)`                                                      |
| Create or edit an Agent                            | `client.resources.agents`                                              |
| Manage files, Memory, or administrative resources  | The corresponding `client.resources` collection                        |
| Build a protocol integration                       | Generated request modules, `Client.execute()`, or raw response streams |

Generated Thread creation and inbox submission return `Result[wire.Submitted]`, not an Interaction. They perform the declared request and do not adopt the higher-level observation lifecycle. Prefer the Agent workflow unless your integration needs to own that protocol itself.

The [generated resources](../a13n/generated/resources.py) expose operation signatures, and [generated models](../a13n/generated/models) describe request and response fields. The [pinned source](../contract/source.json) identifies the Service contract used to generate them. A complete generated surface does not grant a credential permission to invoke every operation.

[Back to the guide](README.md) · [Next: errors and recovery](errors-and-recovery.md)
