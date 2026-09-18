import asyncio
import json

import httpx2
import pytest

from a13n import Client, RunAccepted, SubmissionQueued, text_input
from a13n.generated import models as wire

NOW = "2026-09-17T00:00:00Z"


def acceptance(run_id: str = "run_1", thread_id: str = "thread_1", session_id: str = "session_1") -> dict:
    return {
        "run_id": run_id,
        "run_version": 1,
        "session_id": session_id,
        "thread_id": thread_id,
        "thread_version": 2,
        "schema_version": "1",
        "status": "accepted",
    }


def agent_value() -> dict:
    return {
        "id": "agent_1",
        "key": "helper",
        "name": "Helper",
        "workspace_id": "ws_1",
        "organization_id": "org_1",
        "version": 1,
        "enabled": True,
        "source": "custom",
        "current_revision_id": "revision_1",
        "description": None,
        "archived_at": None,
        "duplicated_from_agent_id": None,
        "duplicated_from_revision_id": None,
        "created_at": NOW,
        "updated_at": NOW,
        "created_by": {"principal_type": "system", "principal_id": "system"},
        "updated_by": {"principal_type": "system", "principal_id": "system"},
    }


def run_value(status: str, *, run_id: str = "run_1") -> dict:
    sealed = status in {"completed", "failed", "cancelled", "waiting"}
    return {
        "agent_id": "agent_1",
        "agent_revision_id": "revision_1",
        "completed_at": NOW if status == "completed" else None,
        "created_at": NOW,
        "effective_agent_config_digest": "digest",
        "environment_access": None,
        "environment_id": None,
        "failure": None,
        "id": run_id,
        "input": None,
        "input_kind": "text",
        "input_text": None,
        "labels": {},
        "lineage_kind": "root",
        "output": {"answer": 42} if status == "completed" else None,
        "output_text": "Answer" if status == "completed" else None,
        "parent_run_id": None,
        "pending": {"kind": "approval"} if status == "waiting" else None,
        "retry_of_run_id": None,
        "sealed_at": NOW if sealed else None,
        "sealed_state_digest_sha256": "sealed" if sealed else None,
        "session_id": "session_1",
        "started_at": NOW,
        "status": status,
        "thread_id": "thread_1",
        "trigger_type": "user",
        "updated_at": NOW,
        "version": 1,
        "wait_reason": "feedback" if status == "waiting" else None,
        "waiting_at": NOW if status == "waiting" else None,
    }


def queued_value(state: str = "queued", *, run_id: str | None = None) -> dict:
    return {
        "authority_principal": {"principal_type": "user", "principal_id": "user_1"},
        "created_at": NOW,
        "queued_submission_id": "queue_1",
        "state": state,
        "submission": {"input": {"schema_version": "2"}},
        "submission_digest_sha256": "digest",
        "thread_id": "thread_1",
        "updated_at": NOW,
        "version": 1,
        **({"consumed_at": NOW, "consumed_run_id": run_id} if state == "consumed" else {}),
    }


def test_agent_start_returns_exact_typed_acceptance_without_rebinding() -> None:
    async def scenario() -> None:
        requests: list[httpx2.Request] = []

        async def handler(request: httpx2.Request) -> httpx2.Response:
            requests.append(request)
            if request.method == "GET":
                return httpx2.Response(200, json=agent_value())
            assert request.headers["idempotency-key"] == "start-1"
            body = json.loads(request.content)
            assert body["agent_id"] == "agent_1"
            assert body["input"]["content"] == [{"type": "text", "text": "Hello"}]
            assert "environment" not in body
            return httpx2.Response(202, json=acceptance(), headers={"X-Request-ID": "req_start"})

        async with Client("https://service.example", "token", transport=httpx2.MockTransport(handler)) as client:
            agent = client.workspaces("ws_1").agents("helper")
            accepted = await agent.start("Hello", idempotency_key="start-1")
            assert isinstance(accepted, RunAccepted)
            assert accepted.outcome == "run_accepted"
            assert accepted.run.id == "run_1"
            assert accepted.thread.id == "thread_1"
            assert accepted.session.id == "session_1"
            assert accepted.receipt.request_id == "req_start"
            assert agent.id == "helper"
        assert [request.url.path for request in requests] == [
            "/api/v1/workspaces/ws_1/agents/helper",
            "/api/v1/workspaces/ws_1/runs",
        ]

    asyncio.run(scenario())


