import asyncio

import httpx2
import pytest

from a13n import Client, ProtocolError, Resumed, Submitted, text_input
from a13n._interaction import _submitted
from a13n._resources import Result
from a13n.generated import models as wire

NOW = "2026-09-24T00:00:00Z"


def thread_view(thread_id: str = "thr_1", workspace_id: str = "ws_1") -> dict:
    return {
        "archived_at": None,
        "created_at": NOW,
        "current_run_id": None,
        "head_run_id": None,
        "id": thread_id,
        "labels": {},
        "last_run_id": None,
        "mcp_headers": {},
        "origin": "new",
        "origin_run_id": None,
        "origin_thread_id": None,
        "origin_tool_call_id": None,
        "session_id": "ses_1",
        "subagent": None,
        "updated_at": NOW,
        "version": 1,
        "workspace_id": workspace_id,
    }


def entry_view(thread_id: str = "thr_1", status: str = "pending") -> dict:
    return {
        "agent_id": "agt_1",
        "agent_revision_id": None,
        "assigned_run_id": None,
        "child_run_id": None,
        "created_at": NOW,
        "delivery": "next_run",
        "failure": None,
        "finished_at": None,
        "id": "ent_1",
        "incorporated_checkpoint_seq": None,
        "kind": "message",
        "options": {},
        "origin_run_id": None,
        "payload": {"content": [{"type": "text", "text": "Hello"}]},
        "position": 1,
        "principal_id": "usr_1",
        "status": status,
        "thread_id": thread_id,
    }


def run_view(run_id: str = "run_1", thread_id: str = "thr_1", status: str = "accepted") -> dict:
    return {
        "agent_id": "agt_1",
        "agent_revision_id": "rev_1",
        "attempts": 0,
        "cancel_requested_at": None,
        "created_at": NOW,
        "current_attempt_id": None,
        "environment_mounts": [],
        "memory_mounts": [],
        "failure": None,
        "id": run_id,
        "labels": {},
        "lineage": "root",
        "max_attempts": 3,
        "options": {},
        "output": None,
        "parent_run_id": None,
        "pending": None,
        "principal_id": "usr_1",
        "resume": None,
        "resumed_by_id": None,
        "revision_selection": "default",
        "sealed_at": NOW if status in {"waiting", "completed", "failed", "cancelled"} else None,
        "session_id": "ses_1",
        "source_entry_id": "ent_1",
        "started_at": None,
        "status": status,
        "thread_id": thread_id,
        "trigger": "input",
        "updated_at": NOW,
        "usage_at_seal": None,
        "version": 1,
        "wait_reason": None,
        "workspace_id": "ws_1",
    }


def submitted(run: bool = True) -> dict:
    return {"thread": thread_view(), "entry": entry_view(), "run": run_view() if run else None}


def test_new_thread_submission_and_replay_preserve_queue_disposition() -> None:
    async def scenario() -> None:
        requests: list[httpx2.Request] = []
        count = 0

        def handle(request: httpx2.Request) -> httpx2.Response:
            nonlocal count
            requests.append(request)
            assert request.url.path == "/api/v1/workspaces/ws_1/threads"
            count += 1
            return httpx2.Response(201 if count == 1 else 200, json=submitted(run=count == 1))

        async with Client("https://service.example", "token", transport=httpx2.MockTransport(handle)) as client:
            first = await client.workspaces("ws_1").start("Hello", agent_id="agt_1", idempotency_key="key")
            assert isinstance(first, Submitted)
            assert first.run is not None and first.run.id == "run_1"
            assert first.thread.id == "thr_1" and first.entry.id == "ent_1"
            assert first.receipt.status_code == 201
            replay = await client.workspaces("ws_1").start("Hello", agent_id="agt_1", idempotency_key="key")
            assert replay.run is None and replay.receipt.status_code == 200
        assert requests[0].headers["idempotency-key"] == "key"
        assert requests[0].content == requests[1].content
        assert b'"text":"Hello"' in requests[0].content

    asyncio.run(scenario())


