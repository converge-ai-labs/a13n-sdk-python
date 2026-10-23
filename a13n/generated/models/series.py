from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.series_labels import SeriesLabels


T = TypeVar("T", bound="Series")


@_attrs_define(repr=False)
class Series:
    """
    Attributes:
        metric (str):
        points (list[list[float | int]]):
        labels (SeriesLabels | Unset):
    """

    metric: str
    points: list[list[float | int]]
    labels: SeriesLabels | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metric = self.metric

        points = []
        for points_item_data in self.points:
            points_item = []
            for points_item_item_data in points_item_data:
                points_item_item: float | int
                points_item_item = points_item_item_data
                points_item.append(points_item_item)

            points.append(points_item)

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metric": metric,
                "points": points,
            }
        )
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.series_labels import SeriesLabels

        d = dict(src_dict)
        metric = d.pop("metric")

        points = []
        _points = d.pop("points")
        for points_item_data in _points:
            points_item = []
            _points_item = points_item_data
            for points_item_item_data in _points_item:

                def _parse_points_item_item(data: object) -> float | int:
                    return cast(float | int, data)

                points_item_item = _parse_points_item_item(points_item_item_data)

                points_item.append(points_item_item)

            points.append(points_item)

        _labels = d.pop("labels", UNSET)
        labels: SeriesLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = SeriesLabels.from_dict(_labels)

        series = cls(
            metric=metric,
            points=points,
            labels=labels,
        )

        series.additional_properties = d
        return series

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
