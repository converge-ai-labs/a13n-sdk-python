# Waiting, approvals, questions, and client tools

A finite Interaction ends at `waiting` if its Run has deferred calls or desktop control has paused execution. Your application must collect **all** decisions and results for that exact waiting Run before resuming it. It does not automatically approve actions, execute client tools, or answer questions.

## Inspect the complete pending batch

```python
from a13n import Approve, Deny, Failed, Returned, RunOutcome


def show_requests(outcome: RunOutcome) -> None:
    if outcome.status != "waiting" or outcome.pending is None:
        return
    for approval in outcome.pending.approvals:
        print("Approval:", approval.tool_call_id, approval.tool_name, approval.arguments)
    for call in outcome.pending.calls:
        print("Call:", call.tool_call_id, call.tool_name, call.arguments)
```

`pending.approvals` require `Approve` or `Deny`. `pending.calls` include application-owned tools, built-in questions such as `ask_user_question`, and custom human-operated tools; supply `Returned` with a JSON value or `Failed` with a reason. The `tool_call_id` is the map key, not a field inside the decision. Preserve the waiting Run ID and all request IDs in your application.

## Submit a complete answer batch

```python
from uuid import uuid4

from a13n import Approve, Deny, Failed, Returned, RunOutcome


async def decide_one_approval(outcome: RunOutcome, approved: bool) -> RunOutcome:
    if outcome.status != "waiting" or outcome.pending is None:
        raise ValueError("Run is not waiting")
    if len(outcome.pending.approvals) != 1 or outcome.pending.calls:
        raise ValueError("This example handles exactly one approval")
    call_id = outcome.pending.approvals[0].tool_call_id
    decision = Approve() if approved else Deny("Declined")
    resumed = await outcome.run.resume({call_id: decision}, idempotency_key=uuid4().hex)
    print("Successor Run:", resumed.run.id)
    return await resumed.result()
```

The Service accepts **no omission defaults or partial answers**. Pass one answer map covering all pending IDs. The SDK splits approvals and calls into both wire maps in one request, including empty categories; Service alone validates completeness and category matching. Missing, unexpected, or category-mismatched IDs reject the *whole* request. Do not infer that omission denies a request or produces a default failed result. A successful resume produces a **different Run**; observing the old Run still yields `waiting`. Save the new ID and persist the idempotency key and complete answer payload before submission if a network failure may require reconciliation.

Your application owns answer collection, draft persistence and when to submit. Service accepts up to 128 combined answers within its 262144-byte canonical body bound. A desktop-only wait accepts an explicit empty batch after stored control completion; pending tool calls and approvals still require full coverage. Invalid coverage or question values raise a known `ApiError`; the batch creates no successor. A repeated identical explicit request under the same key returns the same successor, while a changed body conflicts. The SDK performs one mutation request per invocation and never retries it automatically. Pending approvals may retain presentation metadata; pending calls carry tool name and arguments without question presentation.

## Declare a client tool

A client tool lets the Agent request data or actions belonging to your application without receiving direct database credentials. The Agent configuration defines the name, description and parameter schema:

```python
from a13n import Client
from a13n.generated import models as wire


async def create_order_assistant(client: Client, model_key: str) -> str:
    created = await client.api.agents.create(
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

The definition does not register a Python callback. The Service pauses and returns the call to your application; workspace and Agent permission policy may require an approval before a tool result is returned.

## Return an application-owned tool result

Your application authenticates the caller, checks arguments and authorization, executes the work, and explicitly returns the result. For one `lookup_order` call with no approval:

```python
from uuid import uuid4

from a13n import Approve, Deny, Failed, Returned, RunOutcome


async def return_order_status(outcome: RunOutcome, order_id: str, status: str) -> RunOutcome:
    if outcome.status != "waiting" or outcome.pending is None:
        raise ValueError("Run is not waiting")
    if outcome.pending.approvals or len(outcome.pending.calls) != 1:
        raise ValueError("This example handles exactly one call")
    call = outcome.pending.calls[0]
    if call.tool_name != "lookup_order" or call.arguments.get("order_id") != order_id:
        raise ValueError("Unexpected request")
    result = Returned({"order_id": order_id, "status": status})
    resumed = await outcome.run.resume({call.tool_call_id: result}, idempotency_key=uuid4().hex)
    return await resumed.result()