def test_inbox_submit_explicit_delivery_and_result_identities() -> None:
    async def scenario() -> None:
        def handle(request: httpx2.Request) -> httpx2.Response:
            assert request.url.path == "/api/v1/workspaces/ws_1/threads/thr_1/inbox"
            assert b'"delivery":"steer"' in request.content
            return httpx2.Response(201, json=submitted(run=False))

        async with Client("https://service.example", "token", transport=httpx2.MockTransport(handle)) as client:
            receipt = (
                await client.workspaces("ws_1")
                .threads("thr_1")
                .submit("Hello", agent_id="agt_1", delivery=wire.Delivery.STEER, idempotency_key="k")
            )
            assert receipt.run is None
            assert receipt.entry.selectors == {"workspace_id": "ws_1", "thread_id": "thr_1", "entry_id": "ent_1"}
            assert receipt.receipt.value.entry.status == wire.EntryStatus.PENDING

    asyncio.run(scenario())


def test_mismatched_receipt_is_protocol_error() -> None:
    async def scenario() -> None:
        async with Client("https://service.example", "token") as client:
            body = wire.Submitted.from_dict(submitted())
            body.entry.thread_id = "another"
            receipt = Result(body, 201, {}, b"")
            with pytest.raises(ProtocolError, match="inconsistent"):
                _submitted(client, "ws_1", receipt)

    asyncio.run(scenario())


def test_wait_resume_fork_and_interrupt_are_exact_run_operations() -> None:
    async def scenario() -> None:
        paths: list[str] = []

        def handle(request: httpx2.Request) -> httpx2.Response:
            paths.append(request.url.path)
            if request.url.path.endswith("/fork"):
                return httpx2.Response(201, json=submitted())
            if request.url.path.endswith("/resume"):
                return httpx2.Response(201, json=run_view("run_2"))
            if request.url.path.endswith("/interrupt"):
                return httpx2.Response(200, json=run_view(status="cancelled"))
            return httpx2.Response(200, json=run_view(status="waiting"))

        async with Client("https://service.example", "token", transport=httpx2.MockTransport(handle)) as client:
            run = client.workspaces("ws_1").runs("run_1")
            wait = await run.wait(timeout=1, poll_interval=0.01)
            assert wait.value.status == wire.RunStatus.WAITING
            result = await run.resume(wire.ResumeRequest(), idempotency_key="resume")
            assert isinstance(result, Resumed) and result.run.id == "run_2" and run.id == "run_1"
            fork = await run.fork(wire.Fork(agent_id="agt_1", payload=text_input("Fork")), idempotency_key="fork")
            assert isinstance(fork, Submitted)
            interrupted = await run.interrupt()
            assert interrupted.value.status == wire.RunStatus.CANCELLED
            assert paths == [
                "/api/v1/workspaces/ws_1/runs/run_1",
                "/api/v1/workspaces/ws_1/runs/run_1/resume",
                "/api/v1/workspaces/ws_1/runs/run_1/fork",
                "/api/v1/workspaces/ws_1/runs/run_1/interrupt",
            ]

    asyncio.run(scenario())


@pytest.mark.parametrize("timeout,poll_interval", [(0, 1), (1, 0), (float("inf"), 1)])
def test_wait_rejects_invalid_bounds_without_io(timeout: float, poll_interval: float) -> None:
    async def scenario() -> None:
        async with Client("https://service.example", "token") as client:
            run = client.workspaces("ws_1").runs("run_1")
            with pytest.raises(ValueError):
                await run.wait(timeout=timeout, poll_interval=poll_interval)

    asyncio.run(scenario())


def test_entry_wait_returns_withdrawn_as_settled() -> None:
    async def scenario() -> None:
        def handle(request: httpx2.Request) -> httpx2.Response:
            return httpx2.Response(200, json=entry_view(status="withdrawn"))

        async with Client("https://service.example", "token", transport=httpx2.MockTransport(handle)) as client:
            entry = client.workspaces("ws_1").threads("thr_1").inbox_entries("ent_1")
            result = await entry.wait(timeout=1, poll_interval=0.01)
            assert result.value.status == wire.EntryStatus.WITHDRAWN

    asyncio.run(scenario())
