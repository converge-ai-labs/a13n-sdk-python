from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="DebugHold")


@_attrs_define(repr=False)
class DebugHold:
    """Delay automatic retirement for at most one day; null clears the hold.

    Attributes:
        seconds (int | None):
    """

    seconds: int | None

    def to_dict(self) -> dict[str, Any]:
        seconds: int | None
        seconds = self.seconds

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "seconds": seconds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_seconds(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        seconds = _parse_seconds(d.pop("seconds"))

        debug_hold = cls(
            seconds=seconds,
        )

        return debug_hold
