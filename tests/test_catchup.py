"""Native Service catch-up: saved content, provenance, findings and explicit resume."""

import asyncio
import json
from dataclasses import fields

import httpx2
import pytest
from attrs import fields as wire_fields

from a13n import (
    UNSET,
    AgentOverride,
    ApiError,
    Approve,
    Client,
    DeltaFrame,
    ProtocolError,
    Returned,
    RunOptions,
    TransportError,
)
from a13n.generated import models as wire
from a13n.streaming import _frame
from tests.test_interaction import NOW, run_view, submitted
from tests.test_run_items import continuation, display_item

SOURCE = {
    "kind": "file",
    "memory": "notes",
    "status": "changes",
    "memory_id": None,
    "cursor": None,
    "records": [{"id": "record", "sha256": "digest"}],
    "files": [{"path": "计划.md", "sha256": "digest", "bytes": 0, "truncated": False}],
    "sources_truncated": False,
}
FINDING_CREATE = {
    "agent_id": "agt_1",
    "agent_revision_id": "rev_1",
    "category": "tool_usage",
    "evidence": [{"run_id": "run_1", "trace_id": "0" * 32, "span_ids": []}],
    "explanation": "Observed issue",
    "source_key": "one",
    "suggestion": "Change call",
    "title": "Call issue",
    "severity": "warning",
    "limitations": "",
}
FINDING = {
    **FINDING_CREATE,
    "analysis_id": None,
    "assessment": "unreviewed",
    "assessment_note": "",
    "closed": False,
    "created_at": NOW,
    "created_by_id": "usr_1",
    "id": "fnd_1",
    "source_run_id": None,
    "updated_at": NOW,
    "version": 1,
    "workspace_id": "ws_1",
}
ANALYSIS = {
    "agent_id": None,
    "cited_trace_count": 0,
    "created_at": NOW,
    "finding_count": 0,
    "id": "fan_1",
    "read_trace_ids": [],
    "run_id": "run_2",
    "run_status": "accepted",
    "selected_traces": [],
    "selection": {"agent_id": None, "presets": [], "max_traces": 1},
    "selection_truncated": False,
    "session_id": "ses_1",
    "thread_id": "thr_1",
}
AGENT = {
    "archived_at": None,
    "created_at": NOW,
    "created_by_id": "usr_1",
    "default_revision_id": None,
    "description": "",
    "id": "agt_1",
    "image_url": None,
    "labels": {},
    "name": "Finding Agent",
    "organization_id": "org_1",
    "source": "builtin",
    "updated_at": NOW,
    "updated_by_id": "usr_1",
    "version": 1,
    "workspace_id": "ws_1",
    "preset_kind": "finding",
}


