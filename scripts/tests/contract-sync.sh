#!/usr/bin/env bash
# Offline integration tests shared by the language-local test runners.
set -euo pipefail
scripts=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT
upstream="$work/service"
sdk="$work/sdk"
mkdir -p "$upstream" "$sdk/scripts" "$sdk/contract/fixtures" "$work/bin"
cp "$scripts/sync-contract.sh" "$scripts/open-contract-pr.sh" "$sdk/scripts/"
git init -q -b main "$upstream"
git -C "$upstream" config user.name Test
git -C "$upstream" config user.email test@example.invalid
commit_source() {
  git -C "$upstream" add .
  git -C "$upstream" commit -qm "$1"
  git -C "$upstream" update-ref refs/remotes/origin/main HEAD
  git -C "$upstream" rev-parse HEAD
}
hash() { shasum -a 256 "$1" | cut -d ' ' -f 1; }
reject() {
  if "$@" > "$work/rejected.log" 2>&1; then
    echo "Expected failure: $*" >&2; exit 1
  fi
}
sync() { bash "$sdk/scripts/sync-contract.sh" "$upstream" "$1"; }
check() { bash "$sdk/scripts/sync-contract.sh" --check; }

mkdir -p "$upstream/proto/a13n-service/fixtures" "$upstream/spec/a13n-service" "$sdk/contract/semantics"
printf '{"openapi":"3.1.0","paths":{}}\n' > "$upstream/proto/a13n-service/openapi.json"
printf '{"examples":[]}\n' > "$upstream/proto/a13n-service/fixtures/wire.json"
for name in notification-client run-stream-event; do
  printf '{"type":"object"}\n' > "$upstream/proto/a13n-service/$name.schema.json"
done
printf '# API conventions\n' > "$upstream/spec/api-conventions.md"
printf '# Native streaming\n' > "$upstream/spec/a13n-service/21-native-streaming-and-notifications.md"
printf '# Queued submissions\nDELETE uses query expected_version and 204.\n' > "$upstream/spec/a13n-service/20-agent-control-queued-submissions.md"
initial=$(commit_source 'Initial Service contract')
jq -n --arg commit "$initial" '{repository:"converge-ai-labs/agent-foundation",commit:$commit,files:{}}' > "$sdk/contract/source.json"
while read -r name source; do
  cp "$upstream/$source" "$sdk/contract/$name"
  jq --arg name "$name" --arg source "$source" --arg hash "$(hash "$sdk/contract/$name")" \
    '.files[$name] = {source_path:$source,sha256:$hash}' "$sdk/contract/source.json" > "$work/manifest"
  cp "$work/manifest" "$sdk/contract/source.json"
done <<'FILES'
openapi.json proto/a13n-service/openapi.json
fixtures/wire.json proto/a13n-service/fixtures/wire.json
notification-client.schema.json proto/a13n-service/notification-client.schema.json
run-stream-event.schema.json proto/a13n-service/run-stream-event.schema.json
semantics/api-conventions.md spec/api-conventions.md
semantics/native-streaming-and-notifications.md spec/a13n-service/21-native-streaming-and-notifications.md
semantics/queued-submissions.md spec/a13n-service/20-agent-control-queued-submissions.md
FILES
check
cp -R "$sdk/contract" "$work/initial"
reject sync main
reject sync "${initial:0:12}"
reject sync '$(touch unsafe)'
reject sync 0000000000000000000000000000000000000000
sync "$initial"
diff -r "$sdk/contract" "$work/initial"

rm "$upstream/spec/a13n-service/20-agent-control-queued-submissions.md"
missing=$(commit_source 'Incomplete authority')
reject sync "$missing"
diff -r "$sdk/contract" "$work/initial"
printf '# Queued submissions\nDELETE uses query expected_version and204.\n' > "$upstream/spec/a13n-service/20-agent-control-queued-submissions.md"
complete=$(commit_source 'Complete authority')
# The working tree is deliberately dirty: only committed bytes may be imported.
printf 'uncommitted and invalid JSON' > "$upstream/proto/a13n-service/openapi.json"
sync "$complete"
check
[[ $(jq '.files | length' "$sdk/contract/source.json") == 7 ]]
cmp "$sdk/contract/openapi.json" "$work/initial/openapi.json"
[[ $(jq -r .commit "$sdk/contract/source.json") == "$complete" ]]
cp -R "$sdk/contract" "$work/complete"
reject sync "$initial"
diff -r "$sdk/contract" "$work/complete"
git -C "$upstream" restore proto/a13n-service/openapi.json

printf '# API conventions changed without changing HTTP schemas\n' > "$upstream/spec/api-conventions.md"
semantic=$(commit_source 'Semantic-only update')
sync "$semantic"
cmp "$sdk/contract/openapi.json" "$work/complete/openapi.json"
! cmp -s "$sdk/contract/semantics/api-conventions.md" "$work/complete/semantics/api-conventions.md"
printf '# Runtime-only change\n' > "$upstream/runtime.txt"
runtime=$(commit_source 'Runtime-only update')
sync "$runtime"
[[ $(jq -r .commit "$sdk/contract/source.json") == "$runtime" ]]
cp -R "$sdk/contract" "$work/current"

# A valid object on another branch is not an acceptable main-line source.
git -C "$upstream" switch -qc other
printf 'Unmerged\n' > "$upstream/runtime.txt"
git -C "$upstream" commit -qam Unmerged
unmerged=$(git -C "$upstream" rev-parse HEAD)
reject sync "$unmerged"
git -C "$upstream" switch -q main
printf 'invalid' > "$upstream/proto/a13n-service/run-stream-event.schema.json"
invalid=$(commit_source 'Malformed wire schema')
reject sync "$invalid"
diff -r "$sdk/contract" "$work/current"

