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
        "    assert submission.entry is not None\n"
        "    entry_id: str = submission.entry.id\n"
        "    memory = client.api.memories('mem')\n"
        "    revision = await memory.revisions(5).get()\n"
        "    sequence: int = revision.value.seq\n"
        "    print(sequence)\n"
        "    if submission.run is not None:\n"
        "        status = await submission.run.result(timeout=5, poll_interval=0.1)\n"
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
        "from a13n import Client, RunOptions, RunConfiguration, UrlPart\n"
        "from a13n.generated import models as wire\n"
        "async def use(client: Client) -> None:\n"
        "    options = RunOptions(configuration=RunConfiguration(allowed_hosts=[],\n"
        "        extensions={'example.flag': False}))\n"
        "    first = await client.agents('agent').start('hello', options=options, idempotency_key='start')\n"
        "    assert first.thread is not None\n"
        "    await client.agents('agent').send(first.thread.id, [\n"
        "        UrlPart('https://media.example/video.mp4')],\n"
        "        options=options, idempotency_key='send')\n"
        "    model = wire.ModelConfigInput(model_name='native', model_api='native', characteristics=\n"
        "        wire.HarnessModelCharacteristicsInput(image_input=None,\n"
        "            video_input=wire.VideoInputPolicy(max_video_bytes=0),\n"
        "            url_input=wire.UrlInputSupportInput(video=[wire.VideoUrlType.YOUTUBE])))\n"
        "    provider = client.api.model_providers('provider')\n"
        "    status: wire.AuthorizationStatus = (await provider.authorization.get()).value\n"
        "    start: wire.AuthorizationStart = (await provider.authorize(body=wire.ProviderAuthorizationRequest())).value\n"
        "    await provider.authorization.callback(body=wire.AuthorizationCallback(attempt_id=start.attempt_id,\n"
        "        callback_url='https://operator.example/callback'))\n"
        "    models: list[wire.ProviderModel] = (await provider.models.get()).value\n"
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
        "    client.api.workspaces('ws').runs('run')\n"
        "    client.workspaces('ws')\n"
        "    client.organizations('org')\n"
        "    await client.runs('run').result(timeout='forever', poll_interval=0.1)\n"
        "    await client.agents('agent').send('thread', 123, idempotency_key='key')\n"
        "    await client.threads('thread').stream()\n"
    )
    report = run_pyright(source)
    assert report["returncode"] == 1
    assert len(report["generalDiagnostics"]) == 6


