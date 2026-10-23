from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceCreate")


@_attrs_define(repr=False)
class DeviceCreate:
    """
    Attributes:
        device_id (str):
        name (str):
        metrics_data_source_id (None | str | Unset):
    """

    device_id: str
    name: str
    metrics_data_source_id: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        name = self.name

        metrics_data_source_id: str | Unset | None
        if isinstance(self.metrics_data_source_id, Unset):
            metrics_data_source_id = UNSET
        else:
            metrics_data_source_id = self.metrics_data_source_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "device_id": device_id,
                "name": name,
            }
        )
        if metrics_data_source_id is not UNSET:
            field_dict["metrics_data_source_id"] = metrics_data_source_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        device_id = d.pop("device_id")

        name = d.pop("name")

        def _parse_metrics_data_source_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        metrics_data_source_id = _parse_metrics_data_source_id(d.pop("metrics_data_source_id", UNSET))

        device_create = cls(
            device_id=device_id,
            name=name,
            metrics_data_source_id=metrics_data_source_id,
        )

        return device_create
