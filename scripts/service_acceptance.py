"""HTTP-only installed-SDK acceptance against an existing configured Service.

Requires A13N_SERVICE_URL, A13N_API_TOKEN, A13N_WORKSPACE, A13N_AGENT,
and A13N_CLIENT_TOOL_AGENT. The two Agents must use a reachable Model; the
second must expose a client Tool that can enter waiting state.

The script creates and retains Runs and queued submissions for inspection. Its
single injected disconnect is confined to this process's first Run SSE response.
It never provisions credentials, imports Service code, resets state, or deletes
resources. Output contains identities and protocol evidence, never credentials
or model output.
"""

from __future__ import annotations

import asyncio
import json
import os
from collections.abc import AsyncIterator
from typing import Any
from uuid import uuid4

import httpx2 as httpx

from a13n import ApiError, Client, RunAccepted, SubmissionQueued, text_input
from a13n.generated import models as wire


class _DisconnectAfterEventStream(httpx.AsyncByteStream):
    def __init__(
        self,
        inner: httpx.AsyncByteStream,
        request: httpx.Request,
        transport: DisconnectAfterEventTransport,
    ) -> None:
        self._inner = inner
        self._request = request
        self._transport = transport

    async def __aiter__(self) -> AsyncIterator[bytes]:
        buffered = bytearray()
        async for chunk in self._inner:
            buffered.extend(chunk)
            while boundary := _sse_frame_boundary(buffered):
                end, has_data = boundary
                frame = bytes(buffered[:end])
                del buffered[:end]
                yield frame
                if has_data:
                    self._transport.disconnects += 1
                    await self._inner.aclose()
                    raise httpx.ReadError("Injected Run SSE disconnect after one complete event", request=self._request)
        if buffered:
            yield bytes(buffered)

    async def aclose(self) -> None:
        await self._inner.aclose()


class DisconnectAfterEventTransport(httpx.AsyncBaseTransport):
    """Wrap one real SSE attachment and fail its next read after a complete event."""

    def __init__(self, inner: httpx.AsyncBaseTransport | None = None) -> None:
        self._inner = inner or httpx.AsyncHTTPTransport(trust_env=False, retries=0)
        self._armed = True
        self.disconnects = 0
        self.last_event_ids: list[str | None] = []

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        response = await self._inner.handle_async_request(request)
        if request.url.path.endswith("/stream"):
            self.last_event_ids.append(request.headers.get("last-event-id"))
            if self._armed and 200 <= response.status_code < 300:
                if not isinstance(response.stream, httpx.AsyncByteStream):
                    raise RuntimeError("Run SSE response did not expose an async byte stream")
                self._armed = False
                response.stream = _DisconnectAfterEventStream(response.stream, request, self)
        return response

    async def aclose(self) -> None:
        await self._inner.aclose()


def _sse_frame_boundary(buffer: bytes | bytearray) -> tuple[int, bool] | None:
    candidates = [(buffer.find(separator), separator) for separator in (b"\r\n\r\n", b"\n\n", b"\r\r")]
    found = [(index, separator) for index, separator in candidates if index >= 0]
    if not found:
        return None
    index, separator = min(found, key=lambda item: item[0])
    end = index + len(separator)
    frame = bytes(buffer[:index]).replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    has_data = any(line == b"data" or line.startswith(b"data:") for line in frame.split(b"\n"))
    return end, has_data


def _key(label: str) -> str:
    return f"sdk-task19-{label}-{uuid4().hex}"