def test_frame_discriminants_narrow_data_and_cursor(tmp_path: Path) -> None:
    source = tmp_path / "frames.py"
    source.write_text(
        "from a13n import ThreadFrame, ThreadStream, Client\n"
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
        "    result = await client.api.threads.create(\n"
        "        body=wire.NewThread(agent_id='agent', payload=wire.MessagePayload(content=[\n"
        "            wire.TextPart(type_='text', text='hello')]), memories=[]), idempotency_key='key')\n"
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


def test_ordinal_paging_and_nullable_item_metadata_typing(tmp_path: Path) -> None:
    source = tmp_path / "paged.py"
    source.write_text(
        "from collections.abc import Mapping\n"
        "from pydantic import JsonValue\n"
        "from a13n import Client, ThreadFrame\n"
        "from a13n.generated import models as wire\n"
        "async def use(client: Client, frame: ThreadFrame) -> None:\n"
        "    recent: wire.RunItems = (await client.runs('run').items.get(limit=1)).value\n"
        "    page: wire.RunItems = (await client.runs('run').items.get(before=7, limit=2)).value\n"
        "    await client.runs('run').items.get(after=0)\n"
        "    complete: bool = recent.complete\n"
        "    ordinal: int = recent.items[0].ordinal\n"
        "    if frame.event_type == 'delta' and frame.data['item'] is not None:\n"
        "        item = frame.data['item']\n"
        "        assigned: int | None = item.get('ordinal')\n"
        "        group: str | None = item.get('response_group')\n"
        "        failure: Mapping[str, JsonValue] | None = item.get('failure')\n"
    )
    report = run_pyright(source)
    assert report["returncode"] == 0, report["generalDiagnostics"]


def test_ordinal_paging_rejects_obsolete_fields_and_cursor_facade_typing(tmp_path: Path) -> None:
    source = tmp_path / "obsolete.py"
    source.write_text(
        "from a13n import Client\n"
        "async def misuse(client: Client) -> None:\n"
        "    items = (await client.runs('run').items.get()).value\n"
        "    print(items.dropped)\n"
        "    print((await client.threads('thread').get()).value.head_run_id)\n"
        "    await client.runs('run').items.get(before='cursor')\n"
        "    client.runs('run').items.pages()\n"
    )
    report = run_pyright(source)
    assert report["returncode"] == 1
    assert len(report["generalDiagnostics"]) == 4


def test_root_only_workflow_values_and_resume_typing(tmp_path: Path) -> None:
    source = tmp_path / "workflow.py"
    source.write_text(
        "from pydantic import JsonValue\n"
        "from a13n import (Client, AgentOverride, RunConfiguration, RunOptions, UsageLimit,\n"
        "    TextPart, JsonPart, UrlPart, AssetPart, Approve, Deny, Returned, Failed, PreviewInterrupted)\n"
        "async def use(client: Client) -> None:\n"
        "    options = RunOptions(configuration=RunConfiguration(allowed_hosts=None,\n"
        "        extensions={'example': [False, 0, None]}), overrides=AgentOverride(\n"
        "        output_spec={'schema': {'type': 'object'}}, model_settings={'temperature': 0}),\n"
        "        labels={}, max_usage=UsageLimit(2))\n"
        "    submitted = await client.agents('agent').start([TextPart('hello'), JsonPart(None),\n"
        "        UrlPart('https://example.test'), AssetPart('asset')], options=options)\n"
        "    outcome = await submitted.result()\n"
        "    output: JsonValue = outcome.output\n"
        "    if outcome.pending is not None:\n"
        "        for request in outcome.pending.calls:\n"
        "            arguments: dict[str, JsonValue] = request.arguments\n"
        "    resumed = await outcome.run.resume({'ap': Approve(), 'deny': Deny(None),\n"
        "        'call': Returned(None), 'fail': Failed('unavailable')}, input=None)\n"
        "    assert resumed.run is not None\n"
        "    fork = await resumed.run.fork('alternative', agent_id='agent', options=options)\n"
        "    assert fork.thread is not None and fork.entry is not None\n"
        "    recovered = client.threads(fork.thread.id).interaction(fork.entry.id)\n"
        "    async with recovered:\n"
        "        try:\n"
        "            async for chunk in recovered.text_stream():\n"
        "                text: str = chunk\n"
        "        except PreviewInterrupted:\n"
        "            async for frame in recovered:\n"
        "                print(frame.event_type)\n"
        "        final = await recovered.result()\n"
    )
    report = run_pyright(source)
    assert report["returncode"] == 0, report["generalDiagnostics"]


def test_public_typing_rejects_obsolete_resources_entry(tmp_path: Path) -> None:
    source = tmp_path / "obsolete_entry.py"
    source.write_text("from a13n import Client\ndef misuse(client: Client) -> None:\n    client.resources\n")
    report = run_pyright(source)
    assert report["returncode"] == 1
    assert len(report["generalDiagnostics"]) == 1
    assert '"resources"' in report["generalDiagnostics"][0]["message"]


def test_saved_content_findings_and_provenance_typing(tmp_path: Path) -> None:
    source = tmp_path / "catchup.py"
    source.write_text(
        "from a13n import Client, AgentOverride, RunOptions, ThreadFrame\n"
        "from a13n.generated import models as wire\n"
        "from a13n.streaming import MemorySource, FileSource, RecordSource\n"
        "async def use(client: Client, frame: ThreadFrame) -> None:\n"
        "    options = RunOptions(overrides=AgentOverride(lazy_environment=False,\n"
        "        skill_sync={'mode': 'isolated', 'cache_count': 0}))\n"
        "    prepared: wire.Agent = (await client.api.finding_agent()).value\n"
        "    analysis: wire.Analysis = (await client.api.finding_analyses.create(\n"
        "        body=wire.AnalysisCreate(max_traces=1), idempotency_key='analysis')).value\n"
        "    findings: wire.FindingPage = (await client.api.findings.list(closed=False)).value\n"
        "    finding: wire.Finding = (await client.api.findings('finding').get()).value\n"
        "    await client.api.findings('finding').update(body=wire.FindingUpdate(closed=False))\n"
        "    content: wire.RunContent = (await client.api.runs('run').contents('content').get()).value\n"
        "    authors: wire.MessageAuthors = (await client.api.sessions('session').message_authors.get(\n"
        "        entry_id=['entry'])).value\n"
        "    if frame.event_type == 'delta' and frame.data['item'] is not None:\n"
        "        sources: list[MemorySource] | None = frame.data['item'].get('memory_sources')\n"
        "        if sources:\n"
        "            files: list[FileSource] = sources[0].get('files', [])\n"
        "            records: list[RecordSource] = sources[0].get('records', [])\n"
    )
    report = run_pyright(source)
    assert report["returncode"] == 0, report["generalDiagnostics"]


def test_provenance_and_override_typing_rejects_invalid_native_shapes(tmp_path: Path) -> None:
    source = tmp_path / "bad_catchup.py"
    source.write_text(
        "from a13n import AgentOverride, ThreadFrame\n"
        "from a13n.streaming import MemorySource\n"
        "bad = AgentOverride(lazy_environment='false', skill_sync=123)\n"
        "source: MemorySource = {'kind': 'unknown', 'memory': 'notes', 'status': 'recalled'}\n"
        "def mutate(frame: ThreadFrame) -> None:\n"
        "    if frame.event_type == 'delta' and frame.data['item'] is not None:\n"
        "        frame.data['item']['memory_sources'] = []\n"
    )
    report = run_pyright(source)
    assert report["returncode"] == 1
    assert len(report["generalDiagnostics"]) == 4


def test_shared_memory_computer_and_execution_typing(tmp_path: Path) -> None:
    source = tmp_path / "shared.py"
    source.write_text("""from a13n import Client, AgentOverride, MountCreate, MemoryMount, RunOptions
from a13n.generated import models as wire
async def use(client: Client) -> None:
    options = RunOptions(overrides=AgentOverride(builtin_skills=['platform-operations'], platform_tools={'groups': ['execution']}))
    mount = MountCreate('work', 'env', permission_ceiling={'operations': []})
    created: wire.MemorySpace = (await client.api.memory_spaces.create(body=wire.MemorySpaceCreate(name='Notes'))).value
    space = client.api.memory_spaces(created.id)
    page: wire.MemorySpacePage = (await client.api.memory_spaces.list(enabled=False)).value
    await space.get()
    await space.update(body=wire.MemorySpaceUpdate(enabled=False), if_match='"v1"')
    status: wire.SpaceOrganizationStatus = (await space.organization.get()).value
    accepted: wire.SpaceOrganizationStatus = (await space.organizations.create()).value
    history: wire.RunPage = (await space.organizations.list()).value
    sessions: wire.SessionPage = (await space.sessions.list()).value
    await space.delete(if_match='"v1"')
    selection = wire.SessionMemorySettings(enabled=True, spaces=[wire.SpaceBinding(name='notes', space_id=created.id)])
    await client.api.sessions.create(body=wire.SessionCreate(memory=selection))
    await client.api.sessions('session').update(body=wire.SessionUpdate(labels=None, memory=selection), if_match='"v1"')
    runs: wire.RunPage = (await client.api.runs.list(thread_id='thread')).value
    executed: wire.RunAgent = (await client.api.runs('run').agent.get()).value
    attempt: wire.AttemptView = (await client.api.runs('run').attempts('attempt').get()).value
    image = await client.api.runs('run').images('image').get()
    async with client.api.runs('run').images('image').get_stream() as response:
        data: bytes = await response.aread()
    changed: wire.MountView = (await client.api.threads('thread').environments('work').update(body=wire.MountUpdate(permission_ceiling=wire.EnvironmentPermissionSetInput(operations=[wire.EnvironmentAction.ENVIRONMENT_COMPUTER_OBSERVE])), if_match='"v1"')).value
    check: wire.ComputerCheck = (await client.api.environments('env').computer.check()).value
    refs: wire.EnvironmentProviderReferences = (await client.api.environment_providers('provider').references.get()).value
    await client.api.environment_providers('provider').delete(if_match='"v1"')
    metrics: wire.ModelRequestMetrics = (await client.api.usage.records('record').metrics.get()).value
    speed: float | None = metrics.output_tokens_per_second
    view = (await client.api.runs('run').get()).value
    for memory in view.memory_mounts:
        if isinstance(memory, wire.FrozenMemoryMount):
            print(memory.roots, memory.space_id)
""")
    report = run_pyright(source)
    assert report["returncode"] == 0, report["generalDiagnostics"]


def test_shared_memory_and_host_only_fields_negative_typing(tmp_path: Path) -> None:
    source = tmp_path / "invalid_shared.py"
    source.write_text("""from a13n import Client, AgentOverride, MountCreate, MemoryMount
from a13n.generated import models as wire
async def misuse(client: Client) -> None:
    MountCreate('work', 'env', permission_ceiling=None)
    MemoryMount('notes', 'mem', 'read', roots=[])
    AgentOverride(builtin_skills=['unsupported'])
    wire.SpaceBinding(name='notes', memory_id='mem')
    wire.EnvironmentPermissionSetInput(operations=['computer.*'])
    wire.ModelRequestMetrics()
    await client.api.memory_spaces('space').organizations.create(body={})
    await client.api.runs('run').images('image').get(body={})
""")
    report = run_pyright(source)
    assert report["returncode"] == 1
    assert len(report["generalDiagnostics"]) == 9


def test_session_native_reader_and_frame_payload_typing(tmp_path: Path) -> None:
    source = tmp_path / "session.py"
    source.write_text(
        "from a13n import Client, SessionFrame, SessionStream\n"
        "from a13n.generated import models as wire\n"
        "def consume(frame: SessionFrame) -> None:\n"
        "    if frame.event_type == 'thread':\n"
        "        thread: wire.ThreadView = frame.data.thread\n"
        "        current: wire.RunView | None = frame.data.current_run\n"
        "    elif frame.event_type == 'items':\n"
        "        items: list[wire.Item] = frame.data.items\n"
        "        continuation: wire.DisplayContinuation | None = frame.data.continuation\n"
        "    elif frame.event_type == 'delta':\n"
        "        sequence: int = frame.data.sequence\n"
        "        print(frame.data.event.to_dict())\n"
        "    else:\n"
        "        run_id: str = frame.data.run_id\n"
        "async def use(client: Client) -> None:\n"
        "    async with client.api.sessions('ses').stream.get_stream() as response:\n"
        "        print(response.status_code)\n"
        "    async with SessionStream(client.api.sessions('ses')) as stream:\n"
        "        async for frame in stream:\n"
        "            consume(frame)\n"
    )
    report = run_pyright(source)
    assert report["returncode"] == 0, report["generalDiagnostics"]


def test_session_typing_rejects_cursor_reconnect_and_removed_readback_fields(tmp_path: Path) -> None:
    source = tmp_path / "invalid_session.py"
    source.write_text(
        "from a13n import Client, SessionFrame, SessionStream\n"
        "from a13n.generated import models as wire\n"
        "def misuse(client: Client, frame: SessionFrame, items: wire.RunItems, run: wire.RunView, thread: wire.ThreadView) -> None:\n"
        "    SessionStream(client.api.sessions('ses'), after='1-0')\n"
        "    SessionStream(client.api.sessions('ses'), reconnect=True)\n"
        "    print(frame.cursor)\n"
        "    print(items.baseline, items.continuation, items.position, items.resume_after)\n"
        "    print(run.display_position, thread.message_history)\n"
    )
    report = run_pyright(source)
    assert report["returncode"] == 1
    assert len(report["generalDiagnostics"]) >= 9


def test_desktop_tool_search_context_typing(tmp_path: Path) -> None:
    source = tmp_path / "desktop.py"
    source.write_text(
        "from a13n import Client, AgentOverride, RunOptions, Unset\n"
        "from a13n.generated import models as wire\n"
        "async def use(client: Client) -> None:\n"
        "    search = wire.ToolSearch(config=wire.NativeToolSearchConfig(mode='native', strategy=None),\n"
        "        groups=wire.ToolSearchGroups())\n"
        "    config = wire.AgentConfigInput(model='model', tool_search=search)\n"
        "    proxy = wire.ToolSearch(config=wire.ProxyToolSearchConfig(mode='proxy', max_results=0))\n"
        "    options = RunOptions(overrides=AgentOverride(tool_search=proxy))\n"
        "    usage: wire.ContextUsage | None = (await client.api.usage.context.get(record_id='record')).value\n"
        "    if usage is not None:\n"
        "        window: int | None = usage.context_window_tokens\n"
        "    view: wire.View | None = (await client.api.runs('run').desktop_control.get()).value\n"
        "    opened: wire.View = (await client.api.runs('run').desktop_control.create(\n"
        "        body=wire.Request(mount='computer', reason='Finish sign in'))).value\n"
        "    access: wire.Access = (await client.api.desktop_assistance(opened.id).view(\n"
        "        body=wire.Control(session_id='browser_session_token_1234', epoch=0))).value\n"
        "    await client.api.desktop_assistance(opened.id).complete(\n"
        "        body=wire.Completion(session_id='browser_session_token_1234', epoch=opened.epoch))\n"
        "    outcome = await client.runs('run').observe().result()\n"
        "    if outcome.pending is not None:\n"
        "        desktop: str | Unset | None = outcome.pending.desktop_control_id\n"
        "    successor = await outcome.run.resume({})\n"
    )
    report = run_pyright(source)
    assert report["returncode"] == 0, report["generalDiagnostics"]


def test_desktop_tool_search_context_typing_rejects_mixed_shapes_and_unchecked_null(tmp_path: Path) -> None:
    source = tmp_path / "invalid_desktop.py"
    source.write_text(
        "from a13n import Client, AgentOverride\n"
        "from a13n.generated import models as wire\n"
        "async def misuse(client: Client) -> None:\n"
        "    wire.NativeToolSearchConfig(mode='proxy')\n"
        "    wire.NativeToolSearchConfig(mode='native', search_name='mixed')\n"
        "    wire.NativeToolSearchConfig(mode='native', strategy='invalid')\n"
        "    wire.ProxyToolSearchConfig(mode='proxy', strategy='bm25')\n"
        "    AgentOverride(tool_search='json string')\n"
        "    wire.Control(session_id='browser_session_token_1234', epoch='0')\n"
        "    usage = (await client.api.usage.context.get(run_id='run')).value\n"
        "    print(usage.run_id)\n"
    )
    report = run_pyright(source)
    assert report["returncode"] == 1
    assert len(report["generalDiagnostics"]) == 7, report["generalDiagnostics"]
