# The resource API

The Agent workflow is designed for conversations. `client.api` is the complete, generated API for management and lower-level operations: Agents, Models, Skills, files, Memory, Threads, and administration. Both use the same Client and credentials.

Use this chapter when you need to list or edit resources, inspect HTTP metadata, or work with a Service operation that is not part of `start()` / `send()`.

**Migration:** replace `client.resources.<collection>` with `client.api.<collection>`. The pre-0.1 SDK does not retain a `resources` alias. Authored `client.agents(agent_id)`, `client.threads(thread_id)` and `client.runs(run_id)` workflows are unchanged; the generated graph, credentials and Client lifetime are shared.

## Find a resource and inspect its response

Generated collection methods return a typed value together with the HTTP evidence for that request:

```python
from a13n import Client


async def find_agents(client: Client, query: str) -> None:
    response = await client.api.agents.list(q=query, limit=10)
    for agent in response.value.items:
        print(agent.id, agent.name)
    print("HTTP status:", response.status_code)
    print("Request ID:", response.request_id)
    print("More available:", response.value.next_cursor is not None)
```

A `Result[T]` exposes:

| Property      | Purpose                                                                            |
| ------------- | ---------------------------------------------------------------------------------- |
| `value`       | Parsed model, page, or operation result.                                           |
| `status_code` | Actual successful HTTP status, including distinctions such as creation and replay. |
| `headers`     | Response headers when you need protocol metadata.                                  |
| `etag`        | Version token for operations that support conditional changes.                     |
| `request_id`  | Correlate a request with Service diagnostics.                                      |
| `content`     | Response bytes retained by an ordinary buffered request.                           |

Use generated model attributes in your application. Call `to_dict()` when serializing or inspecting their wire representation. Do not print entire responses in production logs if they may contain sensitive content.

## Traverse more than one page

`list()` performs one request. `iter()` yields individual resources, fetching additional pages only as you consume them:

```python
from a13n import Client


async def print_agent_directory(client: Client) -> None:
    async for agent in client.api.agents.iter(limit=50):
        print(agent.id, agent.name)
```

Here `limit=50` is the page size, not a cap of fifty total results. Break the loop if your application only needs the first match. If you need page metadata, use `pages()` instead:

```python
from a13n import Client


async def inspect_agent_pages(client: Client) -> None:
    async for page in client.api.agents.pages(limit=50):
        print("Page request:", page.request_id, "Items:", len(page.value.items))
```

Cursor pagination is not a transaction across the entire collection. If your application needs a durable export, account for concurrent changes and the Service's retention rules rather than assuming page traversal freezes the dataset.

## Make a conditional edit

Suppose your application lets a user rename an Agent. Read the resource before editing and pass that response's ETag:

```python
from a13n import Client
from a13n.generated import models as wire


async def rename_agent(client: Client, agent_id: str, name: str) -> None:
    resource = client.api.agents(agent_id)
    current = await resource.get()
    updated = await resource.update(body=wire.AgentUpdate(name=name), if_match=current.etag)
    print("Renamed:", updated.value.name, "ETag:", updated.etag)
```

A `412` means the version you edited is no longer current. Return that conflict to the user or reconcile the new value with their edit. Do not silently read another ETag and force the old change through.

