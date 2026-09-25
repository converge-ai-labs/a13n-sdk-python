from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AuthConfiguration")


@_attrs_define(repr=False)
class AuthConfiguration:
    """
    Attributes:
        email_delivery (bool):
        initialized (bool):
    """

    email_delivery: bool
    initialized: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email_delivery = self.email_delivery

        initialized = self.initialized

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email_delivery": email_delivery,
                "initialized": initialized,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email_delivery = d.pop("email_delivery")

        initialized = d.pop("initialized")

        auth_configuration = cls(
            email_delivery=email_delivery,
            initialized=initialized,
        )

        auth_configuration.additional_properties = d
        return auth_configuration

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
