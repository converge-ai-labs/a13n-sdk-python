"""Memory wire/resource regressions: path binding, CAS, mounts and record uncertainty."""

import ast
import asyncio
import json
from pathlib import Path

import httpx2
import pytest

from a13n import ApiError, Client
from a13n.generated import models as wire

ROOT = Path(__file__).resolve().parents[1]
FILE_PATH = "projects/计划 #1%.md"
FILE = {
    "id": "mfile_one",
    "path": FILE_PATH,
    "version": 2,
    "size": 4,
    "content": "text",
    "description": None,
    "updated_by_run_id": None,
    "updated_by_principal_id": "usr_one",
    "created_at": "2026-09-25T00:00:00Z",
    "updated_at": "2026-09-25T00:00:00Z",
}
REVISION = {
    "seq": 5,
    "path": FILE_PATH,
    "op": "update",
    "moved_path": None,
    "run_id": None,
    "tool_call_id": None,
    "principal_id": "usr_one",
    "created_at": "2026-09-25T00:00:00Z",
    "previous_content": "old",
    "content": "text",
    "hunks": ["diff"],
}


def test_every_pinned_operation_has_a_generated_resource_method() -> None:
    document = json.loads((ROOT / "contract/openapi.json").read_text())
    methods = {"get", "post", "put", "patch", "delete", "head", "options", "trace"}
    expected = {
        operation["operationId"].replace("__", "_")
        for path in document["paths"].values()
        for verb, operation in path.items()
        if verb in methods
    }
    tree = ast.parse((ROOT / "a13n/generated/resources.py").read_text())
    called = {
        node.func.value.id
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "asyncio_detailed"
        and isinstance(node.func.value, ast.Name)
    }
    assert called == expected
    assert len(expected) == 233


def test_memory_files_revisions_and_mounts_preserve_paths_and_etags() -> None:
    async def scenario() -> None:
        seen: list[httpx2.Request] = []

        def respond(request: httpx2.Request) -> httpx2.Response:
            seen.append(request)
            if request.method == "DELETE":
                return httpx2.Response(204, headers={"ETag": '"thr:4"'})
            if request.url.path.endswith("/restore"):
                return httpx2.Response(200, json={"path": FILE_PATH, "file": None})
            if request.url.path.endswith("/revisions/5"):
                return httpx2.Response(200, json=REVISION)
            if "/threads/" in request.url.path:
                return httpx2.Response(
                    201 if request.method == "POST" else 200,
                    json={"name": "notes", "memory_id": "mem_one", "access": "read", "recall": False},
                    headers={"ETag": '"thr:3"'},
                )
            return httpx2.Response(200, json=FILE, headers={"ETag": '"file:2"'})

        async with Client("https://service.example", "test", transport=httpx2.MockTransport(respond)) as client:
            memory = client.resources.memories("mem_one")
            file = memory.files(FILE_PATH)
            result = await file.get()
            assert result.value.content == "text" and result.etag == '"file:2"'
            await file.replace(body=wire.MemoryFileReplace(content="new"), if_match=result.etag)
            await memory.files.move(
                body=wire.MemoryFileMove(source=FILE_PATH, destination="new/file.md"), if_match=result.etag
            )
            await file.delete(if_match=result.etag)
            revision = memory.revisions(5)
            assert revision.selectors["seq"] == "5"
            assert (await revision.get()).value.previous_content == "old"
            assert (await revision.restore(if_match='"file:3"')).value.file is None
            await memory.revisions(6).restore()
            mounts = client.resources.threads("thr_one").memories
            mounted = await mounts.create(
                body=wire.MemoryMount(name="notes", memory_id="mem_one", access=wire.MemoryAccess.READ),
                if_match='"thr:2"',
            )
            assert mounted.etag == '"thr:3"'
            await mounts("notes").update(body=wire.MemoryMountUpdate(recall=False), if_match=mounted.etag)
            assert (await mounts("notes").delete(if_match=mounted.etag)).etag == '"thr:4"'
        assert seen[0].url.path.endswith(FILE_PATH)
        assert "%23" in str(seen[0].url) and "%25" in str(seen[0].url)
        assert [r.headers.get("If-Match") for r in seen] == [
            None,
            '"file:2"',
            '"file:2"',
            '"file:2"',
            None,
            '"file:3"',
            None,
            '"thr:2"',
            '"thr:3"',
            '"thr:3"',
        ]
        assert json.loads(seen[1].content) == {"content": "new"}
        assert seen[6].content == b""

    asyncio.run(scenario())