def test_thread_submission_preserves_run_or_queue_disposition() -> None:
    async def queued_scenario() -> None:
        async def handler(request: httpx2.Request) -> httpx2.Response:
            assert request.url.path == "/api/v1/threads/thread_1/runs"
            body = json.loads(request.content)
            assert body["expected_thread_version"] == 7
            return httpx2.Response(
                202,
                json={"outcome": "queued", "queue_version": 3, "queued_submission": queued_value()},
            )

        async with Client("https://service.example", "token", transport=httpx2.MockTransport(handler)) as client:
            result = await client.threads("thread_1").submit(
                text_input("Next"), expected_thread_version=7, idempotency_key="submit-1"
            )
            assert isinstance(result, SubmissionQueued)
            assert result.queued_submission.id == "queue_1"
            assert result.thread.id == "thread_1"
            assert result.receipt.value.queue_version == 3

    async def accepted_scenario() -> None:
        async def handler(_request: httpx2.Request) -> httpx2.Response:
            return httpx2.Response(
                202,
                json={"outcome": "run_accepted", "queue_version": 4, "run": acceptance("run_2")},
            )

        async with Client("https://service.example", "token", transport=httpx2.MockTransport(handler)) as client:
            result = await client.threads("thread_1").submit(
                "Now", expected_thread_version=8, idempotency_key="submit-2"
            )
            assert isinstance(result, RunAccepted)
            assert result.run.id == "run_2"
            assert result.receipt.value.queue_version == 4

    asyncio.run(queued_scenario())
    asyncio.run(accepted_scenario())


def test_wait_queue_observation_controls_and_successors_are_explicit() -> None:
    async def scenario() -> None:
        run_reads = iter([run_value("running"), run_value("waiting")])
        queue_reads = iter([queued_value(), queued_value("consumed", run_id="run_2")])
        requests: list[httpx2.Request] = []

        async def handler(request: httpx2.Request) -> httpx2.Response:
            requests.append(request)
            path = request.url.path
            if path == "/api/v1/runs/run_1" and request.method == "GET":
                return httpx2.Response(200, json=next(run_reads))
            if path == "/api/v1/queued-submissions/queue_1":
                return httpx2.Response(200, json=next(queue_reads))
            if path.endswith("/steer"):
                assert json.loads(request.content)["content"][0]["text"] == "Focus"
                return httpx2.Response(
                    202,
                    json={
                        "accepted_at": NOW,
                        "delivery_sequence": 2,
                        "run_id": "run_1",
                        "session_id": "session_1",
                        "steer_id": "steer_1",
                        "thread_id": "thread_1",
                        "schema_version": "1",
                    },
                )
            if path.endswith("/interrupt"):
                assert json.loads(request.content) == {"expected_run_version": 1, "expected_thread_version": 2}
                return httpx2.Response(
                    202,
                    json={"interrupted_at": NOW, "run_id": "run_1", "schema_version": "1", "status": "cancelled"},
                )
            if path.endswith("/retry"):
                return httpx2.Response(202, json=acceptance("run_3"))
            raise AssertionError(path)

        async with Client("https://service.example", "token", transport=httpx2.MockTransport(handler)) as client:
            run = client.runs("run_1")
            sealed = await run.wait(timeout=1.0, poll_interval=0.001)
            assert sealed.value.status == "waiting"
            assert sealed.value.pending == {"kind": "approval"}

            queue = await client.queued_submissions("queue_1").wait(timeout=1.0, poll_interval=0.001)
            assert queue.value.state == wire.QueuedSubmissionState.CONSUMED
            assert queue.value.consumed_run_id == "run_2"
            assert not any(
                request.method == "POST" and "queued-submissions" in request.url.path for request in requests
            )

            steer = await run.steer("Focus", idempotency_key="steer-1")
            assert steer.value.delivery_sequence == 2
            cancelled = await run.cancel(
                expected_run_version=1,
                expected_thread_version=2,
                idempotency_key="cancel-1",
            )
            assert cancelled.value.status == "cancelled"
            successor = await run.retry(wire.RetryRunRequest(expected_thread_version=3), idempotency_key="retry-1")
            assert successor.run.id == "run_3"
            assert run.id == "run_1"

    asyncio.run(scenario())


