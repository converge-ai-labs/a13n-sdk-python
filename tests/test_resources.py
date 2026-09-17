"""Resource contracts exercised through real serializers and a mock HTTP transport."""

import asyncio
import inspect
import json
from pathlib import Path

import httpx2
import pytest

from a13n import ApiError, Client, ProtocolError, QueuedSubmission, Run, TransportError, text_input
from a13n.generated import models as wire
from a13n.generated import resources
from a13n.generated.types import UNSET

NOW = "2026-09-17T00:00:00Z"


def acceptance(run_id="run_1", thread_id="thread_1"):
    return dict(
        run_id=run_id,
        thread_id=thread_id,
        session_id="session_1",
        run_version=1,
        thread_version=2,
        status="accepted",
        schema_version="1",
    )


def agent_value():
    return dict(
        id="agent_1",
        key="helper",
        name="Helper",
        workspace_id="ws",
        organization_id="org",
        version=1,
        enabled=True,
        source="custom",
        current_revision_id="rev_1",
        description=None,
        archived_at=None,
        duplicated_from_agent_id=None,
        duplicated_from_revision_id=None,
        created_at=NOW,
        updated_at=NOW,
        created_by={"principal_type": "system", "principal_id": "system"},
        updated_by={"principal_type": "system", "principal_id": "system"},
    )


def run_value(status="completed", run_id="run_1"):
    return dict(
        agent_id="agent_1",
        agent_revision_id="rev_1",
        completed_at=NOW if status == "completed" else None,
        created_at=NOW,
        effective_agent_config_digest="digest",
        environment_access=None,
        environment_id=None,
        failure=None,
        id=run_id,
        input=None,
        input_kind="text",
        input_text=None,
        labels={},
        lineage_kind="root",
        output={"answer": 42},
        output_text="Answer",
        parent_run_id=None,
        pending=None,
        retry_of_run_id=None,
        sealed_at=None if status in {"running", "accepted", "new_status"} else NOW,
        sealed_state_digest_sha256=None,
        session_id="session_1",
        started_at=NOW,
        status=status,
        thread_id="thread_1",
        trigger_type="user",
        updated_at=NOW,
        version=1,
        wait_reason=None,
        waiting_at=None,
    )


def queue_value(state="queued"):
    return dict(
        authority_principal={"principal_type": "user", "principal_id": "user_1"},
        created_at=NOW,
        queued_submission_id="queue_1",
        state=state,
        submission={"input": {"schema_version": "2"}},
        submission_digest_sha256="digest",
        thread_id="thread_1",
        updated_at=NOW,
        version=1,
        consumed_run_id="run_2" if state == "consumed" else None,
    )


def error_value(code="conflict"):
    return {
        "error": {"code": code, "message": "Safe explanation", "request_id": "request_body", "details": {"version": 2}}
    }


def test_resource_binding_is_local_typed_and_keeps_compatibility():
    async def scenario():
        async def fail(_request):
            pytest.fail("Binding must not perform I/O")

        async with Client("http://test/prefix", "secret", transport=httpx2.MockTransport(fail)) as client:
            assert client.workspaces("ws").agents("helper").id == "helper"
            assert isinstance(client.runs("run_1"), Run)
            assert callable(client.web_providers)
            assert callable(client.workspace)
            assert isinstance(client.resources.workspaces("ws"), resources.Workspace)
            assert not hasattr(client.sessions("session_1"), "get")
            assert not callable(client.runs("run_1").items)
            with pytest.raises(AttributeError):
                client.runs("run_1").id = "another"
            for selector in ["", ".", ".."]:
                with pytest.raises(ValueError):
                    client.runs(selector)

    asyncio.run(scenario())


def test_every_operation_has_a_reachable_statically_typed_method():
    document = json.loads((Path(__file__).parents[1] / "contract/openapi.json").read_text())
    expected = {op["operationId"] for ops in document["paths"].values() for op in ops.values() if "operationId" in op}
    assert set(resources.OPERATIONS) == expected
    for class_method in resources.OPERATIONS.values():
        cls_name, method_name = class_method.split(".")
        # Introspection belongs in coverage tests, never in resource dispatch.
        method = getattr(getattr(resources, cls_name), method_name)
        signature = inspect.signature(method)
        assert signature.return_annotation
        assert not any(p.kind == p.VAR_KEYWORD for p in signature.parameters.values())
    assert hasattr(resources.Agent, "get")
    assert not hasattr(resources.Agent, "list")


