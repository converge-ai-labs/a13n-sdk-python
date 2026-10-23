from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filesystem_metrics import FilesystemMetrics


T = TypeVar("T", bound="FilesystemObservation")


@_attrs_define(repr=False)
class FilesystemObservation:
    """
    Attributes:
        metrics (FilesystemMetrics | None | Unset):
    """

    metrics: FilesystemMetrics | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.filesystem_metrics import FilesystemMetrics

        metrics: dict[str, Any] | Unset | None
        if isinstance(self.metrics, Unset):
            metrics = UNSET
        elif isinstance(self.metrics, FilesystemMetrics):
            metrics = self.metrics.to_dict()
        else:
            metrics = self.metrics

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if metrics is not UNSET:
            field_dict["metrics"] = metrics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filesystem_metrics import FilesystemMetrics

        d = dict(src_dict)

        def _parse_metrics(data: object) -> FilesystemMetrics | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metrics_type_0 = FilesystemMetrics.from_dict(data)

                return metrics_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FilesystemMetrics | Unset | None, data)

        metrics = _parse_metrics(d.pop("metrics", UNSET))

        filesystem_observation = cls(
            metrics=metrics,
        )

        return filesystem_observation
