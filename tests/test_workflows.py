"""Authored root-only workflows and finite observation regressions."""

import asyncio
import json
from dataclasses import fields

import httpx2
import pytest

from a13n import (
    UNSET,
    AgentOverride,
    ApiError,
    Approve,
    AssetPart,
    Client,
    Deny,
    Failed,
    JsonPart,
    MemoryMount,
    MountCreate,
    PreviewInterrupted,
    ProtocolError,
    Returned,
    RunConfiguration,
    RunOptions,
    SubmissionError,
    TextPart,
    UnknownOutcomeError,
    UrlPart,
    UsageLimit,
)
from tests.test_interaction import entry_view, run_view, submitted


def test_parts_and_all_options_cross_one_generated_transport() -> None:
    async def scenario() -> None:
        requests = []
        options = RunOptions(
            configuration=RunConfiguration(allowed_hosts=None, extensions={"example": [None, False, 0, "", [], {}]}),
            overrides=AgentOverride(**{field.name: None for field in fields(AgentOverride)}),
            max_usage=UsageLimit(2),
            labels={},
        )

        def handle(request):
            requests.append(request)
            return httpx2.Response(201, json=submitted())

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            interaction = await client.agents("agt_1").start(
                [
                    "plain",
                    TextPart("explicit"),
                    JsonPart(False),
                    JsonPart(None),
                    UrlPart("https://example.test"),
                    AssetPart("ast_1"),
                ],
                options=options,
                environments=[MountCreate("work", "env_1", None)],
                memories=[MemoryMount("notes", "mem_1", "write", False)],
                mcp_headers={},
            )
            assert interaction.run is None and interaction.provenance == "submitted"
            assert interaction.idempotency_key == requests[0].headers["idempotency-key"]
        body = json.loads(requests[0].content)
        assert body["options"] == options.to_dict()
        assert body["options"]["configuration"]["extensions"] == {"example": [None, False, 0, "", [], {}]}
        assert body["options"]["overrides"] == {field.name: None for field in fields(AgentOverride)}
        assert body["payload"]["content"] == [
            {"type": "text", "text": "plain"},
            {"type": "text", "text": "explicit"},
            {"type": "json", "value": False},
            {"type": "json", "value": None},
            {"type": "url", "url": "https://example.test"},
            {"type": "asset", "asset_id": "ast_1"},
        ]
        assert body["environments"][0]["working_directory"] is None
        assert body["memories"][0]["recall"] is False
        assert body["mcp_headers"] == {} and len(requests) == 1

    asyncio.run(scenario())


def test_all_non_null_override_fields_remain_selectable_without_wire_import() -> None:
    values = {
        "client_tools": [{"name": "lookup", "description": "find", "parameters_json_schema": {"type": "object"}}],
        "connection_tools": [],
        "instructions": "",
        "media_understanding": {},
        "model": "mdl_1",
        "model_characteristics": {},
        "model_settings": {"extra_body": {"false": False, "zero": 0, "null": None}},
        "output_spec": {"schema": {"type": "object"}},
        "plugins": [],
        "retries": {},
        "reviewer": {"model": "review-model"},
        "skills": [],
        "subagents": {},
        "toolsets": {},
    }
    options = RunOptions(overrides=AgentOverride(**values))
    # The generated adapter, not an alternate authored schema validator, owns serialization.
    assert options.into_wire().to_dict()["overrides"] == values


@pytest.mark.parametrize("output", ["", False, 0, None, [], {}, {"nested": [False, None, 0]}])
def test_exact_outcome_preserves_full_output_and_evidence(output) -> None:
    async def scenario() -> None:
        paths = []

        def handle(request):
            paths.append(request.url.path)
            value = run_view(status="completed")
            value["output"] = output
            return httpx2.Response(200, json=value, headers={"X-Request-ID": "req_1", "ETag": '"run:2"'})

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            selected = client.runs("run_1").observe(timeout=1, poll_interval=0.001)
            assert paths == [] and selected.thread is None and selected.entry is None and selected.receipt is None
            outcome = await selected.result()
            assert outcome.output == output and type(outcome.output) is type(output)
            assert outcome.text == (output if isinstance(output, str) else None)
            assert outcome.thread_id == "thr_1" and outcome.run_id == "run_1"
            assert outcome.evidence.request_id == "req_1" and outcome.evidence.etag == '"run:2"'
            assert await selected.result() is outcome
            await selected.aclose()
        assert paths == ["/api/v1/runs/run_1"]

    asyncio.run(scenario())


