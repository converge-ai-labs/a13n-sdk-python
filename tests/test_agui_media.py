"""Service envelopes retain native AG-UI 1.0 media and inline-child attribution."""

import asyncio

import httpx2

from a13n import Client, ThreadStream
from tests.test_interaction import entry_view, run_view, submitted
from tests.test_streaming import sse

EVENTS = [
    {"type": "RUN_STARTED", "threadId": "harness-thread", "runId": "harness-root", "protocolVersion": "1.0"},
    {"type": "SUBAGENT_STARTED", "subagentRunId": "child", "name": "reviewer", "parentToolCallId": "call"},
    {"type": "TEXT_MESSAGE_CONTENT", "messageId": "same", "delta": "child", "subagentRunId": "child"},
    {"type": "TEXT_MESSAGE_CONTENT", "messageId": "same", "delta": "root"},
    {
        "type": "TOOL_CALL_RESULT",
        "messageId": "tool",
        "toolCallId": "call",
        "role": "tool",
        "subagentRunId": "child",
        "content": [
            {"type": "text", "text": "Result"},
            {
                "type": "image",
                "source": {"type": "url", "value": "https://media.example/image.png", "mimeType": "image/png"},
            },
            {
                "type": "video",
                "source": {"type": "url", "value": "https://media.example/video.mp4", "mimeType": "video/mp4"},
            },
            {"type": "audio", "source": {"type": "file", "value": "provider-file", "provider": "native"}},
            {
                "type": "image",
                "source": {"type": "url", "value": "https://media.example/image.png", "mimeType": "image/png"},
            },
        ],
    },
    {"type": "CUSTOM", "name": "example.future", "value": None, "subagentRunId": "child"},
    {
        "type": "CUSTOM",
        "name": "a13n.input.media",
        "metadata": {"display": False, "media": True},
        "value": {
            "run_id": "child",
            "event": {"content": {"kind": "video-url", "url": "https://media.example/video.mp4"}},
        },
        "subagentRunId": "child",
    },
    {"type": "SUBAGENT_FINISHED", "subagentRunId": "child", "outcome": {"type": "success"}},
]


def envelope(event: dict, sequence: int) -> bytes:
    return sse(
        "delta",
        {"run_id": "run_1", "attempt": 1, "sequence": sequence, "event": event, "item": None},
        f"100-{sequence}",
    )


def test_thread_stream_preserves_canonical_media_unknown_custom_and_child_identity() -> None:
    async def scenario() -> None:
        def handle(_request: httpx2.Request) -> httpx2.Response:
            return httpx2.Response(
                200,
                content=b"".join(envelope(event, index) for index, event in enumerate(EVENTS, 1)),
                headers={"Content-Type": "text/event-stream"},
            )

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            async with ThreadStream(client.threads("thr_1"), reconnect=False) as stream:
                frames = [frame async for frame in stream]
        assert [dict(frame.data["event"]) for frame in frames if frame.event_type == "delta"] == EVENTS

    asyncio.run(scenario())


def test_saved_items_preserve_structured_result_parts_and_child_attribution() -> None:
    async def scenario() -> None:
        parts = EVENTS[4]["content"]
        content = {"toolCallId": "call", "subagentRunId": "child", "result_parts": parts}
        item = {
            "id": "itm_child",
            "kind": "tool_call",
            "state": "completed",
            "content": content,
            "first_stream_id": "1-1",
            "last_stream_id": "1-2",
            "started_at": "2026-10-01T00:00:00Z",
        }

        def handle(request: httpx2.Request) -> httpx2.Response:
            assert request.url.path == "/api/v1/runs/run_1/items"
            return httpx2.Response(
                200,
                json={
                    "run": run_view(status="completed"),
                    "complete": True,
                    "dropped": 0,
                    "position": "1-2",
                    "resume_after": None,
                    "items": [item],
                },
            )

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            saved = await client.runs("run_1").items.get()
        assert saved.value.items[0].content.to_dict() == content
        assert saved.value.items[0].content.to_dict()["result_parts"] == parts

    asyncio.run(scenario())


def test_inline_child_terminal_never_seals_finite_root_interaction() -> None:
    async def scenario() -> None:
        release_root = asyncio.Event()
        seen: list[tuple[str, str]] = []
        child_terminal = {
            "type": "RUN_FINISHED",
            "runId": "child",
            "threadId": "harness-thread",
            "subagentRunId": "child",
            "outcome": {"type": "success"},
        }

        class Stream(httpx2.AsyncByteStream):
            async def __aiter__(self):
                # Foreign Service Run is filtered. Inline-child events belong to this Service Run.
                yield sse(
                    "delta",
                    {
                        "run_id": "run_other",
                        "attempt": 1,
                        "sequence": 1,
                        "event": {"type": "RUN_FINISHED"},
                        "item": None,
                    },
                    "99-0",
                )
                yield envelope(child_terminal, 1)
                yield envelope(EVENTS[4], 2)
                yield envelope(EVENTS[3], 3)
                await asyncio.Event().wait()

        stream = Stream()

        def handle(request: httpx2.Request) -> httpx2.Response:
            seen.append((request.method, request.url.path))
            if request.method == "POST":
                return httpx2.Response(201, json=submitted())
            if request.url.path.endswith("/inbox/ent_1"):
                entry = entry_view(status="consumed")
                entry["assigned_run_id"] = "run_1"
                return httpx2.Response(200, json=entry)
            if request.url.path.endswith("/stream"):
                return httpx2.Response(200, stream=stream, headers={"Content-Type": "text/event-stream"})
            return httpx2.Response(200, json=run_view(status="completed" if release_root.is_set() else "running"))

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            interaction = await client.agents("agt_1").start("x", idempotency_key="child")
            async with asyncio.timeout(3):
                async with interaction:
                    first = await anext(interaction)
                    assert first.event_type == "delta" and dict(first.data["event"]) == child_terminal
                    second = await anext(interaction)
                    assert second.event_type == "delta" and dict(second.data["event"]) == EVENTS[4]
                    third = await anext(interaction)
                    assert third.event_type == "delta" and third.data["event"]["delta"] == "root"
                    result = asyncio.create_task(interaction.result())
                    await asyncio.sleep(0)
                    assert not result.done()
                    release_root.set()
                    assert [frame async for frame in interaction] == []
                    assert (await result).status == "completed"
        assert all(method == "GET" for method, _ in seen[1:])
        assert sum(path.endswith("/stream") for _, path in seen) == 1

    asyncio.run(scenario())
