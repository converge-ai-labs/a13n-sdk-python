from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.grant_access import GrantAccess

T = TypeVar("T", bound="SandboxGrant")


@_attrs_define(repr=False)
class SandboxGrant:
    """
    Attributes:
        access (GrantAccess):
        path (str):
    """

    access: GrantAccess
    path: str

    def to_dict(self) -> dict[str, Any]:
        access = self.access.value

        path = self.path

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "access": access,
                "path": path,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access = GrantAccess(d.pop("access"))

        path = d.pop("path")

        sandbox_grant = cls(
            access=access,
            path=path,
        )

        return sandbox_grant
