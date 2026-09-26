from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProfileUpdate")


@_attrs_define(repr=False)
class ProfileUpdate:
    """
    Attributes:
        current_password (None | str | Unset):
        email (None | str | Unset):
        name (None | str | Unset):
    """

    current_password: str | Unset | None = UNSET
    email: str | Unset | None = UNSET
    name: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        current_password: str | Unset | None
        if isinstance(self.current_password, Unset):
            current_password = UNSET
        else:
            current_password = self.current_password

        email: str | Unset | None
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        name: str | Unset | None
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if current_password is not UNSET:
            field_dict["current_password"] = current_password
        if email is not UNSET:
            field_dict["email"] = email
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_current_password(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        current_password = _parse_current_password(d.pop("current_password", UNSET))

        def _parse_email(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_name(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        name = _parse_name(d.pop("name", UNSET))

        profile_update = cls(
            current_password=current_password,
            email=email,
            name=name,
        )

        return profile_update
