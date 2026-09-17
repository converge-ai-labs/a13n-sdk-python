import json
import subprocess
import sys
from pathlib import Path


def run_pyright(path: Path) -> dict:
    result = subprocess.run(
        ["pyright", "--pythonpath", sys.executable, "--outputjson", str(path)],
        capture_output=True,
        text=True,
    )
    report = json.loads(result.stdout)
    report["returncode"] = result.returncode
    return report


def test_resource_public_typing_accepts_narrowed_async_usage(tmp_path: Path) -> None:
    source = tmp_path / "valid.py"
    source.write_text(
        "from a13n import Client, RunAccepted, SubmissionQueued\n"
        "\n"
        "async def use(client: Client) -> None:\n"
        "    submission = await client.threads('thread').submit(\n"
        "        'hello', expected_thread_version=1, idempotency_key='key'\n"
        "    )\n"
        "    if isinstance(submission, RunAccepted):\n"
        "        stream = submission.run.stream()\n"
        "        async with stream:\n"
        "            async for observation in stream:\n"
        "                cursor: str = observation.cursor\n"
        "                print(cursor)\n"
        "    elif isinstance(submission, SubmissionQueued):\n"
        "        queued_id: str = submission.queued_submission.id\n"
        "        print(queued_id)\n"
    )
    report = run_pyright(source)
    assert report["returncode"] == 0, report["generalDiagnostics"]


def test_resource_public_typing_rejects_invalid_lifecycle_and_request_shapes(tmp_path: Path) -> None:
    source = tmp_path / "invalid.py"
    source.write_text(
        "from a13n import Client\n"
        "\n"
        "async def misuse(client: Client) -> None:\n"
        "    await client.runs('run').stream()\n"
        "    await client.runs('run').wait(timeout='forever', poll_interval=0.1)\n"
        "    await client.threads('thread').submit('hello', idempotency_key='key')\n"
        "    client.runs('run').cancel(expected_run_version=1, idempotency_key='key')\n"
    )
    report = run_pyright(source)
    assert report["returncode"] == 1
    diagnostics = report["generalDiagnostics"]
    assert len(diagnostics) == 4
    assert {diagnostic["rule"] for diagnostic in diagnostics} <= {
        "reportArgumentType",
        "reportCallIssue",
        "reportGeneralTypeIssues",
    }
