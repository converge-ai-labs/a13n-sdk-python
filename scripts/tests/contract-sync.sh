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
    cat "$work/rejected.log" >&2
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

# PR operations use only local bare Git and fake gh/make; never a real API/token.
# Language-specific generated ownership; the remainder of this suite is shared.
export TEST_GENERATED=a13n/generated/current.py TEST_ADDED=a13n/generated/new.py TEST_REMOVED=a13n/generated/obsolete.py
mkdir -p "$sdk/$(dirname "$TEST_GENERATED")" "$sdk/$(dirname "$TEST_ADDED")"
cp "$sdk/contract/openapi.json" "$sdk/$TEST_GENERATED"
if [[ -n "$TEST_REMOVED" ]]; then
  echo obsolete > "$sdk/$TEST_REMOVED"
else
  cp "$sdk/contract/openapi.json" "$sdk/$TEST_ADDED"
fi
printf 'handwritten\n' > "$sdk/handwritten.txt"
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
cat > "$work/bin/make" <<'MAKE'
#!/usr/bin/env bash
set -euo pipefail
[[ "$*" == generate && -z ${GH_TOKEN:-} ]]
echo generate >> "$TEST_GENERATE_LOG"
# Simulate partial writes and unrelated build/handwritten changes before failure.
printf 'partial output\n' > "$TEST_GENERATED"
printf 'not a generated file\n' > handwritten.txt
printf 'untracked build output\n' > unexpected.txt
if [[ ${TEST_GENERATE_FAIL:-false} != false ]]; then exit 1; fi
cp contract/openapi.json "$TEST_GENERATED"
if [[ $(jq '.paths | length' contract/openapi.json) != 0 ]]; then
  cp contract/openapi.json "$TEST_ADDED"
  if [[ -n "$TEST_REMOVED" ]]; then rm -f "$TEST_REMOVED"; fi
elif [[ -z "$TEST_REMOVED" ]]; then
  cp contract/openapi.json "$TEST_ADDED"
fi
MAKE
chmod +x "$work/bin/make"
cat > "$work/bin/gh" <<'GH'
#!/usr/bin/env bash
set -euo pipefail
if [[ "$1 $2" == 'pr list' ]]; then
  [[ " $* " == *' --state all '* ]]
  printf '%s\n' "${TEST_PRS:-[]}"
elif [[ "$1 $2" == 'pr create' ]]; then
  [[ " $* " == *' --draft '* && " $* " == *' --base main '* ]]
  while [[ "$1" != --body-file ]]; do shift; done
  grep -q 'Full SDK CI runs while this PR is still a draft' "$2"
  echo created >> "$TEST_PR_LOG"
  if [[ ${TEST_CREATE_FAIL:-false} == true ]]; then exit 1; fi
else
  echo "Unexpected gh call: $*" >&2; exit 1
fi
GH
chmod +x "$work/bin/gh"
export PATH="$work/bin:$PATH" TEST_PR_LOG="$work/pr.log" GITHUB_REPOSITORY=converge-ai-labs/a13n-sdk-test
export TEST_GENERATE_LOG="$work/generate.log" GH_TOKEN=not-a-real-token
: > "$TEST_GENERATE_LOG"
: > "$TEST_PR_LOG"
# An accepted pin is a no-op, even if generation would fail.
export TEST_GENERATE_FAIL=true
bash "$sdk/scripts/open-contract-pr.sh"
[[ ! -s "$TEST_GENERATE_LOG" && ! -s "$TEST_PR_LOG" ]]

# A semantic/runtime-only update still creates a reviewable pin update.
cp "$work/current/source.json" "$sdk/contract/"
cp "$work/current/semantics/api-conventions.md" "$sdk/contract/semantics/"
export TEST_GENERATE_FAIL=false
bash "$sdk/scripts/open-contract-pr.sh"
[[ -z $(git -C "$sdk" diff main HEAD -- "$TEST_GENERATED" "$TEST_ADDED") ]]
[[ $(git -C "$sdk" show HEAD:contract/source.json | jq -r .commit) == "$runtime" ]]
[[ $(git -C "$sdk" show HEAD:handwritten.txt) == handwritten ]]
! git -C "$sdk" cat-file -e HEAD:unexpected.txt 2>/dev/null

