# Generation and pinned compatibility adapters

`generate.py` runs the pinned HTTP generator over a detached, locally adapted OpenAPI document. `resources.py` emits static, typed resource navigation from those generated signatures and the same adapted document. Both outputs live under `a13n/generated/` and participate in the same byte/name drift check. The resource layer does not implement a second serializer or runtime `__getattr__` dispatcher.

The original `contract/` bytes and provenance remain untouched. Generation needs neither a Service checkout nor network reads of Service source. Its small compatibility adaptations are reviewed SDK behavior, not edits to upstream evidence.

## Known export corrections

Verified against Service source `bcdfb8a88f41ab1c3dfa9d5edfba6c2ce001d60d`:

| Route | Export gap | Evidence and adaptation |
| --- | --- | --- |
| `POST /threads/{thread_id}/queued-submissions/consume` | Only 202 is declared; queue invalidation returns 200. | Vendored `semantics/queued-submissions.md` specifies `submission_failed` with HTTP 200. Add the same receipt shape at 200 when absent. |
| `GET /skill-revisions/{skill_revision_id}/content` | Empty JSON schema for a binary download. | `packages/a13n-service/a13n_service/skills/router.py` returns a streaming ZIP. Adapt the empty JSON declaration to `application/zip` binary. |
| `GET /workspaces/{workspace}/agents/{agent}/avatar/{image_id}` | Empty JSON schema for an image. | `agents/router.py` calls `http_images.image_response`, which returns WebP. Adapt the empty JSON declaration to `image/webp` binary. |

Media adaptations apply only to the exact empty JSON declarations, not a future explicit replacement schema. Review and remove obsolete corrections when the Service exports are fixed. Binary methods now correctly return generated `File` values instead of attempting JSON parsing; resource `get_stream()` methods preserve bounded consumption and the actual response headers. This is an intentional correction to previously unusable binary bindings, not a new binary wire protocol.

Service password-reset and email-change requests legitimately return HTTP 202 with JSON null. The resource result adapter preserves that success as `Result(value=None, ...)`; it does not treat every non-204 null value as a malformed response. Generated parsers still reject missing required model fields and invalid JSON.

## Resource generation policy

Literal route components are typed attributes; parameter components bind a local selector through `__call__`. Aliased parameter spellings at the same route position bind the same identity (for example, Run continuation's `source_run_id`). Generated enum selectors remain typed. CRUD names are `list` for collection representations, `get` for single representations, `create`, `update`, `replace`, and `delete`; single POST command leaves use the protocol command name. Python keywords gain a trailing underscore.

Only actual opaque-cursor collections gain lazy `pages`. Pages retain their complete specialized value rather than flattening away snapshot or recovery metadata. Streaming binary methods are emitted from media declarations. Core interaction helpers use explicit mixins; receipt methods remain separately addressable. `OPERATIONS` records complete method coverage for every pinned Native operation.

The generator must fail on ambiguous member names or unsupported route roots rather than emitting a silently shadowed operation. Resource signatures reuse request models and keyword/header defaults from HTTP bindings. No convenience inserts Service defaults, makes a second workflow identity, or assumes that a Workspace-discovered resource is Workspace-owned.
