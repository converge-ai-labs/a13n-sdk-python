from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.price_tier_input import PriceTierInput


T = TypeVar("T", bound="PriceComponentInput")


@_attrs_define(repr=False)
class PriceComponentInput:
    """One genai-prices usage dimension and its USD unit price.

    Attributes:
        price (float | str):
        price_key (str):
        tiers (list[PriceTierInput] | Unset):
    """

    price: float | str
    price_key: str
    tiers: list[PriceTierInput] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        price: float | str
        price = self.price

        price_key = self.price_key

        tiers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tiers, Unset):
            tiers = []
            for tiers_item_data in self.tiers:
                tiers_item = tiers_item_data.to_dict()
                tiers.append(tiers_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "price": price,
                "price_key": price_key,
            }
        )
        if tiers is not UNSET:
            field_dict["tiers"] = tiers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.price_tier_input import PriceTierInput

        d = dict(src_dict)

        def _parse_price(data: object) -> float | str:
            return cast(float | str, data)

        price = _parse_price(d.pop("price"))

        price_key = d.pop("price_key")

        _tiers = d.pop("tiers", UNSET)
        tiers: list[PriceTierInput] | Unset = UNSET
        if _tiers is not UNSET:
            tiers = []
            for tiers_item_data in _tiers:
                tiers_item = PriceTierInput.from_dict(tiers_item_data)

                tiers.append(tiers_item)

        price_component_input = cls(
            price=price,
            price_key=price_key,
            tiers=tiers,
        )

        return price_component_input
