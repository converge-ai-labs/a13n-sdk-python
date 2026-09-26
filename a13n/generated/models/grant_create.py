from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="GrantCreate")


@_attrs_define(repr=False)
class GrantCreate:
    """
    Attributes:
        principal_id (str):
        role (str):
    """

    principal_id: str
    role: str

    def to_dict(self) -> dict[str, Any]:
        principal_id = self.principal_id

        role = self.role

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "principal_id": principal_id,
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        principal_id = d.pop("principal_id")

        role = d.pop("role")

        grant_create = cls(
            principal_id=principal_id,
            role=role,
        )

        return grant_create