def test_pending_arguments_and_failure_are_public_native_values() -> None:
    async def scenario() -> None:
        def handle(request):
            value = run_view(status="waiting")
            value["pending"] = {
                "approvals": [{"tool_call_id": "ap_1", "tool_name": "approve", "arguments": {"x": False}}],
                "calls": [{"tool_call_id": "call_1", "tool_name": "lookup", "arguments": {}, "presentation": None}],
            }
            value["failure"] = {"code": "example", "message": "diagnostic"}
            return httpx2.Response(200, json=value)

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            result = await client.runs("run_1").result()
            assert result.pending.approvals[0].arguments == {"x": False}
            assert result.pending.approvals[0].presentation is UNSET
            assert result.pending.calls[0].presentation is None
            assert result.failure.code == "example"

    asyncio.run(scenario())


def test_identity_recovery_requires_consumed_not_provisional_assignment() -> None:
    async def scenario() -> None:
        paths = []
        reads = 0

        def handle(request):
            nonlocal reads
            paths.append(request.url.path)
            if "/inbox/" in request.url.path:
                reads += 1
                value = entry_view(status=["assigned", "pending", "consumed"][reads - 1])
                value["assigned_run_id"] = ["run_wrong", None, "run_1"][reads - 1]
            else:
                value = run_view(status="completed")
            return httpx2.Response(200, json=value)

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            recovered = client.threads("thr_1").interaction(
                "ent_1", idempotency_key="saved", timeout=1, poll_interval=0.001
            )
            assert recovered.receipt is None and recovered.provenance == "recovered_entry" and paths == []
            assert recovered.run is None
            result = await recovered.result()
            assert recovered.run is result.run and result.run_id == "run_1"
            await recovered.aclose()
        assert reads == 3 and paths[-1] == "/api/v1/runs/run_1"

    asyncio.run(scenario())


@pytest.mark.parametrize("status", ["failed", "withdrawn"])
def test_recovery_disposition_is_not_an_observed_run_failure(status) -> None:
    async def scenario() -> None:
        value = entry_view(status=status)
        value["assigned_run_id"] = "run_1"
        async with Client(
            "https://service.example", transport=httpx2.MockTransport(lambda _: httpx2.Response(200, json=value))
        ) as client:
            with pytest.raises(SubmissionError):
                await client.threads("thr_1").interaction("ent_1", timeout=1).result()

    asyncio.run(scenario())


@pytest.mark.parametrize("reason", [UNSET, None, ""])
def test_resume_one_batch_binds_exact_successor_and_observer(reason) -> None:
    async def scenario() -> None:
        requests = []

        def handle(request):
            requests.append(request)
            return httpx2.Response(201 if request.method == "POST" else 200, json=run_view("run_2", status="completed"))

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            successor = await client.runs("run_1").resume(
                {"ap": Approve(), "deny": Deny(reason), "call": Returned(None), "bad": Failed("Unavailable")},
                input=[JsonPart(0)],
            )
            assert successor.entry is None and successor.run.id == "run_2" and successor.provenance == "resumed"
            assert successor.idempotency_key == requests[0].headers["idempotency-key"]
            assert (await successor.result(timeout=1)).run_id == "run_2"
            await successor.aclose()
        body = json.loads(requests[0].content)
        assert body["approvals"]["ap"] == {"action": "approve"}
        assert body["approvals"]["deny"] == (
            {"action": "deny"} if reason is UNSET else {"action": "deny", "reason": reason}
        )
        assert body["calls"] == {
            "call": {"status": "returned", "value": None},
            "bad": {"status": "failed", "message": "Unavailable"},
        }
        assert len(requests) == 2 and requests[1].url.path == "/api/v1/runs/run_2"

    asyncio.run(scenario())


@pytest.mark.parametrize("kind", ["transport", "malformed", "identity"])
def test_unknown_dispatch_keeps_key_cause_and_safe_identities_without_retry(kind) -> None:
    async def scenario() -> None:
        requests = []

        def handle(request):
            requests.append(request)
            if kind == "transport":
                raise httpx2.ReadError("lost acknowledgement")
            if kind == "malformed":
                return httpx2.Response(201, json={})
            value = submitted()
            value["thread"]["id"] = "wrong"
            return httpx2.Response(201, json=value)

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            with pytest.raises(UnknownOutcomeError) as error:
                await client.agents("agt_1").send("thr_1", "x")
            assert error.value.idempotency_key == requests[0].headers["idempotency-key"]
            assert error.value.thread_id == "thr_1" and error.value.operation == "send"
            assert error.value.__cause__ is not None and len(requests) == 1
            if kind == "identity":
                assert isinstance(error.value.__cause__, ProtocolError) and error.value.evidence.status_code == 201

    asyncio.run(scenario())


