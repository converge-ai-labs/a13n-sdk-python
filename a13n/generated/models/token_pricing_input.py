from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.token_price_tier_input import TokenPriceTierInput


T = TypeVar("T", bound="TokenPricingInput")


@_attrs_define(repr=False)
class TokenPricingInput:
    """Cliff prices: one input-length tier prices the entire request.

    Attributes:
        tiers (list[TokenPriceTierInput]):
        currency (Literal['USD'] | Unset):
        tier_basis (Literal['input_tokens'] | Unset):
        unit (Literal['million_tokens'] | Unset):
    """

    tiers: list[TokenPriceTierInput]
    currency: Literal["USD"] | Unset = UNSET
    tier_basis: Literal["input_tokens"] | Unset = UNSET
    unit: Literal["million_tokens"] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        tiers = []
        for tiers_item_data in self.tiers:
            tiers_item = tiers_item_data.to_dict()
            tiers.append(tiers_item)

        currency = self.currency

        tier_basis = self.tier_basis

        unit = self.unit

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "tiers": tiers,
            }
        )
        if currency is not UNSET:
            field_dict["currency"] = currency
        if tier_basis is not UNSET:
            field_dict["tier_basis"] = tier_basis
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.token_price_tier_input import TokenPriceTierInput

        d = dict(src_dict)
        tiers = []
        _tiers = d.pop("tiers")
        for tiers_item_data in _tiers:
            tiers_item = TokenPriceTierInput.from_dict(tiers_item_data)

            tiers.append(tiers_item)

        currency = cast(Literal["USD"] | Unset, d.pop("currency", UNSET))
        if currency != "USD" and not isinstance(currency, Unset):
            raise ValueError(f"currency must match const 'USD', got '{currency}'")

        tier_basis = cast(Literal["input_tokens"] | Unset, d.pop("tier_basis", UNSET))
        if tier_basis != "input_tokens" and not isinstance(tier_basis, Unset):
            raise ValueError(f"tier_basis must match const 'input_tokens', got '{tier_basis}'")

        unit = cast(Literal["million_tokens"] | Unset, d.pop("unit", UNSET))
        if unit != "million_tokens" and not isinstance(unit, Unset):
            raise ValueError(f"unit must match const 'million_tokens', got '{unit}'")

        token_pricing_input = cls(
            tiers=tiers,
            currency=currency,
            tier_basis=tier_basis,
            unit=unit,
        )

        return token_pricing_input
