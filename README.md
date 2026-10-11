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
from a13n import Client, PreviewInterrupted


async def main() -> None:
    async with Client(os.environ["A13N_SERVICE_URL"], os.environ["A13N_API_TOKEN"]) as client:
        agent = client.agents(os.environ["A13N_AGENT"])
        interaction = await agent.start("Explain what you can help me with.")
        outcome = await interaction.result()
        print("Status:", outcome.status)
        print("Thread:", interaction.thread.id)

        print("Reply:", outcome.text if outcome.text is not None else outcome.output)


asyncio.run(main())
```

Run it with the environment you created above:

```bash
.venv/bin/python quickstart.py
```

For an ordinary reply, you should see `Status: completed`, a Thread ID, and the Agent's response. A Thread is a conversation; a Run is one execution within it. `start()` returns an **Interaction**, which lets you wait for the result or stream progress.

`outcome.output` preserves the full structured Run output; `outcome.text` is available only when it is a string, including an empty string. Neither requires an Items request. Advanced saved display is a separate, bounded ordinal window; see [windowed display and recovery](docs/streaming-and-results.md#messages-and-structured-output-are-different).

An Agent can also pause for input (`waiting`), fail (`failed`), or be cancelled (`cancelled`). See [read and handle results](docs/streaming-and-results.md#read-a-finished-response) for those cases. Omitting a key generates one key before dispatch, exposed as `interaction.idempotency_key`; the SDK never retries a mutation. Durable or cancellation-safe jobs must persist their own key and identical input/options **before** sending. See [recovery](docs/errors-and-recovery.md).

## Continue the conversation

Add this inside `main()`, while the Client is still open, after the first completed reply:

```python
follow_up = await agent.send(
    interaction.thread.id,
    "Give me a concrete example.",
)
next_outcome = await follow_up.result()
print(next_outcome.status)
```

Save the Thread ID to continue later. Each call to `send()` selects the Agent explicitly; a conversation is not permanently tied to one Agent. Normal explicit messages also continue after failed or cancelled Runs: `last_run_id` names the most recently sealed Run of any outcome, whose nearest checkpoint supplies history. Those outcomes pause automatic advancement, not explicit continuation. A waiting Run instead needs [explicit resume with all answers](docs/waiting-and-tools.md).

## Stream progress

Replace the `start()` / `result()` section with this when you want updates while the Agent works:

```python
interaction = await agent.start("Draft a short project plan.")
async with interaction:
    try:
        async for chunk in interaction.text_stream():
            print(chunk, end="", flush=True)
    except PreviewInterrupted as error:
        print("\nPreview stopped:", error.reason)
    outcome = await interaction.result()
print("Final output:", outcome.output)
print("Status:", outcome.status)
```

The loop ends when this execution finishes or pauses for input, even if the connection stays open. The context manager cleans up the connection if you break out early. Closing it stops local observation, **not** the remote Agent.

Text chunks are provisional root-assistant preview, not a lossless transcript. Gap/reset and unsupported framing stop preview without losing the authoritative result. For native progress events use `async for frame in interaction` instead; never consume raw and text concurrently. [Streaming and results](docs/streaming-and-results.md) explains the limits and local lifetime.

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
