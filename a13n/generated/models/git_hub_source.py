from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="GitHubSource")


@_attrs_define(repr=False)
class GitHubSource:
    """A directory of a public GitHub repository.

    `ref` defaults to the default branch. On a request `commit` is an optional expectation the resolved ref
    must meet; in a manifest it records the commit the package was read from.

        Attributes:
            kind (Literal['github']):
            repository (str):
            commit (None | str | Unset):
            path (str | Unset):
            ref (None | str | Unset):
    """

    kind: Literal["github"]
    repository: str
    commit: str | Unset | None = UNSET
    path: str | Unset = UNSET
    ref: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        repository = self.repository

        commit: str | Unset | None
        if isinstance(self.commit, Unset):
            commit = UNSET
        else:
            commit = self.commit

        path = self.path

        ref: str | Unset | None
        if isinstance(self.ref, Unset):
            ref = UNSET
        else:
            ref = self.ref

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
                "repository": repository,
            }
        )
        if commit is not UNSET:
            field_dict["commit"] = commit
        if path is not UNSET:
            field_dict["path"] = path
        if ref is not UNSET:
            field_dict["ref"] = ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = cast(Literal["github"], d.pop("kind"))
        if kind != "github":
            raise ValueError(f"kind must match const 'github', got '{kind}'")

        repository = d.pop("repository")

        def _parse_commit(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        commit = _parse_commit(d.pop("commit", UNSET))

        path = d.pop("path", UNSET)

        def _parse_ref(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        ref = _parse_ref(d.pop("ref", UNSET))

        git_hub_source = cls(
            kind=kind,
            repository=repository,
            commit=commit,
            path=path,
            ref=ref,
        )

        return git_hub_source
