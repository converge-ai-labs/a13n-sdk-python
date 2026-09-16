from __future__ import annotations

import os
import re
import stat
import tempfile
import tomllib
from dataclasses import dataclass
from pathlib import Path

COMPONENTS = ("a13n-python",)

RELEASE_VERSION_PATTERN = re.compile(
    r"(?P<major>0|[1-9][0-9]*)\."
    r"(?P<minor>0|[1-9][0-9]*)\."
    r"(?P<patch>0|[1-9][0-9]*)"
    r"(?:-rc\.(?P<rc>[1-9][0-9]*))?"
)


class ReleaseVersionError(ValueError):
    pass


@dataclass(frozen=True)
class ReleaseVersion:
    major: int
    minor: int
    patch: int
    rc: int | None

    @property
    def canonical(self) -> str:
        base = f"{self.major}.{self.minor}.{self.patch}"
        if self.rc is None:
            return base
        return f"{base}-rc.{self.rc}"

    @property
    def python_package(self) -> str:
        if self.rc is None:
            return self.canonical
        return f"{self.major}.{self.minor}.{self.patch}rc{self.rc}"

    @property
    def is_prerelease(self) -> bool:
        return self.rc is not None

    @property
    def precedence_key(self) -> tuple[int, int, int, int, int]:
        if self.rc is None:
            return self.major, self.minor, self.patch, 1, 0
        return self.major, self.minor, self.patch, 0, self.rc


def parse_release_version(version: str) -> ReleaseVersion:
    match = RELEASE_VERSION_PATTERN.fullmatch(version)
    if match is None:
        raise ReleaseVersionError(f"Release version must use X.Y.Z or X.Y.Z-rc.N syntax: {version}")
    rc = match.group("rc")
    return ReleaseVersion(
        major=int(match.group("major")),
        minor=int(match.group("minor")),
        patch=int(match.group("patch")),
        rc=int(rc) if rc is not None else None,
    )


def validate_version_syntax(version: str) -> None:
    parse_release_version(version)


_VERSION_LINE_PATTERN = re.compile(r'^(\s*version\s*=\s*")[^"]*(".*?)(\r?\n)?$')


def _load_toml(root: Path, relative_path: Path) -> dict[str, object]:
    path = root / relative_path
    try:
        with path.open("rb") as file:
            return tomllib.load(file)
    except (OSError, tomllib.TOMLDecodeError) as error:
        raise ReleaseVersionError(f"Cannot read TOML from {relative_path}: {error}") from error


def _mapping(value: object, label: str) -> dict[str, object]:
    if not isinstance(value, dict):
        raise ReleaseVersionError(f"Missing {label}")
    return value


def _string(value: object, label: str) -> str:
    if not isinstance(value, str):
        raise ReleaseVersionError(f"Missing {label}")
    return value


def _lock_package_version(root: Path, relative_path: Path, package_name: str) -> str:
    packages = _load_toml(root, relative_path).get("package")
    if not isinstance(packages, list):
        raise ReleaseVersionError(f"Missing package {package_name} in {relative_path}")
    matches = [package for package in packages if isinstance(package, dict) and package.get("name") == package_name]
    if len(matches) != 1:
        raise ReleaseVersionError(
            f"Expected exactly one package {package_name} in {relative_path}, found {len(matches)}"
        )
    return _string(matches[0].get("version"), f"package {package_name} version in {relative_path}")


def _replace_table_version(content: str, table_name: str, version: str, path: Path) -> str:
    lines = content.splitlines(keepends=True)
    active_table: str | None = None
    replacements = 0
    for index, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("[") and stripped.endswith("]"):
            active_table = stripped[1:-1]
            continue
        if active_table != table_name:
            continue
        match = _VERSION_LINE_PATTERN.fullmatch(line)
        if match is None:
            continue
        newline = match.group(3) or ""
        lines[index] = f"{match.group(1)}{version}{match.group(2)}{newline}"
        replacements += 1
    if replacements != 1:
        raise ReleaseVersionError(
            f"Expected exactly one {table_name}.version assignment in {path}, found {replacements}"
        )
    return "".join(lines)