ETags belong to particular resources. An Agent ETag is not interchangeable with a Thread or Memory-file ETag. [Memory editing](files-and-memory.md#update-a-note-without-losing-another-writers-changes) uses the same pattern at the file boundary.

## Omitted, null, and empty values

Generated requests preserve distinctions that matter to partial updates:

- Leaving a field at `UNSET` omits it from the request.
- `None` sends JSON `null` when the field permits it. Its meaning is defined by that operation, not by a universal “delete” rule.
- An empty object or list is an explicit value, not omission.

You can inspect the difference locally without sending a request:

```python
from a13n.generated import models as wire

unchanged = wire.AgentUpdate()
explicit_null = wire.AgentUpdate(description=None)
empty_text = wire.AgentUpdate(description="")

print(unchanged.to_dict())  # {}
print(explicit_null.to_dict())  # {"description": None}
print(empty_text.to_dict())  # {"description": ""}
```

Do not remove `None` from a request dictionary simply to make it look cleaner; that can change its semantics. Likewise, avoid replacing every omitted field with `None` when mapping an application form into a generated model.

For arbitrary object fields, generated models provide `from_dict()`. For example, setting a Run override's `extra_body` to `{}` explicitly clears the inherited object:

```python
from a13n.generated import models as wire

settings = wire.AgentOverrideInputModelSettingsType0.from_dict({"extra_body": {}})
options = wire.RunOptionsInput(overrides=wire.AgentOverrideInput(model_settings=settings))
print(options.to_dict())
```

An explicit `extra_body` or `extra_headers` object replaces the inherited object; it is not recursively merged. Keep provider-specific keys within those provider-specific settings rather than adding unsupported top-level fields.

## Forward native Model settings

A Model's `config.settings` is an open native JSON object, not a second SDK-defined hierarchy. Use the generated mapping wrapper to preserve provider-specific JSON values:

```python
from a13n.generated import models as wire


def model_config(model_api: str, model_name: str) -> wire.ModelConfigInput:
    return wire.ModelConfigInput(
        model_api=model_api,
        model_name=model_name,
        settings=wire.ModelConfigInputSettings.from_dict({"seed": 42, "timeout": 30}),
    )
```

Use this config with `wire.ModelCreate` or `wire.ModelUpdate`. Supported native keys and conflict resolution with explicit config fields belong to the Service and installed provider. Nested objects, arrays, booleans, numbers and null values are forwarded unchanged and retained in Model readback. Omitting `settings` differs from explicitly supplying `{}`; the SDK does not fill provider defaults or validate provider policy.

## Forward image and video policy

Media preparation belongs to Service/Harness, not Model settings or SDK processing. Set native characteristics on a Model config:

```python
from a13n.generated import models as wire

config = wire.ModelConfigInput(
    model_api="your-installed-api",
    model_name="your-model",
    characteristics=wire.HarnessModelCharacteristicsInput(
        image_input=wire.ImageInputPolicy(max_images=4, split_large_images=False),
        video_input=wire.VideoInputPolicy(max_video_bytes=8_000_000),
        url_input=wire.UrlInputSupportInput(video=[wire.VideoUrlType.YOUTUBE]),
    ),
)
```

Use it in `wire.ModelCreate` or `wire.ModelUpdate`. Omitted `image_input` uses native defaults; `image_input=None` disables automatic preparation. Zero limits, false flags and `video=[]` remain explicit values. The Service enforces byte budgets, URL support, host restrictions and TLS; the SDK does not inspect or transform media.

## Select a native Run configuration

Pass configuration through existing typed `options` on `start()` and `send()`; generated `wire.Message` uses the same shape:

```python
from a13n import Client, RunConfiguration, RunOptions, UrlPart


async def restricted_input(client: Client, agent_id: str) -> None:
    options = RunOptions(
        configuration=RunConfiguration(
            allowed_hosts=["media.example.test"],
            extensions={"example.policy": {"enabled": False, "limits": [], "note": None}},
        )
    )
    payload = [
        "Describe this image and video.",
        UrlPart("https://media.example.test/image.png"),
        UrlPart("https://media.example.test/video.mp4"),
    ]
    interaction = await client.agents(agent_id).start(payload, options=options, idempotency_key="media-001")
    outcome = await interaction.result()
    print(outcome.evidence.value.options.configuration)
```

An explicit configuration object is a complete snapshot, not a merge with hidden SDK defaults or revision overrides. `configuration=UNSET` omits it, `configuration=None` sends null, and `RunConfiguration()` sends `{}`. Omission/null select the native default for a new Run and retain the accepted snapshot when steering. `allowed_hosts=None` is unrestricted; `allowed_hosts=[]` denies every native URL destination. Extensions are arbitrary namespaced JSON, not SDK policy.

The Service normalizes/freezes the accepted configuration. Steering and pending edits against an active Run may omit it or match the frozen value; a different explicit snapshot returns `409 conflict` with reason `run_configuration_immutable`. The SDK does not auto-queue or retry that request. `delivery=wire.Delivery.NEXT_RUN` selects a new snapshot, while resume successors and inline children inherit their source's configuration.

## Select Environment and skill preparation

```python
from a13n import AgentOverride, Client, RunOptions


async def isolated_skills(client: Client, agent_id: str) -> None:
    interaction = await client.agents(agent_id).start(
        "Use the selected skills.",
        options=RunOptions(
            overrides=AgentOverride(
                lazy_environment=False,
                skill_sync={"mode": "isolated", "cache_count": 0},
            )
        ),
        idempotency_key="skills-001",
    )
    print((await interaction.result()).status)
```

Omission inherits the Agent's policy. Service defaults to lazy instance readiness and shared skill publication (`mode=shared`, `overwrite=true`, `cleanup=false`). Setting `lazy_environment=False` prepares all frozen mounted instances before Harness entry; execution connections still open on first use. A `skill_sync` override replaces the complete policy block. Shared overwrite replaces selected directories, while shared cleanup removes unselected names; isolated mode uses immutable digest directories, with a default soft budget of 128 packages and zero disabling trimming. Select mode-specific fields only. The SDK forwards these choices without managing Environments or a local skill cache.

## Findings, analyses, and message authors

```python
from a13n import Client
from a13n.generated import models as wire


async def diagnostic_resources(client: Client, session_id: str, entry_ids: list[str]) -> None:
    prepared = await client.api.finding_agent()
    analysis = await client.api.finding_analyses.create(
        body=wire.AnalysisCreate(max_traces=1, presets=[wire.Preset.EXECUTION]),
        idempotency_key="analysis-001",
    )
    print(prepared.value.preset_kind, analysis.value.run_id)
    async for page in client.api.findings.pages(closed=False, limit=10):
        for finding in page.value.items:
            print(finding.id, finding.category, finding.assessment)
    authors = await client.api.sessions(session_id).message_authors.get(entry_id=entry_ids)
    for author in authors.value.items:
        print(author.entry_id, author.principal_id, author.principal)
```

Finding Agent is a builtin preset distinct from Composer. Analysis creation accepts a normal Run; use its `run_id` to observe completion through `client.runs(id)`. Findings retain evidence, limitations and reviewer assessment; zero Findings is not proof of complete inspection or Agent health. Native `findings.create()`, `findings(id).get()` and `findings(id).update(body=..., if_match=...)` remain explicit requests with typed bodies and HTTP evidence. Preparing a preset needs a usable model and Service write permission; analysis and evidence access require their native permissions and configured trace backend.

Message authors are resolved for 1–100 repeated Entry IDs in one Session. Missing, foreign-session and non-message entries are omitted. Principal IDs and original submission times remain stable, while `principal` is a current profile or null; this query does not grant member-directory access.

## Model Provider authorization and discovery

Use the generated Provider graph with an existing Client:

```python
from a13n import Client
from a13n.generated import models as wire


async def begin_provider_authorization(client: Client, provider_id: str, workspace_id: str) -> wire.AuthorizationStart:
    provider = client.api.model_providers(provider_id)
    await provider.authorization.get(x_workspace_id=workspace_id)
    started = await provider.authorize(
        body=wire.ProviderAuthorizationRequest(new_registration=False), x_workspace_id=workspace_id
    )
    return started.value  # Hand the returned URL/method to your application's authorized user; do not log it.


async def complete_manual_authorization(
    client: Client, provider_id: str, workspace_id: str, attempt_id: str, callback_url: str
) -> None:
    await client.api.model_providers(provider_id).authorization.callback(
        body=wire.AuthorizationCallback(attempt_id=attempt_id, callback_url=callback_url),
        x_workspace_id=workspace_id,
    )


async def discover_provider_models(client: Client, provider_id: str, workspace_id: str) -> list[wire.ProviderModel]:
    return (await client.api.model_providers(provider_id).models.get(x_workspace_id=workspace_id)).value
```

Follow the returned `method`: `manual_callback` accepts a pasted callback through `authorization.callback`; `browser_callback` uses the operator-configured hosted flow and status polling. Do not hardcode callback origins, client identity or port, print callback codes, or store Provider tokens. Starting hosted browser authorization requires an unconfined user login, but manual Workspace authorization can use an authorized API key. Service permissions are `read` for status, `write` for authorize/callback/disconnect, and `run` for discovery; the SDK does not replace these checks. OAuth is workspace-shared Provider state, not a personal Connection or a new Client credential.

`await provider.authorization.delete(...)` clears local Provider tokens and reports external revocation separately through nullable `revocation_confirmed`. Treat unknown exchange/revocation outcomes as reported facts, not permission to replay mutations. Hosted callback setup and issuer approval are operator responsibilities.

## Select built-in instructions

`AgentOverride.builtin_skills` selects built-in instruction bundles:

```python
from a13n import AgentOverride, RunOptions

platform_options = RunOptions(
    overrides=AgentOverride(
        builtin_skills=["platform-operations"],
    )
)
```

Use these options with the ordinary Agent workflow. An empty selection is explicit; omission inherits native policy, while permitted null remains null. Instructions do not enable MCP groups or grant tenant permissions. `ToolsetKey.COMPUTER` selects a separate native toolset, not a platform group.

## Check a desktop and restrict a desired mount

```python
from a13n import Client
from a13n.generated import models as wire


async def restrict_mount(client: Client, thread_id: str, mount_name: str) -> wire.MountView:
    thread = client.api.threads(thread_id)
    current = await thread.get()
    updated = await thread.environments(mount_name).update(
        body=wire.MountUpdate(permission_ceiling=wire.EnvironmentPermissionSetInput(operations=[])),
        if_match=current.etag,
    )
    return updated.value


async def check_desktop(client: Client, environment_id: str) -> wire.ComputerCheck:
    return (await client.api.environments(environment_id).computer.check()).value
```

The check does not start an instance, capture pixels or send input. `not_ready` differs from `unsupported`, and provider failures remain errors. Computer use needs an enabled Agent toolset, explicit mount actions and a capable ready provider. Omitted `MountCreate.permission_ceiling` retains file/execution defaults and grants no Computer actions; `{ "operations": [] }` explicitly removes those mount operations. A Thread ceiling update affects future Runs, not accepted frozen mounts, and still requires the Thread ETag.

Environment Provider `references.get()` reports counts and bounded reference samples. `delete(if_match=...)` may fail while references remain. Private provider configuration is write-only: a public read is not a backup of connection credentials. Provider PATCH preserves omitted credentials and header values even when `config` changes. Credentials replace as a whole and null removes them; Provider `extra_headers` updates per name, so omitted names and `{}` retain saved headers. This differs from Model/Agent whole-object `extra_headers` replacement. Public readback reports credential presence and header names, not their private values. Keep private input in the Provider HTTP request, not Composer tool arguments or Run resume answers; saving a Provider and resuming a Run are independent operations.

## Inspect execution, retained images, and timing

```python
from a13n import Client
from a13n.generated import models as wire


async def executed_agent(client: Client, run_id: str) -> wire.RunAgent:
    return (await client.api.runs(run_id).agent.get()).value


async def read_retained_image(client: Client, run_id: str, image_id: str) -> tuple[bytes, str]:
    image = await client.api.runs(run_id).images(image_id).get()
    return image.content, image.headers["content-type"]


async def request_metrics(client: Client, record_id: str) -> wire.ModelRequestMetrics:
    return (await client.api.usage.records(record_id).metrics.get()).value
```

`RunAgent.revision` identifies the frozen revision; `config` adds that Run's overrides. Models, Connections and templates named by the config remain live. Use `client.api.runs.list(...)` for native filtered pages and `runs(id).attempts(attempt_id).get()` for one attempt; neither query changes execution.

Read retained image IDs explicitly from committed history. JPEG and PNG bytes retain their actual Content-Type; this call does not capture a new screenshot. For large images use `.get_stream()` and check status before consuming bytes, as in [Asset downloads](files-and-memory.md#download-without-buffering-the-whole-file). Observation never auto-fetches image references.

Timing is derived by Service, not recomputed by the SDK. `None` means no eligible timing, not zero; zero output on a measured positive-duration request can have zero speed. `UsageSummary.models` covers the entire filtered scope. Read per-Run totals separately with `client.api.usage.runs.pages(...)`; each page has required `items` and nullable `next_cursor`. `ModelUsage` includes required nullable `average_time_to_first_chunk_seconds` and `output_tokens_per_second`; preserve unavailable values rather than replacing them with zeros.

## Read latest-generation context usage

```python
from a13n import Client
from a13n.generated import models as wire


async def latest_context(client: Client, run_id: str) -> wire.ContextUsage | None:
    result = await client.api.usage.context.get(run_id=run_id)
    usage = result.value
    if usage is None:
        print("No completed model contribution", result.request_id)
    else:
        print(usage.run_id, usage.record_id, usage.input_tokens, usage.output_tokens, usage.context_window_tokens)
    return usage
```

Supply **exactly one** of `thread_id`, `run_id`, or `record_id`; Service validates the selection. Thread/Run scope selects the latest completed main-agent model contribution, not aggregate usage or an estimate of the next prompt. Record scope reads that exact contribution, including an attributed child record. HTTP 200 JSON null means no eligible contribution for the selected Thread/Run; missing scopes or records remain errors. All three token/window fields are required but nullable: unavailable stays `None`, and measured zero stays zero. Capacity reflects the current configured window with the Run's applicable frozen Agent override; the SDK invents no occupancy ratio or total. Read `.status_code`, `.request_id` and `.content` on the Result when retaining evidence.

## Choose the right level

| Task                                               | Preferred entry point                                                  |
| -------------------------------------------------- | ---------------------------------------------------------------------- |
| Start or continue a conversation                   | `client.agents(id).start(...)` / `.send(...)`                          |
| Wait for a known execution or resume a waiting one | `client.runs(id)`                                                      |
| Create or edit an Agent                            | `client.api.agents`                                                    |
| Manage files, Memory, or administrative resources  | The corresponding `client.api` collection                              |
| Build a protocol integration                       | Generated request modules, `Client.execute()`, or raw response streams |

Generated Thread creation and inbox submission return `Result[wire.Submitted]`, not an Interaction. They perform the declared request and do not adopt the higher-level observation lifecycle. Prefer the Agent workflow unless your integration needs to own that protocol itself.

The [generated resources](../a13n/generated/resources.py) expose operation signatures, and [generated models](../a13n/generated/models) describe request and response fields. The [pinned source](../contract/source.json) identifies the Service contract used to generate them. A complete generated surface does not grant a credential permission to invoke every operation.

[Back to the guide](README.md) · [Next: errors and recovery](errors-and-recovery.md)

## Browse bounded run history

Run lists return `RunListItem` metadata with `input_preview.text` (at most 200 Unicode code points) and `input_preview.truncated`. Fetch an individual Run for full input, output, options or memory mounts. List `view` selection is removed.

Thread runs default to newest first. `ThreadRunPage` exposes `total`, `previous_cursor` (newer) and `next_cursor` (older). Each `ThreadRunItem` carries its chronological `number`, nullable decimal-string `cost`, `model_calls` and `unpriced_requests`; use the item's `number` instead of the removed page-level `first_number`. Use `anchor` for the first page around an exact Run; subsequent requests send the returned cursor without the anchor. Alternatively, `sort=cost|calls|duration` with `direction=asc|desc` ranks the whole Thread before pagination and cannot be combined with `anchor`. Ranking has no previous cursor. Reads and page iterators are lazy.

Session lists support `sort=updated_at|runs|cost` and `direction=asc|desc`. Session views require `run_count`, nullable decimal-string `cost` and `unpriced_requests`. Unknown cost remains null, distinct from measured zero. Session streams also expose native schedule and occurrence frames.