@pytest.mark.parametrize("mode", ["bearer", "session"])
def test_all_added_operations_share_auth_lifetime_and_native_http_evidence(mode: str) -> None:
    async def scenario() -> None:
        requests = []

        def handle(request):
            requests.append(request)
            path = request.url.path
            if path.endswith("finding-agent"):
                value, status = AGENT, 200
            elif path.endswith("finding-analyses"):
                value = ANALYSIS if request.method == "POST" else {"items": [ANALYSIS], "next_cursor": None}
                status = 201 if request.method == "POST" else 200
            elif path.endswith("findings"):
                value = FINDING if request.method == "POST" else {"items": [FINDING], "next_cursor": None}
                status = 201 if request.method == "POST" else 200
            elif "/findings/" in path:
                value, status = FINDING, 200
            elif "/contents/" in path:
                value, status = (
                    {
                        "id": "cnt_1",
                        "media_type": "application/json",
                        "value": [False, 0, None, {}, []],
                        "truncated": False,
                    },
                    200,
                )
            elif path.endswith("message-authors"):
                value, status = (
                    {"items": [{"entry_id": "ent_1", "principal_id": "usr_1", "principal": None, "submitted_at": NOW}]},
                    200,
                )
            else:
                value, status = submitted(), 201
            return httpx2.Response(
                status, json=value, headers={"X-Request-ID": "req_new", "ETag": '"fnd:1"', "Cache-Control": "no-store"}
            )

        transport = httpx2.MockTransport(handle)
        client = (
            Client.session(
                "https://service.example",
                origin="https://service.example",
                workspace_id="ws_1",
                csrf_token="proof",
                transport=transport,
            )
            if mode == "session"
            else Client("https://service.example", "token", transport=transport)
        )
        async with client:
            api = client.api
            assert not requests
            assert (await api.finding_agent()).value.preset_kind == "finding"
            listed = await api.finding_analyses.list(limit=1)
            assert listed.value.items[0].to_dict() == wire.Analysis.from_dict(ANALYSIS).to_dict()
            created = await api.finding_analyses.create(
                body=wire.AnalysisCreate.from_dict(ANALYSIS["selection"]), idempotency_key="analysis"
            )
            assert created.value.run_id == "run_2"
            assert (await api.findings.list(closed=False, limit=1)).value.items[0].closed is False
            assert (await api.findings.create(body=wire.FindingCreate.from_dict(FINDING_CREATE))).value.id == "fnd_1"
            assert (await api.findings("fnd_1").get()).value.assessment == wire.Assessment.UNREVIEWED
            changed = await api.findings("fnd_1").update(
                body=wire.FindingUpdate(closed=False, assessment_note=None), if_match='"fnd:1"'
            )
            assert changed.request_id == "req_new" and changed.etag == '"fnd:1"'
            content = await api.runs("run_1").contents("cnt_1").get()
            assert content.value.value == [False, 0, None, {}, []] and content.headers["cache-control"] == "no-store"
            authors = await api.sessions("ses_1").message_authors.get(entry_id=["ent_1", "absent"])
            assert authors.value.items[0].principal is None
            assert authors.value.items[0].principal_id == "usr_1"
            interaction = await client.agents("agt_1").start("hello", idempotency_key="start")
            assert interaction.run is None
        assert len(requests) == 10
        assert requests[2].headers["idempotency-key"] == "analysis"
        assert requests[3].url.params["closed"] == "false"
        assert requests[6].headers["if-match"] == '"fnd:1"'
        assert json.loads(requests[6].content) == {"closed": False, "assessment_note": None}
        assert requests[8].url.params.get_list("entry_id") == ["ent_1", "absent"]
        for request in requests:
            if mode == "session":
                assert request.headers["x-workspace-id"] == "ws_1"
                assert request.headers["origin"] == "https://service.example"
                if request.method != "GET":
                    assert request.headers["x-csrf-token"] == "proof"
            else:
                assert request.headers["authorization"] == "Bearer " + "token"
        with pytest.raises(TransportError, match="closed"):
            await api.findings.list()
        assert len(requests) == 10

    asyncio.run(scenario())


def test_new_collection_paging_is_lazy_and_retains_filters() -> None:
    async def scenario() -> None:
        requests = []

        def handle(request):
            requests.append(request)
            return httpx2.Response(
                200,
                json={"items": [], "next_cursor": "next" if len(requests) % 2 else None},
                headers={"X-Request-ID": str(len(requests))},
            )

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            findings = client.api.findings.pages(closed=False, category=wire.Category.TOOL_USAGE, limit=1)
            assert not requests
            assert [page.request_id async for page in findings] == ["1", "2"]
            analyses = client.api.finding_analyses.pages(limit=1)
            assert len(requests) == 2
            assert [page.request_id async for page in analyses] == ["3", "4"]
        assert dict(requests[1].url.params) == {
            "closed": "false",
            "category": "tool_usage",
            "limit": "1",
            "cursor": "next",
        }
        assert dict(requests[3].url.params) == {"limit": "1", "cursor": "next"}

    asyncio.run(scenario())


@pytest.mark.parametrize(
    "sync",
    [UNSET, None, {"mode": "shared", "overwrite": False, "cleanup": False}, {"mode": "isolated", "cache_count": 0}],
)
def test_override_policy_omission_null_false_and_complete_field_coverage(sync) -> None:
    options = RunOptions(overrides=AgentOverride(lazy_environment=False, skill_sync=sync))
    expected = {"lazy_environment": False}
    if sync is not UNSET:
        expected["skill_sync"] = sync
    assert options.into_wire().to_dict() == {"overrides": expected}
    assert RunOptions(overrides=AgentOverride()).into_wire().to_dict() == {"overrides": {}}
    assert RunOptions(overrides=AgentOverride(lazy_environment=None)).into_wire().to_dict() == {
        "overrides": {"lazy_environment": None}
    }
    assert {f.name for f in fields(AgentOverride)} == {f.name for f in wire_fields(wire.AgentOverrideInput)}


