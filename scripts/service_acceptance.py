"""Installed-SDK acceptance against an existing, disposable Native Service.

Requires A13N_SERVICE_URL, A13N_API_TOKEN, A13N_AGENT,
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

from a13n import Client, Interaction, Submitted, ThreadStream
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
        self.stream_queries: list[dict[str, str]] = []

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        response = await self._inner.handle_async_request(request)
        if request.url.path.endswith("/stream"):
            self.last_event_ids.append(request.headers.get("last-event-id"))
            self.stream_queries.append(dict(request.url.params))
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


def _submission_evidence(submitted: Submitted | Interaction) -> dict[str, str | None]:
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


def _accepted_run(submitted: Submitted | Interaction) -> Any:
    if submitted.run is None:
        raise RuntimeError("Idle Thread submission unexpectedly has no Run")
    return submitted.run


async def _wait_run(run: Any, expected: wire.RunStatus) -> dict[str, Any]:
    result = await run.wait(timeout=120.0, poll_interval=0.1)
    if result.status != expected or result.snapshot.value.sealed_at is None:
        raise RuntimeError(f"Run {run.id} sealed as {result.status}; expected {expected}")
    items = (await run.items.get()).value
    if items.run.id != run.id or not items.complete:
        raise RuntimeError("Run items readback is incomplete or belongs to another Run")
    return {
        "run_id": run.id,
        "status": str(result.status),
        "item_count": len(items.items),
        "position": items.position,
    }


async def _disconnect_acceptance(base_url: str, token: str, ca_bundle: str, agent: str) -> dict[str, Any]:
    import ssl

    transport = DisconnectAfterEventTransport(
        httpx.AsyncHTTPTransport(verify=ssl.create_default_context(cafile=ca_bundle), trust_env=False)
    )
    async with Client(base_url, token, transport=transport, ca_bundle=ca_bundle, timeout=60.0) as client:
        submitted = await client.agents(agent).start(
            "[slow] [long] Exercise Native Thread SSE cursor recovery.", idempotency_key=_key("stream")
        )
        cursors: list[str] = []
        frames: list[str] = []
        async with asyncio.timeout(120.0):
            async with ThreadStream(submitted.thread, max_reconnects=3) as stream:
                async for frame in stream:
                    frames.append(frame.event_type)
                    if frame.cursor is not None:
                        cursors.append(frame.cursor)
                    if len(transport.last_event_ids) >= 2 and len(cursors) >= 2:
                        break
        run = _accepted_run(submitted)
        final = await _wait_run(run, wire.RunStatus.COMPLETED)
        saved = (await run.items.get()).value
        if saved.run.id != run.id or saved.position is None:
            raise RuntimeError("Saved display did not expose exact Run coverage for reattachment")
        hint = saved.resume_after if isinstance(saved.resume_after, str) else None
        async with ThreadStream(
            submitted.thread, run=saved.run.id, position=saved.position, after=hint, reconnect=False
        ) as attached:
            if attached.response is None or attached.response.status_code != 200:
                raise RuntimeError("Covered display reattachment did not complete its SSE handshake")
        if transport.stream_queries[-1] != {"run": run.id, "position": saved.position}:
            raise RuntimeError("Covered reattachment did not send paired Run/position query")
        if transport.last_event_ids[-1] != hint:
            raise RuntimeError("Covered reattachment did not forward the saved resume hint")
        coverage = {"run_id": run.id, "position": saved.position, "resume_after": hint}
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
        "covered_reattach": coverage,
    }


def _configuration(label: str) -> wire.RunConfigurationInput:
    return wire.RunConfigurationInput(
        allowed_hosts=None,
        extensions=wire.RunConfigurationInputExtensions.from_dict(
            {
                "sdk.acceptance": {"label": label, "enabled": False, "zero": 0, "empty": [], "nested": {"null": None}},
            }
        ),
    )


def _assert_configuration(run: wire.RunView, expected: wire.RunConfigurationInput) -> None:
    actual = run.options.configuration
    if not isinstance(actual, wire.RunConfigurationOutput) or actual.to_dict() != expected.to_dict():
        raise RuntimeError("Accepted Run did not retain the complete native configuration snapshot")


async def _configuration_acceptance(client: Client, agent: str) -> dict[str, Any]:
    first_configuration = _configuration("start")
    initial = await client.agents(agent).start(
        "Short response with native configuration.",
        options=wire.RunOptionsInput(configuration=first_configuration),
        idempotency_key=_key("configuration-start"),
    )
    initial_outcome = await initial.result(timeout=120.0, poll_interval=0.1)
    _assert_configuration(initial_outcome.snapshot.value, first_configuration)
    next_configuration = _configuration("next_run")
    following = await client.agents(agent).send(
        initial.thread.id,
        "Short follow-up with a new configuration snapshot.",
        delivery=wire.Delivery.NEXT_RUN,
        options=wire.RunOptionsInput(configuration=next_configuration),
        idempotency_key=_key("configuration-next"),
    )
    following_outcome = await following.result(timeout=120.0, poll_interval=0.1)
    _assert_configuration(following_outcome.snapshot.value, next_configuration)
    _assert_configuration((await initial_outcome.run.get()).value, first_configuration)
    if initial_outcome.status != wire.RunStatus.COMPLETED or following_outcome.status != wire.RunStatus.COMPLETED:
        raise RuntimeError("Native configuration acceptance did not complete")
    if following_outcome.run.id == initial_outcome.run.id:
        raise RuntimeError("next_run did not select a distinct configuration snapshot")
    return {"start_run_id": initial_outcome.run.id, "next_run_id": following_outcome.run.id, "snapshot_readback": True}


async def _inbox_and_control(client: Client, agent: str) -> dict[str, Any]:
    source = await client.agents(agent).start(
        "[interruptible] Hold the run long enough for an inbox message.",
        idempotency_key=_key("inbox-source"),
    )
    run = _accepted_run(source)
    queued = await client.agents(agent).send(
        source.thread.id, "Follow-up Native inbox message.", idempotency_key=_key("inbox-next")
    )
    if queued.run is not None:
        raise RuntimeError("Submission to a running Thread did not remain queued")
    first = await _wait_run(run, wire.RunStatus.COMPLETED)
    incorporated = await queued.result(timeout=120.0, poll_interval=0.1)
    settled = (await queued.entry.get()).value
    if (
        settled.status != wire.EntryStatus.CONSUMED
        or settled.assigned_run_id != incorporated.run.id
        or incorporated.status != wire.RunStatus.COMPLETED
    ):
        raise RuntimeError("Queued Agent.send did not incorporate into its exact completed Run")
    second = await _wait_run(incorporated.run, wire.RunStatus.COMPLETED)

    interrupt_source = await client.agents(agent).start(
        "[interruptible] Hold until an interrupt request.", idempotency_key=_key("interrupt-start")
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


async def _import_history(client: Client, agent: str) -> dict[str, Any]:
    history = [
        {
            "kind": "request",
            "parts": [{"part_kind": "user-prompt", "content": "Earlier context"}],
            "metadata": {"source": "sdk-acceptance"},
        },
        {"kind": "response", "parts": [{"part_kind": "text", "content": "Earlier answer"}]},
    ]
    initial = await client.agents(agent).start(
        "Short Native response using imported context.", message_history=history, idempotency_key=_key("import")
    )
    first = await _wait_run(_accepted_run(initial), wire.RunStatus.COMPLETED)
    thread = (await initial.thread.get()).value
    if [message.to_dict() for message in thread.message_history] != history:
        raise RuntimeError("Imported model history readback lost submitted JSON or metadata")
    next_message = await client.agents(agent).send(
        initial.thread.id, "Short follow-up response.", idempotency_key=_key("import-followup")
    )
    subsequent = await next_message.result(timeout=120.0, poll_interval=0.1)
    if subsequent.status != wire.RunStatus.COMPLETED:
        raise RuntimeError("Follow-up on imported Thread did not complete")
    if [message.to_dict() for message in (await initial.thread.get()).value.message_history] != history:
        raise RuntimeError("Follow-up changed initial imported model history")
    return {
        "source": {**_submission_evidence(initial), **first},
        "followup_run_id": subsequent.run.id,
        "history_count": len(history),
    }


async def _resume_and_fork(client: Client, agent: str, client_tool_agent: str) -> dict[str, Any]:
    completed = await client.agents(agent).start("Short Native response.", idempotency_key=_key("fork-source"))
    original = _accepted_run(completed)
    first = await _wait_run(original, wire.RunStatus.COMPLETED)
    forked = await original.fork(
        body=wire.Fork(
            agent_id=agent, payload=wire.MessagePayload(content=[wire.TextPart(type_="text", text="Forked response.")])
        ),
        idempotency_key=_key("fork"),
    )
    if forked.thread.id == completed.thread.id:
        raise RuntimeError("Fork did not create a distinct Thread")
    fork_final = await _wait_run(_accepted_run(forked), wire.RunStatus.COMPLETED)

    inherited_configuration = _configuration("resume")
    waiting = await client.agents(client_tool_agent).start(
        "[client] Review a local SDK scenario.",
        idempotency_key=_key("waiting"),
        options=wire.RunOptionsInput(configuration=inherited_configuration),
    )
    waiting_outcome = await waiting.result(timeout=120.0, poll_interval=0.1)
    waiting_run = waiting_outcome.run
    _assert_configuration(waiting_outcome.snapshot.value, inherited_configuration)
    pending = waiting_outcome.pending
    if (
        waiting_outcome.status != wire.RunStatus.WAITING
        or pending is None
        or pending.approvals
        or len(pending.calls) != 1
    ):
        raise RuntimeError("Finite Interaction did not expose exactly one pending client call")
    waiting_items = (await waiting_run.items.get()).value
    if waiting_items.run.id != waiting_run.id or not waiting_items.complete:
        raise RuntimeError("Waiting Run items readback is incomplete or belongs to another Run")
    waiting_final = {
        "run_id": waiting_run.id,
        "status": str(waiting_outcome.status),
        "item_count": len(waiting_items.items),
        "position": waiting_items.position,
    }
    extra_input = "Additional context submitted atomically with the client tool result."
    resumed = await waiting_run.resume(
        approvals={},
        calls={pending.calls[0].tool_call_id: wire.Returned(status="returned", value={"decision": "approved"})},
        input=extra_input,
        idempotency_key=_key("resume"),
    )
    if resumed.run.id == waiting_run.id:
        raise RuntimeError("Resume did not create a new Run")
    _assert_configuration(resumed.receipt.value, inherited_configuration)
    resume = resumed.receipt.value.resume
    if resume is None or not isinstance(resume.input_, wire.MessagePayload):
        raise RuntimeError("Successor receipt did not retain atomic resume input")
    if resume.input_.to_dict() != {"content": [{"type": "text", "text": extra_input}]}:
        raise RuntimeError("Successor receipt changed atomic resume input")
    resumed_final = await _wait_run(resumed.run, wire.RunStatus.COMPLETED)
    _assert_configuration((await resumed.run.get()).value, inherited_configuration)
    resumed_final["configuration_inherited"] = True
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
    agent = _required("A13N_AGENT")
    client_tool_agent = _required("A13N_CLIENT_TOOL_AGENT")
    ca_bundle = _required("A13N_CA_BUNDLE")
    disconnect = await _disconnect_acceptance(base_url, token, ca_bundle, agent)
    async with Client(base_url, token, ca_bundle=ca_bundle, timeout=60.0) as client:
        configuration = await _configuration_acceptance(client, agent)
        inbox_control = await _inbox_and_control(client, agent)
        imported_history = await _import_history(client, agent)
        successors = await _resume_and_fork(client, agent, client_tool_agent)
    print(
        json.dumps(
            {
                "evidence": "real-https-installed-sdk-native",
                "disconnect": disconnect,
                "configuration": configuration,
                "inbox_control": inbox_control,
                "imported_history": imported_history,
                "successors": successors,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    asyncio.run(main())
