from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.disk_metrics_devices import DiskMetricsDevices


T = TypeVar("T", bound="DiskMetrics")


@_attrs_define(repr=False)
class DiskMetrics:
    """
    Attributes:
        truncated (bool):
        devices (DiskMetricsDevices | Unset):
    """

    truncated: bool
    devices: DiskMetricsDevices | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        truncated = self.truncated

        devices: dict[str, Any] | Unset = UNSET
        if not isinstance(self.devices, Unset):
            devices = self.devices.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "truncated": truncated,
            }
        )
        if devices is not UNSET:
            field_dict["devices"] = devices

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.disk_metrics_devices import DiskMetricsDevices

        d = dict(src_dict)
        truncated = d.pop("truncated")

        _devices = d.pop("devices", UNSET)
        devices: DiskMetricsDevices | Unset
        if isinstance(_devices, Unset):
            devices = UNSET
        else:
            devices = DiskMetricsDevices.from_dict(_devices)

        disk_metrics = cls(
            truncated=truncated,
            devices=devices,
        )

        return disk_metrics
