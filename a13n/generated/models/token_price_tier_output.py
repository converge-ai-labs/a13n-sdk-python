from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.token_rates_output import TokenRatesOutput


T = TypeVar("T", bound="TokenPriceTierOutput")


@_attrs_define(repr=False)
class TokenPriceTierOutput:
    """Complete rates for requests strictly above the input threshold.

    Attributes:
        rates (TokenRatesOutput): USD per million tokens; null is unknown, never free.
        above (int | None | Unset):
    """

    rates: TokenRatesOutput
    above: int | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        rates = self.rates.to_dict()

        above: int | Unset | None
        if isinstance(self.above, Unset):
            above = UNSET
        else:
            above = self.above

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "rates": rates,
            }
        )
        if above is not UNSET:
            field_dict["above"] = above

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.token_rates_output import TokenRatesOutput

        d = dict(src_dict)
        rates = TokenRatesOutput.from_dict(d.pop("rates"))

        def _parse_above(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        above = _parse_above(d.pop("above", UNSET))

        token_price_tier_output = cls(
            rates=rates,
            above=above,
        )

        return token_price_tier_output