# Fresh ephemeral checkout and a real input change (generation is stubbed here).
git -C "$sdk" reset --hard -q
git -C "$sdk" switch -q main
git -C "$sdk" clean -fdq
cp "$work/initial/run-stream-event.schema.json" "$upstream/proto/a13n-service/run-stream-event.schema.json"
jq '.paths["/api/v1/probe"] = {get:{operationId:"probe",responses:{"204":{description:"No content"}}}}' \
  "$upstream/proto/a13n-service/openapi.json" > "$work/http.json"
cp "$work/http.json" "$upstream/proto/a13n-service/openapi.json"
http=$(commit_source 'HTTP operation added')
sync "$http"
branch="sync/service-contract-$http"
base=$(git -C "$sdk" rev-parse HEAD)
export TEST_GENERATE_FAIL=true
reject bash "$sdk/scripts/open-contract-pr.sh"
[[ $(git -C "$sdk" rev-parse HEAD) == "$base" ]]
[[ -z $(git -C "$sdk" diff --cached) ]]
[[ $(cat "$sdk/$TEST_GENERATED") == 'partial output' ]]
! git --git-dir="$work/remote.git" show-ref --verify --quiet "refs/heads/$branch"
[[ $(wc -l < "$TEST_PR_LOG" | tr -d ' ') == 1 ]]

# Retry succeeds; the commit includes generated changes/deletions, not other files.
export TEST_GENERATE_FAIL=false TEST_CREATE_FAIL=true
reject bash "$sdk/scripts/open-contract-pr.sh"
first_head=$(git --git-dir="$work/remote.git" rev-parse "refs/heads/$branch")
[[ $(git -C "$sdk" show HEAD:contract/source.json | jq -r .commit) == "$http" ]]
for output in "$TEST_GENERATED" "$TEST_ADDED"; do
  git -C "$sdk" show "HEAD:$output" > "$work/actual"
  cmp "$work/actual" "$work/http.json"
done
if [[ -n "$TEST_REMOVED" ]]; then ! git -C "$sdk" cat-file -e "HEAD:$TEST_REMOVED" 2>/dev/null; fi
[[ $(git -C "$sdk" show HEAD:handwritten.txt) == handwritten ]]
! git -C "$sdk" cat-file -e HEAD:unexpected.txt 2>/dev/null

# Reviewer edits survive a retry after push succeeded but PR creation failed.
printf 'reviewer adaptation\n' > "$sdk/$TEST_GENERATED"
git -C "$sdk" add -- "$TEST_GENERATED"
git -C "$sdk" commit -qm 'Reviewer adaptation'
git -C "$sdk" push -q origin "HEAD:refs/heads/$branch"
reviewed_head=$(git --git-dir="$work/remote.git" rev-parse "refs/heads/$branch")
[[ "$reviewed_head" != "$first_head" ]]
git -C "$sdk" reset --hard -q
git -C "$sdk" switch -q main
git -C "$sdk" clean -fdq
sync "$http"
export TEST_CREATE_FAIL=false TEST_GENERATE_FAIL=true
before=$(wc -l < "$TEST_GENERATE_LOG")
bash "$sdk/scripts/open-contract-pr.sh"
[[ $(wc -l < "$TEST_GENERATE_LOG") == "$before" ]]
[[ $(git --git-dir="$work/remote.git" rev-parse "refs/heads/$branch") == "$reviewed_head" ]]
[[ $(wc -l < "$TEST_PR_LOG" | tr -d ' ') == 3 ]]
export TEST_PRS='[{"number":1}]'
bash "$sdk/scripts/open-contract-pr.sh"
[[ $(wc -l < "$TEST_GENERATE_LOG") == "$before" ]]
[[ $(wc -l < "$TEST_PR_LOG" | tr -d ' ') == 3 ]]
[[ $(git --git-dir="$work/remote.git" rev-parse "refs/heads/$branch") == "$reviewed_head" ]]
[[ -z $(git --git-dir="$work/remote.git" tag -l) ]]

# Drafts use the same complete CI gate; no draft-specific condition may skip it.
ci="$scripts/../.github/workflows/ci.yml"
grep -q 'types: \[opened, synchronize, reopened, ready_for_review\]' "$ci"
grep -q 'run: make check-all' "$ci"
! grep -q 'if:.*draft' "$ci"
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
