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


def test_public_typing_accepts_agent_submission(tmp_path: Path) -> None:
    source = tmp_path / "valid.py"
    source.write_text(
        "from a13n import Client\n"
        "\n"
        "async def use(client: Client) -> None:\n"
        "    submission = await client.agents('agent').start('hello', idempotency_key='key')\n"
        "    entry_id: str = submission.entry.id\n"
        "    memory = client.resources.memories('mem')\n"
        "    revision = await memory.revisions(5).get()\n"
        "    sequence: int = revision.value.seq\n"
        "    print(sequence)\n"
        "    if submission.run is not None:\n"
        "        status = await submission.run.wait(timeout=5, poll_interval=0.1)\n"
        "        print(status.status)\n"
        "    async with submission:\n"
        "        async for frame in submission:\n"
        "            if frame.cursor is not None:\n"
        "                cursor: str = frame.cursor\n"
        "                print(cursor, entry_id)\n"
    )
    report = run_pyright(source)
    assert report["returncode"] == 0, report["generalDiagnostics"]


def test_native_configuration_media_and_oauth_typing(tmp_path: Path) -> None:
    source = tmp_path / "native.py"
    source.write_text(
        "from a13n import Client\n"
        "from a13n.generated import models as wire\n"
        "async def use(client: Client) -> None:\n"
        "    options = wire.RunOptionsInput(configuration=wire.RunConfigurationInput(allowed_hosts=[],\n"
        "        extensions=wire.RunConfigurationInputExtensions.from_dict({'example.flag': False})))\n"
        "    first = await client.agents('agent').start('hello', options=options, idempotency_key='start')\n"
        "    await client.agents('agent').send(first.thread.id, wire.MessagePayload(content=[\n"
        "        wire.UrlPart(type_='url', url='https://media.example/video.mp4')]),\n"
        "        options=options, idempotency_key='send')\n"
        "    model = wire.ModelConfigInput(model_name='native', model_api='native', characteristics=\n"
        "        wire.HarnessModelCharacteristicsInput(image_input=None,\n"
        "            video_input=wire.VideoInputPolicy(max_video_bytes=0),\n"
        "            url_input=wire.UrlInputSupportInput(video=[wire.VideoUrlType.YOUTUBE])))\n"
        "    provider = client.resources.model_providers('provider')\n"
        "    status: wire.AuthorizationStatus = (await provider.authorization.get()).value\n"
        "    start: wire.AuthorizationStart = (await provider.authorize(body=wire.ProviderAuthorizationRequest())).value\n"
        "    await provider.authorization.callback(body=wire.AuthorizationCallback(attempt_id=start.attempt_id,\n"
        "        callback_url='https://operator.example/callback'))\n"
        "    models: list[wire.ChatGPTModel] = (await provider.models.get()).value\n"
        "    disconnect: wire.AuthorizationDisconnect = (await provider.authorization.delete()).value\n"
    )
    report = run_pyright(source)
    assert report["returncode"] == 0, report["generalDiagnostics"]


def test_public_typing_rejects_invalid_paths_and_wrong_payload(tmp_path: Path) -> None:
    source = tmp_path / "invalid.py"
    source.write_text(
        "from a13n import Client\n"
        "\n"
        "async def misuse(client: Client) -> None:\n"
        "    client.resources.workspaces('ws').runs('run')\n"
        "    client.workspaces('ws')\n"
        "    client.organizations('org')\n"
        "    await client.runs('run').wait(timeout='forever', poll_interval=0.1)\n"
        "    await client.agents('agent').send('thread', 123, idempotency_key='key')\n"
        "    await client.threads('thread').stream()\n"
    )
    report = run_pyright(source)
    assert report["returncode"] == 1
    assert len(report["generalDiagnostics"]) == 6


def test_frame_discriminants_narrow_data_and_cursor(tmp_path: Path) -> None:
    source = tmp_path / "frames.py"
    source.write_text(
        "from a13n import ThreadFrame, ThreadStream, Client, text_input\n"
        "from a13n.generated import models as wire\n"
        "def consume(frame: ThreadFrame) -> None:\n"
        "    if frame.event_type == 'delta':\n"
        "        cursor: str = frame.cursor\n"
        "        run_id: str = frame.data['run_id']\n"
        "        sequence: int = frame.data['sequence']\n"
        "        print(frame.data['event'], frame.data['item'])\n"
        "    elif frame.event_type == 'boundary':\n"
        "        cursor: str = frame.cursor\n"
        "        attempt: int = frame.data['attempt']\n"
        "    elif frame.event_type == 'changed':\n"
        "        no_cursor: None = frame.cursor\n"
        "        version: int = frame.data['version']\n"
        "    elif frame.event_type == 'gap':\n"
        "        no_cursor: None = frame.cursor\n"
        "        position: str | None = frame.data.get('position')\n"
        "    else:\n"
        "        no_cursor: None = frame.cursor\n"
        "        run_id: str = frame.data['run_id']\n"
        "async def full(client: Client) -> None:\n"
        "    stream = ThreadStream(client.threads('thread'), run='run', position='1-3', after='1-0')\n"
        "    result = await client.resources.threads.create(\n"
        "        body=wire.NewThread(agent_id='agent', payload=text_input('hello'), memories=[]), idempotency_key='key')\n"
    )
    report = run_pyright(source)
    assert report["returncode"] == 0, report["generalDiagnostics"]


def test_frame_typing_rejects_wrong_variant_fields_and_writes(tmp_path: Path) -> None:
    source = tmp_path / "invalid_frames.py"
    source.write_text(
        "from a13n import ThreadFrame\n"
        "def misuse(frame: ThreadFrame) -> None:\n"
        "    if frame.event_type == 'changed':\n"
        "        cursor: str = frame.cursor\n"
        "        print(frame.data['run_id'])\n"
        "    elif frame.event_type == 'delta':\n"
        "        frame.data['sequence'] = 5\n"
    )
    report = run_pyright(source)
    assert report["returncode"] == 1
    assert len(report["generalDiagnostics"]) == 3
