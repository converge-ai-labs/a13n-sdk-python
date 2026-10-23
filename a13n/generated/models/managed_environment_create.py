from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.managed_environment_create_metrics_labels import ManagedEnvironmentCreateMetricsLabels


T = TypeVar("T", bound="ManagedEnvironmentCreate")


@_attrs_define(repr=False)
class ManagedEnvironmentCreate:
    """A workspace-managed sandbox reserved from a template, for threads to mount; maintenance creates it.

    Attributes:
        template_id (str):
        metrics_data_source_id (None | str | Unset):
        metrics_labels (ManagedEnvironmentCreateMetricsLabels | Unset):
        name (None | str | Unset):
    """

    template_id: str
    metrics_data_source_id: str | Unset | None = UNSET
    metrics_labels: ManagedEnvironmentCreateMetricsLabels | Unset = UNSET
    name: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        template_id = self.template_id

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
                "template_id": template_id,
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
        from ..models.managed_environment_create_metrics_labels import (
            ManagedEnvironmentCreateMetricsLabels,
        )

        d = dict(src_dict)
        template_id = d.pop("template_id")

        def _parse_metrics_data_source_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        metrics_data_source_id = _parse_metrics_data_source_id(d.pop("metrics_data_source_id", UNSET))

        _metrics_labels = d.pop("metrics_labels", UNSET)
        metrics_labels: ManagedEnvironmentCreateMetricsLabels | Unset
        if isinstance(_metrics_labels, Unset):
            metrics_labels = UNSET
        else:
            metrics_labels = ManagedEnvironmentCreateMetricsLabels.from_dict(_metrics_labels)

        def _parse_name(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        name = _parse_name(d.pop("name", UNSET))

        managed_environment_create = cls(
            template_id=template_id,
            metrics_data_source_id=metrics_data_source_id,
            metrics_labels=metrics_labels,
            name=name,
        )

        return managed_environment_create
