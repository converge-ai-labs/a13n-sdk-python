"""Installed-SDK acceptance against an existing, disposable Native Service.

Requires A13N_SERVICE_URL, A13N_API_TOKEN, A13N_WORKSPACE, A13N_AGENT,
A13N_CLIENT_TOOL_AGENT and A13N_CA_BUNDLE. All HTTP requests use verified TLS;
this script neither provisions credentials nor resets Service state. Its output
contains protocol identities and status, never credentials or model text.
"""

from __future__ import annotations

import asyncio
import json
import os
from collections.abc import AsyncIterator
from typing import Any
from uuid import uuid4

import httpx2 as httpx

from a13n import Client, Submitted
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
                    raise httpx.ReadError(
                        "Injected Thread SSE disconnect after one complete event", request=self._request
                    )
        if buffered:
            yield bytes(buffered)

    async def aclose(self) -> None:
        await self._inner.aclose()


class DisconnectAfterEventTransport(httpx.AsyncBaseTransport):
    """Wrap one real SSE attachment and fail its next read after a complete event."""

    def __init__(self, inner: httpx.AsyncBaseTransport) -> None:
        self._inner = inner
        self._armed = True
        self.disconnects = 0
        self.last_event_ids: list[str | None] = []

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        response = await self._inner.handle_async_request(request)
        if request.url.path.endswith("/stream"):
            self.last_event_ids.append(request.headers.get("last-event-id"))
            if self._armed and 200 <= response.status_code < 300:
                if not isinstance(response.stream, httpx.AsyncByteStream):
                    raise RuntimeError("Thread SSE response did not expose an async byte stream")
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
    return f"sdk-native-{label}-{uuid4().hex}"


