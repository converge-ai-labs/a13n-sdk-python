# Agents and conversations

An Agent combines a model, instructions, and tools. Your application selects an Agent, sends it a message, and receives an Interaction. Use `start()` for a new conversation and `send()` for another message in an existing one.

If you have not connected yet, run the [quick start](../README.md#quick-start) first. The functions below take an open `Client`; call them inside that program's `async with Client(...)` block. They do not create a second connection or an event loop.

## Create your first application Agent

You can use an Agent configured in the Console, or create one in code if your credential permits Agent management. This example creates a project reviewer and returns its ID:

```python
from a13n import Client
from a13n.generated import models as wire


async def create_reviewer(client: Client, model_key: str) -> str:
    created = await client.api.agents.create(
        body=wire.AgentCreate(
            name="Project reviewer",
            config=wire.AgentConfigInput(
                model=model_key,
                instructions="Review project plans. State the biggest risk and suggest one concrete next step.",
            ),
        )
    )
    print("Created Agent:", created.value.id)
    return created.value.id
```

Pass a **configured Model key** from your workspace as `model_key`, not a provider model name copied from another service. Agents and Skills are selected by IDs; Models are selected by keys. Model credentials and availability are managed on the Service, not in this Client.

Save the returned Agent ID. Creating a new Agent on every application request is unnecessary; `client.agents(agent_id)` cheaply binds an existing ID without a network call.

## Ask, then continue

Here is a complete two-message workflow. It returns the conversation ID so your application can store it alongside its own chat record:

```python
from a13n import Client


async def review_plan(client: Client, agent_id: str, plan: str) -> str:
    agent = client.agents(agent_id)
    first = await agent.start(plan)
    outcome = await first.result()
    if outcome.status != "completed":
        print("Review needs attention:", outcome.status)
        return first.thread.id

    print(outcome.text if outcome.text is not None else outcome.output)

    follow_up = await agent.send(
        first.thread.id,
        "Turn your recommendation into three implementation steps.",
    )
    next_outcome = await follow_up.result()
    print("Follow-up:", next_outcome.status)
    print(next_outcome.output)
    return first.thread.id
```

Both messages belong to the same Thread but produce separate executions. A Thread is not permanently bound to an Agent: every `send()` explicitly selects one. Keep that selection in your application rather than relying on a hidden “current Agent.”

The example prints authoritative output directly. String output also has `outcome.text`; structured output stays structured. Saved Items are advanced bounded display, not the final-output owner. A `waiting` result is not a failed request; it needs the [input or tool workflow](waiting-and-tools.md).

For each **new** message, omit the key for an SDK-generated one or select a new application key. For a retry of the **same** message, reuse its original key and payload. Production applications should persist them before submission; see [recovery](errors-and-recovery.md#retry-a-submission-with-an-unknown-outcome).

## Import an existing model conversation

Only `start()` can seed a new Thread with model history. Supply native Pydantic AI model-message JSON objects (for example, from an application's independently installed Pydantic AI serializer), not SDK-specific message classes or a prompt transcript:

```python
from uuid import uuid4

from a13n import Client


async def continue_existing_chat(client: Client, agent_id: str) -> str:
    history = [
        {"kind": "request", "parts": [{"part_kind": "user-prompt", "content": "What is a prime?"}]},
        {"kind": "response", "parts": [{"part_kind": "text", "content": "A prime has two positive divisors."}]},
    ]
    interaction = await client.agents(agent_id).start(
        "Is 11 prime?", message_history=history, idempotency_key=uuid4().hex
    )
    assert interaction.thread is not None
    readback = await interaction.thread.get()
    assert readback.value.id == interaction.thread.id
    return interaction.thread.id
```

The Service validates native history (completed text or closed tool-call/result exchanges), including its 256-message and 262144-byte limits. The SDK does not re-validate, translate, discard metadata or require Pydantic AI to be installed. Thread readback returns Thread metadata, not the imported history; retain your source JSON when you need it. The initial model context uses this seed once; later `send()` calls, resume and forks never submit it again. Import does not create historical Runs, inbox messages or usage. Preserve the same history and idempotency key if retrying the initial submission after an uncertain response.

## Supply structured input

A string is convenient for plain text. An ordered sequence combines strings with public `TextPart`, `JsonPart`, `UrlPart` and `AssetPart` values; constructors supply their wire discriminators:

```python
from a13n import Client, JsonPart, RunOutcome


async def review_budget(client: Client, agent_id: str) -> RunOutcome:
    interaction = await client.agents(agent_id).start(
        [
            "Identify the largest budget risk.",
            JsonPart({"currency": "USD", "budget": 5000, "weeks": 4}),
        ]
    )
    return await interaction.result()
```

`send()`, resume input and fork accept the same public input. See [files and Memory](files-and-memory.md) for an upload-to-message example; uploading bytes alone does not attach them to a conversation.

## Change settings for one execution

Use `options` when a particular request needs different settings without changing the saved Agent. This example selects another configured Model key for one review:

```python
from a13n import AgentOverride, Client, RunConfiguration, RunOptions, RunOutcome, UsageLimit


async def detailed_review(client: Client, agent_id: str, model_key: str, plan: str) -> RunOutcome:
    interaction = await client.agents(agent_id).start(
        plan,
        options=RunOptions(
            configuration=RunConfiguration(allowed_hosts=[], extensions={"example.policy": {"enabled": False}}),
            overrides=AgentOverride(model=model_key, model_settings={"extra_body": {}}),
            labels={"purpose": "review"},
            max_usage=UsageLimit(10),
        ),
    )
    return await interaction.result()
```

`AgentOverride` exposes every selectable field: builtin_skills, client_tools, connection_tools, instructions, lazy_environment, media_understanding, model, model_characteristics, model_settings, output_spec, platform_tools, plugins, retries, reviewer, skill_sync, skills, subagents and toolsets. Nested schema objects are native JSON mappings, for example `skills=[{"skill_id": skill_id}]` or `output_spec={"schema": {"type": "object"}}`. This avoids a second generated-model hierarchy. Provider-specific settings must be supported by the chosen provider; the SDK does not translate provider options.

Public `UNSET` preserves omission. Nullable fields accept `None`, and empty lists/mappings remain explicit. `RunConfiguration(allowed_hosts=None)` is unrestricted; `allowed_hosts=[]` denies native URL access. `RunOptions(configuration=RunConfiguration())` sends an explicit empty snapshot. No adapter inserts defaults or merges policy.

For `model_settings.extra_body` and `extra_headers`, an explicit object replaces the inherited object rather than recursively merging it. An empty object clears it. See [omitted and null values](resources.md#omitted-null-and-empty-values) before building dynamic patches.

| Selection                                | Use it when                                                                                                     |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `agent_revision_id`                      | You need a particular saved Agent revision rather than the current selection.                                   |
| `session_id` on `start()`                | You want to group conversations. It does not choose an existing Thread.                                         |
| `memories` / `environments` on `start()` | The new conversation needs explicit mounts.                                                                     |
| `delivery`                               | You need an explicit message-delivery policy. Keep the default unless your application requires another policy. |

Public `MountCreate(name, environment_id, working_directory=UNSET, permission_ceiling=UNSET)` and `MemoryMount(name, memory_id, access, recall=UNSET)` cover initial mounts; `mcp_headers` is a native mapping. The full management request types remain in [generated models](../a13n/generated/models). Ordinary conversations use `start()` and `send()`.

A Session also owns native [Memory Space selection](files-and-memory.md#share-notes-through-a-memory-space). Creating or updating `SessionMemorySettings` is separate from selecting an existing Thread. The Service settles unresolved Agent memory defaults on the first accepted business Run; a later Agent edit does not rewrite the Session selection.

## Next

[Stream progress and read results](streaming-and-results.md) adds a live display to this workflow without changing how you submit messages.