def _required(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(f"{name} is required")
    return value


def _accepted_evidence(accepted: RunAccepted[Any]) -> dict[str, str]:
    receipt = accepted.receipt.value
    if (
        receipt.run_id != accepted.run.id
        or receipt.thread_id != accepted.thread.id
        or receipt.session_id != accepted.session.id
    ):
        raise RuntimeError("Run acceptance receipt identities do not match the returned resources")
    return {
        "run_id": accepted.run.id,
        "thread_id": accepted.thread.id,
        "session_id": accepted.session.id,
    }


async def _wait_running(run: Any, *, timeout: float = 30.0) -> Any:
    async with asyncio.timeout(timeout):
        while True:
            snapshot = await run.get()
            if snapshot.value.status == wire.RunStatus.RUNNING:
                return snapshot.value
            if snapshot.value.status in {
                wire.RunStatus.COMPLETED,
                wire.RunStatus.FAILED,
                wire.RunStatus.CANCELLED,
                wire.RunStatus.WAITING,
            }:
                raise RuntimeError(f"Run {run.id} sealed as {snapshot.value.status} before reaching running")
            await asyncio.sleep(0.05)


async def _projection(run: Any, *, timeout: float = 30.0) -> dict[str, Any]:
    try:
        first = await run.items.list()
    except ApiError as error:
        if error.status == 409 and error.code == "items_unavailable":
            return {"available": False, "error_code": error.code, "request_id": error.request_id}
        raise
    current = first
    async with asyncio.timeout(timeout):
        while not (current.value.complete and current.value.finalized):
            await asyncio.sleep(0.05)
            current = await run.items.list()
    return {
        "available": True,
        "initial_complete": first.value.complete,
        "initial_finalized": first.value.finalized,
        "complete": current.value.complete,
        "finalized": current.value.finalized,
        "projection_cursor": current.value.projection_cursor,
        "item_count": len(current.value.items),
    }


async def _wait_expected(run: Any, status: wire.RunStatus) -> tuple[Any, dict[str, Any]]:
    result = await run.wait(timeout=120.0, poll_interval=0.1)
    if result.value.status != status:
        raise RuntimeError(f"Run {run.id} sealed as {result.value.status}; expected {status}")
    if result.value.sealed_at is None:
        raise RuntimeError(f"Run {run.id} is terminal without sealed_at")
    return result.value, await _projection(run)


async def _cancel_current(client: Client, run: Any) -> tuple[Any, Any]:
    for _ in range(20):
        run_state = (await run.get()).value
        thread_state = (await client.threads(run_state.thread_id).get()).value
        try:
            receipt = await run.cancel(
                expected_run_version=run_state.version,
                expected_thread_version=thread_state.version,
                idempotency_key=_key("cancel"),
            )
            if receipt.value.run_id != run.id:
                raise RuntimeError("Cancel receipt Run identity does not match the target Run")
            return receipt.value, thread_state
        except ApiError as error:
            if error.status not in {409, 412}:
                raise
            await asyncio.sleep(0.05)
    raise RuntimeError(f"Run {run.id} cancellation could not obtain current versions")


async def _disconnect_acceptance(base_url: str, token: str, workspace_id: str, agent: str) -> dict[str, Any]:
    transport = DisconnectAfterEventTransport()
    async with Client(base_url, token, transport=transport, timeout=60.0) as client:
        accepted = (
            await client.workspaces(workspace_id)
            .agents(agent)
            .start(
                "[slow] [long] Exercise automatic SSE recovery with a local scripted response.",
                idempotency_key=_key("disconnect-start"),
            )
        )
        cursors: list[str] = []
        events: list[str] = []
        async with asyncio.timeout(120.0):
            async with accepted.run.stream(max_reconnects=3) as stream:
                async for observation in stream:
                    cursors.append(observation.cursor)
                    events.append(observation.event.event_type)
        final, projection = await _wait_expected(accepted.run, wire.RunStatus.COMPLETED)
    if transport.disconnects != 1 or len(transport.last_event_ids) < 2:
        raise RuntimeError("The isolated transport did not prove one disconnect and one reconnect")
    if not cursors or transport.last_event_ids[1] != cursors[0]:
        raise RuntimeError("Automatic reconnect did not send the first applied cursor as Last-Event-ID")
    if len(set(cursors)) != len(cursors):
        raise RuntimeError("Automatic reconnect delivered a duplicate cursor")
    return {
        **_accepted_evidence(accepted),
        "status": final.status,
        "event_count": len(events),
        "first_cursor": cursors[0],
        "last_cursor": cursors[-1],
        "disconnects": transport.disconnects,
        "attachment_count": len(transport.last_event_ids),
        "reconnect_last_event_id": transport.last_event_ids[1],
        "projection": projection,
    }


async def _controls(client: Client, workspace_id: str, agent: str) -> dict[str, Any]:
    accepted = (
        await client.workspaces(workspace_id)
        .agents(agent)
        .start(
            "[interruptible] Hold this local draft long enough to exercise steer and cancel.",
            idempotency_key=_key("control-start"),
        )
    )
    running = await _wait_running(accepted.run)
    steer = await accepted.run.steer("Focus only on SDK compatibility evidence.", idempotency_key=_key("steer"))
    if (
        steer.value.run_id != accepted.run.id
        or steer.value.thread_id != accepted.thread.id
        or steer.value.session_id != accepted.session.id
    ):
        raise RuntimeError("Steer receipt identities do not match the target Run")
    interrupt, cancelled_thread = await _cancel_current(client, accepted.run)
    final, projection = await _wait_expected(accepted.run, wire.RunStatus.CANCELLED)
    return {
        **_accepted_evidence(accepted),
        "running_version": running.version,
        "steer_id": steer.value.steer_id,
        "steer_delivery_sequence": steer.value.delivery_sequence,
        "cancel_status": interrupt.status,
        "cancel_thread_version": cancelled_thread.version,
        "status": final.status,
        "projection": projection,
    }


async def _queue(client: Client, workspace_id: str, agent: str) -> dict[str, Any]:
    source = (
        await client.workspaces(workspace_id)
        .agents(agent)
        .start(
            "[interruptible] Complete this source after a queued follow-up is accepted.",
            idempotency_key=_key("queue-source"),
        )
    )
    await _wait_running(source.run)
    thread = await source.thread.get()
    submission = await source.thread.submit(
        "Queued follow-up: return a smaller fictional release scope.",
        expected_thread_version=thread.value.version,
        idempotency_key=_key("queue-submit"),
    )
    if not isinstance(submission, SubmissionQueued):
        raise RuntimeError("The representative queue submission was accepted immediately instead of queued")
    queued_wire = submission.receipt.value.queued_submission
    if not isinstance(queued_wire, wire.QueuedSubmission):
        raise RuntimeError("Queued receipt does not contain a queued submission")
    if queued_wire.queued_submission_id != submission.queued_submission.id or queued_wire.thread_id != source.thread.id:
        raise RuntimeError("Queued submission receipt identities do not match the returned resources")
    source_final, source_projection = await _wait_expected(source.run, wire.RunStatus.COMPLETED)
    disposition = await submission.queued_submission.wait(timeout=120.0, poll_interval=0.1)
    if disposition.value.state != wire.QueuedSubmissionState.CONSUMED:
        raise RuntimeError(f"Queued submission ended as {disposition.value.state}")
    consumed_run_id = disposition.value.consumed_run_id
    if not isinstance(consumed_run_id, str) or not consumed_run_id:
        raise RuntimeError("Consumed queued submission has no Run identity")
    consumed_run = client.runs(consumed_run_id)
    consumed_final, consumed_projection = await _wait_expected(consumed_run, wire.RunStatus.COMPLETED)
    if consumed_final.thread_id != source.thread.id or consumed_final.session_id != source.session.id:
        raise RuntimeError("Consumed queued Run does not belong to the source Thread and Session")
    return {
        "source": {**_accepted_evidence(source), "status": source_final.status, "projection": source_projection},
        "queued_submission_id": submission.queued_submission.id,
        "queue_version": submission.receipt.value.queue_version,
        "queue_state": disposition.value.state,
        "consumed_run_id": consumed_run_id,
        "consumed_status": consumed_final.status,
        "consumed_projection": consumed_projection,
    }


async def _successors(client: Client, workspace_id: str, agent: str, client_tool_agent: str) -> dict[str, Any]:
    failed = (
        await client.workspaces(workspace_id)
        .agents(agent)
        .start("[fail] Exercise failed Run retry identity.", idempotency_key=_key("failed-start"))
    )
    failed_final, failed_projection = await _wait_expected(failed.run, wire.RunStatus.FAILED)
    failed_thread = await failed.thread.get()
    retried = await failed.run.retry(
        wire.RetryRunRequest(expected_thread_version=failed_thread.value.version),
        idempotency_key=_key("retry"),
    )
    retry_final, retry_projection = await _wait_expected(retried.run, wire.RunStatus.FAILED)
    if retried.thread.id != failed.thread.id or retried.session.id != failed.session.id:
        raise RuntimeError("Retry successor does not belong to the source Thread and Session")

    completed = (
        await client.workspaces(workspace_id)
        .agents(agent)
        .start(
            "Create a short local response for continue and fork acceptance.",
            idempotency_key=_key("completed-start"),
        )
    )
    completed_final, completed_projection = await _wait_expected(completed.run, wire.RunStatus.COMPLETED)
    completed_thread = await completed.thread.get()
    continued = await completed.run.continue_from(
        wire.ContinueRunRequest(
            expected_thread_version=completed_thread.value.version,
            input_=text_input("Continue with one compatibility note."),
        ),
        idempotency_key=_key("continue"),
    )
    continue_final, continue_projection = await _wait_expected(continued.run, wire.RunStatus.COMPLETED)
    forked = await completed.run.fork(
        wire.ForkRunRequest(input_=text_input("Fork an independent compatibility note.")),
        idempotency_key=_key("fork"),
    )
    fork_final, fork_projection = await _wait_expected(forked.run, wire.RunStatus.COMPLETED)
    if continued.thread.id != completed.thread.id or continued.session.id != completed.session.id:
        raise RuntimeError("Continue successor does not belong to the source Thread and Session")
    if forked.thread.id == completed.thread.id or forked.session.id != completed.session.id:
        raise RuntimeError("Fork successor did not create a new Thread in the source Session")

    waiting = (
        await client.workspaces(workspace_id)
        .agents(client_tool_agent)
        .start(
            "[client] Review this fictional local SDK rollout.",
            idempotency_key=_key("feedback-start"),
        )
    )
    waiting_final, waiting_projection = await _wait_expected(waiting.run, wire.RunStatus.WAITING)
    if not waiting_final.sealed_state_digest_sha256:
        raise RuntimeError("Waiting Run has no sealed state digest")
    pending = await waiting.run.pending_actions.list()
    if len(pending.value.items) != 1 or pending.value.items[0].kind != "client_tool":
        raise RuntimeError("Waiting Run did not retain exactly one client Tool action")
    waiting_thread = await waiting.thread.get()
    feedback = await waiting.run.feedback(
        wire.WaitingRunFeedbackRequest(
            expected_thread_version=waiting_thread.value.version,
            sealed_state_digest_sha256=waiting_final.sealed_state_digest_sha256,
            resolutions=[
                wire.CompletePendingResolution(
                    call_id=pending.value.items[0].call_id,
                    result={"decision": "approved-for-sdk-acceptance", "reason": "Local scripted evidence"},
                    action="complete",
                )
            ],
        ),
        idempotency_key=_key("feedback"),
    )
    feedback_final, feedback_projection = await _wait_expected(feedback.run, wire.RunStatus.COMPLETED)
    if feedback.thread.id != waiting.thread.id or feedback.session.id != waiting.session.id:
        raise RuntimeError("Feedback successor does not belong to the source Thread and Session")

    return {
        "retry": {
            "source": {**_accepted_evidence(failed), "status": failed_final.status, "projection": failed_projection},
            "successor": {**_accepted_evidence(retried), "status": retry_final.status, "projection": retry_projection},
        },
        "continue": {
            "source": {
                **_accepted_evidence(completed),
                "status": completed_final.status,
                "projection": completed_projection,
            },
            "successor": {
                **_accepted_evidence(continued),
                "status": continue_final.status,
                "projection": continue_projection,
            },
        },
        "fork": {
            "source": {
                **_accepted_evidence(completed),
                "status": completed_final.status,
                "projection": completed_projection,
            },
            "successor": {
                **_accepted_evidence(forked),
                "status": fork_final.status,
                "projection": fork_projection,
            },
        },
        "feedback": {
            "source": {
                **_accepted_evidence(waiting),
                "status": waiting_final.status,
                "pending_call_id": pending.value.items[0].call_id,
                "projection": waiting_projection,
            },
            "successor": {
                **_accepted_evidence(feedback),
                "status": feedback_final.status,
                "projection": feedback_projection,
            },
        },
    }


async def main() -> None:
    base_url = _required("A13N_SERVICE_URL")
    token = _required("A13N_API_TOKEN")
    workspace_id = _required("A13N_WORKSPACE")
    agent = _required("A13N_AGENT")
    client_tool_agent = _required("A13N_CLIENT_TOOL_AGENT")

    disconnect = await _disconnect_acceptance(base_url, token, workspace_id, agent)
    async with Client(base_url, token, timeout=60.0) as client:
        controls = await _controls(client, workspace_id, agent)
        queue = await _queue(client, workspace_id, agent)
        successors = await _successors(client, workspace_id, agent, client_tool_agent)
    print(
        json.dumps(
            {
                "evidence": "real-http-installed-sdk-local-scripted-provider",
                "disconnect": disconnect,
                "controls": controls,
                "queue": queue,
                "successors": successors,
            },
            default=str,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    asyncio.run(main())
