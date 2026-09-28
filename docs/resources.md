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
