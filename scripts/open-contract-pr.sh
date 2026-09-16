#!/usr/bin/env bash
# Run only in an ephemeral SDK main checkout after sync-contract.sh succeeds.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
: "${GITHUB_REPOSITORY:?SDK repository is required}"
bash scripts/sync-contract.sh --check
commit=$(jq -r .commit contract/source.json)
previous=$(git show HEAD:contract/source.json | jq -er .commit)
[[ "$commit" != "$previous" ]] || { echo 'Contract pin is unchanged'; exit 0; }
branch="sync/service-contract-$commit"
prs=$(gh pr list --repo "$GITHUB_REPOSITORY" --head "$branch" --base main --state all --json number)
if [[ $(jq length <<< "$prs") != 0 ]]; then
  echo "A PR already exists for $commit; leave reviewer changes and closed decisions untouched."
  exit 0
fi
remote=$(git -c credential.helper= -c 'credential.helper=!gh auth git-credential' ls-remote --heads origin "refs/heads/$branch")
if [[ -z "$remote" ]]; then
  # Generate only new proposals; retries must not replace reviewer work.
  # Do not pass the PR credential to generator subprocesses.
  env -u GH_TOKEN make generate
  git switch -c "$branch"
  git add -A -- contract a13n/generated
  git -c user.name='Service contract sync' -c user.email='service-contract-sync@users.noreply.github.com' \
    commit -m "chore: update Service contract to $commit"
  # Use the step-scoped App token through gh, never in a URL or persisted credential.
  git -c credential.helper= -c 'credential.helper=!gh auth git-credential' push origin "HEAD:refs/heads/$branch"
fi
# A push may have succeeded before a prior PR creation failed. Reuse that branch
# without force-pushing or replacing adaptation work already made by reviewers.
body=$(mktemp)
trap 'rm -f "$body"' EXIT
cat > "$body" <<EOF
## Contract update

Pinned Service source: https://github.com/converge-ai-labs/agent-foundation/commit/$commit

Changes since the accepted SDK pin: https://github.com/converge-ai-labs/agent-foundation/compare/$previous...$commit

This draft imports committed HTTP/wire definitions, shared fixtures, API conventions,
Native streaming semantics and queued-submission semantics, with source paths and SHA-256 hashes,
and includes SDK-local HTTP generation. Full SDK CI runs while this PR is still a draft.
The compare includes implementation changes even when exported schemas are unchanged.
It does not execute Service code or imply that this SDK already supports the new contract.

## Maintainer acceptance

- [ ] Review the source range, compatibility and non-HTTP behavior against the owning specifications.
- [ ] Review the generated diff; adapt handwritten code/templates and add protocol tests as needed.
- [ ] Regenerate after template/input changes and run \`make check-all\` on this branch.
- [ ] Resolve CI failures, mark this PR ready and merge only through normal review.

A failed generation or incompatible change requires adaptation, not a silent contract downgrade.
No release, tag, auto-merge or package version change is requested by this automation.
EOF
gh pr create --repo "$GITHUB_REPOSITORY" --base main --head "$branch" --draft \
  --title "chore: update Service contract to ${commit:0:12}" --body-file "$body"
