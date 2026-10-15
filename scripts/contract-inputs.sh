#!/usr/bin/env bash
# Shared input selection for local imports and automatic proposals.
files='{
  "openapi.json": "proto/a13n-service/openapi.json",
  "thread-stream.schema.json": "proto/a13n-service/thread-stream.schema.json",
  "session-stream.schema.json": "proto/a13n-service/session-stream.schema.json",
  "semantics/api-conventions.md": "spec/api-conventions.md",
  "semantics/runs.md": "spec/a13n-service/05-runs.md",
  "semantics/facts-and-delivery.md": "spec/a13n-service/07-facts-and-delivery.md",
  "semantics/api.md": "spec/a13n-service/10-api.md"
}'

contract_input_selection_matches() {
  jq -e --argjson files "$files" \
    '.files as $owned | all($files | to_entries[]; $owned[.key].source_path == .value)' "${1:-contract/source.json}" >/dev/null
}

contract_inputs_changed() {
  local upstream=$1 previous=$2 incoming=$3 status=0
  local -a paths
  # A newly selected input may already exist at both revisions. It still needs
  # importing when the SDK snapshot has never consumed it.
  contract_input_selection_matches || return 0
  mapfile -t paths < <(jq -r '.[]' <<< "$files")
  git -C "$upstream" diff --quiet --no-ext-diff "$previous" "$incoming" -- "${paths[@]}" || status=$?
  case "$status" in
    0) return 1 ;;
    1) return 0 ;;
    *) echo 'Contract sync: cannot compare source inputs' >&2; exit "$status" ;;
  esac
}