def test_pre_dispatch_validation_closed_client_and_rejection_are_not_unknown() -> None:
    async def scenario() -> None:
        calls = []

        def handle(request):
            calls.append(request)
            return httpx2.Response(
                409, json={"error": {"code": "conflict", "message": "frozen", "details": {}, "request_id": None}}
            )

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            with pytest.raises(TypeError):
                await client.agents("agt_1").start([object()])
            with pytest.raises(ValueError):
                await client.agents("agt_1").start("x", idempotency_key="")
            with pytest.raises(ApiError):
                await client.agents("agt_1").start("x")
            assert len(calls) == 1
        from a13n import TransportError

        with pytest.raises(TransportError) as error:
            await client.agents("agt_1").start("x")
        assert not isinstance(error.value, UnknownOutcomeError) and len(calls) == 1

    asyncio.run(scenario())


def delta(event, sequence=None, run_id="run_1", attempt=1):
    return {"run_id": run_id, "attempt": attempt, "sequence": sequence, "item": None, "event": event}


def sse(event_type, data, cursor=None):
    prefix = f"id: {cursor}\n" if cursor else ""
    return f"{prefix}event: {event_type}\ndata: {json.dumps(data)}\n\n".encode()


async def preview_scenario(events, callback):
    finished = False
    closed = asyncio.Event()

    class Stream(httpx2.AsyncByteStream):
        async def __aiter__(self):
            sequences = {}
            for index, (event_type, data) in enumerate(events):
                if event_type == "delta":
                    key = (data["run_id"], data["attempt"])
                    if data["sequence"] is None:
                        data = {**data, "sequence": sequences.get(key, 0) + 1}
                    sequences[key] = data["sequence"]
                yield sse(event_type, data, f"1700000000000-{index}" if event_type in {"delta", "boundary"} else None)
            await asyncio.Event().wait()

        async def aclose(self):
            closed.set()

    def handle(request):
        if request.url.path.endswith("/stream"):
            return httpx2.Response(200, stream=Stream(), headers={"content-type": "text/event-stream"})
        value = run_view(status="completed" if finished else "running")
        value["output"] = {"final": False}
        return httpx2.Response(200, json=value)

    def finish():
        nonlocal finished
        finished = True

    async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
        observation = client.runs("run_1").observe(timeout=1, poll_interval=0.001)
        async with observation:
            await callback(observation, finish)
    assert closed.is_set()


def test_preview_root_filtering_interleaving_and_raw_exclusivity() -> None:
    events = [
        (
            "delta",
            delta({"type": "TEXT_MESSAGE_START", "messageId": "child", "role": "assistant", "subagentRunId": "child"}),
        ),
        (
            "delta",
            delta(
                {"type": "TEXT_MESSAGE_CONTENT", "messageId": "child", "delta": "not root", "subagentRunId": "child"}
            ),
        ),
        (
            "delta",
            delta(
                {
                    "type": "TEXT_MESSAGE_START",
                    "messageId": "hidden",
                    "role": "assistant",
                    "metadata": {"display": False},
                }
            ),
        ),
        ("delta", delta({"type": "TEXT_MESSAGE_CONTENT", "messageId": "hidden", "delta": "hidden"})),
        ("delta", delta({"type": "TEXT_MESSAGE_START", "messageId": "one", "role": "assistant"})),
        ("delta", delta({"type": "TEXT_MESSAGE_START", "messageId": "two", "role": "assistant"})),
        ("delta", delta({"type": "CUSTOM", "name": "future", "value": None})),
        ("delta", delta({"type": "TEXT_MESSAGE_CONTENT", "messageId": "one", "delta": "Hello "})),
        ("delta", delta({"type": "TEXT_MESSAGE_END", "messageId": "one"})),
        ("delta", delta({"type": "TEXT_MESSAGE_CONTENT", "messageId": "two", "delta": "world"})),
    ]

    async def callback(observation, finish):
        preview = observation.text_stream()
        assert await anext(preview) == "Hello "
        with pytest.raises(RuntimeError, match="active"):
            await anext(observation)
        with pytest.raises(RuntimeError, match="one preview"):
            await anext(observation.text_stream())
        assert await anext(preview) == "world"
        finish()
        assert [chunk async for chunk in preview] == []
        assert (await observation.result()).output == {"final": False}

    asyncio.run(preview_scenario(events, callback))


