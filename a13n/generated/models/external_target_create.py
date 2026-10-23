from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.external_target_create_metrics_labels import ExternalTargetCreateMetricsLabels


T = TypeVar("T", bound="ExternalTargetCreate")


@_attrs_define(repr=False)
class ExternalTargetCreate:
    """An envd daemon someone runs, registered by its endpoint and the token it accepts.

    Attributes:
        endpoint (str):
        token (str):
        metrics_data_source_id (None | str | Unset):
        metrics_labels (ExternalTargetCreateMetricsLabels | Unset):
        name (None | str | Unset):
    """

    endpoint: str
    token: str
    metrics_data_source_id: str | Unset | None = UNSET
    metrics_labels: ExternalTargetCreateMetricsLabels | Unset = UNSET
    name: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        endpoint = self.endpoint

        token = self.token

        metrics_data_source_id: str | Unset | None
        if isinstance(self.metrics_data_source_id, Unset):
            metrics_data_source_id = UNSET
        else:
            metrics_data_source_id = self.metrics_data_source_id

        metrics_labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metrics_labels, Unset):
            metrics_labels = self.metrics_labels.to_dict()

        name: str | Unset | None
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "endpoint": endpoint,
                "token": token,
            }
        )
        if metrics_data_source_id is not UNSET:
            field_dict["metrics_data_source_id"] = metrics_data_source_id
        if metrics_labels is not UNSET:
            field_dict["metrics_labels"] = metrics_labels
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.external_target_create_metrics_labels import ExternalTargetCreateMetricsLabels

        d = dict(src_dict)
        endpoint = d.pop("endpoint")

        token = d.pop("token")

        def _parse_metrics_data_source_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        metrics_data_source_id = _parse_metrics_data_source_id(d.pop("metrics_data_source_id", UNSET))

        _metrics_labels = d.pop("metrics_labels", UNSET)
        metrics_labels: ExternalTargetCreateMetricsLabels | Unset
        if isinstance(_metrics_labels, Unset):
            metrics_labels = UNSET
        else:
            metrics_labels = ExternalTargetCreateMetricsLabels.from_dict(_metrics_labels)

        def _parse_name(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        name = _parse_name(d.pop("name", UNSET))

        external_target_create = cls(
            endpoint=endpoint,
            token=token,
            metrics_data_source_id=metrics_data_source_id,
            metrics_labels=metrics_labels,
            name=name,
        )

        return external_target_create
