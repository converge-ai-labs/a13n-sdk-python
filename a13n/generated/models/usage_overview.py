from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.daily_usage import DailyUsage
    from ..models.model_metrics import ModelMetrics
    from ..models.run_metrics import RunMetrics
    from ..models.usage_series import UsageSeries


T = TypeVar("T", bound="UsageOverview")


@_attrs_define(repr=False)
class UsageOverview:
    """
    Attributes:
        daily (list[DailyUsage]):
        runs (RunMetrics):
        usage (ModelMetrics):
        series (list[UsageSeries] | Unset):
    """

    daily: list[DailyUsage]
    runs: RunMetrics
    usage: ModelMetrics
    series: list[UsageSeries] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        daily = []
        for daily_item_data in self.daily:
            daily_item = daily_item_data.to_dict()
            daily.append(daily_item)

        runs = self.runs.to_dict()

        usage = self.usage.to_dict()

        series: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.series, Unset):
            series = []
            for series_item_data in self.series:
                series_item = series_item_data.to_dict()
                series.append(series_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "daily": daily,
                "runs": runs,
                "usage": usage,
            }
        )
        if series is not UNSET:
            field_dict["series"] = series

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.daily_usage import DailyUsage
        from ..models.model_metrics import ModelMetrics
        from ..models.run_metrics import RunMetrics
        from ..models.usage_series import UsageSeries

        d = dict(src_dict)
        daily = []
        _daily = d.pop("daily")
        for daily_item_data in _daily:
            daily_item = DailyUsage.from_dict(daily_item_data)

            daily.append(daily_item)

        runs = RunMetrics.from_dict(d.pop("runs"))

        usage = ModelMetrics.from_dict(d.pop("usage"))

        _series = d.pop("series", UNSET)
        series: list[UsageSeries] | Unset = UNSET
        if _series is not UNSET:
            series = []
            for series_item_data in _series:
                series_item = UsageSeries.from_dict(series_item_data)

                series.append(series_item)

        usage_overview = cls(
            daily=daily,
            runs=runs,
            usage=usage,
            series=series,
        )

        usage_overview.additional_properties = d
        return usage_overview

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
