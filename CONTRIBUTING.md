# Contributing

Write code, documentation, commit messages, Issues and pull requests in English. Use Issues for unresolved product, architecture, compatibility or scope decisions, and pull requests for reviewed changes. Accepted design belongs in `spec/`; proposals and progress do not.

Use short-lived, descriptive branches from `main` and Conventional Commit PR titles. Draft PRs run the full CI gate; mark ready after compatibility review and resolving failures. Merge through pull requests with resolved review threads. Keep changes focused and preserve unrelated work. Repository settings retain the parent project's squash-only merge, protected main and immutable release-tag policies.

## Development

Install Python 3.13, uv and Make. Run `make install` to synchronize `uv.lock`. `make format` applies Ruff and Markdown formatting; `make check` is non-mutating lint and type checking; `make test` runs SDK and generator tests; `make check-all` also verifies generated output and builds distributions. CI runs the same complete gate from this repository alone. Reuse valid checks whose inputs have not changed and report partial or unavailable validation explicitly.

### Quality gates

After `make install`, run `make hooks-install` once per checkout to install pre-commit. Commit hooks run file hygiene, Markdown formatting, and Ruff on changed files; Pyright, tests, generation, and builds stay in the explicit Make/CI gates. The profiles match the parent repository: Ruff's moderate correctness/maintainability rules and Pyright `standard`, not every optional strict rule.

| Command            | Purpose                                                                 |
| ------------------ | ----------------------------------------------------------------------- |
| `make format`      | Apply code and owned-document formatting                                |
| `make lint`        | Check formatting and lint without modifying files                       |
| `make typecheck`   | Check package and tooling types, including generated code               |
| `make check`       | Run lint and type checking                                              |
| `make hooks-check` | Run all pre-commit hooks; formatter changes fail the run for review     |
| `make check-all`   | Run hooks, provenance/generated drift, static checks, tests, and builds |

CI uses the same complete gate without installing Git hooks. If a hook rewrites files, review and stage its intended changes, then rerun; never bypass a failing hook. Vendored `contract/` evidence is excluded from hooks and Markdown formatting, except the locally owned `contract/README.md`; provenance and generated-output checks remain mandatory. Generated Python remains under Ruff, Pyright, and tests; fix its generator rather than hand-editing output.

Fix behavior at its owner, avoid speculative abstractions, and retain meaningful transport, wire and negative type tests. Generated output must type-check and pass tests. Change templates/adapters rather than hand-editing generated code. Credential diagnostics must remain redacted, omission must remain distinct from null, and mutation failures must not trigger automatic replay.

## Releases

Keep source versions at `0.0.0`. Stable versions use `X.Y.Z`; release candidates use `X.Y.Z-rc.N` with a positive, non-zero-prefixed N. Python artifacts normalize RC versions to `X.Y.ZrcN`. The release channel is `release/a13n/python/<version>` and the registry environment is `sdk-python-pypi`. Release versions are injected only in the ephemeral release checkout, not committed as version-only changes. Tag a main-line commit whose required CI passed. Publishing requires separate maintainer authorization and registry credentials; a successful local build is not a published release.

### Release operations

The release workflow verifies that the tagged commit is an ancestor of `origin/main` and that its latest push-triggered `ci.yml` run on `main` completed successfully. It fails rather than waiting for CI or silently using an older successful attempt. Rerun a blocked release only after CI succeeds. This read-only check uses `actions: read`; it does not replace branch protection or rerun the full test suite. Local tests for this boundary require Git, Bash and jq and use a fake GitHub CLI response, not production credentials.

Version preparation and artifact builds operate in ephemeral checkouts. Do not commit their modified manifests/lockfiles. Release tags are immutable, and a retry must retain the same tag and source commit. Publication is not transactional across registry and GitHub: an earlier job may have published before a later job failed. Inspect the registry, tags, artifacts and workflow result before rerunning; do not move tags or assume every publish step is idempotent.

Changelogs use first-parent history scoped to this repository and select only ancestor tags from the same release channel. RCs compare against an earlier RC for the same target, otherwise the preceding stable; stable releases compare against the preceding stable. PR labels classify and omit entries with a Conventional Commit fallback. Curated `.github/release-notes/COMPONENT/VERSION.md` notes are optional. Preview an existing, locally fetched tag without publishing (GitHub PR-label reads still require `gh` authentication):

```bash
GITHUB_REPOSITORY=converge-ai-labs/a13n-sdk-python \
  python3 scripts/create-github-release.py a13n-python 1.2.3 "a13n SDK 1.2.3" --dry-run
```

