from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.daily_usage import DailyUsage


T = TypeVar("T", bound="UsageSeries")


@_attrs_define(repr=False)
class UsageSeries:
    """
    Attributes:
        daily (list[DailyUsage]):
        key (None | str):
        name (None | str):
    """

    daily: list[DailyUsage]
    key: str | None
    name: str | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        daily = []
        for daily_item_data in self.daily:
            daily_item = daily_item_data.to_dict()
            daily.append(daily_item)

        key: str | None
        key = self.key

        name: str | None
        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "daily": daily,
                "key": key,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.daily_usage import DailyUsage

        d = dict(src_dict)
        daily = []
        _daily = d.pop("daily")
        for daily_item_data in _daily:
            daily_item = DailyUsage.from_dict(daily_item_data)

            daily.append(daily_item)

        def _parse_key(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        key = _parse_key(d.pop("key"))

        def _parse_name(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        name = _parse_name(d.pop("name"))

        usage_series = cls(
            daily=daily,
            key=key,
            name=name,
        )

        usage_series.additional_properties = d
        return usage_series

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
