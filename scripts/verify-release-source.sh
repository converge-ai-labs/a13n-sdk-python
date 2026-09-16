#!/usr/bin/env bash
# Read-only prerequisite check. Release jobs do not repeat CI or wait for it.
set -euo pipefail
: "${GITHUB_REPOSITORY:?GITHUB_REPOSITORY is required}"
commit="$(git rev-parse HEAD)"
git merge-base --is-ancestor "$commit" refs/remotes/origin/main || {
  echo 'Release commit must be on origin/main' >&2
  exit 1
}
# Query the owned workflow, not a mutable check name supplied by another app.
runs="$(gh api --paginate --slurp "repos/$GITHUB_REPOSITORY/actions/workflows/ci.yml/runs?head_sha=$commit&branch=main&event=push&per_page=100")"
printf '%s' "$runs" | jq -e --arg commit "$commit" '
  [.[].workflow_runs[] | select(.head_sha == $commit and .head_branch == "main" and .event == "push")]
  | sort_by([.run_number, .run_attempt]) | last
  | .status == "completed" and .conclusion == "success"
' >/dev/null || {
  echo "Latest main SDK CI run for $commit must have succeeded; rerun release after CI completes" >&2
  exit 1
}
echo "Verified main SDK CI for $commit"
