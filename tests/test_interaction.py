import asyncio
import json

import httpx2
import pytest

from a13n import Client, InboxEntry, Interaction, ProtocolError, Resumed, Submitted, text_input
from a13n._interaction import _submitted
from a13n._resources import Result
from a13n.generated import models as wire

NOW = "2026-09-24T00:00:00Z"


def thread_view(thread_id: str = "thr_1", workspace_id: str = "ws_1") -> dict:
    return {
        "archived_at": None,
        "created_at": NOW,
        "current_run_id": None,
        "id": thread_id,
        "labels": {},
        "last_run_id": None,
        "mcp_headers": {},
        "message_history": [],
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
            assert request.url.path == "/api/v1/threads"
            count += 1
            return httpx2.Response(201 if count == 1 else 200, json=submitted(run=count == 1))

        async with Client("https://service.example", "token", transport=httpx2.MockTransport(handle)) as client:
            first = await client.agents("agt_1").start("Hello", idempotency_key="key")
            assert isinstance(first, Interaction)
            assert first.run is not None and first.run.id == "run_1"
            assert first.thread.id == "thr_1" and first.entry.id == "ent_1"
            assert first.receipt.status_code == 201
            replay = await client.agents("agt_1").start("Hello", idempotency_key="key")
            assert replay.run is None and replay.receipt.status_code == 200
        assert requests[0].headers["idempotency-key"] == "key"
        assert requests[0].content == requests[1].content
        assert b'"text":"Hello"' in requests[0].content

    asyncio.run(scenario())


def test_imported_history_is_only_seeded_on_creation_and_preserved_on_readback() -> None:
    history = [
        {"kind": "request", "parts": [{"part_kind": "user-prompt", "content": "Earlier"}], "metadata": {"id": 1}},
        {
            "kind": "response",
            "parts": [{"part_kind": "tool-call", "tool_name": "lookup", "tool_call_id": "call_1", "args": {"x": 1}}],
            "provider_details": {"source": "external"},
        },
        {
            "kind": "request",
            "parts": [
                {
                    "part_kind": "tool-return",
                    "tool_name": "lookup",
                    "tool_call_id": "call_1",
                    "content": {"found": True},
                }
            ],
        },
    ]

    async def scenario() -> None:
        paths: list[str] = []

        def handle(request: httpx2.Request) -> httpx2.Response:
            paths.append(request.url.path)
            if request.method == "GET":
                view = thread_view()
                view["message_history"] = history
                return httpx2.Response(200, json=view)
            body = json.loads(request.content)
            if request.url.path == "/api/v1/threads":
                assert body["message_history"] == history
            else:
                assert "message_history" not in body
            return httpx2.Response(201, json=submitted())

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            agent = client.agents("agt_1")
            created = await agent.start("New", message_history=history, idempotency_key="create")
            readback = await created.thread.get()
            assert [item.to_dict() for item in readback.value.message_history] == history
            await agent.send(created.thread.id, "Next", idempotency_key="follow-up")
            assert created.run is not None
            await created.run.fork(
                body=wire.Fork(agent_id="agt_1", payload=text_input("Branch")), idempotency_key="fork"
            )
        assert paths == [
            "/api/v1/threads",
            "/api/v1/threads/thr_1",
            "/api/v1/threads/thr_1/inbox",
            "/api/v1/runs/run_1/fork",
        ]

    asyncio.run(scenario())


def test_explicit_empty_history_and_omission_are_distinct() -> None:
    async def scenario() -> None:
        bodies: list[dict] = []

        def handle(request: httpx2.Request) -> httpx2.Response:
            bodies.append(json.loads(request.content))
            return httpx2.Response(201, json=submitted())

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            agent = client.agents("agt_1")
            await agent.start("No history", idempotency_key="a")
            await agent.start("Empty history", message_history=[], idempotency_key="b")
        assert "message_history" not in bodies[0]
        assert bodies[1]["message_history"] == []

    asyncio.run(scenario())


def test_resume_sends_full_mixed_batch_and_attachment_in_one_request() -> None:
    async def scenario() -> None:
        requests: list[httpx2.Request] = []

        def handle(request: httpx2.Request) -> httpx2.Response:
            requests.append(request)
            assert request.url.path == "/api/v1/runs/run_1/resume"
            return httpx2.Response(201, json=run_view("run_2"))

        payload = wire.MessagePayload(
            content=[
                wire.TextPart(type_="text", text="Alongside the result"),
                wire.AssetPart(type_="asset", asset_id="ast_1"),
            ]
        )
        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            result = await client.runs("run_1").resume(
                approvals={"approval_1": wire.Deny(action="deny", reason="Declined")},
                calls={
                    "call_1": wire.Returned(status="returned", value={"answer": [1, {"ok": True}]}),
                    "call_2": wire.Failed(status="failed", message="Unavailable"),
                },
                input=payload,
                idempotency_key="batch",
            )
            assert result.run.id == "run_2"
        assert len(requests) == 1
        assert requests[0].headers["idempotency-key"] == "batch"
        assert json.loads(requests[0].content) == {
            "approvals": {"approval_1": {"action": "deny", "reason": "Declined"}},
            "calls": {
                "call_1": {"status": "returned", "value": {"answer": [1, {"ok": True}]}},
                "call_2": {"status": "failed", "message": "Unavailable"},
            },
            "input": payload.to_dict(),
        }

    asyncio.run(scenario())


@pytest.mark.parametrize("input,expected", [(None, None), ("", {"content": [{"type": "text", "text": ""}]})])
def test_resume_optional_input_distinguishes_absent_and_empty(input: str | None, expected: dict | None) -> None:
    async def scenario() -> None:
        bodies: list[dict] = []

        def handle(request: httpx2.Request) -> httpx2.Response:
            bodies.append(json.loads(request.content))
            return httpx2.Response(201, json=run_view("run_2"))

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            run = client.runs("run_1")
            if input is None:
                await run.resume(
                    approvals={},
                    calls={"question_1": wire.Returned(status="returned", value={"answers": {"Choose": "A"}})},
                    idempotency_key="no-input",
                )
            else:
                await run.resume(approvals={}, calls={}, input=input, idempotency_key="empty-input")
        assert len(bodies) == 1
        assert bodies[0]["approvals"] == {}
        if input is None:
            assert bodies[0]["calls"] == {"question_1": {"status": "returned", "value": {"answers": {"Choose": "A"}}}}
            assert "input" not in bodies[0]
        else:
            assert bodies[0] == {"approvals": {}, "calls": {}, "input": expected}

    asyncio.run(scenario())


def test_low_level_resume_posts_exact_generated_body_once() -> None:
    async def scenario() -> None:
        requests: list[httpx2.Request] = []

        def handle(request: httpx2.Request) -> httpx2.Response:
            requests.append(request)
            return httpx2.Response(201, json=run_view("run_2"))

        body = wire.Resume.from_dict(
            {
                "approvals": {"approval_1": {"action": "approve"}},
                "calls": {"question_1": {"status": "returned", "value": {"answers": {"Choice?": "A"}}}},
                "input": {"content": [{"type": "asset", "asset_id": "ast_1"}]},
            }
        )
        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            result = await client.resources.runs("run_1").resume(body=body, idempotency_key="low-level")
            assert isinstance(result, Result) and result.value.id == "run_2"
        assert len(requests) == 1
        assert requests[0].url.path == "/api/v1/runs/run_1/resume"
        assert requests[0].headers["idempotency-key"] == "low-level"
        assert json.loads(requests[0].content) == body.to_dict()

    asyncio.run(scenario())


def test_inbox_submit_explicit_delivery_and_result_identities() -> None:
    async def scenario() -> None:
        def handle(request: httpx2.Request) -> httpx2.Response:
            assert request.url.path == "/api/v1/threads/thr_1/inbox"
            assert b'"delivery":"steer"' in request.content
            return httpx2.Response(201, json=submitted(run=False))

        async with Client("https://service.example", "token", transport=httpx2.MockTransport(handle)) as client:
            receipt = await client.agents("agt_1").send(
                "thr_1", "Hello", delivery=wire.Delivery.STEER, idempotency_key="k"
            )
            assert receipt.run is None
            assert receipt.entry.selectors == {"thread_id": "thr_1", "entry_id": "ent_1"}
            assert receipt.receipt.value.entry.status == wire.EntryStatus.PENDING

    asyncio.run(scenario())


def test_mismatched_receipt_is_protocol_error() -> None:
    async def scenario() -> None:
        async with Client("https://service.example", "token") as client:
            body = wire.Submitted.from_dict(submitted())
            body.entry.thread_id = "another"
            receipt = Result(body, 201, {}, b"")
            with pytest.raises(ProtocolError, match="inconsistent"):
                _submitted(client, receipt)

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
            run = client.runs("run_1")
            wait = await run.wait(timeout=1, poll_interval=0.01)
            assert wait.status == wire.RunStatus.WAITING
            result = await run.resume(approvals={}, calls={}, idempotency_key="resume")
            assert isinstance(result, Resumed) and result.run.id == "run_2" and run.id == "run_1"
            fork = await run.fork(body=wire.Fork(agent_id="agt_1", payload=text_input("Fork")), idempotency_key="fork")
            assert isinstance(fork, Submitted)
            interrupted = await run.interrupt()
            assert interrupted.value.status == wire.RunStatus.CANCELLED
            assert paths == [
                "/api/v1/runs/run_1",
                "/api/v1/runs/run_1/resume",
                "/api/v1/runs/run_1/fork",
                "/api/v1/runs/run_1/interrupt",
            ]

    asyncio.run(scenario())


@pytest.mark.parametrize("timeout,poll_interval", [(0, 1), (1, 0), (float("inf"), 1)])
def test_wait_rejects_invalid_bounds_without_io(timeout: float, poll_interval: float) -> None:
    async def scenario() -> None:
        async with Client("https://service.example", "token") as client:
            run = client.runs("run_1")
            with pytest.raises(ValueError):
                await run.wait(timeout=timeout, poll_interval=poll_interval)

    asyncio.run(scenario())


def test_entry_wait_returns_withdrawn_as_settled() -> None:
    async def scenario() -> None:
        def handle(request: httpx2.Request) -> httpx2.Response:
            return httpx2.Response(200, json=entry_view(status="withdrawn"))

        async with Client("https://service.example", "token", transport=httpx2.MockTransport(handle)) as client:
            entry = InboxEntry(client, {"thread_id": "thr_1", "entry_id": "ent_1"})
            result = await entry.wait(timeout=1, poll_interval=0.01)
            assert result.value.status == wire.EntryStatus.WITHDRAWN

    asyncio.run(scenario())


@pytest.mark.parametrize("accepted", [True, False])
def test_full_thread_body_returns_bound_receipt_without_losing_options(accepted: bool) -> None:
    import json

    async def scenario() -> None:
        body = wire.NewThread.from_dict(
            {
                "agent_id": "agt_1",
                "payload": {"content": [{"type": "text", "text": "Hello"}]},
                "session_id": None,
                "memories": [{"name": "notes", "memory_id": "mem_1", "access": "read"}],
                "environments": [],
                "mcp_headers": {"mcp_1": {"X-Tenant": "tenant"}},
            }
        )
        calls = 0

        def handle(request: httpx2.Request) -> httpx2.Response:
            nonlocal calls
            calls += 1
            assert json.loads(request.content) == body.to_dict()
            assert request.headers["idempotency-key"] == "rich"
            return httpx2.Response(201, json=submitted(run=accepted), headers={"X-Request-Id": "req_1"})

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            result = await client.resources.threads.create(body=body, idempotency_key="rich")
            assert isinstance(result, Result)
            assert result.value.thread.id == "thr_1" and result.value.entry.id == "ent_1"
            assert (result.value.run is not None) == accepted
            assert result.request_id == "req_1"
            assert result.status_code == 201
        assert calls == 1

    asyncio.run(scenario())


def test_full_inbox_body_uses_the_same_bound_receipt() -> None:
    async def scenario() -> None:
        transport = httpx2.MockTransport(lambda _: httpx2.Response(200, json=submitted(run=False)))
        async with Client("https://service.example", transport=transport) as client:
            result = await client.resources.threads("thr_1").inbox_entries.create(
                body=wire.Message(agent_id="agt_1", payload=text_input("Hello")), idempotency_key="full"
            )
            assert isinstance(result, Result) and result.value.run is None
            assert result.status_code == 200
            with pytest.raises(ProtocolError, match="inconsistent"):
                await client.agents("agt_1").send("wrong", "Hello", idempotency_key="wrong")

    asyncio.run(scenario())


def test_workspace_key_submissions_bind_canonical_receipt_ids() -> None:
    async def scenario() -> None:
        paths: list[str] = []

        def handle(request: httpx2.Request) -> httpx2.Response:
            paths.append(request.url.path)
            if request.url.path.endswith("/resume"):
                return httpx2.Response(201, json=run_view("run_2"))
            return httpx2.Response(201, json=submitted())

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            created = await client.agents("agt_1").start("Hello", idempotency_key="create")
            assert created.thread.selectors == {"thread_id": "thr_1"}
            assert created.entry.selectors == {"thread_id": "thr_1", "entry_id": "ent_1"}
            assert created.run is not None and created.run.selectors == {"run_id": "run_1"}
            posted = await client.agents("agt_1").send("thr_1", "Hello", idempotency_key="post")
            assert posted.thread.selectors == {"thread_id": "thr_1"}
            resumed = await client.runs("run_1").resume(approvals={}, calls={}, idempotency_key="resume")
            assert resumed.run.selectors == {"run_id": "run_2"}
            assert paths == [
                "/api/v1/threads",
                "/api/v1/threads/thr_1/inbox",
                "/api/v1/runs/run_1/resume",
            ]

    asyncio.run(scenario())


def test_agent_interaction_result_only_waits_for_consumption_and_exact_run() -> None:
    from a13n import Interaction

    async def scenario() -> None:
        paths: list[str] = []
        entry_reads = 0
        run_reads = 0

        def handle(request: httpx2.Request) -> httpx2.Response:
            nonlocal entry_reads, run_reads
            paths.append(request.url.path)
            if request.method == "POST":
                assert request.headers["idempotency-key"] == "once"
                return httpx2.Response(201, json=submitted(run=False))
            if request.url.path.endswith("/inbox/ent_1"):
                entry_reads += 1
                state = entry_view(status=["assigned", "pending", "consumed"][min(entry_reads - 1, 2)])
                state["assigned_run_id"] = "run_2" if entry_reads == 3 else "run_1" if entry_reads == 1 else None
                return httpx2.Response(200, json=state)
            assert request.url.path == "/api/v1/runs/run_2"
            run_reads += 1
            return httpx2.Response(200, json=run_view("run_2", status="waiting" if run_reads == 1 else "completed"))

        async with Client("https://service.example", "token", transport=httpx2.MockTransport(handle)) as client:
            interaction = await client.agents("agt_1").start("Hi", idempotency_key="once")
            assert isinstance(interaction, Interaction)
            assert interaction.run is None and interaction.thread.id == "thr_1"
            outcome = await interaction.result(timeout=1, poll_interval=0.001)
            assert outcome.status == wire.RunStatus.WAITING and outcome.run.id == "run_2"
        assert paths.count("/api/v1/threads") == 1
        assert not any(path.endswith("/stream") for path in paths)
        assert entry_reads == 3 and run_reads == 1

    asyncio.run(scenario())


@pytest.mark.parametrize("status", ["failed", "withdrawn"])
def test_failed_or_withdrawn_entry_is_typed_disposition(status: str) -> None:
    from a13n import SubmissionError

    async def scenario() -> None:
        paths: list[str] = []

        def handle(request: httpx2.Request) -> httpx2.Response:
            paths.append(request.url.path)
            if request.method == "POST":
                return httpx2.Response(201, json=submitted(run=False))
            return httpx2.Response(200, json=entry_view(status=status))

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            interaction = await client.agents("agt_1").send("thr_1", "Hi", idempotency_key="once")
            with pytest.raises(SubmissionError) as caught:
                await interaction.result(timeout=1)
            assert caught.value.entry_id == "ent_1"
            assert caught.value.thread_id == "thr_1"
            assert caught.value.entry.value.status == status
            assert "Hi" not in str(caught.value)
        assert len(paths) == 2

    asyncio.run(scenario())


def test_submitted_wait_has_one_deadline_and_no_replay() -> None:
    async def scenario() -> None:
        calls = 0

        async def handle(request: httpx2.Request) -> httpx2.Response:
            nonlocal calls
            calls += 1
            if request.method == "POST":
                return httpx2.Response(201, json=submitted(run=True))
            await asyncio.sleep(0.05)
            return httpx2.Response(200, json=entry_view(status="pending"))

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            interaction = await client.agents("agt_1").start("Hi", idempotency_key="once")
            with pytest.raises(TimeoutError):
                await interaction.result(timeout=0.02, poll_interval=0.001)
        assert calls == 2

    asyncio.run(scenario())


def test_finite_interaction_filters_foreign_frames_and_ends_on_idle_socket() -> None:
    import json

    from a13n import Interaction

    def frame(event: str, data: dict, cursor: str | None = None) -> bytes:
        return (f"event: {event}\n" + (f"id: {cursor}\n" if cursor else "") + f"data: {json.dumps(data)}\n\n").encode()

    class IdleStream(httpx2.AsyncByteStream):
        def __init__(self) -> None:
            self.released = False
            self.sent = False

        async def __aiter__(self):
            if not self.sent:
                self.sent = True
                yield b"".join(
                    [
                        frame("boundary", {"run_id": "run_other", "attempt": 1, "sequence": 1}, "1-0"),
                        frame("changed", {"version": 2}),
                        frame("gap", {"run_id": "run_1"}),
                    ]
                )
            await asyncio.Event().wait()

        async def aclose(self) -> None:
            self.released = True

    async def scenario() -> None:
        stream = IdleStream()
        done = asyncio.Event()
        paths: list[str] = []

        def handle(request: httpx2.Request) -> httpx2.Response:
            paths.append(request.url.path)
            if request.method == "POST":
                return httpx2.Response(201, json=submitted())
            if request.url.path.endswith("/inbox/ent_1"):
                entry = entry_view(status="consumed")
                entry["assigned_run_id"] = "run_1"
                return httpx2.Response(200, json=entry)
            if request.url.path.endswith("/stream"):
                return httpx2.Response(200, stream=stream, headers={"Content-Type": "text/event-stream"})
            assert request.url.path == "/api/v1/runs/run_1"
            return httpx2.Response(200, json=run_view(status="completed" if done.is_set() else "running"))

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            interaction = await client.agents("agt_1").start("Hi", idempotency_key="once")
            assert isinstance(interaction, Interaction)
            async with interaction:
                first = await asyncio.wait_for(anext(interaction), timeout=1)
                assert first.event_type == "gap" and first.data["run_id"] == "run_1"
                done.set()
                remaining = [event async for event in interaction]
                assert remaining == []
                assert (await interaction.result()).status == wire.RunStatus.COMPLETED
            assert stream.released
        assert paths.count("/api/v1/threads") == 1

    asyncio.run(scenario())


def test_early_context_exit_cancels_local_observer_without_restarting_result() -> None:
    async def scenario() -> None:
        paths: list[str] = []

        def handle(request: httpx2.Request) -> httpx2.Response:
            paths.append(request.url.path)
            if request.method == "POST":
                return httpx2.Response(201, json=submitted())
            if request.url.path.endswith("/inbox/ent_1"):
                entry = entry_view(status="consumed")
                entry["assigned_run_id"] = "run_1"
                return httpx2.Response(200, json=entry)
            return httpx2.Response(200, json=run_view(status="running"))

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            interaction = await client.agents("agt_1").start("Hi", idempotency_key="once")
            async with interaction:
                pass
            with pytest.raises(RuntimeError, match="closed before an outcome"):
                await interaction.result()
        assert paths.count("/api/v1/threads") == 1

    asyncio.run(scenario())


def test_exact_run_wait_rejects_wrong_run_same_thread() -> None:
    async def scenario() -> None:
        transport = httpx2.MockTransport(
            lambda _: httpx2.Response(200, json=run_view(run_id="run_other", status="completed"))
        )
        async with Client("https://service.example", transport=transport) as client:
            with pytest.raises(ProtocolError, match="inconsistent identity"):
                await client.runs("run_1").wait(timeout=1)

    asyncio.run(scenario())


def test_result_only_then_context_is_cached_and_does_not_reobserve() -> None:
    async def scenario() -> None:
        paths: list[str] = []

        def handle(request: httpx2.Request) -> httpx2.Response:
            paths.append(request.url.path)
            if request.method == "POST":
                return httpx2.Response(201, json=submitted())
            if request.url.path.endswith("/inbox/ent_1"):
                entry = entry_view(status="consumed")
                entry["assigned_run_id"] = "run_1"
                return httpx2.Response(200, json=entry)
            return httpx2.Response(200, json=run_view(status="completed"))

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            interaction = await client.agents("agt_1").start("Hi", idempotency_key="once")
            outcome = await interaction.result(timeout=1)
            assert await interaction.result() is outcome
            async with interaction:
                assert [frame async for frame in interaction] == []
                assert await interaction.result() is outcome
        assert paths == ["/api/v1/threads", "/api/v1/threads/thr_1/inbox/ent_1", "/api/v1/runs/run_1"]

    asyncio.run(scenario())


def test_agent_start_preserves_all_typed_thread_fields_and_extra_mapping_clear() -> None:
    import json

    async def scenario() -> None:
        options = wire.RunOptionsInput.from_dict(
            {"overrides": {"model_settings": {"extra_body": {}, "extra_headers": {"X-Trace": "yes"}}}}
        )
        memories = [wire.MemoryMount(name="notes", memory_id="mem_1", access=wire.MemoryAccess.READ)]
        environments = [wire.MountCreate(name="work", environment_id="env_1")]
        headers = wire.McpHeaders.from_dict({"server": {"X-Tenant": "tenant"}})
        sent: list[dict] = []

        def handle(request: httpx2.Request) -> httpx2.Response:
            sent.append(json.loads(request.content))
            return httpx2.Response(201, json=submitted())

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            await client.agents("agt_1").start(
                wire.MessagePayload.from_dict({"content": [{"type": "text", "text": "structured"}]}),
                idempotency_key="rich",
                agent_revision_id="rev_1",
                session_id=None,
                delivery=wire.Delivery.STEER,
                options=options,
                memories=memories,
                environments=environments,
                mcp_headers=headers,
            )
        assert len(sent) == 1
        assert sent[0] == {
            "agent_id": "agt_1",
            "agent_revision_id": "rev_1",
            "session_id": None,
            "payload": {"content": [{"type": "text", "text": "structured"}]},
            "delivery": "steer",
            "options": options.to_dict(),
            "memories": [memory.to_dict() for memory in memories],
            "environments": [environment.to_dict() for environment in environments],
            "mcp_headers": headers.to_dict(),
        }
        assert sent[0]["options"]["overrides"]["model_settings"]["extra_body"] == {}

    asyncio.run(scenario())


def test_result_only_close_cancels_owned_reads_and_joins_observer() -> None:
    async def scenario() -> None:
        reads = 0
        started = asyncio.Event()

        async def handle(request: httpx2.Request) -> httpx2.Response:
            nonlocal reads
            if request.method == "POST":
                return httpx2.Response(201, json=submitted(run=False))
            reads += 1
            started.set()
            await asyncio.sleep(0.01)
            return httpx2.Response(200, json=entry_view(status="pending"))

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            interaction = await client.agents("agt_1").start("Hi", idempotency_key="once")
            observation = asyncio.create_task(interaction.result(timeout=2, poll_interval=0.001))
            await started.wait()
            await interaction.aclose()
            at_close = reads
            with pytest.raises(asyncio.CancelledError):
                await observation
            await asyncio.sleep(0.03)
            assert reads == at_close
            with pytest.raises(RuntimeError, match="closed before an outcome"):
                await interaction.result()

    asyncio.run(scenario())


def test_close_before_context_entry_cannot_restart_observation() -> None:
    async def scenario() -> None:
        requests = 0

        def handle(request: httpx2.Request) -> httpx2.Response:
            nonlocal requests
            requests += 1
            return httpx2.Response(201, json=submitted())

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            interaction = await client.agents("agt_1").start("Hi", idempotency_key="once")
            await interaction.aclose()
            with pytest.raises(RuntimeError, match="closed"):
                async with interaction:
                    pass
            with pytest.raises(RuntimeError, match="closed before an outcome"):
                await interaction.result()
        assert requests == 1

    asyncio.run(scenario())


def test_concurrent_result_and_context_share_one_entry_and_run_observer() -> None:
    async def scenario() -> None:
        entered = asyncio.Event()
        release = asyncio.Event()
        paths: list[str] = []

        async def handle(request: httpx2.Request) -> httpx2.Response:
            paths.append(request.url.path)
            if request.method == "POST":
                return httpx2.Response(201, json=submitted())
            if request.url.path.endswith("/inbox/ent_1"):
                entered.set()
                await release.wait()
                entry = entry_view(status="consumed")
                entry["assigned_run_id"] = "run_1"
                return httpx2.Response(200, json=entry)
            return httpx2.Response(200, json=run_view(status="completed"))

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            interaction = await client.agents("agt_1").start("Hi", idempotency_key="once")
            result_task = asyncio.create_task(interaction.result(timeout=1, poll_interval=0.01))
            await entered.wait()

            async def consume_context() -> None:
                async with interaction:
                    assert [frame async for frame in interaction] == []

            context_task = asyncio.create_task(consume_context())
            release.set()
            await context_task
            assert (await result_task).status == wire.RunStatus.COMPLETED
        assert paths == ["/api/v1/threads", "/api/v1/threads/thr_1/inbox/ent_1", "/api/v1/runs/run_1"]

    asyncio.run(scenario())


def test_result_cancellation_closes_owned_observation_without_remote_mutation() -> None:
    async def scenario() -> None:
        entered = asyncio.Event()
        reads = 0
        posts = 0

        async def handle(request: httpx2.Request) -> httpx2.Response:
            nonlocal reads, posts
            if request.method == "POST":
                posts += 1
                return httpx2.Response(201, json=submitted(run=False))
            reads += 1
            entered.set()
            await asyncio.Event().wait()
            raise AssertionError("Cancellation failed to stop the in-flight read")

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            interaction = await client.agents("agt_1").start("Hi", idempotency_key="once")
            observation = asyncio.create_task(interaction.result(timeout=2))
            await entered.wait()
            observation.cancel()
            with pytest.raises(asyncio.CancelledError):
                await observation
            at_cancel = reads
            await asyncio.sleep(0.02)
            assert reads == at_cancel and posts == 1
            with pytest.raises(RuntimeError, match="closed before an outcome"):
                await interaction.result()

    asyncio.run(scenario())


@pytest.mark.parametrize("resume_after", [None, "1700000000000-0"])
def test_run_items_preserves_display_coverage_and_resume_hint(resume_after: str | None) -> None:
    snapshot = {
        "run": wire.RunView.from_dict(run_view()).to_dict(),
        "items": [],
        "complete": False,
        "baseline": True,
        "position": "1-5",
        "resume_after": resume_after,
    }
    parsed = wire.RunItems.from_dict(snapshot)
    assert parsed.position == "1-5" and parsed.resume_after == resume_after
    assert parsed.to_dict() == snapshot
    del snapshot["resume_after"]
    omitted_hint = wire.RunItems.from_dict(snapshot)
    assert "resume_after" not in omitted_hint.to_dict()


def test_gap_recovery_is_explicit_readback_then_new_covered_stream() -> None:
    from a13n import ThreadStream

    async def scenario() -> None:
        requests: list[httpx2.Request] = []

        def handle(request: httpx2.Request) -> httpx2.Response:
            requests.append(request)
            if request.url.path.endswith("/items"):
                return httpx2.Response(
                    200,
                    json={
                        "run": run_view(),
                        "items": [],
                        "complete": False,
                        "baseline": True,
                        "position": "1-5",
                        "resume_after": "500-0",
                    },
                )
            assert request.url.path == "/api/v1/threads/thr_1/stream"
            if len(requests) == 1:
                assert not request.url.params and "last-event-id" not in request.headers
                content = b'event: gap\ndata: {"run_id":"run_1","position":"1-5"}\n\n'
            else:
                assert dict(request.url.params) == {"run": "run_1", "position": "1-5"}
                assert request.headers["last-event-id"] == "500-0"
                content = b'id: 501-0\nevent: boundary\ndata: {"run_id":"run_1","attempt":1,"sequence":5}\n\n'
            return httpx2.Response(200, content=content, headers={"Content-Type": "text/event-stream"})

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            async with ThreadStream(client.threads("thr_1"), reconnect=False) as initial:
                gap = await anext(initial)
                assert gap.event_type == "gap" and gap.data.get("position") == "1-5"
            assert len(requests) == 1  # Parser never read or silently merged a snapshot.
            snapshot = (await client.runs(gap.data["run_id"]).items.get()).value
            assert snapshot.position is not None and isinstance(snapshot.resume_after, str)
            async with ThreadStream(
                client.threads("thr_1"),
                run=snapshot.run.id,
                position=snapshot.position,
                after=snapshot.resume_after,
                reconnect=False,
            ) as recovered:
                boundary = await anext(recovered)
                assert boundary.event_type == "boundary" and boundary.data["sequence"] == 5
        assert [request.method for request in requests] == ["GET", "GET", "GET"]

    asyncio.run(scenario())


@pytest.mark.parametrize("status", ["failed", "cancelled"])
def test_normal_send_continues_latest_sealed_failure_history_without_retry_or_fork(status: str) -> None:
    async def scenario() -> None:
        requests: list[tuple[str, str]] = []
        source_thread = thread_view()
        source_thread["last_run_id"] = "run_failed"

        def handle(request: httpx2.Request) -> httpx2.Response:
            requests.append((request.method, request.url.path))
            if request.url.path == "/api/v1/runs/run_failed":
                return httpx2.Response(200, json=run_view(run_id="run_failed", status=status))
            if request.url.path == "/api/v1/threads/thr_1":
                return httpx2.Response(200, json=source_thread)
            if request.method == "POST":
                assert request.url.path == "/api/v1/threads/thr_1/inbox"
                assert request.headers["idempotency-key"] == "continue"
                assert json.loads(request.content)["payload"] == {"content": [{"type": "text", "text": "Continue"}]}
                return httpx2.Response(
                    201,
                    json={
                        "thread": source_thread,
                        "entry": entry_view(),
                        "run": run_view(run_id="run_next"),
                    },
                )
            if request.url.path == "/api/v1/threads/thr_1/inbox/ent_1":
                entry = entry_view(status="consumed")
                entry["assigned_run_id"] = "run_next"
                return httpx2.Response(200, json=entry)
            assert request.url.path == "/api/v1/runs/run_next"
            return httpx2.Response(200, json=run_view(run_id="run_next", status="completed"))

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            source = await client.runs("run_failed").wait()
            assert source.status == status
            assert (await client.threads("thr_1").get()).value.last_run_id == "run_failed"
            following = await client.agents("agt_1").send("thr_1", "Continue", idempotency_key="continue")
            result = await following.result()
            assert result.run.id == "run_next" and result.status == "completed"
        assert [path for method, path in requests if method == "POST"] == ["/api/v1/threads/thr_1/inbox"]

    asyncio.run(scenario())


def test_historical_complete_window_does_not_seal_finite_interaction() -> None:
    async def scenario() -> None:
        reads = 0
        methods: list[tuple[str, str]] = []

        def handle(request: httpx2.Request) -> httpx2.Response:
            nonlocal reads
            methods.append((request.method, request.url.path))
            if request.method == "POST":
                return httpx2.Response(201, json=submitted())
            if request.url.path.endswith("/items"):
                assert dict(request.url.params) == {"before": "2"}
                return httpx2.Response(
                    200,
                    json={
                        "run": run_view(status="completed"),
                        "items": [],
                        "baseline": False,
                        "complete": True,
                        "position": None,
                        "continuation": None,
                        "resume_after": None,
                    },
                )
            if request.url.path.endswith("/inbox/ent_1"):
                entry = entry_view(status="consumed")
                entry["assigned_run_id"] = "run_1"
                return httpx2.Response(200, json=entry)
            assert request.url.path == "/api/v1/runs/run_1"
            reads += 1
            return httpx2.Response(200, json=run_view(status="running" if reads == 1 else "completed"))

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            interaction = await client.agents("agt_1").start("Hello", idempotency_key="start")
            page = (await client.runs("run_1").items.get(before=2)).value
            assert page.complete and not page.baseline and reads == 0
            outcome = await interaction.result(poll_interval=0.001)
            assert outcome.status == "completed" and reads == 2
        assert all(not path.endswith("/stream") for _, path in methods)

    asyncio.run(scenario())
