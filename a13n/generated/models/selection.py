from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.selection_metrics_labels import SelectionMetricsLabels


T = TypeVar("T", bound="Selection")


@_attrs_define(repr=False)
class Selection:
    """
    Attributes:
        metrics_data_source_id (None | str):
        metrics_labels (SelectionMetricsLabels | Unset):
    """

    metrics_data_source_id: str | None
    metrics_labels: SelectionMetricsLabels | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        metrics_data_source_id: str | None
        metrics_data_source_id = self.metrics_data_source_id

        metrics_labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metrics_labels, Unset):
            metrics_labels = self.metrics_labels.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "metrics_data_source_id": metrics_data_source_id,
            }
        )
        if metrics_labels is not UNSET:
            field_dict["metrics_labels"] = metrics_labels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.selection_metrics_labels import SelectionMetricsLabels

        d = dict(src_dict)

        def _parse_metrics_data_source_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        metrics_data_source_id = _parse_metrics_data_source_id(d.pop("metrics_data_source_id"))

        _metrics_labels = d.pop("metrics_labels", UNSET)
        metrics_labels: SelectionMetricsLabels | Unset
        if isinstance(_metrics_labels, Unset):
            metrics_labels = UNSET
        else:
            metrics_labels = SelectionMetricsLabels.from_dict(_metrics_labels)

        selection = cls(
            metrics_data_source_id=metrics_data_source_id,
            metrics_labels=metrics_labels,
        )

        return selection
