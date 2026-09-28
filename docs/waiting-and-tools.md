# Waiting, approvals, and client tools

Some tasks cannot finish in one execution. An Agent may need a person's approval, an answer to a question, or a result from a tool that runs in your application. In each case the Interaction ends with `waiting`, and your application decides how to proceed.

This chapter assumes you already have an outcome from `await interaction.result()`. See [Agent configuration](agents-and-conversations.md) if you need to create an Agent first.

## Show what the Agent is asking for

Do not treat every pending item as a tool you should execute. Read its kind, name, and arguments before presenting an action:

```python
from a13n import RunOutcome
from a13n.generated import models as wire


def show_requests(outcome: RunOutcome) -> None:
    if outcome.status != wire.RunStatus.WAITING or outcome.pending is None:
        return
    for item in outcome.pending.items:
        print("Request:", item.tool_call_id)
        print("Kind:", item.kind, "Tool:", item.tool_name)
        print("Arguments:", item.arguments.to_dict())
```

Use `tool_call_id` to associate your response with the correct request. There can be more than one item. Your UI should retain the Run ID and the request IDs, not just show an undifferentiated “Continue” button.

| Pending kind  | Application responsibility                                                           | Answer model                               |
| ------------- | ------------------------------------------------------------------------------------ | ------------------------------------------ |
| `approval`    | Show the proposed action and collect a real decision.                                | `Approve` or `Reject`                      |
| `client_tool` | Validate and run an application-owned tool, then supply its result.                  | `Complete`                                 |
| `user_input`  | Collect the person's reply. A question-only wait continues with an ordinary message. | `agent.send(...)`, not a structured answer |

The SDK does not approve actions, run local tools, or answer questions on your behalf. A `user_input` item accepts no structured resume answer. For a question-only wait (every pending item is `user_input`), send the person's reply as a normal message on the same Thread; the Service starts a successor with that message. Ordinary text never grants an approval or completes a client tool.

## Resume after an approval decision

This helper takes a decision your application has already collected. It handles exactly one pending approval, then observes the newly created execution. For multiple pending requests, collect the entire batch first: omitted approvals are rejected, and omitted tool results or questions become `no_response`. A partial batch does not leave the other requests open.

```python
from uuid import uuid4

from a13n import RunOutcome
from a13n.generated import models as wire


async def answer_approval(outcome: RunOutcome, tool_call_id: str, approved: bool) -> RunOutcome:
    if outcome.status != wire.RunStatus.WAITING or outcome.pending is None:
        raise ValueError("The Run is not waiting for an answer")
    if len(outcome.pending.items) != 1:
        raise ValueError("This example requires exactly one pending request; collect a full batch otherwise")
    request = next((item for item in outcome.pending.items if item.tool_call_id == tool_call_id), None)
    if request is None or request.kind != wire.PendingKind.APPROVAL:
        raise ValueError("Select a pending approval request")

    answer: wire.Approve | wire.Reject
    if approved:
        answer = wire.Approve(action="approve", tool_call_id=tool_call_id)
    else:
        answer = wire.Reject(action="reject", tool_call_id=tool_call_id, reason="Declined by the reviewer")
    resumed = await outcome.run.resume([answer], idempotency_key=uuid4().hex)
    print("Successor Run:", resumed.run.id)
    return await resumed.run.wait()
```

A successful resume creates a **different Run**. Waiting on the original Run still returns its original `waiting` state. Save `resumed.run.id` if the application must continue observing after a restart. The successor may itself return `waiting`; process the new outcome rather than automatically accepting further requests.

The UUID is suitable for this one-shot example. In an application, persist a resume operation's key and answer payload before sending, just as you would for a message submission.

## Declare a client tool

A client tool is useful when the Agent needs data or actions that belong to your application. For example, an order-support Agent can request an order status without receiving direct database credentials.

This function creates an Agent with one read-only tool definition. Replace `model_key` with a configured Model key:

