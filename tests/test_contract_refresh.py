"""Contract refresh regressions for request context and catalog/navigation APIs."""

import asyncio
import json

import httpx2
import pytest

from a13n import UNSET, Client, RunOptions
from a13n.generated import models as wire
from tests.test_interaction import submitted


@pytest.mark.parametrize("context", [UNSET, None, {}, {"headers": {}}, {"headers": {"X-Tenant": "demo"}}])
def test_request_context_is_explicit_body_data(context):
    expected = {} if context is UNSET else {"context": context}
    assert RunOptions(context=context).into_wire().to_dict() == expected

    async def scenario():
        def respond(request):
            assert request.headers["authorization"] == "Bearer transport-only"
            assert json.loads(request.content)["options"] == expected
            return httpx2.Response(201, json=submitted())

        async with Client("https://service.test", "transport-only", transport=httpx2.MockTransport(respond)) as client:
            await client.agents("agt_1").start("hello", options=RunOptions(context=context))
            await client.agents("agt_1").send("thr_1", "hello", options=RunOptions(context=context))

    asyncio.run(scenario())


def test_new_models_preserve_required_nullable_and_arbitrary_json():
    assert wire.UsageSummary.from_dict({"models": []}).to_dict() == {"models": []}
    for model in (wire.RunUsagePage, wire.MemberUsagePage, wire.ThreadNavigationPage):
        assert model.from_dict({"items": [], "next_cursor": None}).to_dict() == {"items": [], "next_cursor": None}
        with pytest.raises(KeyError):
            model.from_dict({"items": []})
    plugin = {
        "plugin_key": "example",
        "display_name": "Example",
        "description": "Example plugin",
        "config_schema": None,
        "distribution_name": None,
        "distribution_version": None,
    }
    assert wire.PluginType.from_dict(plugin).to_dict() == plugin
    for key in ("config_schema", "distribution_name", "distribution_version"):
        with pytest.raises(KeyError):
            wire.PluginType.from_dict({k: v for k, v in plugin.items() if k != key})
    result = {"result": {"nested": [None, False, 0, "é", {"large": 9007199254740993}]}}
    assert wire.AppToolResult.from_dict(result).to_dict() == result
    assert wire.RequestContext.from_dict({}).to_dict() == {}
    assert wire.BackgroundCompactionPolicy.from_dict({"enabled": False, "blocking_threshold": 0.95}).to_dict() == {
        "enabled": False,
        "blocking_threshold": 0.95,
    }


def test_refreshed_resources_preserve_wire_requests_and_paging():
    async def scenario():
        seen = []
        page_calls = 0
        app_reference = dict(
            app_id="app",
            connection_id="con",
            agent_revision_id="rev",
            source_run_id="run",
            tool_call_id="call",
            tool_name="chart",
            resource_uri="ui://chart",
        )
        resource = dict(
            uri="ui://chart", mime_type="text/html", html="<p>Chart</p>", metadata={"nested": [None, False]}
        )

        def respond(request):
            nonlocal page_calls
            path = request.url.path
            seen.append(path)
            if request.method == "DELETE":
                assert request.headers["if-match"] == '"version"'
                assert not request.content
                return httpx2.Response(204)
            if path.endswith("/builtin-skills/platform-operations/content"):
                assert request.url.params["package_digest"] == "a" * 64
                return httpx2.Response(200, content=b"PK\x03\x04archive", headers={"Content-Type": "application/zip"})
            if path.endswith("/builtin-skills") or path.endswith("/plugins"):
                return httpx2.Response(200, json={"items": []})
            if path.endswith("/builtin-skills/platform-operations"):
                return httpx2.Response(
                    200,
                    json=dict(
                        name="platform-operations",
                        description="Platform",
                        root="root",
                        files=[],
                        package_digest="a" * 64,
                        package_size=11,
                    ),
                )
            if path.endswith("/usage/runs"):
                assert request.url.params["thread_id"] == "thr"
                assert request.url.params["limit"] == "2"
                assert request.url.params.get("cursor") == (None if page_calls == 0 else "next")
                page_calls += 1
                return httpx2.Response(200, json={"items": [], "next_cursor": "next" if page_calls == 1 else None})
            if path.endswith("/sessions/ses/threads"):
                assert request.url.params.get_list("origin") == ["new", "child"]
                assert request.url.params.get_list("thread_id") == ["thr_1", "thr_2"]
                return httpx2.Response(200, json={"items": [], "next_cursor": None})
            if path.endswith("/usage/members"):
                assert request.url.params["principal_id"] == "principal"
                return httpx2.Response(200, json={"items": [], "next_cursor": None})
            if path.endswith("/open"):
                assert request.method == "POST" and not request.content
                return httpx2.Response(
                    200, json=dict(reference=app_reference, tool={}, arguments={}, result={}, resource=resource)
                )
            if path.endswith("/resources/read"):
                assert json.loads(request.content) == {"uri": "ui://chart"}
                return httpx2.Response(200, json=resource)
            assert path.endswith("/tools/call")
            assert json.loads(request.content) == {"name": "chart", "arguments": {"n": 0}}
            return httpx2.Response(200, json={"result": {"ok": True}})

        async with Client("https://service.test", "key", transport=httpx2.MockTransport(respond)) as client:
            assert not (await client.api.builtin_skills.get()).value.items
            detail = (await client.api.builtin_skills("platform-operations").get()).value
            assert detail.package_digest == "a" * 64
            async with client.api.builtin_skills("platform-operations").content.get_stream(
                package_digest=detail.package_digest
            ) as response:
                assert await response.aread() == b"PK\x03\x04archive"
            assert not (await client.api.plugins.get()).value.items
            for providers in (
                client.api.connector_providers,
                client.api.memory_providers,
                client.api.model_providers,
                client.api.web_providers,
            ):
                result = await providers("provider").delete(if_match='"version"')
                assert result.value is None and result.status_code == 204
            pages = [page async for page in client.api.usage.runs.pages(thread_id="thr", limit=2)]
            assert len(pages) == 2
            await client.api.sessions("ses").threads.list(
                origin=[wire.ListSessionThreadsOriginType0Item.NEW, wire.ListSessionThreadsOriginType0Item.CHILD],
                thread_id=["thr_1", "thr_2"],
            )
            import datetime

            await client.api.usage.members.list(
                start=datetime.datetime(2026, 10, 1, tzinfo=datetime.UTC),
                end=datetime.datetime(2026, 11, 1, tzinfo=datetime.UTC),
                principal_id="principal",
            )
            app = client.api.runs("run").apps("app")
            assert (await app.open()).value.reference.app_id == "app"
            assert (await app.resources.read(body=wire.AppResourceRead(uri="ui://chart"))).value.html == "<p>Chart</p>"
            assert (
                await app.tools.call(body=wire.AppToolCall.from_dict({"name": "chart", "arguments": {"n": 0}}))
            ).value.result.to_dict() == {"ok": True}
        assert len(seen) == 15

    asyncio.run(scenario())
