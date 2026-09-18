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
reject() {
  if "$@" > "$work/rejected.log" 2>&1; then
    cat "$work/rejected.log" >&2
    echo "Expected failure: $*" >&2; exit 1
  fi
}
sync() { bash "$sdk/scripts/sync-contract.sh" "$upstream" "$1"; }

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
  jq --arg name "$name" --arg source "$source" \
    '.files[$name] = {source_path:$source}' "$sdk/contract/source.json" > "$work/manifest"
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
printf 'initial generator dependency\n' > "$sdk/generator-dependency.txt"
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
[[ -z ${GH_TOKEN:-} ]]
if [[ "$*" == install ]]; then
  cp generator-dependency.txt "$TEST_INSTALLED"
  exit 0
fi
[[ "$*" == generate ]]
if [[ ${TEST_NEEDS_INSTALL:-false} == true ]]; then
  cmp generator-dependency.txt "$TEST_INSTALLED"
fi
echo generate >> "$TEST_GENERATE_LOG"
if [[ ${TEST_CONCURRENT:-false} == true ]]; then
  git clone -q --branch sync/service-contract "$TEST_REMOTE" "$TEST_RACE_DIR"
  git -C "$TEST_RACE_DIR" config user.name Reviewer
  git -C "$TEST_RACE_DIR" config user.email reviewer@example.invalid
  echo concurrent > "$TEST_RACE_DIR/concurrent.txt"
  git -C "$TEST_RACE_DIR" add concurrent.txt
  git -C "$TEST_RACE_DIR" commit -qm 'Concurrent reviewer work'
  git -C "$TEST_RACE_DIR" push -q origin HEAD
fi
if [[ ${TEST_PR_RACE:-} == notes ]]; then
  jq '.[0].body += "\nNotes added during generation.\n"' "$TEST_PR_STATE" > "$TEST_PR_STATE.next"
  mv "$TEST_PR_STATE.next" "$TEST_PR_STATE"
elif [[ ${TEST_PR_RACE:-} == close ]]; then
  jq '.[0].state = "CLOSED"' "$TEST_PR_STATE" > "$TEST_PR_STATE.next"
  mv "$TEST_PR_STATE.next" "$TEST_PR_STATE"
elif [[ ${TEST_PR_RACE:-} == delete ]]; then
  git --git-dir="$TEST_REMOTE" update-ref -d refs/heads/sync/service-contract
fi
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
operation=$2
if [[ "$1" == api ]]; then
  [[ " $* " == *' --paginate '* && " $* " == *' head=converge-ai-labs:sync/service-contract '* ]]
  if [[ -s "$TEST_PR_STATE" ]]; then
    jq --arg repo "$GITHUB_REPOSITORY" \
      --arg head "$(git --git-dir="$TEST_REMOTE" rev-parse refs/heads/sync/service-contract 2>/dev/null || true)" '
      map({number, state: (.state | ascii_downcase),
        merged_at: (if .state == "MERGED" then "2026-09-17" else null end),
        head: {repo: {full_name: $repo}, sha: (if .state == "OPEN" then $head else .headRefOid end)}})
      + [{number:999, state:"closed", merged_at:null, head:{repo:{full_name:"fork/sdk"},sha:$head}}]
      ' "$TEST_PR_STATE"
  else
    echo '[]'
  fi
elif [[ "$1 $2" == 'pr view' ]]; then
  jq '.[0]' "$TEST_PR_STATE"
elif [[ "$1" == pr && ( "$operation" == create || "$operation" == edit ) ]]; then
  if [[ "$operation" == create ]]; then
    [[ " $* " == *' --draft '* && " $* " == *' --base main '* ]]
  fi
  while [[ "$1" != --body-file ]]; do shift; done
  grep -q 'Full SDK CI runs while this PR is still a draft' "$2"
  echo "$operation" >> "$TEST_PR_LOG"
  if [[ ${TEST_METADATA_FAIL:-false} == true ]]; then exit 1; fi
  if [[ "$operation" == create ]]; then
    jq -n --rawfile body "$2" '[{number:1,state:"OPEN",body:$body,isDraft:true}]' > "$TEST_PR_STATE"
  else
    jq --rawfile body "$2" '.[0].body = $body' "$TEST_PR_STATE" > "$TEST_PR_STATE.next"
    mv "$TEST_PR_STATE.next" "$TEST_PR_STATE"
  fi
