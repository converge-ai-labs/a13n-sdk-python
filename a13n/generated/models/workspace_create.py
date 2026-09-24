from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="WorkspaceCreate")


@_attrs_define(repr=False)
class WorkspaceCreate:
    """
    Attributes:
        key (str):
        name (str):
    """

    key: str
    name: str

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        name = d.pop("name")

        workspace_create = cls(
            key=key,
            name=name,
        )

        return workspace_create
