from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.grant_access import GrantAccess

T = TypeVar("T", bound="VmMount")


@_attrs_define(repr=False)
class VmMount:
    """
    Attributes:
        access (GrantAccess):
        source (str):
        target (str):
    """

    access: GrantAccess
    source: str
    target: str

    def to_dict(self) -> dict[str, Any]:
        access = self.access.value

        source = self.source

        target = self.target

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "access": access,
                "source": source,
                "target": target,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access = GrantAccess(d.pop("access"))

        source = d.pop("source")

        target = d.pop("target")

        vm_mount = cls(
            access=access,
            source=source,
            target=target,
        )

        return vm_mount