def test_saved_content_references_and_memory_provenance_round_trip_without_expansion() -> None:
    item = display_item(1)
    item["content"]["memory_sources"] = [SOURCE]
    item.update(
        content_refs={
            "text": {"id": "cnt_1", "size_bytes": 0, "media_type": "text/plain", "preview": "", "truncated": False}
        },
    )
    assert wire.Item.from_dict(item).to_dict() == item
    state = continuation()
    state["memory_sources"] = {"itm_1": [SOURCE]}
    assert wire.DisplayContinuation.from_dict(state).to_dict() == state
    provenance = {
        "content_matches": False,
        "created": None,
        "last_write": {
            "principal_id": None,
            "principal_name": None,
            "run_id": "run_1",
            "attempt_id": None,
            "tool_call_id": None,
            "confirmed_at": NOW.replace("Z", "+00:00"),
        },
    }
    record = {"id": "rec_1", "text": "saved", "provenance": provenance}
    assert wire.MemoryRecordView.from_dict(record).to_dict() == record
    assert wire.MemoryRecordView.from_dict({"id": "rec_1", "text": "saved", "provenance": None}).provenance is None
    assert wire.MemoryRecordView.from_dict({"id": "rec_1", "text": "saved"}).provenance is UNSET
    assert wire.ProviderModel.from_dict(
        {"slug": "choice", "display_name": "Choice", "characteristics": None}
    ).to_dict() == {"slug": "choice", "display_name": "Choice", "characteristics": None}


@pytest.mark.parametrize(
    "sources", [UNSET, None, [], [SOURCE], [{"kind": "record", "memory": "notes", "status": "recalled"}]]
)
def test_raw_memory_sources_preserve_optional_null_and_omitted_defaults(sources) -> None:
    item = {"id": "itm_1", "kind": "observation", "state": "completed"}
    if sources is not UNSET:
        item["memory_sources"] = sources
    value = {"run_id": "run_1", "attempt": 1, "sequence": 1, "event": {}, "item": item}
    frame = _frame("delta", [json.dumps(value)], "1-0")
    assert isinstance(frame, DeltaFrame) and frame.data["item"] == item
    assert frame.data["item"] is not None
    if sources is UNSET:
        assert "memory_sources" not in frame.data["item"]


@pytest.mark.parametrize(
    "sources",
    [
        {},
        [None],
        [{"kind": "file", "memory": "notes"}],
        [{**SOURCE, "kind": "unknown"}],
        [{**SOURCE, "status": "unknown"}],
        [{**SOURCE, "memory_id": 1}],
        [{**SOURCE, "cursor": False}],
        [{**SOURCE, "records": None}],
        [{**SOURCE, "files": None}],
        [{**SOURCE, "sources_truncated": 0}],
        [{**SOURCE, "extra": None}],
        [{**SOURCE, "records": [{"id": "r"}]}],
        [{**SOURCE, "files": [{"path": "p", "sha256": "s", "bytes": True}]}],
        [{**SOURCE, "files": [{"path": "p", "sha256": "s", "bytes": -1}]}],
        [{**SOURCE, "files": [{"path": "p", "sha256": "s", "bytes": 0, "truncated": None}]}],
    ],
)
def test_raw_memory_source_schema_rejects_invalid_shapes(sources) -> None:
    value = {
        "run_id": "run_1",
        "attempt": 1,
        "sequence": 1,
        "event": {},
        "item": {"id": "itm_1", "kind": "observation", "state": "completed", "memory_sources": sources},
    }
    with pytest.raises(ProtocolError, match="Malformed"):
        _frame("delta", [json.dumps(value)], "1-0")