elif [[ "$1 $2" == 'pr ready' ]]; then
  [[ " $* " == *' --undo '* ]]
  jq '.[0].isDraft = true' "$TEST_PR_STATE" > "$TEST_PR_STATE.next"
  mv "$TEST_PR_STATE.next" "$TEST_PR_STATE"
else
  echo "Unexpected gh call: $*" >&2; exit 1
fi
GH
chmod +x "$work/bin/gh"
export PATH="$work/bin:$PATH" TEST_PR_LOG="$work/pr.log" GITHUB_REPOSITORY=converge-ai-labs/a13n-sdk-test
export TEST_PR_STATE="$work/pr-state.json" TEST_REMOTE="$work/remote.git"
export TEST_GENERATE_LOG="$work/generate.log" GH_TOKEN=not-a-real-token
export TEST_INSTALLED="$work/installed-dependency"
: > "$TEST_GENERATE_LOG"
: > "$TEST_PR_LOG"
branch=sync/service-contract
propose() { bash "$sdk/scripts/open-contract-pr.sh" "$upstream" "$1"; }
head() { git --git-dir="$TEST_REMOTE" rev-parse "refs/heads/$branch"; }
fresh() {
  # Only disposable test checkouts are reset; production requires a clean tree.
  git -C "$sdk" reset --hard -q
  git -C "$sdk" switch --detach -q main
  git -C "$sdk" clean -fdq
}
set_pr() {
  jq "$1" "$TEST_PR_STATE" > "$work/pr-next.json"
  mv "$work/pr-next.json" "$TEST_PR_STATE"
}
next_source() {
  printf '%s\n' "$1" >> "$upstream/runtime.txt"
  commit_source "$1"
}
# An accepted pin is a no-op, even if generation would fail.
export TEST_GENERATE_FAIL=true
propose "$complete"
[[ ! -s "$TEST_GENERATE_LOG" && ! -s "$TEST_PR_LOG" ]]
reject propose main
reject propose "$unmerged"
printf dirty > "$sdk/dirty.txt"
reject propose "$runtime"
rm "$sdk/dirty.txt"

# A semantic/runtime-only update still creates a reviewable pin update.
export TEST_GENERATE_FAIL=false
propose "$runtime"
[[ -z $(git -C "$sdk" diff main HEAD -- "$TEST_GENERATED" "$TEST_ADDED") ]]
[[ $(git -C "$sdk" show HEAD:contract/source.json | jq -r .commit) == "$runtime" ]]
[[ $(git -C "$sdk" show HEAD:handwritten.txt) == handwritten ]]
! git -C "$sdk" cat-file -e HEAD:unexpected.txt 2>/dev/null
first_head=$(head)

# A real HTTP input change fails without altering the existing remote proposal.
fresh
cp "$work/initial/run-stream-event.schema.json" "$upstream/proto/a13n-service/run-stream-event.schema.json"
jq '.paths["/api/v1/probe"] = {get:{operationId:"probe",responses:{"204":{description:"No content"}}}}' \
  "$upstream/proto/a13n-service/openapi.json" > "$work/http.json"
cp "$work/http.json" "$upstream/proto/a13n-service/openapi.json"
http=$(commit_source 'HTTP operation added')
export TEST_GENERATE_FAIL=true
reject propose "$http"
[[ $(head) == "$first_head" ]]
[[ -z $(git -C "$sdk" diff --cached) ]]
[[ $(cat "$sdk/$TEST_GENERATED") == 'partial output' ]]
[[ $(grep -c create "$TEST_PR_LOG") == 1 ]]

# Retry advances the same branch; failed metadata reconciliation is recoverable.
fresh
export TEST_GENERATE_FAIL=false TEST_METADATA_FAIL=true
reject propose "$http"
http_head=$(head)
[[ "$http_head" != "$first_head" ]]
git -C "$sdk" merge-base --is-ancestor "$first_head" "$http_head"
for output in "$TEST_GENERATED" "$TEST_ADDED"; do
  git -C "$sdk" show "HEAD:$output" > "$work/actual"
  cmp "$work/actual" "$work/http.json"
