from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.price_component_output import PriceComponentOutput
    from ..models.pricing_constraint import PricingConstraint


T = TypeVar("T", bound="ModelPriceRuleOutput")


@_attrs_define(repr=False)
class ModelPriceRuleOutput:
    """One complete set of prices and the condition selecting it.

    Attributes:
        prices (list[PriceComponentOutput]):
        rule_id (str):
        constraint (PricingConstraint | Unset): A stable condition selecting one ordered model price rule.
        max_input_tokens (int | None | Unset):
        service_tier (None | str | Unset):
    """

    prices: list[PriceComponentOutput]
    rule_id: str
    constraint: PricingConstraint | Unset = UNSET
    max_input_tokens: int | Unset | None = UNSET
    service_tier: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        prices = []
        for prices_item_data in self.prices:
            prices_item = prices_item_data.to_dict()
            prices.append(prices_item)

        rule_id = self.rule_id

        constraint: dict[str, Any] | Unset = UNSET
        if not isinstance(self.constraint, Unset):
            constraint = self.constraint.to_dict()

        max_input_tokens: int | Unset | None
        if isinstance(self.max_input_tokens, Unset):
            max_input_tokens = UNSET
        else:
            max_input_tokens = self.max_input_tokens

        service_tier: str | Unset | None
        if isinstance(self.service_tier, Unset):
            service_tier = UNSET
        else:
            service_tier = self.service_tier

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "prices": prices,
                "rule_id": rule_id,
            }
        )
        if constraint is not UNSET:
            field_dict["constraint"] = constraint
        if max_input_tokens is not UNSET:
            field_dict["max_input_tokens"] = max_input_tokens
        if service_tier is not UNSET:
            field_dict["service_tier"] = service_tier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.price_component_output import PriceComponentOutput
        from ..models.pricing_constraint import PricingConstraint

        d = dict(src_dict)
        prices = []
        _prices = d.pop("prices")
        for prices_item_data in _prices:
            prices_item = PriceComponentOutput.from_dict(prices_item_data)

            prices.append(prices_item)

        rule_id = d.pop("rule_id")

        _constraint = d.pop("constraint", UNSET)
        constraint: PricingConstraint | Unset
        if isinstance(_constraint, Unset):
            constraint = UNSET
        else:
            constraint = PricingConstraint.from_dict(_constraint)

        def _parse_max_input_tokens(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        max_input_tokens = _parse_max_input_tokens(d.pop("max_input_tokens", UNSET))

        def _parse_service_tier(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        service_tier = _parse_service_tier(d.pop("service_tier", UNSET))

        model_price_rule_output = cls(
            prices=prices,
            rule_id=rule_id,
            constraint=constraint,
            max_input_tokens=max_input_tokens,
            service_tier=service_tier,
        )

        return model_price_rule_output
