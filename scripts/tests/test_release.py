from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPTS = Path(__file__).resolve().parents[1]
ROOT = SCRIPTS.parent
sys.path.insert(0, str(SCRIPTS))

from release_notes import (  # noqa: E402
    ReleaseChange,
    build_release_command,
    collect_release_changes,
    load_pull_request_labels,
    previous_release_tag,
    read_manual_release_notes,
    release_tag,
    render_release_notes,
)
from release_version import (  # noqa: E402
    COMPONENTS,
    ReleaseVersionError,
    component_versions,
    parse_release_version,
    prepare_component_version,
    validate_component_version,
)

COMPONENT = COMPONENTS[0]


def git(root: Path, *arguments: str) -> str:
    return subprocess.check_output(["git", *arguments], cwd=root, text=True).strip()


@pytest.fixture
def repository(tmp_path: Path) -> Path:
    git(tmp_path, "init", "-b", "main")
    git(tmp_path, "config", "user.name", "Release Test")
    git(tmp_path, "config", "user.email", "release@example.test")
    (tmp_path / "README.md").write_text("Initial\n")
    git(tmp_path, "add", ".")
    git(tmp_path, "commit", "-qm", "Initial source")
    return tmp_path


@pytest.mark.parametrize("version", ["1.2.3", "0.0.0", "12.30.40-rc.21"])
def test_canonical_versions(version: str) -> None:
    assert parse_release_version(version).canonical == version
    assert release_tag(COMPONENT, version).endswith(version)
    assert parse_release_version("1.2.3-rc.4").python_package == "1.2.3rc4"


@pytest.mark.parametrize(
    "version",
    ["v1.2.3", "01.2.3", "1.2", "1.2.3rc1", "1.2.3-rc.0", "1.2.3-rc.01", "1.2.3+build", "1.2.3\n", "../1.2.3"],
)
def test_invalid_version_never_mutates(tmp_path: Path, version: str) -> None:
    with pytest.raises(ReleaseVersionError):
        prepare_component_version(tmp_path, COMPONENT, version)
    assert not list(tmp_path.iterdir())


def test_unknown_component_is_rejected(tmp_path: Path) -> None:
    with pytest.raises(ValueError):
        prepare_component_version(tmp_path, "another-repository", "1.2.3")


def test_preceding_channel_and_rc_train() -> None:
    def tag(version: str) -> str:
        return release_tag(COMPONENT, version)

    tags = [tag(value) for value in ("1.9.0", "1.10.0", "1.11.0-rc.8", "2.0.0-rc.1", "2.0.0-rc.2", "2.0.0")]
    tags += ["release/unrelated/9.0.0", tag("1.0.0") + "invalid"]
    assert previous_release_tag(COMPONENT, "2.0.0", tags) == tag("1.10.0")
    assert previous_release_tag(COMPONENT, "2.0.0-rc.2", tags) == tag("2.0.0-rc.1")
    assert previous_release_tag(COMPONENT, "2.0.0-rc.1", tags) == tag("1.10.0")
    assert previous_release_tag(COMPONENT, "1.0.0", tags) is None


@pytest.mark.parametrize("component", COMPONENTS)
@pytest.mark.parametrize("version", ["1.2.3", "1.2.3-rc.4"])
def test_release_command(component: str, version: str) -> None:
    command = build_release_command(
        component=component, version=version, repository="owner/repo", title="Release", assets=["dist/file"]
    )
    assert command[:4] == ["gh", "release", "create", release_tag(component, version)]
    assert "--verify-tag" in command
    assert ("--prerelease" in command) == ("-rc." in version)
    assert ("--latest=false" in command) == ("-rc." in version or component == "a13n-service-cli")
    assert command[-2:] == ["--notes-file", "-"]


