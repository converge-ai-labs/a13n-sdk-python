from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="Position")


@_attrs_define(repr=False)
class Position:
    """
    Attributes:
        h (int):
        w (int):
        x (int):
        y (int):
    """

    h: int
    w: int
    x: int
    y: int

    def to_dict(self) -> dict[str, Any]:
        h = self.h

        w = self.w

        x = self.x

        y = self.y

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "h": h,
                "w": w,
                "x": x,
                "y": y,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        h = d.pop("h")

        w = d.pop("w")

        x = d.pop("x")

        y = d.pop("y")

        position = cls(
            h=h,
            w=w,
            x=x,
            y=y,
        )

        return position
