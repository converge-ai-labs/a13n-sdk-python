from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.price_tier_output import PriceTierOutput


T = TypeVar("T", bound="PriceComponentOutput")


@_attrs_define(repr=False)
class PriceComponentOutput:
    """One genai-prices usage dimension and its USD unit price.

    Attributes:
        price (str):
        price_key (str):
        tiers (list[PriceTierOutput] | Unset):
    """

    price: str
    price_key: str
    tiers: list[PriceTierOutput] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
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
        from ..models.price_tier_output import PriceTierOutput

        d = dict(src_dict)
        price = d.pop("price")

        price_key = d.pop("price_key")

        _tiers = d.pop("tiers", UNSET)
        tiers: list[PriceTierOutput] | Unset = UNSET
        if _tiers is not UNSET:
            tiers = []
            for tiers_item_data in _tiers:
                tiers_item = PriceTierOutput.from_dict(tiers_item_data)

                tiers.append(tiers_item)

        price_component_output = cls(
            price=price,
            price_key=price_key,
            tiers=tiers,
        )

        return price_component_output
