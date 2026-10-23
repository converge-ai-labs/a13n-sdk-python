from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connection_metrics_tcp_states import ConnectionMetricsTcpStates


T = TypeVar("T", bound="ConnectionMetrics")


@_attrs_define(repr=False)
class ConnectionMetrics:
    """
    Attributes:
        tcp_states (ConnectionMetricsTcpStates | Unset):
        tcp_total (int | None | Unset):
        udp_sockets (int | None | Unset):
    """

    tcp_states: ConnectionMetricsTcpStates | Unset = UNSET
    tcp_total: int | Unset | None = UNSET
    udp_sockets: int | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        tcp_states: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tcp_states, Unset):
            tcp_states = self.tcp_states.to_dict()

        tcp_total: int | Unset | None
        if isinstance(self.tcp_total, Unset):
            tcp_total = UNSET
        else:
            tcp_total = self.tcp_total

        udp_sockets: int | Unset | None
        if isinstance(self.udp_sockets, Unset):
            udp_sockets = UNSET
        else:
            udp_sockets = self.udp_sockets

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if tcp_states is not UNSET:
            field_dict["tcp_states"] = tcp_states
        if tcp_total is not UNSET:
            field_dict["tcp_total"] = tcp_total
        if udp_sockets is not UNSET:
            field_dict["udp_sockets"] = udp_sockets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connection_metrics_tcp_states import ConnectionMetricsTcpStates

        d = dict(src_dict)
        _tcp_states = d.pop("tcp_states", UNSET)
        tcp_states: ConnectionMetricsTcpStates | Unset
        if isinstance(_tcp_states, Unset):
            tcp_states = UNSET
        else:
            tcp_states = ConnectionMetricsTcpStates.from_dict(_tcp_states)

        def _parse_tcp_total(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        tcp_total = _parse_tcp_total(d.pop("tcp_total", UNSET))

        def _parse_udp_sockets(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        udp_sockets = _parse_udp_sockets(d.pop("udp_sockets", UNSET))

        connection_metrics = cls(
            tcp_states=tcp_states,
            tcp_total=tcp_total,
            udp_sockets=udp_sockets,
        )

        return connection_metrics