@pytest.mark.parametrize("timeout,poll_interval", [(0.0, 0.1), (1.0, 0.0), (float("inf"), 0.1)])
def test_wait_rejects_invalid_local_budgets_without_io(timeout: float, poll_interval: float) -> None:
    async def scenario() -> None:
        calls = 0

        async def handler(_request: httpx2.Request) -> httpx2.Response:
            nonlocal calls
            calls += 1
            return httpx2.Response(500)

        async with Client("https://service.example", transport=httpx2.MockTransport(handler)) as client:
            with pytest.raises(ValueError):
                await client.runs("run_1").wait(timeout=timeout, poll_interval=poll_interval)
        assert calls == 0

    asyncio.run(scenario())


@pytest.mark.parametrize("identifier", [None, "", 42])
def test_queued_receipt_requires_nonempty_identity(identifier: object) -> None:
    from a13n import ProtocolError

    async def handler(_request: httpx2.Request) -> httpx2.Response:
        value = queued_value()
        value["queued_submission_id"] = identifier
        return httpx2.Response(202, json={"outcome": "queued", "queue_version": 1, "queued_submission": value})

    async def scenario() -> None:
        async with Client("https://service.example", transport=httpx2.MockTransport(handler)) as client:
            with pytest.raises(ProtocolError, match="identity"):
                await client.threads("thread_1").submit("Next", expected_thread_version=1, idempotency_key="submit")

    asyncio.run(scenario())


def test_feedback_continue_and_fork_preserve_exact_successor_identities() -> None:
    requests = []

    async def handler(request: httpx2.Request) -> httpx2.Response:
        requests.append(request)
        command = request.url.path.rsplit("/", 1)[1]
        body = json.loads(request.content)
        assert request.headers["idempotency-key"] == command
        if command == "feedback":
            assert body["sealed_state_digest_sha256"] == "sealed"
        if command != "fork":
            assert body["expected_thread_version"] == 4
        return httpx2.Response(
            202, json=acceptance("run_" + command, "thread_new" if command == "fork" else "thread_1", "session_1")
        )

    async def scenario() -> None:
        async with Client("https://service.example", transport=httpx2.MockTransport(handler)) as client:
            run = client.runs("run_1")
            feedback = await run.feedback(
                wire.WaitingRunFeedbackRequest(expected_thread_version=4, sealed_state_digest_sha256="sealed"),
                idempotency_key="feedback",
            )
            continued = await run.continue_from(
                wire.ContinueRunRequest(expected_thread_version=4, input_=text_input("Continue")),
                idempotency_key="continue",
            )
            forked = await run.fork(wire.ForkRunRequest(input_=text_input("Fork")), idempotency_key="fork")
            assert feedback.run.id == "run_feedback" and continued.run.id == "run_continue"
            assert forked.run.id == "run_fork" and forked.thread.id == "thread_new"
            assert forked.session.id == continued.session.id == "session_1"
            assert run.id == "run_1"
        assert len(requests) == 3

    asyncio.run(scenario())


@pytest.mark.parametrize("outcome", ["run_accepted", "queued"])
def test_thread_submission_rejects_two_dispositions(outcome: str) -> None:
    from a13n import ProtocolError

    async def handler(_request: httpx2.Request) -> httpx2.Response:
        return httpx2.Response(
            202, json={"outcome": outcome, "queue_version": 1, "run": acceptance(), "queued_submission": queued_value()}
        )

    async def scenario() -> None:
        async with Client("https://service.example", transport=httpx2.MockTransport(handler)) as client:
            with pytest.raises(ProtocolError, match="disposition"):
                await client.threads("thread_1").submit("Next", expected_thread_version=1, idempotency_key="submit")

    asyncio.run(scenario())


@pytest.mark.parametrize("outcome", ["run_accepted", "queued"])
def test_thread_submission_accepts_null_inactive_disposition(outcome: str) -> None:
    async def handler(_request: httpx2.Request) -> httpx2.Response:
        return httpx2.Response(
            202,
            json={
                "outcome": outcome,
                "queue_version": 1,
                "run": acceptance() if outcome == "run_accepted" else None,
                "queued_submission": queued_value() if outcome == "queued" else None,
            },
        )

    async def scenario() -> None:
        async with Client("https://service.example", transport=httpx2.MockTransport(handler)) as client:
            result = await client.threads("thread_1").submit(
                "Next", expected_thread_version=1, idempotency_key="submit"
            )
            assert result.outcome == outcome

    asyncio.run(scenario())


