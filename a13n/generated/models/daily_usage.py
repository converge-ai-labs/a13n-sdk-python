from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_metrics import ModelMetrics


T = TypeVar("T", bound="DailyUsage")


@_attrs_define(repr=False)
class DailyUsage:
    """
    Attributes:
        date (datetime.date):
        usage (ModelMetrics):
    """

    date: datetime.date
    usage: ModelMetrics
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date.isoformat()

        usage = self.usage.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "usage": usage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_metrics import ModelMetrics

        d = dict(src_dict)
        date = datetime.date.fromisoformat(d.pop("date"))

        usage = ModelMetrics.from_dict(d.pop("usage"))

        daily_usage = cls(
            date=date,
            usage=usage,
        )

        daily_usage.additional_properties = d
        return daily_usage

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
