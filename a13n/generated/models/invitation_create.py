from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="InvitationCreate")


@_attrs_define(repr=False)
class InvitationCreate:
    """
    Attributes:
        email (str):
        role (str):
    """

    email: str
    role: str

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        role = self.role

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "email": email,
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        role = d.pop("role")

        invitation_create = cls(
            email=email,
            role=role,
        )

        return invitation_create