@pytest.mark.parametrize(
    "reason,status",
    [
        ("pending_coverage_mismatch", 400),
        ("invalid_question_response", 400),
        ("not_idle_waiting_head", 409),
        ("idempotency_key_reused", 409),
    ],
)
def test_explicit_batch_rejections_are_known_and_never_automatically_retried(reason, status) -> None:
    async def scenario() -> None:
        requests = []
        details = {"reason": reason, "field": "calls", "missing": ["call_2"], "unexpected": []}

        def handle(request):
            requests.append(request)
            return httpx2.Response(
                status,
                json={
                    "error": {
                        "code": "invalid_argument" if status == 400 else "conflict",
                        "message": "Rejected",
                        "details": details,
                        "request_id": "rejected",
                    }
                },
            )

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            for _ in range(2):  # Explicit caller replay, never SDK replay.
                with pytest.raises(ApiError) as caught:
                    await client.runs("run_1").resume(
                        {"approve": Approve(), "call_1": Returned({"answers": {}, "response": None})},
                        idempotency_key="same",
                    )
                assert caught.value.details == details and caught.value.status == status
        assert len(requests) == 2 and requests[0].content == requests[1].content
        assert json.loads(requests[0].content) == {
            "approvals": {"approve": {"action": "approve"}},
            "calls": {"call_1": {"status": "returned", "value": {"answers": {}, "response": None}}},
        }

    asyncio.run(scenario())


def test_question_batch_explicit_replay_binds_same_distinct_successor() -> None:
    async def scenario() -> None:
        requests = []
        answer = {"answers": {"Choose": ["One", "Two"]}, "response": "context"}

        def handle(request):
            requests.append(request)
            return httpx2.Response(200, json=run_view("run_2"))

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            for _ in range(2):
                interaction = await client.runs("run_1").resume(
                    {"question": Returned(answer)}, input=None, idempotency_key="same"
                )
                assert interaction.run is not None and interaction.run.id == "run_2"
                assert interaction.entry is None
        assert len(requests) == 2 and requests[0].content == requests[1].content
        assert json.loads(requests[0].content) == {
            "approvals": {},
            "calls": {"question": {"status": "returned", "value": answer}},
            "input": None,
        }

    asyncio.run(scenario())


def test_imported_history_preserves_nested_argument_and_result_object_order() -> None:
    async def scenario() -> None:
        history = [
            {
                "kind": "response",
                "parts": [
                    {
                        "part_kind": "tool-call",
                        "tool_name": "lookup",
                        "tool_call_id": "call",
                        "args": {"z": {"last": 0, "first": False}, "a": None},
                    }
                ],
            },
            {
                "kind": "request",
                "parts": [
                    {
                        "part_kind": "tool-return",
                        "tool_name": "lookup",
                        "tool_call_id": "call",
                        "content": {"z": {"last": 0, "first": False}, "a": None},
                    }
                ],
            },
        ]
        from tests.test_interaction import thread_view

        sent = []

        def handle(request):
            if request.method == "POST":
                body = json.loads(request.content)
                sent.extend(body["message_history"])
                return httpx2.Response(201, json=submitted())
            return httpx2.Response(200, json=thread_view())

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            interaction = await client.agents("agt_1").start("next", message_history=history)
            assert "message_history" not in (await interaction.thread.get()).value.to_dict()
            for values in [sent]:
                for message, key in zip(values, ["args", "content"], strict=True):
                    value = message["parts"][0][key]
                    assert list(value) == ["z", "a"]
                    assert list(value["z"]) == ["last", "first"]

    asyncio.run(scenario())


def test_duplicate_submission_replays_exact_failed_entry_without_unknown_outcome_or_retry() -> None:
    from a13n import SubmissionError
    from tests.test_interaction import entry_view

    async def scenario() -> None:
        requests = []
        writes = 0

        def handle(request):
            nonlocal writes
            requests.append(request)
            if request.method == "POST":
                writes += 1
                return httpx2.Response(201 if writes == 1 else 200, json=submitted())
            value = entry_view(status="failed")
            value["failure"] = {"code": "invalid_argument", "message": "Rejected after acceptance"}
            return httpx2.Response(200, json=value)

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            first = await client.agents("agt_1").start("same", idempotency_key="duplicate")
            replay = await client.agents("agt_1").start("same", idempotency_key="duplicate")
            assert first.entry.id == replay.entry.id == "ent_1"
            assert first.receipt.status_code == 201 and replay.receipt.status_code == 200
            for interaction in (first, replay):
                with pytest.raises(SubmissionError) as caught:
                    await interaction.result(timeout=1, poll_interval=0.001)
                assert caught.value.entry_id == "ent_1"
                assert caught.value.entry.value.status == "failed"
                assert interaction.run is None
        assert len(requests) == 4 and writes == 2
        assert requests[0].content == requests[1].content

    asyncio.run(scenario())