@pytest.mark.parametrize(
    "notice,reason",
    [
        (("gap", {"run_id": "run_1"}), "gap"),
        (("reset", {"run_id": "run_1"}), "reset"),
        (
            (
                "delta",
                delta(
                    {
                        "type": "CUSTOM",
                        "name": "a13n.stream.fragment",
                        "value": {"id": "opaque", "index": 0, "count": 2, "data": '{"type":"CUSTOM"'},
                    }
                ),
            ),
            "fragment",
        ),
        (("delta", delta({"type": "TEXT_MESSAGE_CONTENT", "messageId": "missing", "delta": "x"})), "missing_start"),
        (("delta", delta({"type": "TEXT_MESSAGE_START", "messageId": "bad"})), "ambiguous_role"),
        (
            ("delta", delta({"type": "TEXT_MESSAGE_CONTENT", "messageId": "one", "delta": "x"}, attempt=2)),
            "attempt_changed",
        ),
    ],
)
def test_preview_interruption_is_sticky_but_raw_and_result_remain_usable(notice, reason) -> None:
    events = [
        ("delta", delta({"type": "TEXT_MESSAGE_START", "messageId": "one", "role": "assistant"})),
        notice,
        ("delta", delta({"type": "CUSTOM", "name": "future.raw", "value": None})),
    ]

    async def callback(observation, finish):
        with pytest.raises(PreviewInterrupted) as error:
            await anext(observation.text_stream())
        assert error.value.reason == reason and error.value.run_id == "run_1"
        with pytest.raises(PreviewInterrupted) as again:
            await anext(observation.text_stream())
        assert again.value is error.value
        frame = await anext(observation)
        assert frame.data["event"]["name"] == "future.raw"
        finish()
        assert (await observation.result()).output == {"final": False}

    asyncio.run(preview_scenario(events, callback))


def test_preview_bounded_active_state_interrupts_instead_of_eviction() -> None:
    events = [
        ("delta", delta({"type": "TEXT_MESSAGE_START", "messageId": str(index), "role": "assistant"}))
        for index in range(129)
    ]

    async def callback(observation, finish):
        with pytest.raises(PreviewInterrupted, match="active_message_limit"):
            await anext(observation.text_stream())
        finish()
        assert (await observation.result()).status == "completed"

    asyncio.run(preview_scenario(events, callback))


def test_foreign_gap_and_child_fragments_do_not_interrupt_root_preview() -> None:
    events = [
        ("gap", {"run_id": "foreign"}),
        (
            "delta",
            delta(
                {
                    "type": "CUSTOM",
                    "name": "a13n.stream.fragment",
                    "subagentRunId": "child",
                    "value": {"id": "opaque", "index": 0, "count": 2, "data": '{"type":"CUSTOM"'},
                }
            ),
        ),
        ("delta", delta({"type": "TEXT_MESSAGE_START", "messageId": "one", "role": "assistant", "sequence": 100})),
        ("delta", delta({"type": "CUSTOM", "name": "source.coordinates", "value": {"sequence": 500}})),
        ("delta", delta({"type": "TEXT_MESSAGE_CONTENT", "messageId": "one", "delta": "safe", "sequence": 200})),
    ]

    async def callback(observation, finish):
        preview = observation.text_stream()
        assert await anext(preview) == "safe"
        finish()
        assert [chunk async for chunk in preview] == []

    asyncio.run(preview_scenario(events, callback))


@pytest.mark.parametrize("input", [UNSET, None, ["context", JsonPart(None)]])
def test_resume_input_preserves_omission_null_and_public_parts(input) -> None:
    async def scenario() -> None:
        requests = []

        def handle(request):
            requests.append(request)
            return httpx2.Response(201, json=run_view("run_2", status="completed"))

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            resumed = await client.runs("run_1").resume({}, input=input)
            assert resumed.entry is None and resumed.run.id == "run_2"
        body = json.loads(requests[0].content)
        expected = {"approvals": {}, "calls": {}}
        if input is None:
            expected["input"] = None
        elif input is not UNSET:
            expected["input"] = {"content": [{"type": "text", "text": "context"}, {"type": "json", "value": None}]}
        assert body == expected and len(requests) == 1

    asyncio.run(scenario())


