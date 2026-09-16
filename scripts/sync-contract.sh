#!/usr/bin/env bash
# Copy committed Service evidence only. Never execute code from the source checkout.
set -euo pipefail
root=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
cd "$root"
fail() { echo "Contract sync: $*" >&2; exit 1; }
sha256() { shasum -a 256 "$1" | cut -d ' ' -f 1; }
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

check_snapshot() {
  jq -e --arg repository "$repository" --argjson files "$files" '
    .repository == $repository and (.commit | type == "string" and test("^[0-9a-f]{40}$"))
    and (.files | type == "object")
    and (.files | map_values(.source_path)) == $files
    and all(.files[]; .sha256 | type == "string" and test("^[0-9a-f]{64}$"))
  ' contract/source.json >/dev/null || fail 'invalid source manifest or incomplete file set'
  # Do not silently discard unrecorded evidence, including Markdown and symlinks.
  [[ -z $(find contract -type l -print) ]] || fail 'snapshot contains a symlink'
  actual=$(find contract -type f ! -path contract/source.json ! -path contract/README.md | sed 's|^contract/||' | LC_ALL=C sort)
  expected=$(jq -r '.files | keys[]' contract/source.json | LC_ALL=C sort)
  [[ "$actual" == "$expected" ]] || fail 'snapshot file set differs from source manifest'
  while IFS=$'\t' read -r name hash; do
    [[ $(sha256 "contract/$name") == "$hash" ]] || fail "hash mismatch: $name"
    if [[ "$name" == *.json ]]; then
      jq -e 'type == "object"' "contract/$name" >/dev/null || fail "invalid JSON object: $name"
    fi
  done < <(jq -r '.files | to_entries[] | [.key, .value.sha256] | @tsv' contract/source.json)
}

if [[ ${1:-} == --check && $# == 1 ]]; then
  check_snapshot
  exit 0
fi
[[ $# == 2 ]] || fail 'usage: bash scripts/sync-contract.sh SERVICE_CHECKOUT FULL_SHA | --check'
upstream=$(cd "$1" && pwd)
commit=$2
[[ "$commit" =~ ^[0-9a-f]{40}$ ]] || fail 'a complete lowercase 40-character commit SHA is required'
check_snapshot
previous=$(jq -r .commit contract/source.json)
[[ $(git -C "$upstream" rev-parse "$commit^{commit}") == "$commit" ]] || fail 'source is not the requested commit'
git -C "$upstream" merge-base --is-ancestor "$commit" refs/remotes/origin/main || fail 'source commit is not on origin/main'
git -C "$upstream" merge-base --is-ancestor "$previous" "$commit" || fail 'source would rewind or diverge from the existing pin'

stage=$(mktemp -d)
trap 'rm -rf "$stage"' EXIT
# Verify the old provenance against Git, not just against self-declared hashes.
while IFS=$'\t' read -r name source_path; do
  git -C "$upstream" show "$previous:$source_path" > "$stage/previous"
  cmp -s "$stage/previous" "contract/$name" || fail "existing provenance does not match Service Git: $name"
done < <(jq -r '.files | to_entries[] | [.key, .value.source_path] | @tsv' contract/source.json)
if [[ "$previous" == "$commit" ]]; then
  echo "Contract already pinned to $commit"
  exit 0
fi

# Resolve and validate every input before modifying the SDK working tree.
jq -n --arg repository "$repository" --arg commit "$commit" '{repository:$repository, commit:$commit, files:{}}' > "$stage/source.json"
while IFS=$'\t' read -r name source_path; do
  mkdir -p "$stage/$(dirname "$name")"
  [[ $(git -C "$upstream" cat-file -t "$commit:$source_path") == blob ]] || fail "missing source blob: $source_path"
  git -C "$upstream" show "$commit:$source_path" > "$stage/$name"
  if [[ "$name" == *.json ]]; then
    jq -e 'type == "object"' "$stage/$name" >/dev/null || fail "invalid source JSON: $source_path"
  fi
  jq --arg name "$name" --arg source_path "$source_path" --arg hash "$(sha256 "$stage/$name")" \
    '.files[$name] = {source_path:$source_path, sha256:$hash}' "$stage/source.json" > "$stage/next.json"
  mv "$stage/next.json" "$stage/source.json"
done < <(jq -nr --argjson files "$files" '$files | to_entries[] | [.key, .value] | @tsv')

while IFS= read -r name; do
  mkdir -p "contract/$(dirname "$name")"
  cp "$stage/$name" "contract/$name"
done < <(jq -r '.files | keys[]' "$stage/source.json")
cp "$stage/source.json" contract/source.json
check_snapshot
echo "Pinned Service contract to $commit; run make generate and make check-all before accepting it."