# Local hashes and actual upstream provenance are both required.
printf 'tampered' >> "$sdk/contract/semantics/api-conventions.md"
reject check
jq --arg hash "$(hash "$sdk/contract/semantics/api-conventions.md")" '.files["semantics/api-conventions.md"].sha256 = $hash' \
  "$sdk/contract/source.json" > "$work/manifest"
cp "$work/manifest" "$sdk/contract/source.json"
check
reject sync "$runtime"
cp "$work/current/source.json" "$sdk/contract/"
cp "$work/current/semantics/api-conventions.md" "$sdk/contract/semantics/"
printf 'unrecorded evidence' > "$sdk/contract/unrecorded.md"
reject check
rm "$sdk/contract/unrecorded.md"
jq 'del(.files["semantics/api-conventions.md"])' "$sdk/contract/source.json" > "$work/manifest"
cp "$work/manifest" "$sdk/contract/source.json"
reject check
cp "$work/current/source.json" "$sdk/contract/"
check

# PR operations use only local bare Git and a fake gh; never a real API/token.
git init -q -b main "$sdk"
git -C "$sdk" config user.name Test
git -C "$sdk" config user.email test@example.invalid
cp "$work/complete/source.json" "$sdk/contract/"
cp "$work/complete/semantics/api-conventions.md" "$sdk/contract/semantics/"
git -C "$sdk" add .
git -C "$sdk" commit -qm 'Accepted snapshot'
git init -q --bare "$work/remote.git"
git -C "$sdk" remote add origin "$work/remote.git"
git -C "$sdk" push -q origin main
cp "$work/current/source.json" "$sdk/contract/"
cp "$work/current/semantics/api-conventions.md" "$sdk/contract/semantics/"
cat > "$work/bin/gh" <<'GH'
#!/usr/bin/env bash
set -euo pipefail
if [[ "$1 $2" == 'pr list' ]]; then
  printf '%s\n' "${TEST_PRS:-[]}"
elif [[ "$1 $2" == 'pr create' ]]; then
  [[ " $* " == *' --draft '* && " $* " == *' --base main '* ]]
  echo created >> "$TEST_PR_LOG"
  if [[ ${TEST_CREATE_FAIL:-false} == true ]]; then exit 1; fi
else
  echo "Unexpected gh call: $*" >&2; exit 1
fi
GH
chmod +x "$work/bin/gh"
export PATH="$work/bin:$PATH" TEST_PR_LOG="$work/pr.log" GITHUB_REPOSITORY=converge-ai-labs/a13n-sdk-test
export TEST_CREATE_FAIL=true
reject bash "$sdk/scripts/open-contract-pr.sh"
branch="sync/service-contract-$runtime"
first_head=$(git --git-dir="$work/remote.git" rev-parse "refs/heads/$branch")
# Retry from a fresh main checkout after push succeeded but PR creation failed.
git -C "$sdk" switch -q main
cp "$work/current/source.json" "$sdk/contract/"
cp "$work/current/semantics/api-conventions.md" "$sdk/contract/semantics/"
export TEST_CREATE_FAIL=false
bash "$sdk/scripts/open-contract-pr.sh"
[[ $(git --git-dir="$work/remote.git" rev-parse "refs/heads/$branch") == "$first_head" ]]
[[ $(wc -l < "$TEST_PR_LOG" | tr -d ' ') == 2 ]]
export TEST_PRS='[{"number":1}]'
bash "$sdk/scripts/open-contract-pr.sh"
[[ $(wc -l < "$TEST_PR_LOG" | tr -d ' ') == 2 ]]
[[ $(git --git-dir="$work/remote.git" rev-parse "refs/heads/$branch") == "$first_head" ]]
[[ -z $(git --git-dir="$work/remote.git" tag -l) ]]
# Execute the workflow's actual input-validation block with synthetic event files.
awk '/^        run: \|$/ {capture=1; next} capture && /^$/ {exit} capture {print substr($0,11)}' \
  "$scripts/../.github/workflows/sync-service-contract.yml" > "$work/read-event.sh"
[[ -s "$work/read-event.sh" ]]
export EVENT_NAME=repository_dispatch GITHUB_EVENT_PATH="$work/event.json" GITHUB_OUTPUT="$work/output"
export GITHUB_SHA="$initial" MANUAL_SHA="$initial"
jq -n --arg sha "$runtime" '{client_payload:{repository:"converge-ai-labs/agent-foundation",commit:$sha}}' > "$GITHUB_EVENT_PATH"
bash -euo pipefail "$work/read-event.sh"
[[ $(cat "$GITHUB_OUTPUT") == "sha=$runtime" ]]
jq '.client_payload.repository = "other/source"' "$GITHUB_EVENT_PATH" > "$work/event-invalid.json"
export GITHUB_EVENT_PATH="$work/event-invalid.json"
reject bash -euo pipefail "$work/read-event.sh"
export EVENT_NAME=workflow_dispatch MANUAL_SHA=main
reject bash -euo pipefail "$work/read-event.sh"
export MANUAL_SHA="$runtime"
bash -euo pipefail "$work/read-event.sh"
[[ $(wc -l < "$GITHUB_OUTPUT" | tr -d ' ') == 2 ]]
echo 'Contract sync integration checks passed (offline Git and fake GitHub only).'
