from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

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
    """

    prices: list[PriceComponentOutput]
    rule_id: str
    constraint: PricingConstraint | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        prices = []
        for prices_item_data in self.prices:
            prices_item = prices_item_data.to_dict()
            prices.append(prices_item)

        rule_id = self.rule_id

        constraint: dict[str, Any] | Unset = UNSET
        if not isinstance(self.constraint, Unset):
            constraint = self.constraint.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "prices": prices,
                "rule_id": rule_id,
            }
        )
        if constraint is not UNSET:
            field_dict["constraint"] = constraint

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

        model_price_rule_output = cls(
            prices=prices,
            rule_id=rule_id,
            constraint=constraint,
        )

        return model_price_rule_output