def _required(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(f"{name} is required")
    return value


def _submission_evidence(submitted: Submitted) -> dict[str, str | None]:
    value = submitted.receipt.value
    if (
        value.thread.id != submitted.thread.id
        or value.entry.id != submitted.entry.id
        or value.entry.thread_id != submitted.thread.id
        or (value.run.id if value.run is not None else None)
        != (submitted.run.id if submitted.run is not None else None)
    ):
        raise RuntimeError("Submission receipt identities do not match bound resources")
    return {
        "thread_id": submitted.thread.id,
        "entry_id": submitted.entry.id,
        "run_id": submitted.run.id if submitted.run else None,
    }


def _accepted_run(submitted: Submitted) -> Any:
    if submitted.run is None:
        raise RuntimeError("Idle Thread submission unexpectedly has no Run")
    return submitted.run


async def _wait_run(run: Any, expected: wire.RunStatus) -> dict[str, Any]:
    result = await run.wait(timeout=120.0, poll_interval=0.1)
    if result.value.status != expected or result.value.sealed_at is None:
        raise RuntimeError(f"Run {run.id} sealed as {result.value.status}; expected {expected}")
    items = (await run.items.get()).value
    if items.run.id != run.id or not items.complete:
        raise RuntimeError("Run items readback is incomplete or belongs to another Run")
    return {
        "run_id": run.id,
        "status": str(result.value.status),
        "item_count": len(items.items),
        "position": items.position,
    }


async def _disconnect_acceptance(
    base_url: str, token: str, ca_bundle: str, workspace_id: str, agent: str
) -> dict[str, Any]:
    import ssl

    transport = DisconnectAfterEventTransport(
        httpx.AsyncHTTPTransport(verify=ssl.create_default_context(cafile=ca_bundle), trust_env=False)
    )
    async with Client(base_url, token, transport=transport, ca_bundle=ca_bundle, timeout=60.0) as client:
        submitted = await client.workspaces(workspace_id).start(
            "[slow] [long] Exercise Native Thread SSE cursor recovery.", agent_id=agent, idempotency_key=_key("stream")
        )
        cursors: list[str] = []
        frames: list[str] = []
        async with asyncio.timeout(120.0):
            async with submitted.thread.stream(max_reconnects=3) as stream:
                async for frame in stream:
                    frames.append(frame.event_type)
                    if frame.cursor is not None:
                        cursors.append(frame.cursor)
                    if len(transport.last_event_ids) >= 2 and len(cursors) >= 2:
                        break
        final = await _wait_run(_accepted_run(submitted), wire.RunStatus.COMPLETED)
    if transport.disconnects != 1 or len(transport.last_event_ids) < 2:
        raise RuntimeError("Isolated transport did not prove one disconnect and reconnect")
    if not cursors or transport.last_event_ids[1] != cursors[0]:
        raise RuntimeError("Reconnect did not send the first applied cursor as Last-Event-ID")
    if len(set(cursors)) != len(cursors):
        raise RuntimeError("Reconnect delivered a duplicate cursor")
    return {
        **_submission_evidence(submitted),
        **final,
        "frame_count": len(frames),
        "disconnects": transport.disconnects,
        "reconnect_last_event_id": transport.last_event_ids[1],
    }


async def _inbox_and_control(client: Client, workspace_id: str, agent: str) -> dict[str, Any]:
    workspace = client.workspaces(workspace_id)
    source = await workspace.start(
        "[interruptible] Hold the run long enough for an inbox message.",
        agent_id=agent,
        idempotency_key=_key("inbox-source"),
    )
    run = _accepted_run(source)
    queued = await source.thread.submit(
        "Follow-up Native inbox message.", agent_id=agent, idempotency_key=_key("inbox-next")
    )
    if queued.run is not None:
        raise RuntimeError("Submission to a running Thread did not remain queued")
    first = await _wait_run(run, wire.RunStatus.COMPLETED)
    settled = (await queued.entry.wait(timeout=120.0, poll_interval=0.1)).value
    if settled.status != wire.EntryStatus.CONSUMED or not settled.assigned_run_id:
        raise RuntimeError(f"Inbox entry ended as {settled.status}, without an assigned Run")
    second = await _wait_run(workspace.runs(settled.assigned_run_id), wire.RunStatus.COMPLETED)

    interrupt_source = await workspace.start(
        "[interruptible] Hold until an interrupt request.", agent_id=agent, idempotency_key=_key("interrupt-start")
    )
    interrupt_run = _accepted_run(interrupt_source)
    interrupted = await interrupt_run.interrupt()
    if interrupted.value.id != interrupt_run.id:
        raise RuntimeError("Interrupt receipt identifies a different Run")
    final = await _wait_run(interrupt_run, wire.RunStatus.CANCELLED)
    return {
        "source": {**_submission_evidence(source), **first},
        "queued": {**_submission_evidence(queued), "entry_status": str(settled.status), "successor": second},
        "interrupt": {**_submission_evidence(interrupt_source), **final},
    }


async def _resume_and_fork(client: Client, workspace_id: str, agent: str, client_tool_agent: str) -> dict[str, Any]:
    workspace = client.workspaces(workspace_id)
    completed = await workspace.start("Short Native response.", agent_id=agent, idempotency_key=_key("fork-source"))
    original = _accepted_run(completed)
    first = await _wait_run(original, wire.RunStatus.COMPLETED)
    forked = await original.fork(
        wire.Fork(
            agent_id=agent, payload=wire.MessagePayload(content=[wire.TextPart(type_="text", text="Forked response.")])
        ),
        idempotency_key=_key("fork"),
    )
    if forked.thread.id == completed.thread.id:
        raise RuntimeError("Fork did not create a distinct Thread")
    fork_final = await _wait_run(_accepted_run(forked), wire.RunStatus.COMPLETED)

    waiting = await workspace.start(
        "[client] Review a local SDK scenario.", agent_id=client_tool_agent, idempotency_key=_key("waiting")
    )
    waiting_run = _accepted_run(waiting)
    waiting_final = await _wait_run(waiting_run, wire.RunStatus.WAITING)
    pending = (await waiting_run.get()).value.pending
    if pending is None or len(pending.items) != 1:
        raise RuntimeError("Waiting Run did not expose exactly one pending action")
    resumed = await waiting_run.resume(
        wire.ResumeRequest(
            answers=[
                wire.Complete(
                    action="complete", tool_call_id=pending.items[0].tool_call_id, result={"decision": "approved"}
                )
            ]
        ),
        idempotency_key=_key("resume"),
    )
    if resumed.run.id == waiting_run.id:
        raise RuntimeError("Resume did not create a new Run")
    resumed_final = await _wait_run(resumed.run, wire.RunStatus.COMPLETED)
    return {
        "fork": {
            "source": {**_submission_evidence(completed), **first},
            "successor": {**_submission_evidence(forked), **fork_final},
        },
        "resume": {"source": {**_submission_evidence(waiting), **waiting_final}, "successor": resumed_final},
    }


async def main() -> None:
    base_url = _required("A13N_SERVICE_URL")
    token = _required("A13N_API_TOKEN")
    workspace_id = _required("A13N_WORKSPACE")
    agent = _required("A13N_AGENT")
    client_tool_agent = _required("A13N_CLIENT_TOOL_AGENT")
    ca_bundle = _required("A13N_CA_BUNDLE")
    disconnect = await _disconnect_acceptance(base_url, token, ca_bundle, workspace_id, agent)
    async with Client(base_url, token, ca_bundle=ca_bundle, timeout=60.0) as client:
        inbox_control = await _inbox_and_control(client, workspace_id, agent)
        successors = await _resume_and_fork(client, workspace_id, agent, client_tool_agent)
    print(
        json.dumps(
            {
                "evidence": "real-https-installed-sdk-native",
                "disconnect": disconnect,
                "inbox_control": inbox_control,
                "successors": successors,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    asyncio.run(main())
