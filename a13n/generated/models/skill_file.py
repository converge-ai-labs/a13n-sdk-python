from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SkillFile")


@_attrs_define(repr=False)
class SkillFile:
    """
    Attributes:
        path (str):
        size (int):
    """

    path: str
    size: int

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        size = self.size

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "path": path,
                "size": size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path")

        size = d.pop("size")

        skill_file = cls(
            path=path,
            size=size,
        )

        return skill_file
