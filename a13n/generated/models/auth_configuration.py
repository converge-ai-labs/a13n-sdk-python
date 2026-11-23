from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.oidc_sign_in import OIDCSignIn


T = TypeVar("T", bound="AuthConfiguration")


@_attrs_define(repr=False)
class AuthConfiguration:
    """
    Attributes:
        email_delivery (bool):
        initialized (bool):
        manual_password_reset (bool):
        oidc_providers (list[OIDCSignIn]):
        password_enabled (bool):
    """

    email_delivery: bool
    initialized: bool
    manual_password_reset: bool
    oidc_providers: list[OIDCSignIn]
    password_enabled: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email_delivery = self.email_delivery

        initialized = self.initialized

        manual_password_reset = self.manual_password_reset

        oidc_providers = []
        for oidc_providers_item_data in self.oidc_providers:
            oidc_providers_item = oidc_providers_item_data.to_dict()
            oidc_providers.append(oidc_providers_item)

        password_enabled = self.password_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email_delivery": email_delivery,
                "initialized": initialized,
                "manual_password_reset": manual_password_reset,
                "oidc_providers": oidc_providers,
                "password_enabled": password_enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.oidc_sign_in import OIDCSignIn

        d = dict(src_dict)
        email_delivery = d.pop("email_delivery")

        initialized = d.pop("initialized")

        manual_password_reset = d.pop("manual_password_reset")

        oidc_providers = []
        _oidc_providers = d.pop("oidc_providers")
        for oidc_providers_item_data in _oidc_providers:
            oidc_providers_item = OIDCSignIn.from_dict(oidc_providers_item_data)

            oidc_providers.append(oidc_providers_item)

        password_enabled = d.pop("password_enabled")

        auth_configuration = cls(
            email_delivery=email_delivery,
            initialized=initialized,
            manual_password_reset=manual_password_reset,
            oidc_providers=oidc_providers,
            password_enabled=password_enabled,
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
