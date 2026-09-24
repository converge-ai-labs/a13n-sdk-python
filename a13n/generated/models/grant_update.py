from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="GrantUpdate")


@_attrs_define(repr=False)
class GrantUpdate:
    """
    Attributes:
        role (str):
    """

    role: str

    def to_dict(self) -> dict[str, Any]:
        role = self.role

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        role = d.pop("role")

        grant_update = cls(
            role=role,
        )

        return grant_update