done
if [[ -n "$TEST_REMOVED" ]]; then ! git -C "$sdk" cat-file -e "HEAD:$TEST_REMOVED" 2>/dev/null; fi
[[ $(git -C "$sdk" show HEAD:handwritten.txt) == handwritten ]]
! git -C "$sdk" cat-file -e HEAD:unexpected.txt 2>/dev/null
fresh
export TEST_METADATA_FAIL=false TEST_GENERATE_FAIL=true
before=$(wc -l < "$TEST_GENERATE_LOG")
propose "$http"
[[ $(wc -l < "$TEST_GENERATE_LOG") == "$before" && $(head) == "$http_head" ]]
jq -e --arg sha "$http" '.[0].body | contains($sha)' "$TEST_PR_STATE" >/dev/null

# Old events cannot rewind an unmerged newer proposal. Same-SHA retries preserve
# reviewer commits, notes, and readiness rather than regenerating their changes.
fresh
propose "$runtime"
[[ $(head) == "$http_head" ]]
git -C "$sdk" switch --detach -q "$http_head"
printf 'reviewer adaptation\n' > "$sdk/$TEST_GENERATED"
printf 'reviewer handwritten adaptation\n' > "$sdk/handwritten.txt"
printf 'updated generator dependency\n' > "$sdk/generator-dependency.txt"
git -C "$sdk" add -- "$TEST_GENERATED" handwritten.txt generator-dependency.txt
git -C "$sdk" commit -qm 'Reviewer adaptation'
git -C "$sdk" push -q origin "HEAD:refs/heads/$branch"
reviewed_head=$(head)
set_pr '.[0].body += "\nMaintainer notes: keep this context.\n" | .[0].isDraft = false'
fresh
propose "$http"
[[ $(head) == "$reviewed_head" && $(wc -l < "$TEST_GENERATE_LOG") == "$before" ]]
[[ $(jq -r '.[0].isDraft' "$TEST_PR_STATE") == false ]]
grep -q 'Maintainer notes' "$TEST_PR_STATE"

# SDK main can advance while a proposal is open. Merge its fixes, preserve
# handwritten adaptation, and return a genuinely newer source revision to draft.
fresh
git -C "$sdk" switch -q main
printf 'accepted SDK fix\n' > "$sdk/sdk-fix.txt"
git -C "$sdk" add sdk-fix.txt
git -C "$sdk" commit -qm 'SDK main fix'
git -C "$sdk" push -q origin main
newer=$(next_source 'Newer runtime')
export TEST_GENERATE_FAIL=false TEST_PR_RACE=notes
propose "$newer"
unset TEST_PR_RACE
grep -q 'Notes added during generation' "$TEST_PR_STATE"
[[ $(git -C "$sdk" show HEAD:handwritten.txt) == 'reviewer handwritten adaptation' ]]
[[ $(git -C "$sdk" show HEAD:sdk-fix.txt) == 'accepted SDK fix' ]]
git -C "$sdk" merge-base --is-ancestor "$reviewed_head" HEAD
[[ $(jq -r '.[0].isDraft' "$TEST_PR_STATE") == true ]]
[[ $(grep -c create "$TEST_PR_LOG") == 1 ]]
grep -q 'Maintainer notes' "$TEST_PR_STATE"

# Closing is an explicit pause, not permission to recreate the same proposal.
fresh
set_pr '.[0].state = "CLOSED"'
closed_head=$(head)
after_closed=$(next_source 'After closure')
propose "$after_closed"
[[ $(head) == "$closed_head" ]]
set_pr '.[0].state = "OPEN"'
propose "$after_closed"

