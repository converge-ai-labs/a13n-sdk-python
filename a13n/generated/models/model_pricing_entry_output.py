from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_price_rule_output import ModelPriceRuleOutput


T = TypeVar("T", bound="ModelPricingEntryOutput")


@_attrs_define(repr=False)
class ModelPricingEntryOutput:
    """Complete pricing declaration for one provider-qualified model.

    Attributes:
        model (str):
        provider (str):
        rules (list[ModelPriceRuleOutput]):
        source (str):
        source_revision (str):
        context_window (int | None | Unset):
        source_url (None | str | Unset):
    """

    model: str
    provider: str
    rules: list[ModelPriceRuleOutput]
    source: str
    source_revision: str
    context_window: int | Unset | None = UNSET
    source_url: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        model = self.model

        provider = self.provider

        rules = []
        for rules_item_data in self.rules:
            rules_item = rules_item_data.to_dict()
            rules.append(rules_item)

        source = self.source

        source_revision = self.source_revision

        context_window: int | Unset | None
        if isinstance(self.context_window, Unset):
            context_window = UNSET
        else:
            context_window = self.context_window

        source_url: str | Unset | None
        if isinstance(self.source_url, Unset):
            source_url = UNSET
        else:
            source_url = self.source_url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "model": model,
                "provider": provider,
                "rules": rules,
                "source": source,
                "source_revision": source_revision,
            }
        )
        if context_window is not UNSET:
            field_dict["context_window"] = context_window
        if source_url is not UNSET:
            field_dict["source_url"] = source_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_price_rule_output import ModelPriceRuleOutput

        d = dict(src_dict)
        model = d.pop("model")

        provider = d.pop("provider")

        rules = []
        _rules = d.pop("rules")
        for rules_item_data in _rules:
            rules_item = ModelPriceRuleOutput.from_dict(rules_item_data)

            rules.append(rules_item)

        source = d.pop("source")

        source_revision = d.pop("source_revision")

        def _parse_context_window(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        context_window = _parse_context_window(d.pop("context_window", UNSET))

        def _parse_source_url(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        source_url = _parse_source_url(d.pop("source_url", UNSET))

        model_pricing_entry_output = cls(
            model=model,
            provider=provider,
            rules=rules,
            source=source,
            source_revision=source_revision,
            context_window=context_window,
            source_url=source_url,
        )

        return model_pricing_entry_output
