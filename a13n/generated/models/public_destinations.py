from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="PublicDestinations")


@_attrs_define(repr=False)
class PublicDestinations:
    """
    Attributes:
        mode (Literal['public']):
    """

    mode: Literal["public"]

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "mode": mode,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mode = cast(Literal["public"], d.pop("mode"))
        if mode != "public":
            raise ValueError(f"mode must match const 'public', got '{mode}'")

        public_destinations = cls(
            mode=mode,
        )

        return public_destinations
