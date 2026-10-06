import asyncio

import httpx2
import pytest

from a13n import ApiError, Client
from a13n.generated import models as wire
from a13n.generated.types import UNSET
from tests.test_interaction import NOW, run_view


def display_item(ordinal: int, state: str = "completed") -> dict:
    return {
        "id": f"itm_{ordinal}",
        "ordinal": ordinal,
        "kind": "text_message",
        "state": state,
        "content": {"text": "Saved", "subagentRunId": "child"},
        "started_at": NOW.replace("Z", "+00:00"),
        "first_stream_id": "1-1",
        "last_stream_id": "1-5",
    }


def continuation() -> dict:
    part = {"kind": "tool_call", "part_id": "call_1", "tool_name": None, "emitted_content": False}
    return {
        "run_id": "run_1",
        "position": {"attempt": 1, "sequence": 5},
        "next_ordinal": 8,
        "full_content": False,
        "arguments": {
            "stream": {"partial": [None, False, 0]},
            "key": "call_1",
            "at": NOW.replace("Z", "+00:00"),
            "sequence": 5,
            "event": {"type": "CUSTOM", "value": {"unknown": None}},
            "size": 12,
        },
        "fragments": {
            "gap": False,
            "max_bytes": 8192,
            "max_pending": 2,
            "pending": {"custom_1": {"count": 2, "parts": ['{"partial":', "false"], "size": 17}},
        },
        "observer": {
            "run_id": "harness_1",
            "thread_id": None,
            "state": {
                "request_index": 2,
                "parts": {"call_1": part},
                "threads": {"child": "harness_thread"},
                "children": {"child": {"children": {"grandchild": {"parts": {"call_2": part}}}}},
            },
        },
        "response_groups": {"child": "response_1"},
    }


def test_recursive_display_continuation_round_trip_and_nullable_coverage() -> None:
    value = continuation()
    parsed = wire.DisplayContinuation.from_dict(value)
    assert parsed.to_dict() == value
    assert isinstance(parsed.fragments, wire.FragmentState)
    assert isinstance(parsed.observer, wire.ObserverContinuation)
    assert parsed.position.sequence == 5
    snapshot = {
        "run": wire.RunView.from_dict(run_view()).to_dict(),
        "items": [display_item(7)],
        "baseline": True,
        "complete": False,
        "position": "1-5",
        "continuation": value,
        "resume_after": None,
    }
    assert wire.RunItems.from_dict(snapshot).to_dict() == snapshot
    snapshot.update(position=None, continuation=None)
    assert wire.RunItems.from_dict(snapshot).to_dict() == snapshot
    del snapshot["continuation"]
    del snapshot["resume_after"]
    assert wire.RunItems.from_dict(snapshot).continuation is UNSET
    assert wire.RunItems.from_dict(snapshot).to_dict() == snapshot


def test_item_requires_ordinal() -> None:
    value = display_item(1)
    del value["ordinal"]
    with pytest.raises(KeyError):
        wire.Item.from_dict(value)


@pytest.mark.parametrize("status", ["running", "completed"])
def test_baseline_tail_above_limit_and_historical_windows_are_native_single_requests(status: str) -> None:
    async def scenario() -> None:
        queries: list[dict[str, str]] = []

        def handle(request: httpx2.Request) -> httpx2.Response:
            assert request.method == "GET" and request.url.path == "/api/v1/runs/run_1/items"
            query = dict(request.url.params)
            queries.append(query)
            historical = "before" in query or "after" in query
            if "before" in query:
                ordinals = [3, 4]
            elif "after" in query:
                ordinals = [1, 2]
            else:
                ordinals = [5, 6, 7]  # All mutable tail retained despite limit=1.
            return httpx2.Response(
                200,
                json={
                    "run": run_view(status=status),
                    "items": [
                        display_item(i, state="in_progress" if status == "running" else "completed") for i in ordinals
                    ],
                    "baseline": not historical,
                    "complete": status == "completed",
                    "position": None if historical else "1-5",
                    "continuation": None if historical else continuation(),
                    "resume_after": None if historical else "500-0",
                },
            )

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            items = client.runs("run_1").items
            baseline = (await items.get(limit=1)).value
            assert baseline.baseline and baseline.complete == (status == "completed") and len(baseline.items) == 3
            assert baseline.items[0].ordinal == 5  # Even sealed does not mean all history loaded.
            assert baseline.items[0].state == ("in_progress" if status == "running" else "completed")
            assert baseline.items[0].content.to_dict()["subagentRunId"] == "child"
            for page in [(await items.get(before=5, limit=2)).value, (await items.get(after=0, limit=2)).value]:
                assert not page.baseline and page.complete == (status == "completed")
                assert page.position is page.continuation is page.resume_after is None
            await items.get()
            await items.get(before=None, after=None)
        assert queries == [{"limit": "1"}, {"before": "5", "limit": "2"}, {"after": "0", "limit": "2"}, {}, {}]

    asyncio.run(scenario())


@pytest.mark.parametrize("query", [{"before": 0}, {"after": -1}, {"limit": 501}, {"before": 2, "after": 0}])
def test_invalid_ordinal_queries_propagate_service_errors_without_replay(query: dict[str, int]) -> None:
    async def scenario() -> None:
        calls = 0

        def handle(request: httpx2.Request) -> httpx2.Response:
            nonlocal calls
            calls += 1
            assert dict(request.url.params) == {key: str(value) for key, value in query.items()}
            return httpx2.Response(
                400,
                json={
                    "error": {
                        "code": "invalid_argument",
                        "message": "Invalid ordinal window",
                        "details": {"field": next(iter(query))},
                        "request_id": None,
                    }
                },
            )

        async with Client("https://service.example", transport=httpx2.MockTransport(handle)) as client:
            with pytest.raises(ApiError) as error:
                await client.runs("run_1").items.get(**query)
            assert error.value.status == 400 and error.value.code == "invalid_argument"
        assert calls == 1

    asyncio.run(scenario())


@pytest.mark.parametrize("position", [None, "1-5"])
def test_run_display_position_nullable_and_run_items_baseline_required(position: str | None) -> None:
    view = run_view()
    view["display_position"] = position
    parsed = wire.RunView.from_dict(view)
    assert parsed.display_position == position and parsed.to_dict()["display_position"] == position
    with pytest.raises(KeyError):
        wire.RunItems.from_dict({"run": view, "items": [], "complete": False, "position": None})


def test_continuation_arguments_explicit_null_and_omission_are_distinct() -> None:
    value = continuation()
    value["arguments"] = None
    assert wire.DisplayContinuation.from_dict(value).to_dict()["arguments"] is None
    del value["arguments"]
    assert wire.DisplayContinuation.from_dict(value).arguments is UNSET
    assert wire.DisplayContinuation.from_dict(value).to_dict() == value