@pytest.mark.parametrize("command", ["feedback", "retry", "continue", "fork"])
def test_successor_acceptance_rejects_source_run_identity(command: str) -> None:
    from a13n import ProtocolError

    calls = []

    async def handler(request: httpx2.Request) -> httpx2.Response:
        calls.append(request)
        return httpx2.Response(202, json=acceptance("run_source"))

    async def scenario() -> None:
        async with Client("https://service.example", transport=httpx2.MockTransport(handler)) as client:
            run = client.runs("run_source")
            with pytest.raises(ProtocolError, match="new Run"):
                if command == "feedback":
                    await run.feedback(
                        wire.WaitingRunFeedbackRequest(expected_thread_version=1, sealed_state_digest_sha256="sealed"),
                        idempotency_key="key",
                    )
                elif command == "retry":
                    await run.retry(wire.RetryRunRequest(expected_thread_version=1), idempotency_key="key")
                elif command == "continue":
                    await run.continue_from(
                        wire.ContinueRunRequest(expected_thread_version=1, input_=text_input("Continue")),
                        idempotency_key="key",
                    )
                else:
                    await run.fork(wire.ForkRunRequest(input_=text_input("Fork")), idempotency_key="key")
            assert run.id == "run_source"
        assert len(calls) == 1
        assert calls[0].url.path == f"/api/v1/runs/run_source/{command}"

    asyncio.run(scenario())


@pytest.mark.parametrize("command", ["start", "submit", "steer"])
@pytest.mark.parametrize("invalid", [None, 42, {}])
def test_input_helpers_reject_invalid_type_before_io(command: str, invalid: object) -> None:
    calls = []

    async def handler(request: httpx2.Request) -> httpx2.Response:
        calls.append(request)
        return httpx2.Response(200, json=agent_value())

    async def scenario() -> None:
        async with Client("https://service.example", transport=httpx2.MockTransport(handler)) as client:
            with pytest.raises(ValueError, match="input"):
                if command == "start":
                    await client.workspaces("ws").agents("helper").start(invalid, idempotency_key="key")
                elif command == "submit":
                    await client.threads("thread_1").submit(invalid, expected_thread_version=1, idempotency_key="key")
                else:
                    await client.runs("run_1").steer(invalid, idempotency_key="key")
        assert calls == []

    asyncio.run(scenario())


@pytest.mark.parametrize("sealed", ["completed", "failed", "cancelled", "waiting"])
def test_wait_ignores_unknown_status_and_returns_each_sealed_state(sealed: str) -> None:
    statuses = iter(["future_nonterminal_status", sealed])
    calls = []

    async def handler(request: httpx2.Request) -> httpx2.Response:
        calls.append(request)
        return httpx2.Response(200, json=run_value(next(statuses)))

    async def scenario() -> None:
        async with Client("https://service.example", transport=httpx2.MockTransport(handler)) as client:
            result = await client.runs("run_1").wait(timeout=1, poll_interval=0.001)
            assert result.value.status == sealed
        assert len(calls) == 2
        assert all(request.method == "GET" for request in calls)

    asyncio.run(scenario())


@pytest.mark.parametrize("stage", ["request", "sleep"])
@pytest.mark.parametrize("cancel", [False, True])
def test_wait_deadline_and_caller_cancel_end_local_work_only(stage: str, cancel: bool) -> None:
    started = asyncio.Event()
    never = asyncio.Event()
    calls = []

    async def handler(request: httpx2.Request) -> httpx2.Response:
        calls.append(request)
        started.set()
        if stage == "request":
            await never.wait()
        return httpx2.Response(200, json=run_value("running"))

    async def scenario() -> None:
        async with Client("https://service.example", transport=httpx2.MockTransport(handler)) as client:
            waiting = asyncio.create_task(client.runs("run_1").wait(timeout=30 if cancel else 0.02, poll_interval=10))
            await started.wait()
            await asyncio.sleep(0)
            if cancel:
                waiting.cancel()
            with pytest.raises(asyncio.CancelledError if cancel else TimeoutError):
                await waiting
            assert not client._tasks
        assert len(calls) == 1 and calls[0].method == "GET"

    asyncio.run(scenario())