def test_notes_classification_labels_and_escaping(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    changes = [
        ReleaseChange("a" * 40, "feat: [untrusted](url) (#12)", labels=("bug",)),
        ReleaseChange("b" * 40, "chore: omit", labels=("chore",)),
        ReleaseChange("c" * 40, "feat!: upgrade", labels=("breaking-change", "skip-changelog")),
    ]
    notes = render_release_notes(
        component=COMPONENT,
        version="2.0.0",
        repository="owner/repo",
        previous_tag=release_tag(COMPONENT, "1.0.0"),
        changes=changes,
        manual_notes="## Highlights",
    )
    assert "### Bug fixes" in notes and "\\[untrusted\\]" in notes
    assert "### Breaking changes" in notes and "omit" not in notes
    assert "https://github.com/owner/repo/pull/12" in notes
    assert "(repository comparison)" in notes
    assert notes.startswith("## Highlights\n")
    manual = tmp_path / ".github/release-notes" / COMPONENT / "2.0.0.md"
    manual.parent.mkdir(parents=True)
    manual.write_text("\nHighlights\n")
    assert read_manual_release_notes(tmp_path, COMPONENT, "2.0.0") == "Highlights"
    assert read_manual_release_notes(tmp_path, COMPONENT, "1.0.0") is None
    assert (
        render_release_notes(
            component=COMPONENT, version="1.0.0", repository="owner/repo", previous_tag=None, manual_notes="First"
        )
        == "First\n"
    )
    calls = []

    def query(*args: object, **kwargs: object) -> subprocess.CompletedProcess[str]:
        calls.append(args)
        return subprocess.CompletedProcess([], 0, stdout="bug\n")

    monkeypatch.setattr(subprocess, "run", query)
    labelled = load_pull_request_labels([changes[0], changes[0]], "owner/repo")
    assert len(calls) == 1
    assert all(change.labels == ("bug",) for change in labelled)


def test_first_parent_history_root_paths_and_channel_ancestry(repository: Path) -> None:
    before = release_tag(COMPONENT, "1.0.0")
    current = release_tag(COMPONENT, "2.0.0")
    git(repository, "tag", before)
    git(repository, "checkout", "-qb", "unmerged")
    (repository / "unmerged.txt").write_text("other\n")
    git(repository, "add", ".")
    git(repository, "commit", "-qm", "Unmerged")
    unreachable = release_tag(COMPONENT, "1.9.0")
    git(repository, "tag", unreachable)
    git(repository, "checkout", "-q", "main")
    git(repository, "checkout", "-qb", "feature")
    (repository / "README.md").write_text("Feature\n")
    git(repository, "add", ".")
    git(repository, "commit", "-qm", "feat: branch detail")
    git(repository, "checkout", "-q", "main")
    git(repository, "merge", "--no-ff", "-qm", "feat: reviewed root change", "feature")
    git(repository, "tag", current)
    changes = collect_release_changes(repository, COMPONENT, before, current)
    assert [change.subject for change in changes] == ["feat: reviewed root change"]
    merged = git(repository, "tag", "--merged", current).splitlines()
    assert unreachable not in merged
    assert previous_release_tag(COMPONENT, "2.0.0", merged) == before


@pytest.mark.parametrize(
    "state", ["success", "failure", "in_progress", "missing", "other-sha", "older-success", "off-main", "api-failure"]
)
def test_release_requires_successful_owned_main_ci(repository: Path, state: str) -> None:
    commit = git(repository, "rev-parse", "HEAD")
    git(repository, "update-ref", "refs/remotes/origin/main", commit)
    if state == "off-main":
        (repository / "README.md").write_text("not merged\n")
        git(repository, "add", ".")
        git(repository, "commit", "-qm", "Off main")
    run = {
        "head_sha": commit,
        "head_branch": "main",
        "event": "push",
        "run_number": 1,
        "run_attempt": 1,
        "status": "completed",
        "conclusion": "success",
    }
    runs = [run]
    if state == "failure":
        run["conclusion"] = "failure"
    if state == "in_progress":
        run["status"] = "in_progress"
    if state == "missing":
        runs = []
    if state == "other-sha":
        run["head_sha"] = "0" * 40
    if state == "older-success":
        runs.append({**run, "run_attempt": 2, "conclusion": "failure"})
    payload = repository / "runs.json"
    payload.write_text(json.dumps([{"workflow_runs": runs}]))
    binary = repository / "bin"
    binary.mkdir()
    gh = binary / "gh"
    gh.write_text("#!/bin/sh\nexit 1\n" if state == "api-failure" else '#!/bin/sh\ncat "$CI_FIXTURE"\n')
    gh.chmod(0o755)
    env = {
        **os.environ,
        "PATH": f"{binary}{os.pathsep}{os.environ['PATH']}",
        "CI_FIXTURE": str(payload),
        "GITHUB_REPOSITORY": "owner/repo",
    }
    result = subprocess.run(
        ["bash", str(SCRIPTS / "verify-release-source.sh")], cwd=repository, env=env, capture_output=True, text=True
    )
    assert (result.returncode == 0) == (state == "success"), result.stderr


@pytest.mark.parametrize("component", COMPONENTS)
@pytest.mark.parametrize("version", ["1.2.3", "1.2.3-rc.4"])
def test_only_own_manifest_and_lock_are_versioned(tmp_path: Path, component: str, version: str) -> None:
    from release_version import MANIFESTS

    originals = {}
    for manifest, lock, _, _ in MANIFESTS.values():
        for name in (manifest, lock):
            target = tmp_path / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, target)
            originals[name] = target.read_bytes()
    validate_component_version(tmp_path, component, "0.0.0")
    changed = prepare_component_version(tmp_path, component, version)
    manifest, lock, _, _ = MANIFESTS[component]
    assert set(changed) == {Path(manifest), Path(lock)}
    expected = version.replace("-rc.", "rc") if component == "a13n-python" else version
    assert set(component_versions(tmp_path, component).values()) == {expected}
    assert prepare_component_version(tmp_path, component, version) == ()
    validate_component_version(tmp_path, component, version)
    # Restoring source identity must restore exact bytes, including every unrelated
    # package entry, dependency range, CLI SDK dependency and lock checksum.
    prepare_component_version(tmp_path, component, "0.0.0")
    for name, original in originals.items():
        assert (tmp_path / name).read_bytes() == original


@pytest.mark.parametrize("component", COMPONENTS)
def test_invalid_lock_is_detected_before_manifest_write(tmp_path: Path, component: str) -> None:
    from release_version import MANIFESTS

    manifest, lock, _, _ = MANIFESTS[component]
    target = tmp_path / manifest
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ROOT / manifest, target)
    original = target.read_bytes()
    (tmp_path / lock).write_text("version = 4\n")
    with pytest.raises(ValueError):
        prepare_component_version(tmp_path, component, "1.2.3")
    assert target.read_bytes() == original
