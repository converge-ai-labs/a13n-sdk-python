from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..._validation import validate_model
from ..models.access_mode import AccessMode

if TYPE_CHECKING:
    from ..models.view import View


T = TypeVar("T", bound="Access")


@_attrs_define(repr=False)
class Access:
    """
    Attributes:
        assistance (View):
        expires_in_seconds (float):
        mode (AccessMode):
        password (str):
        websocket_url (str):
    """

    assistance: View
    expires_in_seconds: float
    mode: AccessMode
    password: str
    websocket_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assistance = self.assistance.to_dict()

        expires_in_seconds = self.expires_in_seconds

        mode = self.mode.value

        password = self.password

        websocket_url = self.websocket_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assistance": assistance,
                "expires_in_seconds": expires_in_seconds,
                "mode": mode,
                "password": password,
                "websocket_url": websocket_url,
            }
        )

        validate_model("Access", field_dict)
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        validate_model("Access", src_dict)
        from ..models.view import View

        d = dict(src_dict)
        assistance = View.from_dict(d.pop("assistance"))

        expires_in_seconds = d.pop("expires_in_seconds")

        mode = AccessMode(d.pop("mode"))

        password = d.pop("password")

        websocket_url = d.pop("websocket_url")

        access = cls(
            assistance=assistance,
            expires_in_seconds=expires_in_seconds,
            mode=mode,
            password=password,
            websocket_url=websocket_url,
        )

        access.additional_properties = d
        return access

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
