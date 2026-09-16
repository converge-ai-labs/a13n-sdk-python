# Contributing

Write code, documentation, commit messages, Issues and pull requests in English. Use Issues for unresolved product, architecture, compatibility or scope decisions, and pull requests for reviewed changes. Accepted design belongs in `spec/`; proposals and progress do not.

Use short-lived, descriptive branches from `main` and Conventional Commit PR titles. Draft PRs skip code CI; mark ready when review and validation are useful. Merge through pull requests with resolved review threads. Keep changes focused and preserve unrelated work. Repository settings retain the parent project's squash-only merge, protected main and immutable release-tag policies.

## Development

Install Python 3.13, uv and Make. Run `make install` to synchronize `uv.lock`. `make format` applies Ruff; `make check` is non-mutating lint and type checking; `make test` runs SDK and generator tests; `make check-all` also verifies generated output and builds distributions. CI runs the same complete gate from this repository alone. Reuse valid checks whose inputs have not changed and report partial or unavailable validation explicitly.

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

`sync-service-contract.yml` receives Service dispatches or a manual full SHA and opens a **draft PR** containing the snapshot. Maintainers generate, adapt and test, then mark it ready for ordinary CI and review. It never merges, tags or releases. Each SHA has one branch; retries preserve existing open/closed PRs and reviewer edits. If push succeeded before PR creation failed, a retry creates the missing draft without rewriting the branch. Run `open-contract-pr.sh` only in an ephemeral CI checkout.

### Setup

Install both repositories' workflows on their default branches first. Use a dedicated GitHub App installed only on Service and the four SDK repos, with Contents and Pull requests read/write. Configure variable `SERVICE_CONTRACT_APP_CLIENT_ID` and secret `SERVICE_CONTRACT_APP_PRIVATE_KEY` in those repos (or restrict an organization secret to them). Never copy a developer's OAuth token. Workflows request separate Service-read and destination-write tokens and do not persist checkout credentials. Without a client ID the job is skipped; configuration enables it without another feature flag.

Verify one known main SHA end to end before relying on notifications: dispatch, draft, provenance, adaptation and ready-PR CI. Source import is not compatibility acceptance. Offline tests use temporary Git repos and fake GitHub responses; they do not prove App installation or delivery. Registry credentials and release authorization remain separate.
