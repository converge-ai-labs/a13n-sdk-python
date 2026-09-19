from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="DirectoryEntry")


@_attrs_define(repr=False)
class DirectoryEntry:
    """
    Attributes:
        name (str):
        path (str):
    """

    name: str
    path: str

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        path = self.path

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "path": path,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        path = d.pop("path")

        directory_entry = cls(
            name=name,
            path=path,
        )

        return directory_entry