# Squash merge and automatic branch deletion start a new cycle from SDK main.
fresh
git -C "$sdk" fetch -q origin "$branch"
merged_head=$(head)
git -C "$sdk" switch -q main
git -C "$sdk" merge --squash "$merged_head"
git -C "$sdk" commit -qm 'Accept contract'
git -C "$sdk" push -q origin main
set_pr ".[0].state = \"MERGED\" | .[0].headRefOid = \"$merged_head\""
git -C "$sdk" push -q origin ":refs/heads/$branch"
after_merge=$(next_source 'After merge')
export TEST_METADATA_FAIL=true
reject propose "$after_merge"
new_head=$(head)
git -C "$sdk" merge-base --is-ancestor main "$new_head"
# Retry after push succeeded but creation failed must not regenerate or lose work.
fresh
export TEST_GENERATE_FAIL=true TEST_METADATA_FAIL=false
before=$(wc -l < "$TEST_GENERATE_LOG")
propose "$after_merge"
[[ $(head) == "$new_head" && $(wc -l < "$TEST_GENERATE_LOG") == "$before" ]]
[[ $(jq -r '.[0].state' "$TEST_PR_STATE") == OPEN ]]

# A retained, exactly merged branch can also be recycled without force-updating
# history. A failed generation must leave that retained branch untouched.
fresh
git -C "$sdk" switch -q main
git -C "$sdk" merge --squash "$new_head"
git -C "$sdk" commit -qm 'Accept next contract'
git -C "$sdk" push -q origin main
set_pr ".[0].state = \"MERGED\" | .[0].headRefOid = \"$new_head\""
latest=$(next_source 'Retained branch cycle')
reject propose "$latest"
[[ $(head) == "$new_head" ]]
fresh
export TEST_GENERATE_FAIL=false
propose "$latest"
git -C "$sdk" merge-base --is-ancestor main HEAD
[[ $(jq -r '.[0].state' "$TEST_PR_STATE") == OPEN ]]
# Old accepted events do not create more PRs, and no tags/releases were emitted.
fresh
before=$(wc -l < "$TEST_PR_LOG")
propose "$runtime"
[[ $(wc -l < "$TEST_PR_LOG") == "$before" ]]
[[ -z $(git --git-dir="$TEST_REMOTE" tag -l) ]]

# A concurrent reviewer push rejects our non-fast-forward update; retry keeps it.
export TEST_CONCURRENT=true TEST_RACE_DIR="$work/racing-reviewer"
concurrent=$(next_source 'Concurrent update')
reject propose "$concurrent"
racing_head=$(head)
[[ $(git --git-dir="$TEST_REMOTE" show "$racing_head:contract/source.json" | jq -r .commit) == "$latest" ]]
fresh
export TEST_CONCURRENT=false
propose "$concurrent"
git -C "$sdk" merge-base --is-ancestor "$racing_head" HEAD
[[ $(git -C "$sdk" show HEAD:concurrent.txt) == concurrent ]]

# Human PR closure during generation is respected before publishing any update.
fresh
before_close=$(head)
closing=$(next_source 'Closure race')
export TEST_PR_RACE=close
reject propose "$closing"
[[ $(head) == "$before_close" ]]
set_pr '.[0].state = "OPEN"'
fresh
# A branch deleted between fetch and push must not be silently recreated.
export TEST_PR_RACE=delete
reject propose "$closing"
! git --git-dir="$TEST_REMOTE" show-ref --verify --quiet "refs/heads/$branch"
unset TEST_PR_RACE
# Restore the disposable fixture's deleted branch before testing recovery.
git --git-dir="$TEST_REMOTE" update-ref "refs/heads/$branch" "$before_close"
fresh
propose "$closing"

# Conflicting accepted SDK changes stop instead of overwriting adaptation work.
fresh
git -C "$sdk" switch --detach -q "$(head)"
echo 'proposal adaptation' > "$sdk/handwritten.txt"
git -C "$sdk" commit -qam 'Proposal adaptation'
git -C "$sdk" push -q origin "HEAD:refs/heads/$branch"
conflict_head=$(head)
fresh
git -C "$sdk" switch -q main
echo 'different accepted adaptation' > "$sdk/handwritten.txt"
git -C "$sdk" commit -qam 'Accepted adaptation'
git -C "$sdk" push -q origin main
conflict=$(next_source 'Conflict update')
reject propose "$conflict"
[[ $(head) == "$conflict_head" ]]
fresh

# An open PR whose branch disappeared must not silently lose reviewer work.
git -C "$sdk" push -q origin ":refs/heads/$branch"
reject propose "$conflict"

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