def test_unseen_hidden_content_and_end_do_not_interrupt_visible_preview() -> None:
    events = [
        (
            "delta",
            delta(
                {"type": "TEXT_MESSAGE_CONTENT", "messageId": "hidden", "delta": None, "metadata": {"display": False}}
            ),
        ),
        ("delta", delta({"type": "TEXT_MESSAGE_END", "messageId": "hidden", "metadata": {"display": False}})),
        ("delta", delta({"type": "TEXT_MESSAGE_START", "messageId": "one", "role": "assistant"})),
        ("delta", delta({"type": "TEXT_MESSAGE_CONTENT", "messageId": "one", "delta": "safe visible reply"})),
    ]

    async def callback(observation, finish):
        preview = observation.text_stream()
        assert await anext(preview) == "safe visible reply"
        finish()
        assert [chunk async for chunk in preview] == []
        assert (await observation.result()).output == {"final": False}

    asyncio.run(preview_scenario(events, callback))


@pytest.mark.parametrize("kind", ["root", "child", "hidden", "boundary", "repeated"])
def test_preview_service_sequence_discontinuity_is_sticky_before_semantic_filtering(kind) -> None:
    event = {"type": "TEXT_MESSAGE_CONTENT", "messageId": "one", "delta": "unsafe"}
    if kind == "child":
        event["subagentRunId"] = "child"
    elif kind == "hidden":
        event["metadata"] = {"display": False}
    notice = (
        ("boundary", {"run_id": "run_1", "attempt": 1, "sequence": 12})
        if kind == "boundary"
        else ("delta", delta(event, sequence=10 if kind == "repeated" else 12))
    )
    events = [
        ("delta", delta({"type": "TEXT_MESSAGE_START", "messageId": "one", "role": "assistant"}, sequence=10)),
        notice,
        ("delta", delta({"type": "CUSTOM", "name": "future.raw", "value": None})),
    ]

    async def callback(observation, finish):
        with pytest.raises(PreviewInterrupted) as error:
            await anext(observation.text_stream())
        assert error.value.reason == "sequence_gap"
        with pytest.raises(PreviewInterrupted) as again:
            await anext(observation.text_stream())
        assert again.value is error.value
        assert (await anext(observation)).data["event"]["name"] == "future.raw"
        finish()
        assert (await observation.result()).output == {"final": False}

    asyncio.run(preview_scenario(events, callback))


def test_preview_late_boundaries_and_nested_source_coordinates_do_not_regress_outer_progress() -> None:
    events = [
        ("delta", delta({"type": "TEXT_MESSAGE_START", "messageId": "one", "role": "assistant"}, sequence=10)),
        (
            "delta",
            delta(
                {
                    "type": "TEXT_MESSAGE_CONTENT",
                    "messageId": "child",
                    "delta": "hidden child",
                    "subagentRunId": "child",
                },
                sequence=11,
            ),
        ),
        (
            "delta",
            delta(
                {
                    "type": "TEXT_MESSAGE_CONTENT",
                    "messageId": "hidden",
                    "delta": "hidden",
                    "metadata": {"display": False},
                },
                sequence=12,
            ),
        ),
        (
            "delta",
            delta(
                {"type": "CUSTOM", "name": "source.coordinates", "sequence": 500, "value": {"sequence": 900}},
                sequence=13,
            ),
        ),
        ("delta", delta({"type": "TEXT_MESSAGE_CONTENT", "messageId": "one", "delta": "A"}, sequence=14)),
        ("boundary", {"run_id": "run_1", "attempt": 1, "sequence": 11}),
        ("delta", delta({"type": "TEXT_MESSAGE_CONTENT", "messageId": "one", "delta": "B"}, sequence=15)),
        ("boundary", {"run_id": "run_1", "attempt": 1, "sequence": 15}),
        (
            "delta",
            delta(
                {"type": "TEXT_MESSAGE_CONTENT", "messageId": "foreign", "delta": "foreign"},
                sequence=100,
                run_id="foreign",
            ),
        ),
        ("delta", delta({"type": "TEXT_MESSAGE_CONTENT", "messageId": "one", "delta": "C"}, sequence=16)),
    ]

    async def callback(observation, finish):
        preview = observation.text_stream()
        assert [await anext(preview) for _ in range(3)] == ["A", "B", "C"]
        finish()
        assert [chunk async for chunk in preview] == []
        assert (await observation.result()).output == {"final": False}

    asyncio.run(preview_scenario(events, callback))