The first channel release uses initial or curated notes rather than attributing extracted monorepo history to this repository's PR numbers. RC GitHub Releases explicitly avoid `latest`. Repository privacy is separate from package visibility: registry publication can expose the package even when its source repository remains private.

The `sdk-python-pypi` environment must supply `PYPI_TOKEN` for the existing `a13n` package. The build attaches both wheel and sdist to the GitHub Release after registry publication. Environment/rules copying does not transfer this secret.

## Service contract updates

Contract tooling requires Git, Bash, jq and `shasum`. Ordinary builds need no Service checkout or credentials. Generation verifies the local manifest and hashes before reading the snapshot; `contract/README.md` is local guidance, not upstream evidence.

From a clean SDK branch, with the Service repository's full `origin/main` history fetched:

```bash
bash scripts/sync-contract.sh /path/to/agent-foundation FULL_40_CHARACTER_SERVICE_SHA
make generate
make check-all
```

Sync copies Git blobs, never working-tree files or executable Service code. It requires a complete main-line SHA, forward ancestry from the old pin, and byte-accurate old provenance. Missing/malformed inputs fail before writes; same-SHA retries do nothing. Inspect any interrupted local write and restore only the affected snapshot before retrying. The snapshot includes OpenAPI, both wire schemas, fixtures, API conventions, Native streaming and queue semantics. The source compare exposes runtime-only changes too. Follow recorded upstream paths for related specifications; accepted specs take precedence over inconsistent implementation.

`sync-service-contract.yml` receives Service dispatches or a manual full SHA, prepares the SDK toolchain and invokes `open-contract-pr.sh` in an ephemeral checkout. The script selects the existing rolling proposal (or current SDK `main`), copies the requested snapshot and runs `make generate`, then creates or updates a **draft PR** containing the snapshot and generated output. Only `contract/` and `a13n/generated/` are staged. It never merges, tags or releases.

Generation failure stops before committing or pushing; discard the ephemeral checkout and retry after fixing the cause. There is no contract-only fallback. Full SDK CI runs on drafts, so compilation/test failures remain visible for maintainer adaptation. Review compatibility and generated changes, fix templates or handwritten code as needed, regenerate and resolve CI failures before marking ready.

Each repository has at most one open automatic update PR on `sync/service-contract`. Its snapshot still records the complete immutable Service SHA. The workflow serializes updates; the script additionally compares incoming ancestry against both the accepted `main` pin and the pending proposal, so equal or older notifications never regenerate or rewind newer work. A newer source merges current SDK `main` into the proposal and appends the snapshot/generated changes without force-updating the branch. Handwritten code, templates and reviewer commits are retained; merge conflicts, invalid provenance, failed generation and concurrent pushes stop before replacing remote work. Generated files remain generator-owned, not a place for handwritten adaptation.

The marked source block and PR title track the proposed SHA and its range from the accepted pin. Notes outside that block are preserved. New source revisions return ready PRs to draft and require fresh review; same-SHA retries preserve readiness and only reconcile metadata. If push succeeded before PR creation/editing failed, retry reuses the remote snapshot without regenerating it. Closing an unmerged rolling PR pauses automatic proposals until a maintainer reopens it.

After merge, the next update starts from SDK `main`. Normally GitHub deletes the merged branch; if it remains at exactly the recorded merged head, automation removes it with an exact-head lease only after generation succeeds, then creates the next branch without replacing a concurrently created ref. Any commits added after merge are instead retained and reviewed. A missing branch for an open PR is an error, not permission to discard reviewer work. During migration, inspect old `sync/service-contract-<SHA>` PRs for manual work and close superseded proposals only after the rolling replacement is verified.

### Setup

Install both repositories' workflows on their default branches first. Use a dedicated GitHub App installed only on Service and the four SDK repos, with Contents and Pull requests read/write. Configure variable `SERVICE_CONTRACT_APP_CLIENT_ID` and secret `SERVICE_CONTRACT_APP_PRIVATE_KEY` in those repos (or restrict an organization secret to them). Never copy a developer's OAuth token. Workflows request separate Service-read and destination-write tokens and do not persist checkout credentials. Without a client ID the job is skipped; configuration enables it without another feature flag.

Verify one known main SHA end to end before relying on notifications: dispatch, generation, draft contents, provenance and draft CI. Successful generation is not compatibility acceptance. Offline tests use temporary Git repos and fake GitHub responses; they do not prove App installation or delivery. Registry credentials and release authorization remain separate.