```python
from a13n import Client
from a13n.generated import models as wire


async def create_order_assistant(client: Client, model_key: str) -> str:
    created = await client.resources.agents.create(
        body=wire.AgentCreate(
            name="Order assistant",
            config=wire.AgentConfigInput(
                model=model_key,
                instructions="Use lookup_order for order status. Do not invent a status.",
                client_tools=[
                    wire.ClientToolDefinition(
                        name="lookup_order",
                        description="Read the current status of an order visible to this customer.",
                        parameters_json_schema=wire.ClientToolDefinitionParametersJsonSchema.from_dict(
                            {
                                "type": "object",
                                "properties": {"order_id": {"type": "string"}},
                                "required": ["order_id"],
                                "additionalProperties": False,
                            }
                        ),
                    )
                ],
            ),
        )
    )
    return created.value.id
```

The definition describes the tool; it does not register a Python callback. When that tool is requested, the Service pauses and returns the request to your application. Workspace and Agent permission policy may require an approval before the client-tool completion step.

## Return an application-owned tool result

After authenticating the application user, checking their access to the requested order, and reading your database, pass the result to a helper like this:

```python
from uuid import uuid4

from a13n import RunOutcome
from a13n.generated import models as wire


async def complete_order_lookup(outcome: RunOutcome, tool_call_id: str, order_id: str, status: str) -> RunOutcome:
    if outcome.status != wire.RunStatus.WAITING or outcome.pending is None:
        raise ValueError("No waiting tool request")
    if len(outcome.pending.items) != 1:
        raise ValueError("This example requires exactly one pending request; collect a full batch otherwise")
    request = next((item for item in outcome.pending.items if item.tool_call_id == tool_call_id), None)
    if request is None or request.kind != wire.PendingKind.CLIENT_TOOL or request.tool_name != "lookup_order":
        raise ValueError("Select a lookup_order client-tool request")
    if request.arguments.to_dict().get("order_id") != order_id:
        raise ValueError("The result does not belong to the requested order")

    resumed = await outcome.run.resume(
        [
            wire.Complete(
                action="complete",
                tool_call_id=tool_call_id,
                result={"order_id": order_id, "status": status},
            )
        ],
        idempotency_key=uuid4().hex,
    )
    return await resumed.run.wait()
```

Only dispatch tool names that your application implements. Validate arguments and authorization before performing the action; a well-formed model-generated request is not authorization. For tools with side effects, store the execution result by request ID so reconciling a network failure does not perform the business action twice.

The returned outcome can be displayed with the [saved-result example](streaming-and-results.md#read-a-finished-response). A tool result is input to the successor Run, not necessarily the final user-facing answer.

## Reply to a question

When all pending items are questions, collect the person's response and send it on the same Thread:

```python
from uuid import uuid4

from a13n import Client, RunOutcome
from a13n.generated import models as wire


async def reply_to_questions(client: Client, agent_id: str, outcome: RunOutcome, reply: str) -> RunOutcome:
    if outcome.status != wire.RunStatus.WAITING or outcome.pending is None or not outcome.pending.items:
        raise ValueError("The Run is not waiting for questions")
    if any(item.kind != wire.PendingKind.USER_INPUT for item in outcome.pending.items):
        raise ValueError("Handle approvals and client tools explicitly before sending an ordinary reply")
    interaction = await client.agents(agent_id).send(
        outcome.snapshot.value.thread_id, reply, idempotency_key=uuid4().hex
    )
    return await interaction.result()
```

The Service closes those question calls without fabricated structured results and incorporates the person's message once. For a mixed pending set, use the [Run contract](../contract/semantics/runs.md) to design an explicit answer batch; do not guess a generic completion action.

## Branch instead of resuming

Resume continues a waiting execution on its existing Thread. Forking has a different purpose: `run.fork(body=wire.Fork(...), idempotency_key=...)` creates a separate Thread from a selected point. It is not a substitute for answering an approval or a way to make the old Run change state.

[Back to the guide](README.md) · [Next: files and Memory](files-and-memory.md)