```

For tools with side effects, store the application execution result by request ID so uncertain network outcomes do not cause duplicate business actions. `Failed("...")` supplies a native failed call result; an error-shaped JSON object inside `Returned` is still a successful return.

## Answer a question and optionally add a message

A built-in `ask_user_question` is a **call**, not an ordinary message request. Match its exact ID and supply a `Returned` value in the Harness `UserQuestionAnswers` shape: `{"answers": {question_text: selection}}`, optionally with `"response": "free text"`. The Service validates the result against that call's arguments. An intentional skip is `Failed("No response was given")`. Do not send an ordinary message to resolve a waiting question.

```python
from a13n import Returned

answer = Returned({"answers": {"Which option?": "A"}})
resumed = await outcome.run.resume(
    {question.tool_call_id: answer},
    input="Additional context after answering the question.",
    idempotency_key=uuid4().hex,
)
```

`input` is optional ordinary user content submitted **atomically with all answers** to the successor Run. It can be a string or ordered public text, JSON, Asset or URL parts. Omitting `input` leaves the field absent; `input=None` explicitly sends null. `Returned(None)` explicitly supplies JSON null; omitting a value is not an answer. `Deny()` omits its reason while `Deny(None)` and `Deny("")` preserve null and empty string. It cannot fill missing call results, answer a question by itself, or authorize an approval. The SDK performs one resume request, not a resume followed by `send()`. The returned Interaction has no fabricated Entry; `.run` is its exact successor, `.receipt` retains the resume HTTP evidence, and `.result()`, native iteration and `.text_stream()` use the same finite observer. The successor may wait again; inspect its own pending batch instead of automatically resolving it.

## Inspect and complete desktop control

Desktop waits are distinct from ordinary client tools. Inspect `outcome.evidence.value.wait_reason` and `outcome.pending.desktop_control_id`. A user-control wait can contain empty calls and approvals. Completion records cleanup and readiness; **resume remains a separate explicit command**:

```python
from a13n import Client, RunOutcome
from a13n.generated import models as wire


async def complete_user_control(
    client: Client,
    outcome: RunOutcome,
    browser_session: str,
    epoch: int,
    resume_key: str,
) -> str:
    pending = outcome.pending
    if pending is None or not isinstance(pending.desktop_control_id, str):
        raise ValueError("No desktop control wait")
    if pending.calls or pending.approvals:
        raise ValueError("This example handles a desktop-only wait")
    control = client.api.desktop_assistance(pending.desktop_control_id)
    completed = await control.complete(
        body=wire.Completion(session_id=browser_session, epoch=epoch, outcome=wire.CompletionOutcome.COMPLETED),
    )
    if completed.value.state != "ready_to_resume":
        raise ValueError("Desktop cleanup is not ready")
    successor = await outcome.run.resume({}, idempotency_key=resume_key)
    assert successor.run is not None
    return successor.run.id
```

`browser_session` is an application-generated 20–72-character token using letters, digits, `_` or `-`, **not** a Service Session resource ID. Epoch is the current nonnegative desktop epoch. Obtain both from your application's explicit desktop access flow:

```python
from a13n import Client
from a13n.generated import models as wire


async def open_desktop_view(client: Client, run_id: str, browser_session: str) -> wire.Access:
    opened = await client.api.runs(run_id).desktop_control.create(
        body=wire.Request(mount="computer", reason="Finish sign in"),
    )
    return (
        await client.api.desktop_assistance(opened.value.id).view(
            body=wire.Control(session_id=browser_session, epoch=opened.value.epoch),
        )
    ).value
```

Opening creates a viewing context without reserving execution. `desktop_assistance(id).request_control()` explicitly requests suspension and may return preparing; read the Run and native metadata before requesting a control grant with `.control(body=Control(...))`. Metadata reads use `runs(id).desktop_control.get()` (nullable) or, for an Agent assistance call, `runs(id).desktop_assistance(call_id).get()`. Access requires current Service execution authority, the frozen mount and a matching provider generation. Keep the no-store `Access.websocket_url` and password private; the SDK launches no browser and renews no lease automatically.

For **Agent-requested assistance**, complete the assistance resource first, then return its **exact persisted outcome** under that deferred call ID together with every other pending answer. Do not turn a user-control ID into a synthetic call result. Mixed waits still require all real calls and approvals. `.disconnect(body=Control(...))` releases the caller's browser access without completing assistance; local disconnection, lease expiry and observation cancellation do not resume execution. Neither kind of completion starts a Run automatically.

## Branch instead of resuming

`await run.fork("Alternative approach", agent_id=agent_id, options=RunOptions(...))` returns an Interaction for a separate Thread from a completed or waiting Run. It does not answer or alter the original wait. Forking a waiting Run has its own Service-defined treatment of inherited requests; it is not a partial-resume shortcut.

[Back to the guide](README.md) · [Next: files and Memory](files-and-memory.md)
