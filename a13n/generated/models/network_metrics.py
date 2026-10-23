from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.network_metrics_interfaces import NetworkMetricsInterfaces


T = TypeVar("T", bound="NetworkMetrics")


@_attrs_define(repr=False)
class NetworkMetrics:
    """
    Attributes:
        truncated (bool):
        interfaces (NetworkMetricsInterfaces | Unset):
    """

    truncated: bool
    interfaces: NetworkMetricsInterfaces | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        truncated = self.truncated

        interfaces: dict[str, Any] | Unset = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = self.interfaces.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "truncated": truncated,
            }
        )
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.network_metrics_interfaces import NetworkMetricsInterfaces

        d = dict(src_dict)
        truncated = d.pop("truncated")

        _interfaces = d.pop("interfaces", UNSET)
        interfaces: NetworkMetricsInterfaces | Unset
        if isinstance(_interfaces, Unset):
            interfaces = UNSET
        else:
            interfaces = NetworkMetricsInterfaces.from_dict(_interfaces)

        network_metrics = cls(
            truncated=truncated,
            interfaces=interfaces,
        )

        return network_metrics
