from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceAccountCreate")


@_attrs_define(repr=False)
class ServiceAccountCreate:
    """
    Attributes:
        name (str):
        description (str | Unset):
        role (str | Unset):
    """

    name: str
    description: str | Unset = UNSET
    role: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        role = self.role

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description", UNSET)

        role = d.pop("role", UNSET)

        service_account_create = cls(
            name=name,
            description=description,
            role=role,
        )

        return service_account_create