def test_agent_start_preserves_input_options_acceptance_and_shared_pool():
    calls = []

    async def handler(request):
        calls.append(request)
        assert request.headers["authorization"] == "Bearer secret"
        if request.method == "GET":
            assert request.url.raw_path == b"/prefix/api/v1/workspaces/ws/agents/key%2Fwith%20space"
            return httpx2.Response(200, json=agent_value())
        assert request.url.path == "/prefix/api/v1/workspaces/ws/runs"
        assert request.headers["idempotency-key"] == "start-1"
        assert json.loads(request.content) == {
            "agent_id": "agent_1",
            "input": {"schema_version": "2", "content": [{"type": "text", "text": "Hello"}]},
            "environment": None,
            "agent_revision_id": "rev_selected",
        }
        return httpx2.Response(202, json=acceptance(), headers={"etag": '"v1"', "x-request-id": "req_1"})

    async def scenario():
        client = Client("http://test/prefix", "secret", transport=httpx2.MockTransport(handler))
        agent = client.workspaces("ws").agents("key/with space")
        async with client:
            run = await agent.start(
                "Hello", idempotency_key="start-1", environment=None, agent_revision_id="rev_selected"
            )
            assert run.id == "run_1"
            assert run.acceptance.value.session_id == "session_1"
            assert run.acceptance.etag == '"v1"'
            assert run.acceptance.request_id == "req_1"
            assert "secret" not in repr(run)
            assert "run_1" not in repr(run.acceptance)
        with pytest.raises(TransportError, match="closed"):
            await run.get()
        assert len(calls) == 2

    asyncio.run(scenario())


@pytest.mark.parametrize("status", ["completed", "failed", "cancelled", "waiting"])
def test_wait_observes_exact_run_and_stops_on_all_sealed_states(status):
    calls = []

    async def handler(request):
        calls.append(request)
        assert request.method == "GET" and request.url.path == "/api/v1/runs/run_1"
        return httpx2.Response(200, json=run_value("running" if len(calls) == 1 else status))

    async def scenario():
        async with Client("http://test", "secret", transport=httpx2.MockTransport(handler)) as client:
            result = await client.runs("run_1").wait(timeout=1, poll_interval=0.001)
            assert result.value.status == status
            assert len(calls) == 2

    asyncio.run(scenario())


def test_unknown_status_wait_timeout_never_interrupts_or_advances():
    calls = []

    async def handler(request):
        calls.append(request)
        return httpx2.Response(200, json=run_value("new_status"))

    async def scenario():
        async with Client("http://test", "secret", transport=httpx2.MockTransport(handler)) as client:
            snapshot = await client.runs("run_1").get()
            assert snapshot.value.status == "new_status"
            with pytest.raises(TimeoutError):
                await client.runs("run_1").wait(timeout=0.02, poll_interval=0.001)
        assert calls and all(r.method == "GET" for r in calls)

    asyncio.run(scenario())


@pytest.mark.parametrize(
    "command,body",
    [
        ("feedback", wire.WaitingRunFeedbackRequest(expected_thread_version=2, sealed_state_digest_sha256="digest")),
        ("retry", wire.RetryRunRequest(expected_thread_version=2)),
        ("fork", wire.ForkRunRequest(input_=text_input("fork"))),
        ("continue_", wire.ContinueRunRequest(expected_thread_version=2, input_=text_input("continue"))),
    ],
)
def test_explicit_commands_return_new_run_without_rebinding(command, body):
    async def handler(request):
        assert request.url.path == "/api/v1/runs/run_1/" + command.rstrip("_")
        assert request.headers["idempotency-key"] == "command-1"
        assert json.loads(request.content) == body.to_dict()
        return httpx2.Response(202, json=acceptance("run_2", "child" if command == "fork" else "thread_1"))

    async def scenario():
        async with Client("http://test", "secret", transport=httpx2.MockTransport(handler)) as client:
            original = client.runs("run_1")
            successor = await getattr(original, command)(body, idempotency_key="command-1")
            assert original.id == "run_1" and successor.id == "run_2"
            assert successor.acceptance.value.session_id == "session_1"
            assert successor.acceptance.value.thread_id == ("child" if command == "fork" else "thread_1")
            assert original.acceptance is None

    asyncio.run(scenario())


