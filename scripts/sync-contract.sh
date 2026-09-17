#!/usr/bin/env bash
# Copy committed Service evidence only. Never execute code from the source checkout.
set -euo pipefail
root=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
cd "$root"
fail() { echo "Contract sync: $*" >&2; exit 1; }
repository=converge-ai-labs/agent-foundation
files='{
  "openapi.json": "proto/a13n-service/openapi.json",
  "notification-client.schema.json": "proto/a13n-service/notification-client.schema.json",
  "run-stream-event.schema.json": "proto/a13n-service/run-stream-event.schema.json",
  "fixtures/wire.json": "proto/a13n-service/fixtures/wire.json",
  "semantics/api-conventions.md": "spec/api-conventions.md",
  "semantics/native-streaming-and-notifications.md": "spec/a13n-service/21-native-streaming-and-notifications.md",
  "semantics/queued-submissions.md": "spec/a13n-service/20-agent-control-queued-submissions.md"
}'

[[ $# == 2 ]] || fail 'usage: bash scripts/sync-contract.sh SERVICE_CHECKOUT FULL_SHA'
upstream=$(cd "$1" && pwd)
commit=$2
[[ "$commit" =~ ^[0-9a-f]{40}$ ]] || fail 'a complete lowercase 40-character commit SHA is required'
previous=$(jq -er .commit contract/source.json)
[[ $(git -C "$upstream" rev-parse "$commit^{commit}") == "$commit" ]] || fail 'source is not the requested commit'
git -C "$upstream" merge-base --is-ancestor "$commit" refs/remotes/origin/main || fail 'source commit is not on origin/main'
git -C "$upstream" merge-base --is-ancestor "$previous" "$commit" || fail 'source would rewind or diverge from the existing pin'

if [[ "$previous" == "$commit" ]]; then
  echo "Contract already pinned to $commit"
  exit 0
fi

# Stage the new inputs before modifying the SDK working tree.
stage=$(mktemp -d)
trap 'rm -rf "$stage"' EXIT
jq -n --arg repository "$repository" --arg commit "$commit" '{repository:$repository, commit:$commit, files:{}}' > "$stage/source.json"
while IFS=$'\t' read -r name source_path; do
  mkdir -p "$stage/$(dirname "$name")"
  git -C "$upstream" show "$commit:$source_path" > "$stage/$name"
  if [[ "$name" == *.json ]]; then
    jq -e 'type == "object"' "$stage/$name" >/dev/null || fail "invalid source JSON: $source_path"
  fi
  jq --arg name "$name" --arg source_path "$source_path" \
    '.files[$name] = {source_path:$source_path}' "$stage/source.json" > "$stage/next.json"
  mv "$stage/next.json" "$stage/source.json"
done < <(jq -nr --argjson files "$files" '$files | to_entries[] | [.key, .value] | @tsv')

while IFS= read -r name; do
  mkdir -p "contract/$(dirname "$name")"
  cp "$stage/$name" "contract/$name"
done < <(jq -r '.files | keys[]' "$stage/source.json")
cp "$stage/source.json" contract/source.json
echo "Pinned Service contract to $commit; run make generate and make check-all before accepting it."
