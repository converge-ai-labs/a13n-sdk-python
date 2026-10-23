from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DaemonMetrics")


@_attrs_define(repr=False)
class DaemonMetrics:
    """
    Attributes:
        connections (int):
        sessions (int):
        processes (int | None | Unset):
        retained_output_bytes (int | None | Unset):
        transfers (int | None | Unset):
    """

    connections: int
    sessions: int
    processes: int | Unset | None = UNSET
    retained_output_bytes: int | Unset | None = UNSET
    transfers: int | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        connections = self.connections

        sessions = self.sessions

        processes: int | Unset | None
        if isinstance(self.processes, Unset):
            processes = UNSET
        else:
            processes = self.processes

        retained_output_bytes: int | Unset | None
        if isinstance(self.retained_output_bytes, Unset):
            retained_output_bytes = UNSET
        else:
            retained_output_bytes = self.retained_output_bytes

        transfers: int | Unset | None
        if isinstance(self.transfers, Unset):
            transfers = UNSET
        else:
            transfers = self.transfers

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "connections": connections,
                "sessions": sessions,
            }
        )
        if processes is not UNSET:
            field_dict["processes"] = processes
        if retained_output_bytes is not UNSET:
            field_dict["retained_output_bytes"] = retained_output_bytes
        if transfers is not UNSET:
            field_dict["transfers"] = transfers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connections = d.pop("connections")

        sessions = d.pop("sessions")

        def _parse_processes(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        processes = _parse_processes(d.pop("processes", UNSET))

        def _parse_retained_output_bytes(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        retained_output_bytes = _parse_retained_output_bytes(d.pop("retained_output_bytes", UNSET))

        def _parse_transfers(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        transfers = _parse_transfers(d.pop("transfers", UNSET))

        daemon_metrics = cls(
            connections=connections,
            sessions=sessions,
            processes=processes,
            retained_output_bytes=retained_output_bytes,
            transfers=transfers,
        )

        return daemon_metrics
