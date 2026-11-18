from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CredentialCreate")


@_attrs_define(repr=False)
class CredentialCreate:
    """
    Attributes:
        allowed_hosts (list[str]):
        name (str):
        value (str):
        description (str | Unset):
    """

    allowed_hosts: list[str]
    name: str
    value: str
    description: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        allowed_hosts = self.allowed_hosts

        name = self.name

        value = self.value

        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "allowed_hosts": allowed_hosts,
                "name": name,
                "value": value,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allowed_hosts = cast(list[str], d.pop("allowed_hosts"))

        name = d.pop("name")

        value = d.pop("value")

        description = d.pop("description", UNSET)

        credential_create = cls(
            allowed_hosts=allowed_hosts,
            name=name,
            value=value,
            description=description,
        )

        return credential_create
