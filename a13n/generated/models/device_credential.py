from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.device import Device


T = TypeVar("T", bound="DeviceCredential")


@_attrs_define(repr=False)
class DeviceCredential:
    """
    Attributes:
        device (Device):
        token (str):
    """

    device: Device
    token: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device = self.device.to_dict()

        token = self.token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "device": device,
                "token": token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.device import Device

        d = dict(src_dict)
        device = Device.from_dict(d.pop("device"))

        token = d.pop("token")

        device_credential = cls(
            device=device,
            token=token,
        )

        device_credential.additional_properties = d
        return device_credential

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
