from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PressureLevel")


@_attrs_define(repr=False)
class PressureLevel:
    """
    Attributes:
        avg10_percent (float):
        avg300_percent (float):
        avg60_percent (float):
        total_usec (int):
    """

    avg10_percent: float
    avg300_percent: float
    avg60_percent: float
    total_usec: int

    def to_dict(self) -> dict[str, Any]:
        avg10_percent = self.avg10_percent

        avg300_percent = self.avg300_percent

        avg60_percent = self.avg60_percent

        total_usec = self.total_usec

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "avg10_percent": avg10_percent,
                "avg300_percent": avg300_percent,
                "avg60_percent": avg60_percent,
                "total_usec": total_usec,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avg10_percent = d.pop("avg10_percent")

        avg300_percent = d.pop("avg300_percent")

        avg60_percent = d.pop("avg60_percent")

        total_usec = d.pop("total_usec")

        pressure_level = cls(
            avg10_percent=avg10_percent,
            avg300_percent=avg300_percent,
            avg60_percent=avg60_percent,
            total_usec=total_usec,
        )

        return pressure_level
