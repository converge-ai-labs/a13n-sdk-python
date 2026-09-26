from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.provider_test_status import ProviderTestStatus

T = TypeVar("T", bound="ProviderTest")


@_attrs_define(repr=False)
class ProviderTest:
    """
    Attributes:
        message (None | str):
        provider_id (str):
        provider_version (int):
        status (ProviderTestStatus):
    """

    message: str | None
    provider_id: str
    provider_version: int
    status: ProviderTestStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message: str | None
        message = self.message

        provider_id = self.provider_id

        provider_version = self.provider_version

        status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "provider_id": provider_id,
                "provider_version": provider_version,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_message(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        message = _parse_message(d.pop("message"))

        provider_id = d.pop("provider_id")

        provider_version = d.pop("provider_version")

        status = ProviderTestStatus(d.pop("status"))

        provider_test = cls(
            message=message,
            provider_id=provider_id,
            provider_version=provider_version,
            status=status,
        )

        provider_test.additional_properties = d
        return provider_test

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
