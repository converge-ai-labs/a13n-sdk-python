from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.credential_mode import CredentialMode

T = TypeVar("T", bound="AuthenticationCase")


@_attrs_define(repr=False)
class AuthenticationCase:
    """Override credential presence for one declared configuration field value.

    Attributes:
        equals (bool | int | None | str):
        field (str):
        mode (CredentialMode):
    """

    equals: bool | int | str | None
    field: str
    mode: CredentialMode

    def to_dict(self) -> dict[str, Any]:
        equals: bool | int | str | None
        equals = self.equals

        field = self.field

        mode = self.mode.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "equals": equals,
                "field": field,
                "mode": mode,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_equals(data: object) -> bool | int | str | None:
            if data is None:
                return data
            return cast(bool | int | str | None, data)

        equals = _parse_equals(d.pop("equals"))

        field = d.pop("field")

        mode = CredentialMode(d.pop("mode"))

        authentication_case = cls(
            equals=equals,
            field=field,
            mode=mode,
        )

        return authentication_case
