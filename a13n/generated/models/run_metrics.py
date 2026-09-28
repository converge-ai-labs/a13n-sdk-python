from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RunMetrics")


@_attrs_define(repr=False)
class RunMetrics:
    """
    Attributes:
        average_duration_seconds (float | None):
        runs (int):
    """

    average_duration_seconds: float | None
    runs: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        average_duration_seconds: float | None
        average_duration_seconds = self.average_duration_seconds

        runs = self.runs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "average_duration_seconds": average_duration_seconds,
                "runs": runs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_average_duration_seconds(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        average_duration_seconds = _parse_average_duration_seconds(d.pop("average_duration_seconds"))

        runs = d.pop("runs")

        run_metrics = cls(
            average_duration_seconds=average_duration_seconds,
            runs=runs,
        )

        run_metrics.additional_properties = d
        return run_metrics

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
