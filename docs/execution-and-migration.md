# Execution settings and Service compatibility

## Set Thread defaults and one Run override

The following fragment assumes an authenticated client and an existing Agent. The top-level execution field sets the new Thread's defaults; `options.execution` changes only the submitted Run.

```python
from a13n import ExecutionOverride, RunOptions, ToolExecutionOverride

interaction = await client.agents(agent_id).start(
    "Run the checks",
    execution=ExecutionOverride(environment={"APP_ENV": "staging", "EMPTY": ""}),
    options=RunOptions(
        execution=ExecutionOverride(
            environment={"APP_ENV": "test"},
            tools=ToolExecutionOverride(mode="auto", foreground_wait_seconds=0),
            steering="boundary",
        )
    ),
)
await interaction.close()
```

For an existing Thread, use `agent.send(thread_id, input, options=RunOptions(execution=...))` for one Run. Update persistent Thread defaults through `client.api.threads(thread_id).update(body=wire.ThreadUpdate(execution=wire.ExecutionOverride.from_dict({"environment": {"APP_ENV": "staging"}})), if_match=etag)`, importing `wire` from `a13n.generated.models`. Saved Agent configuration uses `wire.AgentConfigInput(model=model_key, execution=wire.ExecutionOverride(...))` through the normal Agent revision API.

Authored values use `UNSET` for omission and `None` for explicit null. Generated models use the same presence conventions. Both preserve empty mappings, strings and zero.

The existing generated `ExecutionOverride` at `start()` and mapping form in `RunOptions.execution` remain accepted. The public value classes above provide typed convenience without moving inheritance into the SDK.

## Inheritance belongs to Service

For each environment variable the order is recipe → Agent revision → Thread → Run → explicit command. A later layer replaces only the same key. For example, recipe `{A: "1", B: "recipe"}`, Thread `{B: "thread"}` and Run `{A: "2"}` resolve to `{A: "2", B: "thread"}` before command-specific values.

SDKs only serialize choices. Service freezes the Agent/Thread/Run overlay at acceptance; the mount supplies its frozen recipe at command dispatch. Neither SDK nor Service changes shared sandbox global variables for a Run. These are ordinary readable configuration fields, not secret storage.

On Thread PATCH, an omitted field retains its existing setting. A supplied environment map replaces that Thread map in full; null or `{}` clears that layer, exposing lower defaults. An empty string is an explicit empty value, not removal. `execution: null` clears all Thread execution overrides. A per-Run null map inherits; it does not erase lower layers. Existing accepted Runs retain their frozen settings. A conflicting override for an active Run's steer is validated by Service; the SDK does not silently retry or create another Run.

## Request context and the refreshed native surface

Use `RunOptions(context={"headers": {"X-Tenant": "demo"}})` to submit explicit Run context. Omission, `None`, and an object remain distinct on the wire. HTTP authentication and transport headers are never copied into this field. Service normalizes and freezes accepted context; recovery, resume and child Runs retain it. New messages and forks start with empty context when omitted; steering retains the accepted context when omitted.

Usage summaries contain `models`; read Run breakdowns through `client.api.usage.runs.pages(...)`. The refreshed API also exposes built-in Skill catalogs/details/ZIP archives, plugin catalogs, Session Thread navigation, member usage, provider deletion with optional `If-Match`, and committed App open/resource/tool operations. Session streams add repeatable `app_ready` frames after committed Items.

Thread SSE transport truncation, including EOF within a UTF-8 code point, uses the existing bounded reconnect policy from the last applied cursor. Complete malformed UTF-8 or JSON remains a protocol failure. SessionStream continues to expose a single connection with caller-owned reconnect.

## Additional snapshot change

Span-content reads now locate the requested span directly. The native span-content operation no longer takes a search cursor or exposes cursor-page iteration; continue text fragments with `version` and `next_offset` instead.

## Compatibility inherited from the prerequisite update

- Native detail endpoints can return detailed records, compact summaries or text fragments. Inspect the returned variant in native API code. High-level execution observers explicitly request detailed records and retain their complete-result semantics.
- Run lists contain bounded discovery metadata (`RunListItem`), not full execution records. Read an individual Run for complete inputs, results and execution settings. Thread history includes both cursor directions and an optional anchor.
- Cursor helpers retain filters and response metadata for supported paginated results, including compact/detailed unions. Ordinal Run items remain a separate API; text fragments use offsets, not cursor helpers.
- Session streams include typed `schedule` and `occurrence` events alongside `thread`, `items`, `delta` and `gap`. Update exhaustive switches. Session frames still carry no Thread reconnect cursor.
- Tool discovery now uses proxy `ToolSearchConfig`. Retired native-mode/strategy types and the `platform_tools` override have been removed. Select tools via the current `toolsets` contract and built-in instructions via `builtin_skills`; Service owns authorization.
- Newly exposed native resources include schedules, devices, metrics data sources and dashboards. This sync does not add SDK-owned scheduling, retries or telemetry collection.

The contract snapshot is pinned to merged Service commit [`b4c9b1345752`](https://github.com/converge-ai-labs/agent-foundation/commit/b4c9b1345752bbaef3a8b076475112535357fbc7); [source metadata](../contract/source.json) records every consumed input.
