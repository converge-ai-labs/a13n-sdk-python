from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthorizationDisconnect")


@_attrs_define(repr=False)
class AuthorizationDisconnect:
    """
    Attributes:
        local_tokens_cleared (bool | Unset):
        revocation_confirmed (bool | None | Unset):
    """

    local_tokens_cleared: bool | Unset = UNSET
    revocation_confirmed: bool | Unset | None = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        local_tokens_cleared = self.local_tokens_cleared

        revocation_confirmed: bool | Unset | None
        if isinstance(self.revocation_confirmed, Unset):
            revocation_confirmed = UNSET
        else:
            revocation_confirmed = self.revocation_confirmed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if local_tokens_cleared is not UNSET:
            field_dict["local_tokens_cleared"] = local_tokens_cleared
        if revocation_confirmed is not UNSET:
            field_dict["revocation_confirmed"] = revocation_confirmed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        local_tokens_cleared = d.pop("local_tokens_cleared", UNSET)

        def _parse_revocation_confirmed(data: object) -> bool | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | Unset | None, data)

        revocation_confirmed = _parse_revocation_confirmed(d.pop("revocation_confirmed", UNSET))

        authorization_disconnect = cls(
            local_tokens_cleared=local_tokens_cleared,
            revocation_confirmed=revocation_confirmed,
        )

        authorization_disconnect.additional_properties = d
        return authorization_disconnect

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