@pytest.mark.parametrize("outcome", ["run_accepted", "queued"])
def test_thread_submit_preserves_actual_branch_and_queue_version(outcome):
    async def handler(request):
        assert request.url.path == "/api/v1/threads/thread_1/runs"
        assert request.headers["idempotency-key"] == "submit-1"
        value = {"outcome": outcome, "queue_version": 7}
        value["run" if outcome == "run_accepted" else "queued_submission"] = (
            acceptance() if outcome == "run_accepted" else queue_value()
        )
        return httpx2.Response(202, json=value)

    async def scenario():
        async with Client("http://test", "secret", transport=httpx2.MockTransport(handler)) as client:
            submitted = await client.threads("thread_1").submit(
                wire.ThreadRunSubmissionRequest(expected_thread_version=1, input_=text_input("hi")),
                idempotency_key="submit-1",
            )
            assert submitted.receipt.value.queue_version == 7
            assert isinstance(submitted.resource, Run if outcome == "run_accepted" else QueuedSubmission)
            assert submitted.resource.id == ("run_1" if outcome == "run_accepted" else "queue_1")

    asyncio.run(scenario())


@pytest.mark.parametrize("state", ["consumed", "failed"])
def test_queue_wait_only_reads_and_keeps_non_consumption_outcome(state):
    calls = []

    async def handler(request):
        calls.append(request)
        assert request.method == "GET" and request.url.path == "/api/v1/queued-submissions/queue_1"
        return httpx2.Response(200, json=queue_value("queued" if len(calls) == 1 else state))

    async def scenario():
        async with Client("http://test", "secret", transport=httpx2.MockTransport(handler)) as client:
            result = await client.queued_submissions("queue_1").wait(timeout=1, poll_interval=0.001)
            assert result.snapshot.value.state == state
            assert result.run.id == "run_2" if state == "consumed" else result.run is None
            assert len(calls) == 2

    asyncio.run(scenario())


def test_queue_consumption_failed_200_is_a_receipt_not_an_error():
    async def handler(request):
        assert request.url.path == "/api/v1/threads/thread_1/queued-submissions/consume"
        return httpx2.Response(
            200, json={"outcome": "submission_failed", "queue_version": 3, "queued_submission": queue_value("failed")}
        )

    async def scenario():
        async with Client("http://test", "secret", transport=httpx2.MockTransport(handler)) as client:
            result = await client.threads("thread_1").queued_submissions.consume(
                body=wire.ConsumeQueuedSubmissionRequest(expected_thread_version=1, expected_queue_version=2),
                idempotency_key="consume-1",
            )
            assert result.status == 200 and result.value.outcome == "submission_failed"
            assert result.value.run is UNSET

    asyncio.run(scenario())


def test_pages_are_lazy_continue_empty_page_and_keep_filters_metadata():
    calls = []

    async def handler(request):
        calls.append(request)
        assert request.url.params["limit"] == "1"
        assert request.url.params["order"] == "asc"
        cursor = request.url.params.get("cursor")
        assert cursor == (None if len(calls) == 1 else "opaque&next")
        return httpx2.Response(
            200,
            json={
                "items": [],
                "next_cursor": "opaque&next" if cursor is None else None,
                "snapshot_version": 7,
                "projection_cursor": "100-0",
                "complete": True,
                "finalized": False,
                "incomplete_reason": None,
            },
            headers={"x-request-id": str(len(calls))},
        )

    async def scenario():
        async with Client("http://test", "secret", transport=httpx2.MockTransport(handler)) as client:
            iterator = client.runs("run_1").items.pages(limit=1, order=wire.GetRunsRunIdItemsOrder.ASC)
            assert not calls
            first = await anext(iterator)
            assert len(calls) == 1 and first.value.projection_cursor == "100-0"
            second = await anext(iterator)
            assert second.request_id == "2" and second.value.snapshot_version == 7
            with pytest.raises(StopAsyncIteration):
                await anext(iterator)
            assert len(calls) == 2

    asyncio.run(scenario())


def test_repeated_cursor_is_explicit_error_not_an_infinite_loop():
    async def handler(request):
        return httpx2.Response(200, json={"items": [], "next_cursor": "same"})

    async def scenario():
        async with Client("http://test", "secret", transport=httpx2.MockTransport(handler)) as client:
            with pytest.raises(ProtocolError, match="repeated"):
                async for _ in client.workspaces("ws").agents.pages():
                    pass

    asyncio.run(scenario())


