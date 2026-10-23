from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.collector_capability import CollectorCapability


T = TypeVar("T", bound="Capabilities")


@_attrs_define(repr=False)
class Capabilities:
    """
    Attributes:
        collectors (list[CollectorCapability]):
        proxy (bool):
    """

    collectors: list[CollectorCapability]
    proxy: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collectors = []
        for collectors_item_data in self.collectors:
            collectors_item = collectors_item_data.to_dict()
            collectors.append(collectors_item)

        proxy = self.proxy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collectors": collectors,
                "proxy": proxy,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.collector_capability import CollectorCapability

        d = dict(src_dict)
        collectors = []
        _collectors = d.pop("collectors")
        for collectors_item_data in _collectors:
            collectors_item = CollectorCapability.from_dict(collectors_item_data)

            collectors.append(collectors_item)

        proxy = d.pop("proxy")

        capabilities = cls(
            collectors=collectors,
            proxy=proxy,
        )

        capabilities.additional_properties = d
        return capabilities

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
