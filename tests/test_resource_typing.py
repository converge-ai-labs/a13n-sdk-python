"""Exercise public resource signatures with the installed static checker."""

import json
import subprocess
import sys
from pathlib import Path


def test_resource_public_types_accept_valid_usage_and_reject_wrong_requests(tmp_path: Path):
    good = tmp_path / "valid.py"
    good.write_text("""
from a13n import Client, Run, Result, text_input
from a13n.generated.models import RunResource, ThreadRunSubmissionRequest, UpdateAgentRequest, RetryRunRequest

async def use(client: Client) -> Result[RunResource]:
    agent = client.workspaces("ws").agents("helper")
    run: Run = await agent.start("Hello", idempotency_key="start-key")
    snapshot = await agent.get()
    if snapshot.etag is not None:
        await agent.update(body=UpdateAgentRequest(description=None), if_match=snapshot.etag)
    submission = await client.threads("thread").submit(
        ThreadRunSubmissionRequest(expected_thread_version=2, input_=text_input("next")),
        idempotency_key="submit-key",
    )
    if isinstance(submission.resource, Run):
        await submission.resource.retry(RetryRunRequest(expected_thread_version=3), idempotency_key="retry-key")
    async with run.stream() as events:
        async for observation in events:
            cursor: str = observation.cursor
            break
    return await run.wait(timeout=5)
""")
    result = subprocess.run(
        ["pyright", "--pythonpath", sys.executable, "--outputjson", str(good)], capture_output=True, text=True
    )
    assert result.returncode == 0, result.stdout
    bad = tmp_path / "invalid.py"
    bad.write_text("""
from a13n import Client
from a13n.generated.models import RetryRunRequest
async def bad(client: Client):
    await client.workspaces("ws").agents("agent").start(42, idempotency_key="key")
    await client.runs("run").retry("not a request", idempotency_key="key")
    await client.workspaces("ws").agents("agent").update(body=RetryRunRequest(expected_thread_version=1), if_match="etag")
    await client.runs("run").retry(RetryRunRequest(expected_thread_version=1))
""")
    result = subprocess.run(
        ["pyright", "--pythonpath", sys.executable, "--outputjson", str(bad)], capture_output=True, text=True
    )
    assert result.returncode == 1
    diagnostics = json.loads(result.stdout)["generalDiagnostics"]
    assert len(diagnostics) == 4, diagnostics
    assert {item["rule"] for item in diagnostics} == {"reportArgumentType", "reportCallIssue"}