def test_scopes_mutation_null_etag_errors_and_no_replay():
    calls = []

    async def handler(request):
        calls.append(request)
        assert request.url.path == "/api/v1/organizations/org/web-providers/provider"
        assert request.headers["if-match"] == '"v1"'
        assert json.loads(request.content) == {"credential": None}
        return httpx2.Response(412, json=error_value(), headers={"retry-after": "5"})

    async def scenario():
        async with Client("http://test", "secret", transport=httpx2.MockTransport(handler)) as client:
            with pytest.raises(ApiError) as caught:
                await (
                    client.organizations("org")
                    .web_providers("provider")
                    .update(body=wire.UpdateWebProviderRequest(credential=None), if_match='"v1"')
                )
            assert caught.value.status == 412
            assert caught.value.details == {"version": 2}
            assert caught.value.request_id == "request_body" and caught.value.retry_after == "5"
            assert len(calls) == 1

    asyncio.run(scenario())


def test_transport_failure_does_not_replay_and_malformed_success_is_protocol_error():
    calls = []

    async def handler(request):
        calls.append(request)
        if request.method == "POST":
            raise httpx2.ReadError("response lost")
        return httpx2.Response(200, json={"unexpected": "shape"})

    async def scenario():
        async with Client("http://test", "secret", transport=httpx2.MockTransport(handler)) as client:
            with pytest.raises(TransportError, match="unknown"):
                await client.runs("run_1").retry(
                    wire.RetryRunRequest(expected_thread_version=1), idempotency_key="retry-1"
                )
            with pytest.raises(ProtocolError):
                await client.runs("run_1").get()
            assert len(calls) == 2

    asyncio.run(scenario())


def test_generated_binary_resource_stream_does_not_buffer_and_releases_response():
    closed = []

    class Body(httpx2.AsyncByteStream):
        async def __aiter__(self):
            yield b"first"
            pytest.fail("Early break must not read remaining binary content")

        async def aclose(self):
            closed.append(True)

    async def handler(request):
        assert request.url.path == "/api/v1/assets/asset_1/content"
        return httpx2.Response(200, stream=Body())

    async def scenario():
        async with Client("http://test", "secret", transport=httpx2.MockTransport(handler)) as client:
            async with client.resources.assets("asset_1").content.get_stream() as response:
                assert await anext(response.aiter_bytes()) == b"first"
            assert closed

    asyncio.run(scenario())


@pytest.mark.parametrize("operation", ["password_reset", "email_change"])
def test_accepted_json_null_is_success_not_missing_response(operation):
    async def handler(request):
        return httpx2.Response(
            202, content=b"null", headers={"content-type": "application/json", "x-request-id": "accepted"}
        )

    async def scenario():
        async with Client("http://test", "secret", transport=httpx2.MockTransport(handler)) as client:
            if operation == "password_reset":
                result = await client.resources.auth.password_reset.create(
                    body=wire.PasswordResetRequest(email="user@example.test")
                )
            else:
                result = await client.resources.users.me.email_change.create(
                    body=wire.EmailChangeRequest(email="user@example.test", current_password="test-only")
                )
            assert result.status == 202 and result.value is None
            assert result.request_id == "accepted" and result.content == b"null"

    asyncio.run(scenario())


@pytest.mark.parametrize("kind", ["skill", "avatar"])
def test_known_binary_export_adapters_support_buffered_and_streaming_content(kind):
    content = b"PK\\\xff\x00binary"

    async def handler(request):
        assert request.url.path == (
            "/api/v1/skill-revisions/revision/content"
            if kind == "skill"
            else "/api/v1/workspaces/ws/agents/helper/avatar/image"
        )
        return httpx2.Response(
            200, content=content, headers={"content-type": "application/zip" if kind == "skill" else "image/webp"}
        )

    async def scenario():
        async with Client("http://test", "secret", transport=httpx2.MockTransport(handler)) as client:
            resource = (
                client.resources.skill_revisions("revision").content
                if kind == "skill"
                else client.workspaces("ws").agents("helper").avatar("image")
            )
            result = await resource.get()
            assert result.value.payload.read() == content
            async with resource.get_stream() as response:
                assert b"".join([part async for part in response.aiter_bytes()]) == content

    asyncio.run(scenario())
