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


def test_public_typing_accepts_workspace_scoped_submission(tmp_path: Path) -> None:
    source = tmp_path / "valid.py"
    source.write_text(
        "from a13n import Client\n"
        "\n"
        "async def use(client: Client) -> None:\n"
        "    submission = await client.workspaces('ws').start('hello', agent_id='agent', idempotency_key='key')\n"
        "    entry_id: str = submission.entry.id\n"
        "    if submission.run is not None:\n"
        "        status = await submission.run.wait(timeout=5, poll_interval=0.1)\n"
        "        print(status.value.status)\n"
        "    async with submission.thread.stream() as stream:\n"
        "        async for frame in stream:\n"
        "            if frame.cursor is not None:\n"
        "                cursor: str = frame.cursor\n"
        "                print(cursor, entry_id)\n"
    )
    report = run_pyright(source)
    assert report["returncode"] == 0, report["generalDiagnostics"]


def test_public_typing_rejects_global_paths_and_wrong_payload(tmp_path: Path) -> None:
    source = tmp_path / "invalid.py"
    source.write_text(
        "from a13n import Client\n"
        "\n"
        "async def misuse(client: Client) -> None:\n"
        "    client.runs('run')\n"
        "    await client.workspaces('ws').runs('run').wait(timeout='forever', poll_interval=0.1)\n"
        "    await client.workspaces('ws').threads('thread').submit('hello', idempotency_key='key')\n"
        "    await client.workspaces('ws').threads('thread').stream()\n"
    )
    report = run_pyright(source)
    assert report["returncode"] == 1
    assert len(report["generalDiagnostics"]) == 4