def _replace_lock_package_version(
    content: str,
    package_name: str,
    version: str,
    path: Path,
) -> str:
    lines = content.splitlines(keepends=True)
    starts = [index for index, line in enumerate(lines) if line.strip() == "[[package]]"]
    starts.append(len(lines))
    matching_blocks: list[tuple[int, int]] = []
    name_pattern = re.compile(rf'^\s*name\s*=\s*"{re.escape(package_name)}"\s*(?:#.*)?(?:\r?\n)?$')
    for block_index in range(len(starts) - 1):
        start = starts[block_index]
        end = starts[block_index + 1]
        if any(name_pattern.fullmatch(line) is not None for line in lines[start:end]):
            matching_blocks.append((start, end))
    if len(matching_blocks) != 1:
        raise ReleaseVersionError(
            f"Expected exactly one package {package_name} in {path}, found {len(matching_blocks)}"
        )

    start, end = matching_blocks[0]
    version_indexes = [
        index for index in range(start, end) if _VERSION_LINE_PATTERN.fullmatch(lines[index]) is not None
    ]
    if len(version_indexes) != 1:
        raise ReleaseVersionError(
            f"Expected exactly one version for package {package_name} in {path}, found {len(version_indexes)}"
        )
    index = version_indexes[0]
    match = _VERSION_LINE_PATTERN.fullmatch(lines[index])
    if match is None:
        raise AssertionError("version line disappeared")
    newline = match.group(3) or ""
    lines[index] = f"{match.group(1)}{version}{match.group(2)}{newline}"
    return "".join(lines)


def _read_text(root: Path, relative_path: Path) -> str:
    try:
        return (root / relative_path).read_text(encoding="utf-8")
    except OSError as error:
        raise ReleaseVersionError(f"Cannot read {relative_path}: {error}") from error


def _atomic_write(path: Path, content: str) -> None:
    mode = stat.S_IMODE(path.stat().st_mode)
    descriptor, temporary_name = tempfile.mkstemp(
        dir=path.parent,
        prefix=f".{path.name}.",
        suffix=".tmp",
        text=True,
    )
    temporary_path = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="") as file:
            file.write(content)
            file.flush()
            os.fsync(file.fileno())
        os.chmod(temporary_path, mode)
        os.replace(temporary_path, path)
    except BaseException:
        temporary_path.unlink(missing_ok=True)
        raise


MANIFESTS = {"a13n-python": ("pyproject.toml", "uv.lock", "project", "a13n")}


def _manifest(component: str) -> tuple[Path, Path, str, str]:
    if component not in COMPONENTS:
        raise ReleaseVersionError(f"Unknown release component: {component}")
    manifest, lock, table, package = MANIFESTS[component]
    return Path(manifest), Path(lock), table, package


def component_versions(root: Path, component: str) -> dict[str, str]:
    manifest, lock, table, package = _manifest(component)
    metadata = _mapping(_load_toml(root, manifest).get(table), f"{table} in {manifest}")
    return {
        str(manifest): _string(metadata.get("version"), f"version in {manifest}"),
        f"{lock} package {package}": _lock_package_version(root, lock, package),
    }


def _package_version(version: str) -> str:
    release = parse_release_version(version)
    return release.python_package


def validate_component_version(root: Path, component: str, version: str) -> None:
    expected = _package_version(version)
    mismatches = {label: actual for label, actual in component_versions(root, component).items() if actual != expected}
    if mismatches:
        raise ReleaseVersionError(f"Expected {component} version {expected}: {mismatches}")


def prepare_component_version(root: Path, component: str, version: str) -> tuple[Path, ...]:
    expected = _package_version(version)
    component_versions(root, component)
    manifest, lock, table, package = _manifest(component)
    # Plan every edit before writing, preserving dependency versions and formatting.
    planned = {
        manifest: _replace_table_version(_read_text(root, manifest), table, expected, manifest),
        lock: _replace_lock_package_version(_read_text(root, lock), package, expected, lock),
    }
    changed = tuple(path for path in sorted(planned) if planned[path] != _read_text(root, path))
    for path in changed:
        _atomic_write(root / path, planned[path])
    validate_component_version(root, component, version)
    return changed
