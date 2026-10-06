# a13n Python SDK

Call an Agent, continue a conversation, and stream its progress from Python. The Agent runs on your a13n Service; this SDK connects your application to it.

Requires **Python 3.13+** and access to an a13n Service.

## Quick start

### 1. Install this checkout

This repository contains the pre-release SDK. To try the code documented here, install from source rather than assuming the package registry has the same API:

```bash
git clone https://github.com/converge-ai-labs/a13n-sdk-python.git
cd a13n-sdk-python
uv venv --python 3.13
uv pip install .
```

### 2. Get your connection details

Ask your Service administrator, or use your Console, for:

| Setting            | What to provide                                          |
| ------------------ | -------------------------------------------------------- |
| `A13N_SERVICE_URL` | The Service URL, without `/api/v1`; not the Console URL. |
| `A13N_API_TOKEN`   | An API key for the workspace you want to use.            |
| `A13N_AGENT`       | The ID of an Agent configured with a working model.      |

Set these environment variables in your shell or secret manager. For example, in Bash:

```bash
export A13N_SERVICE_URL='https://your-service.example'
export A13N_AGENT='your-agent-id'
read -rsp 'API key: ' A13N_API_TOKEN; echo
export A13N_API_TOKEN
```

The API key selects the workspace for you. No workspace ID is needed for this example.

### 3. Send a message

Save this as `quickstart.py`:

```python
import asyncio
import os
from uuid import uuid4

from a13n import Client


async def main() -> None:
    async with Client(os.environ["A13N_SERVICE_URL"], os.environ["A13N_API_TOKEN"]) as client:
        agent = client.agents(os.environ["A13N_AGENT"])
        interaction = await agent.start("Explain what you can help me with.", idempotency_key=uuid4().hex)
        outcome = await interaction.result()
        print("Status:", outcome.status)
        print("Thread:", interaction.thread.id)

        messages = await outcome.run.items.get()
        for item in messages.value.items:
            content = item.content.to_dict()
            if item.kind == "text_message" and content.get("role") == "assistant":
                print(content.get("text", "[message content omitted]"))


asyncio.run(main())
```

Run it with the environment you created above:

```bash
.venv/bin/python quickstart.py
```

For an ordinary reply, you should see `Status: completed`, a Thread ID, and the Agent's response. A Thread is a conversation; a Run is one execution within it. `start()` returns an **Interaction**, which lets you wait for the result or stream progress.

Saved Items are a recent ordinal window, not necessarily all display history. `run.items.get(before=..., after=..., limit=...)` supports explicit historical windows; `complete` means the Run is sealed, not that every Item was loaded. See [windowed display and recovery](docs/streaming-and-results.md#messages-and-structured-output-are-different).

An Agent can also pause for input (`waiting`), fail (`failed`), or be cancelled (`cancelled`). See [read and handle results](docs/streaming-and-results.md#read-a-finished-response) for those cases. The example uses a fresh idempotency key for each new message; in an application, save that key if you may need to retry the same submission.

## Continue the conversation

Add this inside `main()`, while the Client is still open, after the first completed reply:

```python
follow_up = await agent.send(
    interaction.thread.id,
    "Give me a concrete example.",
    idempotency_key=uuid4().hex,
)
next_outcome = await follow_up.result()
print(next_outcome.status)
```

Save the Thread ID to continue later. Each call to `send()` selects the Agent explicitly; a conversation is not permanently tied to one Agent. Normal explicit messages also continue after failed or cancelled Runs: `last_run_id` names the most recently sealed Run of any outcome, whose nearest checkpoint supplies history. Those outcomes pause automatic advancement, not explicit continuation. A waiting Run instead needs [explicit resume with all answers](docs/waiting-and-tools.md).

## Stream progress

Replace the `start()` / `result()` section with this when you want updates while the Agent works:

```python
interaction = await agent.start("Draft a short project plan.", idempotency_key=uuid4().hex)
async with interaction:
    async for frame in interaction:
        print(frame.event_type, frame.data)
    outcome = await interaction.result()
print("Status:", outcome.status)
```

The loop ends when this execution finishes or pauses for input, even if the connection stays open. The context manager cleans up the connection if you break out early. Closing it stops local observation, **not** the remote Agent.

These frames are progress events, not just text tokens. For the saved response, use `outcome.run.items.get()` as in the quick start. A stream can have gaps; [streaming and results](docs/streaming-and-results.md) explains how to handle them.

## Next steps

The [Python SDK guide](docs/README.md) takes you from your first conversation to an application that can recover after interruptions:

- [Create Agents and continue conversations](docs/agents-and-conversations.md)
- [Stream progress and read results](docs/streaming-and-results.md)
- [Handle approvals and client tools](docs/waiting-and-tools.md)
- [Attach files and work with Memory](docs/files-and-memory.md)
- [Configure authentication and connections](docs/connections.md)
- [Use the complete resource API](docs/resources.md)
- [Handle errors and recover work](docs/errors-and-recovery.md)

For development and testing, see [Contributing](CONTRIBUTING.md). The [SDK specification](spec/README.md) and [pinned Service source](contract/source.json) describe compatibility and implementation contracts.

Licensed under Apache-2.0.
