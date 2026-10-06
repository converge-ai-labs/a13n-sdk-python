"""Installed-SDK acceptance against an existing, disposable Native Service.

Requires A13N_SERVICE_URL, A13N_API_TOKEN, A13N_AGENT,
A13N_CLIENT_TOOL_AGENT, A13N_FAILURE_PROMPT and A13N_CA_BUNDLE.
A13N_FAILURE_PROMPT is a disposable fixture's latest-input-only failure trigger,
not a Service API capability. All HTTP requests use verified TLS;
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

from a13n import ApiError, Client, Interaction, Run, Submitted, ThreadStream
from a13n.generated import models as wire
from a13n.generated.types import UNSET


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
    if items.run.id != run.id or not items.complete or not items.baseline:
        raise RuntimeError("Default Run display is not a sealed baseline for the exact Run")
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
    continued = await _continue_sealed(client, agent, interrupt_source, interrupt_run)
    return {
        "source": {**_submission_evidence(source), **first},
        "queued": {**_submission_evidence(queued), "entry_status": str(settled.status), "successor": second},
        "interrupt": {**_submission_evidence(interrupt_source), **final, "normal_continuation": continued},
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
    if waiting_items.run.id != waiting_run.id or not waiting_items.complete or not waiting_items.baseline:
        raise RuntimeError("Waiting Run display is not a sealed baseline for the exact Run")
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


async def _continue_sealed(client: Client, agent: str, source: Interaction, run: Run) -> dict[str, Any]:
    thread = (await source.thread.get()).value
    if thread.last_run_id != run.id or thread.current_run_id is not None:
        raise RuntimeError("Idle Thread does not name its latest sealed failed/cancelled Run")
    following = await client.agents(agent).send(
        source.thread.id, "Normal follow-up after the sealed outcome.", idempotency_key=_key("sealed-followup")
    )
    successor = _accepted_run(following)
    accepted = following.receipt.value.run
    if accepted is None or accepted.id == run.id or accepted.parent_run_id != run.id:
        raise RuntimeError("Normal message did not continue the latest sealed Run's history")
    outcome = await following.result(timeout=120.0, poll_interval=0.1)
    if outcome.status != wire.RunStatus.COMPLETED or outcome.run.id != successor.id:
        raise RuntimeError("Normal explicit continuation did not complete its exact successor")
    if (await source.thread.get()).value.last_run_id != successor.id:
        raise RuntimeError("Completed successor did not become the Thread's latest sealed Run")
    return {"run_id": successor.id, "parent_run_id": accepted.parent_run_id, "status": str(outcome.status)}


async def _failed_continuation_acceptance(client: Client, agent: str, failure_prompt: str) -> dict[str, Any]:
    initial = await client.agents(agent).start("Establish continuation history.", idempotency_key=_key("failure-base"))
    original = await initial.result(timeout=120.0, poll_interval=0.1)
    if original.status != wire.RunStatus.COMPLETED:
        raise RuntimeError("Failure continuation scenario could not establish an earlier completed Run")
    failed = await client.agents(agent).send(initial.thread.id, failure_prompt, idempotency_key=_key("failure"))
    failed_run = _accepted_run(failed)
    sealed = await _wait_run(failed_run, wire.RunStatus.FAILED)
    if (await failed_run.get()).value.parent_run_id != original.run.id:
        raise RuntimeError("Failed Run did not retain its earlier continuation parent")
    following = await _continue_sealed(client, agent, failed, failed_run)
    return {"previous_run_id": original.run.id, "source": sealed, "normal_continuation": following}


def _historical_window(saved: wire.RunItems, run_id: str) -> None:
    if saved.run.id != run_id or saved.baseline or not saved.complete:
        raise RuntimeError("Historical display window has incorrect Run or baseline/seal metadata")
    if saved.continuation is not None or saved.position is not None or saved.resume_after is not None:
        raise RuntimeError("Historical ordinal window incorrectly advertises live coverage")
    ordinals = [item.ordinal for item in saved.items]
    if ordinals and ordinals != list(range(ordinals[0], ordinals[-1] + 1)):
        raise RuntimeError("Historical display ordinals are not dense and ordered")


async def _paged_display_acceptance(client: Client, agent: str) -> dict[str, Any]:
    initial = await client.agents(agent).start(
        "[slow] [long] Exercise native ordinal display windows.", idempotency_key=_key("paged-display")
    )
    outcome = await initial.result(timeout=120.0, poll_interval=0.1)
    if outcome.status != wire.RunStatus.COMPLETED:
        raise RuntimeError("Paged display scenario did not complete")
    run = outcome.run
    recent = (await run.items.get(limit=1)).value
    if recent.run.id != run.id or not recent.baseline or not recent.complete or not recent.items:
        raise RuntimeError("Default recent read did not return its exact sealed baseline")
    if recent.position is None or not isinstance(recent.continuation, wire.DisplayContinuation):
        raise RuntimeError("Completed default display did not expose shared normalization continuation")
    cut = recent.continuation.position
    if recent.position != f"{cut.attempt}-{cut.sequence}" or recent.continuation.run_id != run.id:
        raise RuntimeError("Default display continuation and coverage disagree")
    ordinals = [item.ordinal for item in recent.items]
    if ordinals != list(range(ordinals[0], ordinals[-1] + 1)):
        raise RuntimeError("Default display ordinals are not dense and ordered")
    before = (await run.items.get(before=ordinals[0], limit=1)).value
    forward = (await run.items.get(after=0, limit=1)).value
    _historical_window(before, run.id)
    _historical_window(forward, run.id)
    if any(item.ordinal >= ordinals[0] for item in before.items):
        raise RuntimeError("before ordinal bound is not exclusive")
    if len(forward.items) != 1 or forward.items[0].ordinal != 1:
        raise RuntimeError("after=0 did not return the first display Item")
    for query in ({"before": 0}, {"after": -1}, {"limit": 501}, {"before": 2, "after": 0}):
        try:
            await run.items.get(
                before=query.get("before", UNSET), after=query.get("after", UNSET), limit=query.get("limit", UNSET)
            )
        except ApiError as error:
            if error.status != 400 or error.code != "invalid_argument":
                raise
        else:
            raise RuntimeError("Service accepted an invalid ordinal window")
    return {
        "run_id": run.id,
        "recent_ordinals": ordinals,
        "baseline": recent.baseline,
        "complete": recent.complete,
        "position": recent.position,
        "next_ordinal": recent.continuation.next_ordinal,
        "earlier_ordinals": [item.ordinal for item in before.items],
        "first_ordinal": forward.items[0].ordinal,
        "invalid_windows_rejected": 4,
    }


async def main() -> None:
    base_url = _required("A13N_SERVICE_URL")
    token = _required("A13N_API_TOKEN")
    agent = _required("A13N_AGENT")
    client_tool_agent = _required("A13N_CLIENT_TOOL_AGENT")
    ca_bundle = _required("A13N_CA_BUNDLE")
    failure_prompt = _required("A13N_FAILURE_PROMPT")
    disconnect = await _disconnect_acceptance(base_url, token, ca_bundle, agent)
    async with Client(base_url, token, ca_bundle=ca_bundle, timeout=60.0) as client:
        configuration = await _configuration_acceptance(client, agent)
        inbox_control = await _inbox_and_control(client, agent)
        imported_history = await _import_history(client, agent)
        successors = await _resume_and_fork(client, agent, client_tool_agent)
        paged_display = await _paged_display_acceptance(client, agent)
        failed_continuation = await _failed_continuation_acceptance(client, agent, failure_prompt)
    print(
        json.dumps(
            {
                "evidence": "real-https-installed-sdk-native",
                "disconnect": disconnect,
                "configuration": configuration,
                "inbox_control": inbox_control,
                "imported_history": imported_history,
                "successors": successors,
                "paged_display": paged_display,
                "failed_continuation": failed_continuation,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    asyncio.run(main())
