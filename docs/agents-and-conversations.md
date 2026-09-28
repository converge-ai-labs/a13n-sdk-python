# Agents and conversations

An Agent combines a model, instructions, and tools. Your application selects an Agent, sends it a message, and receives an Interaction. Use `start()` for a new conversation and `send()` for another message in an existing one.

If you have not connected yet, run the [quick start](../README.md#quick-start) first. The functions below take an open `Client`; call them inside that program's `async with Client(...)` block. They do not create a second connection or an event loop.

## Create your first application Agent

You can use an Agent configured in the Console, or create one in code if your credential permits Agent management. This example creates a project reviewer and returns its ID:

```python
from a13n import Client
from a13n.generated import models as wire


async def create_reviewer(client: Client, model_key: str) -> str:
    created = await client.resources.agents.create(
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
from uuid import uuid4

from a13n import Client
from a13n.generated import models as wire


async def review_plan(client: Client, agent_id: str, plan: str) -> str:
    agent = client.agents(agent_id)
    first = await agent.start(plan, idempotency_key=uuid4().hex)
    outcome = await first.result()
    if outcome.status != wire.RunStatus.COMPLETED:
        print("Review needs attention:", outcome.status)
        return first.thread.id

    messages = await outcome.run.items.get()
    print(messages.value.to_dict())

    follow_up = await agent.send(
        first.thread.id,
        "Turn your recommendation into three implementation steps.",
        idempotency_key=uuid4().hex,
    )
    next_outcome = await follow_up.result()
    print("Follow-up:", next_outcome.status)
    next_messages = await next_outcome.run.items.get()
    print(next_messages.value.to_dict())
    return first.thread.id
```

Both messages belong to the same Thread but produce separate executions. A Thread is not permanently bound to an Agent: every `send()` explicitly selects one. Keep that selection in your application rather than relying on a hidden “current Agent.”

The example prints saved Items, including messages and tool activity. To display assistant text only, use the filtering loop in the quick start. A `waiting` result is not a failed request; it needs the [input or tool workflow](waiting-and-tools.md).

For each **new** message, generate a new idempotency key. For a retry of the **same** message, reuse its original key and payload. Production applications should persist them before submission; see [recovery](errors-and-recovery.md#retry-a-submission-with-an-unknown-outcome).

## Supply structured input

A string is convenient for plain text. A `MessagePayload` lets you combine text with JSON or an uploaded Asset:

```python
from uuid import uuid4

from a13n import Client, RunOutcome
from a13n.generated import models as wire


async def review_budget(client: Client, agent_id: str) -> RunOutcome:
    payload = wire.MessagePayload(
        content=[
            wire.TextPart(type_="text", text="Identify the largest budget risk."),
            wire.JsonPart(type_="json", value={"currency": "USD", "budget": 5000, "weeks": 4}),
        ]
    )
    interaction = await client.agents(agent_id).start(payload, idempotency_key=uuid4().hex)
    return await interaction.result()
```

`send()` accepts the same payload type. See [files and Memory](files-and-memory.md) for an upload-to-message example; uploading bytes alone does not attach them to a conversation.

## Change settings for one execution

Use `options` when a particular request needs different settings without changing the saved Agent. This example selects another configured Model key for one review:

```python
from uuid import uuid4

from a13n import Client, RunOutcome
from a13n.generated import models as wire


async def detailed_review(client: Client, agent_id: str, model_key: str, plan: str) -> RunOutcome:
    interaction = await client.agents(agent_id).start(
        plan,
        options=wire.RunOptionsInput(overrides=wire.AgentOverrideInput(model=model_key)),
        idempotency_key=uuid4().hex,
    )
    return await interaction.result()
```

Other typed settings include instructions, client tools, Skills, and model settings. Use `wire.SkillSelection(skill_id=...)` for a Skill. Provider-specific settings must be supported by your chosen provider; the SDK does not translate arbitrary provider options.

For `model_settings.extra_body` and `extra_headers`, an explicit object replaces the inherited object rather than recursively merging it. An empty object clears it. See [omitted and null values](resources.md#omitted-null-and-empty-values) before building dynamic patches.

| Selection                                | Use it when                                                                                                     |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `agent_revision_id`                      | You need a particular saved Agent revision rather than the current selection.                                   |
| `session_id` on `start()`                | You want to group conversations. It does not choose an existing Thread.                                         |
| `memories` / `environments` on `start()` | The new conversation needs explicit mounts.                                                                     |
| `delivery`                               | You need an explicit message-delivery policy. Keep the default unless your application requires another policy. |

The full request types live in [generated models](../a13n/generated/models). For ordinary conversations, keep using `start()` and `send()` rather than assembling low-level Thread submissions yourself.

## Next

[Stream progress and read results](streaming-and-results.md) adds a live display to this workflow without changing how you submit messages.