def test_record_shapes_search_body_and_no_write_replay() -> None:
    async def scenario() -> None:
        seen: list[httpx2.Request] = []

        def respond(request: httpx2.Request) -> httpx2.Response:
            seen.append(request)
            if request.method == "DELETE":
                return httpx2.Response(
                    409,
                    json={
                        "error": {
                            "code": "conflict",
                            "message": "unknown",
                            "details": {"reason": "write_unconfirmed"},
                            "request_id": "req_one",
                        }
                    },
                )
            if request.url.path.endswith("/search"):
                return httpx2.Response(
                    200,
                    json={
                        "items": [{"id": "r1", "text": "note", "score": None, "updated_at": None}],
                        "next_cursor": None,
                    },
                )
            return httpx2.Response(200, json={"id": "r1", "text": "changed", "score": None, "updated_at": None})

        async with Client("https://service.example", "test", transport=httpx2.MockTransport(respond)) as client:
            records = client.resources.memories("mem_one").records
            found = await records.search(body=wire.MemoryRecordSearch(query="private query", limit=3))
            assert found.value.items[0].score is None
            await records("r1").replace(body=wire.MemoryRecordText(text="changed"))
            with pytest.raises(ApiError) as error:
                await records("r1").delete()
            assert error.value.details["reason"] == "write_unconfirmed"
        assert len(seen) == 3
        assert seen[0].url.query == b""
        assert json.loads(seen[0].content) == {"query": "private query", "limit": 3}
        assert all("If-Match" not in r.headers for r in seen)
        assert [r.method for r in seen] == ["POST", "PUT", "DELETE"]

    asyncio.run(scenario())


def test_memory_pages_snapshot_labels_and_preserve_opaque_cursors() -> None:
    async def scenario() -> None:
        seen: list[httpx2.Request] = []

        def respond(request: httpx2.Request) -> httpx2.Response:
            seen.append(request)
            return httpx2.Response(
                200, json={"items": [], "next_cursor": "opaque +/=" if "cursor" not in request.url.params else None}
            )

        async with Client("https://service.example", "test", transport=httpx2.MockTransport(respond)) as client:
            labels = ["team:a", "scope:b"]
            pages = client.resources.memories.pages(label=labels)
            labels.append("later")
            assert not seen
            assert len([page async for page in pages]) == 2
            assert seen[0].url.params.get_list("label") == ["team:a", "scope:b"]
            assert seen[1].url.params["cursor"] == "opaque +/="

    asyncio.run(scenario())


def test_bootstrap_and_initialization_configuration_are_available() -> None:
    async def scenario() -> None:
        seen: list[httpx2.Request] = []

        def respond(request: httpx2.Request) -> httpx2.Response:
            seen.append(request)
            if request.method == "GET":
                return httpx2.Response(200, json={"email_delivery": False, "initialized": True})
            return httpx2.Response(
                409,
                json={
                    "error": {
                        "code": "conflict",
                        "message": "already initialized",
                        "details": {},
                        "request_id": "req_one",
                    }
                },
            )

        async with Client.session(
            "https://service.example", origin="https://service.example", transport=httpx2.MockTransport(respond)
        ) as client:
            assert (await client.resources.auth.configuration.get()).value.initialized is True
            with pytest.raises(ApiError):
                await client.resources.auth.bootstrap(
                    body=wire.BootstrapInput(email="owner@example.test", password="test-only")
                )
        assert len(seen) == 2
        assert seen[1].url.path == "/api/v1/auth/bootstrap"

    asyncio.run(scenario())
