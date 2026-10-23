from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceUpdate")


@_attrs_define(repr=False)
class DeviceUpdate:
    """
    Attributes:
        enabled (bool | None | Unset):
        metrics_data_source_id (None | str | Unset):
        name (None | str | Unset):
    """

    enabled: bool | Unset | None = UNSET
    metrics_data_source_id: str | Unset | None = UNSET
    name: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        enabled: bool | Unset | None
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        metrics_data_source_id: str | Unset | None
        if isinstance(self.metrics_data_source_id, Unset):
            metrics_data_source_id = UNSET
        else:
            metrics_data_source_id = self.metrics_data_source_id

        name: str | Unset | None
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if metrics_data_source_id is not UNSET:
            field_dict["metrics_data_source_id"] = metrics_data_source_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_enabled(data: object) -> bool | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | Unset | None, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        def _parse_metrics_data_source_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        metrics_data_source_id = _parse_metrics_data_source_id(d.pop("metrics_data_source_id", UNSET))

        def _parse_name(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        name = _parse_name(d.pop("name", UNSET))

        device_update = cls(
            enabled=enabled,
            metrics_data_source_id=metrics_data_source_id,
            name=name,
        )

        return device_update
