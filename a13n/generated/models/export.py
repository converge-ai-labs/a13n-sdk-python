from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.export_protocol import ExportProtocol
from ..types import UNSET, Unset

T = TypeVar("T", bound="Export")


@_attrs_define(repr=False)
class Export:
    """
    Attributes:
        endpoint (str):
        interval_seconds (int | Unset):
        protocol (ExportProtocol | Unset):
    """

    endpoint: str
    interval_seconds: int | Unset = UNSET
    protocol: ExportProtocol | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        endpoint = self.endpoint

        interval_seconds = self.interval_seconds

        protocol: str | Unset = UNSET
        if not isinstance(self.protocol, Unset):
            protocol = self.protocol.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "endpoint": endpoint,
            }
        )
        if interval_seconds is not UNSET:
            field_dict["interval_seconds"] = interval_seconds
        if protocol is not UNSET:
            field_dict["protocol"] = protocol

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        endpoint = d.pop("endpoint")

        interval_seconds = d.pop("interval_seconds", UNSET)

        _protocol = d.pop("protocol", UNSET)
        protocol: ExportProtocol | Unset
        if isinstance(_protocol, Unset):
            protocol = UNSET
        else:
            protocol = ExportProtocol(_protocol)

        export = cls(
            endpoint=endpoint,
            interval_seconds=interval_seconds,
            protocol=protocol,
        )

        return export
