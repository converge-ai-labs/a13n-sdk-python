from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="PriceTierInput")


@_attrs_define(repr=False)
class PriceTierInput:
    """One cliff-pricing threshold applied to the complete usage quantity.

    Attributes:
        price (float | str):
        start (int):
    """

    price: float | str
    start: int

    def to_dict(self) -> dict[str, Any]:
        price: float | str
        price = self.price

        start = self.start

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "price": price,
                "start": start,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_price(data: object) -> float | str:
            return cast(float | str, data)

        price = _parse_price(d.pop("price"))

        start = d.pop("start")

        price_tier_input = cls(
            price=price,
            start=start,
        )

        return price_tier_input
