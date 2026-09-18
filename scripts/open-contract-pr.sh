#!/usr/bin/env bash
# Run only in a clean, ephemeral SDK checkout with complete Service Git history.
set -euo pipefail

fail() { echo "Contract PR: $*" >&2; exit 1; }
remote_git() { git -c credential.helper= -c 'credential.helper=!gh auth git-credential' "$@"; }
bot_git() { git -c user.name='Service contract sync' -c user.email='service-contract-sync@users.noreply.github.com' "$@"; }

# Parse the whole function before switching checkouts: the proposal may contain
# an older copy of this script, while this invocation must use main's automation.
main() {
  cd "$(dirname "${BASH_SOURCE[0]}")/.."
  : "${GITHUB_REPOSITORY:?SDK repository is required}"
  [[ $# == 2 ]] || fail 'usage: open-contract-pr.sh SERVICE_CHECKOUT FULL_SHA'
  upstream=$(cd "$1" && pwd)
  commit=$2
  [[ "$commit" =~ ^[0-9a-f]{40}$ ]] || fail 'a full Service SHA is required'
  [[ -z $(git status --porcelain) ]] || fail 'use a clean ephemeral checkout'
  [[ $(git -C "$upstream" rev-parse "$commit^{commit}") == "$commit" ]] || fail 'invalid source commit'
  git -C "$upstream" merge-base --is-ancestor "$commit" origin/main || fail 'source is not on Service main'

  branch=sync/service-contract
  remote_git fetch origin '+refs/heads/main:refs/remotes/origin/main'
  previous=$(git show origin/main:contract/source.json | jq -er .commit)
  if git -C "$upstream" merge-base --is-ancestor "$commit" "$previous"; then
    echo 'Source is already accepted or older than the accepted pin'
    return
  fi
  git -C "$upstream" merge-base --is-ancestor "$previous" "$commit" || fail 'source diverges from the accepted pin'

  # Only the latest lifecycle of this fixed branch matters. PR numbers increase.
  # REST's owner-qualified head filter plus the exact repository check excludes
  # fork PRs with the same branch name before selecting the latest lifecycle.
  prs=$(gh api --method GET --paginate "repos/$GITHUB_REPOSITORY/pulls" \
    -f state=all -f head="${GITHUB_REPOSITORY%%/*}:$branch" -f base=main \
    -f sort=created -f direction=desc -f per_page=100 | jq -s --arg repo "$GITHUB_REPOSITORY" '
      add | map(select(.head.repo.full_name == $repo)) | sort_by(.number) | reverse | .[:1]
      | map({number, headRefOid: .head.sha,
          state: (if .merged_at != null then "MERGED" else (.state | ascii_upcase) end)})')
  state=$(jq -r '.[0].state // ""' <<< "$prs")
  number=$(jq -r '.[0].number // ""' <<< "$prs")
  remote=$(remote_git ls-remote --heads origin "refs/heads/$branch")
  remote=${remote%%$'\t'*}
  retired=
  if [[ "$state" == CLOSED ]]; then
    echo "PR #$number was closed without merging; reopen it to resume automatic updates."
    return
  fi
  if [[ -n "$remote" ]]; then
    remote_git fetch origin "+refs/heads/$branch:refs/remotes/origin/$branch"
    remote=$(git rev-parse "origin/$branch")
    if [[ "$state" == MERGED && "$remote" == "$(jq -r '.[0].headRefOid' <<< "$prs")" ]]; then
      # Reuse the name after squash merge, but never discard later reviewer work.
      retired=$remote
      git switch --detach origin/main
    else
      git switch --detach "origin/$branch"
    fi
  else
    [[ "$state" != OPEN ]] || fail 'open PR branch is missing; restore it before retrying'
    git switch --detach origin/main
  fi

  current=$(jq -er .commit contract/source.json)
  if [[ "$commit" != "$current" ]] && git -C "$upstream" merge-base --is-ancestor "$commit" "$current"; then
    echo 'Ignoring an event older than the pending proposal'
    return
  fi
  git -C "$upstream" merge-base --is-ancestor "$current" "$commit" || fail 'source diverges from the pending pin'
  if [[ "$commit" != "$current" ]]; then
    # Incorporate accepted SDK fixes and retain the proposal's handwritten work.
    # Conflicts or generation failures stop before any remote branch mutation.
    bot_git merge --no-edit origin/main
    env -u GH_TOKEN bash scripts/sync-contract.sh "$upstream" "$commit"
    env -u GH_TOKEN make generate
    git add -A -- contract a13n/generated
    bot_git commit -m "chore(contract): update Service snapshot to $commit"
    if [[ "$state" == OPEN ]]; then
      live_pr=$(gh pr view "$number" --repo "$GITHUB_REPOSITORY" --json state,isDraft)
      [[ $(jq -r .state <<< "$live_pr") == OPEN ]] || fail 'PR was closed or merged during generation; inspect before retrying'
      if [[ $(jq -r .isDraft <<< "$live_pr") == false ]]; then
        gh pr ready "$number" --repo "$GITHUB_REPOSITORY" --undo
      fi
    fi
    if [[ -n "$retired" ]]; then
      # Delete only the exact, already-merged branch head; never force-update it.
      remote_git push --force-with-lease="refs/heads/$branch:$retired" origin ":refs/heads/$branch"
      remote=
    fi
    if [[ -z "$remote" ]]; then
      # An empty lease refuses to replace a concurrently created branch.
      remote_git push --force-with-lease="refs/heads/$branch:" origin "HEAD:refs/heads/$branch"
    else
      # Require both fast-forward ancestry and the exact observed remote head.
      # A plain push could recreate a branch deleted by a concurrent PR merge.
      git merge-base --is-ancestor "$remote" HEAD || fail 'proposal update is not a fast-forward'
      remote_git push --force-with-lease="refs/heads/$branch:$remote" origin "HEAD:refs/heads/$branch"
    fi
  fi

  # Reconcile metadata even on same-SHA retries after push/create/edit failures.
  # Only the marked source block is replaced; maintainer notes stay intact.
  start='<!-- service-contract:begin -->'
  end='<!-- service-contract:end -->'
  managed=$(cat <<EOF
$start
## Contract update

Pinned Service source: https://github.com/converge-ai-labs/agent-foundation/commit/$commit

Changes since the accepted SDK pin: https://github.com/converge-ai-labs/agent-foundation/compare/$previous...$commit

This rolling draft imports committed HTTP/wire definitions, shared fixtures, API conventions,
Native streaming semantics and queued-submission semantics, with source paths,
and includes SDK-local HTTP generation. Full SDK CI runs while this PR is still a draft.
The compare includes implementation changes even when exported schemas are unchanged.
It does not execute Service code or imply that this SDK already supports the new contract.
$end
EOF
)
  body=$(mktemp)
  trap 'rm -f "$body"' EXIT
  if [[ "$state" == OPEN ]]; then
    live_pr=$(gh pr view "$number" --repo "$GITHUB_REPOSITORY" --json state,body)
    [[ $(jq -r .state <<< "$live_pr") == OPEN ]] || fail 'PR was closed or merged during publication; inspect before retrying'
    old_body=$(jq -r .body <<< "$live_pr")
    [[ "$old_body" == *"$start"*"$end"* ]] || fail 'source markers are missing from PR body; restore them before retrying'
    printf '%s%s%s\n' "${old_body%%"$start"*}" "$managed" "${old_body#*"$end"}" > "$body"
    gh pr edit "$number" --repo "$GITHUB_REPOSITORY" \
      --title "chore(contract): update Service snapshot to ${commit:0:12}" --body-file "$body"
  else
    cat > "$body" <<EOF
$managed

## Maintainer acceptance

Review compatibility and non-HTTP behavior against the owning specifications, adapt handwritten
code/templates and protocol tests as needed, regenerate and run \`make check-all\`.
Resolve CI failures and review the latest source SHA before marking ready and merging.
New source updates return this PR to draft; keep review notes outside the marked source block.

A failed generation or incompatible change requires adaptation, not a silent contract downgrade.
No release, tag, auto-merge or package version change is requested by this automation.
EOF
    gh pr create --repo "$GITHUB_REPOSITORY" --base main --head "$branch" --draft \
      --title "chore(contract): update Service snapshot to ${commit:0:12}" --body-file "$body"
  fi
}

main "$@"
