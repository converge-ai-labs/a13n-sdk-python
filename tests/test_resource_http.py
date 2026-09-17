"""Loopback HTTP integration, not a real Service or model-provider test."""

import asyncio
import json

from a13n import Client, text_input
from a13n.generated.models import StartRunRequest


def test_start_stream_and_read_items_over_real_http_sockets():
    async def scenario():
        observed = []
        failures = []
        receipt = {
            "run_id": "run_1",
            "session_id": "session_1",
            "thread_id": "thread_1",
            "run_version": 1,
            "thread_version": 1,
        }
        event = {
            "event_id": "rse_" + "a" * 20,
            "event_type": "a13n.item.delta",
            "run_id": "run_1",
            "thread_id": "thread_1",
            "occurred_at": "2026-09-17T00:00:00Z",
            "payload": {"text": "Hello"},
            "schema_version": "1",
        }

        async def serve(reader, writer):
            try:
                request = await reader.readuntil(b"\r\n\r\n")
                lines = request.decode().split("\r\n")
                method, path, _ = lines[0].split(" ")
                headers = {
                    key.lower(): value.strip() for line in lines[1:] if line for key, value in [line.split(":", 1)]
                }
                body = await reader.readexactly(int(headers.get("content-length", "0")))
                observed.append((method, path))
                assert headers["authorization"] == "Bearer test-only"
                if path.endswith("/stream"):
                    assert headers["last-event-id"] == "99-0"
                    data = ("id: 100-0\nevent: a13n.item.delta\ndata: " + json.dumps(event) + "\n\n").encode()
                    writer.write(
                        b"HTTP/1.1 200 OK\r\nContent-Type: text/event-stream\r\nTransfer-Encoding: chunked\r\nConnection: close\r\n\r\n"
                    )
                    for offset in range(0, len(data), 7):
                        part = data[offset : offset + 7]
                        writer.write(f"{len(part):x}\r\n".encode() + part + b"\r\n")
                        await writer.drain()
                    writer.write(b"0\r\n\r\n")
                else:
                    if method == "POST":
                        assert path == "/prefix/api/v1/workspaces/ws/runs"
                        assert headers["idempotency-key"] == "start-once"
                        assert json.loads(body)["input"]["content"][0]["text"] == "hello"
                        payload, status = receipt, b"202 Accepted"
                    else:
                        assert path.startswith("/prefix/api/v1/runs/run_1/items")
                        payload, status = (
                            {
                                "items": [],
                                "next_cursor": None,
                                "projection_cursor": "100-0",
                                "snapshot_version": 1,
                                "complete": True,
                                "finalized": True,
                                "incomplete_reason": None,
                            },
                            b"200 OK",
                        )
                    encoded = json.dumps(payload).encode()
                    writer.write(
                        b"HTTP/1.1 "
                        + status
                        + b"\r\nContent-Type: application/json\r\nContent-Length: "
                        + str(len(encoded)).encode()
                        + b'\r\nETag: "v1"\r\nConnection: close\r\n\r\n'
                        + encoded
                    )
                await writer.drain()
            except Exception as exc:
                failures.append(exc)
            finally:
                writer.close()
                await writer.wait_closed()

        server = await asyncio.start_server(serve, "127.0.0.1", 0)
        async with server:
            port = server.sockets[0].getsockname()[1]
            async with Client(f"http://127.0.0.1:{port}/prefix", "test-only") as client:
                result = await client.workspaces("ws").runs.create(
                    body=StartRunRequest(agent_id="agent_1", input_=text_input("hello")), idempotency_key="start-once"
                )
                assert result.status == 202 and result.etag == '"v1"'
                run = client.runs(result.value.run_id)
                async with run.stream(after="99-0") as events:
                    collected = [item async for item in events]
                assert [item.cursor for item in collected] == ["100-0"]
                pages = [page async for page in run.items.pages()]
                assert pages[0].value.finalized and pages[0].value.projection_cursor == "100-0"
        assert not failures, failures
        assert len(observed) == 3

    asyncio.run(scenario())
