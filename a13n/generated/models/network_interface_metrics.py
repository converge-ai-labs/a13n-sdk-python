from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NetworkInterfaceMetrics")


@_attrs_define(repr=False)
class NetworkInterfaceMetrics:
    """
    Attributes:
        identity (str):
        receive_drops (int | None | Unset):
        receive_errors (int | None | Unset):
        received_bytes (int | None | Unset):
        received_packets (int | None | Unset):
        transmit_drops (int | None | Unset):
        transmit_errors (int | None | Unset):
        transmitted_bytes (int | None | Unset):
        transmitted_packets (int | None | Unset):
    """

    identity: str
    receive_drops: int | Unset | None = UNSET
    receive_errors: int | Unset | None = UNSET
    received_bytes: int | Unset | None = UNSET
    received_packets: int | Unset | None = UNSET
    transmit_drops: int | Unset | None = UNSET
    transmit_errors: int | Unset | None = UNSET
    transmitted_bytes: int | Unset | None = UNSET
    transmitted_packets: int | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        identity = self.identity

        receive_drops: int | Unset | None
        if isinstance(self.receive_drops, Unset):
            receive_drops = UNSET
        else:
            receive_drops = self.receive_drops

        receive_errors: int | Unset | None
        if isinstance(self.receive_errors, Unset):
            receive_errors = UNSET
        else:
            receive_errors = self.receive_errors

        received_bytes: int | Unset | None
        if isinstance(self.received_bytes, Unset):
            received_bytes = UNSET
        else:
            received_bytes = self.received_bytes

        received_packets: int | Unset | None
        if isinstance(self.received_packets, Unset):
            received_packets = UNSET
        else:
            received_packets = self.received_packets

        transmit_drops: int | Unset | None
        if isinstance(self.transmit_drops, Unset):
            transmit_drops = UNSET
        else:
            transmit_drops = self.transmit_drops

        transmit_errors: int | Unset | None
        if isinstance(self.transmit_errors, Unset):
            transmit_errors = UNSET
        else:
            transmit_errors = self.transmit_errors

        transmitted_bytes: int | Unset | None
        if isinstance(self.transmitted_bytes, Unset):
            transmitted_bytes = UNSET
        else:
            transmitted_bytes = self.transmitted_bytes

        transmitted_packets: int | Unset | None
        if isinstance(self.transmitted_packets, Unset):
            transmitted_packets = UNSET
        else:
            transmitted_packets = self.transmitted_packets

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "identity": identity,
            }
        )
        if receive_drops is not UNSET:
            field_dict["receive_drops"] = receive_drops
        if receive_errors is not UNSET:
            field_dict["receive_errors"] = receive_errors
        if received_bytes is not UNSET:
            field_dict["received_bytes"] = received_bytes
        if received_packets is not UNSET:
            field_dict["received_packets"] = received_packets
        if transmit_drops is not UNSET:
            field_dict["transmit_drops"] = transmit_drops
        if transmit_errors is not UNSET:
            field_dict["transmit_errors"] = transmit_errors
        if transmitted_bytes is not UNSET:
            field_dict["transmitted_bytes"] = transmitted_bytes
        if transmitted_packets is not UNSET:
            field_dict["transmitted_packets"] = transmitted_packets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identity = d.pop("identity")

        def _parse_receive_drops(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        receive_drops = _parse_receive_drops(d.pop("receive_drops", UNSET))

        def _parse_receive_errors(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        receive_errors = _parse_receive_errors(d.pop("receive_errors", UNSET))

        def _parse_received_bytes(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        received_bytes = _parse_received_bytes(d.pop("received_bytes", UNSET))

        def _parse_received_packets(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        received_packets = _parse_received_packets(d.pop("received_packets", UNSET))

        def _parse_transmit_drops(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        transmit_drops = _parse_transmit_drops(d.pop("transmit_drops", UNSET))

        def _parse_transmit_errors(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        transmit_errors = _parse_transmit_errors(d.pop("transmit_errors", UNSET))

        def _parse_transmitted_bytes(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        transmitted_bytes = _parse_transmitted_bytes(d.pop("transmitted_bytes", UNSET))

        def _parse_transmitted_packets(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        transmitted_packets = _parse_transmitted_packets(d.pop("transmitted_packets", UNSET))

        network_interface_metrics = cls(
            identity=identity,
            receive_drops=receive_drops,
            receive_errors=receive_errors,
            received_bytes=received_bytes,
            received_packets=received_packets,
            transmit_drops=transmit_drops,
            transmit_errors=transmit_errors,
            transmitted_bytes=transmitted_bytes,
            transmitted_packets=transmitted_packets,
        )

        return network_interface_metrics
