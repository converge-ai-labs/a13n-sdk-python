from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.model_capability import ModelCapability
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.token_pricing_output import TokenPricingOutput


T = TypeVar("T", bound="ModelDeclarationsOutput")


@_attrs_define(repr=False)
class ModelDeclarationsOutput:
    """Harness-facing facts and authoring choices declared for one saved Model.

    Attributes:
        capabilities (list[ModelCapability] | Unset):
        context_window_tokens (int | None | Unset):
        pricing (None | TokenPricingOutput | Unset):
        structured_output (bool | None | Unset):
        supports_tools (bool | None | Unset):
    """

    capabilities: list[ModelCapability] | Unset = UNSET
    context_window_tokens: int | Unset | None = UNSET
    pricing: TokenPricingOutput | Unset | None = UNSET
    structured_output: bool | Unset | None = UNSET
    supports_tools: bool | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.token_pricing_output import TokenPricingOutput

        capabilities: list[str] | Unset = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = []
            for capabilities_item_data in self.capabilities:
                capabilities_item = capabilities_item_data.value
                capabilities.append(capabilities_item)

        context_window_tokens: int | Unset | None
        if isinstance(self.context_window_tokens, Unset):
            context_window_tokens = UNSET
        else:
            context_window_tokens = self.context_window_tokens

        pricing: dict[str, Any] | Unset | None
        if isinstance(self.pricing, Unset):
            pricing = UNSET
        elif isinstance(self.pricing, TokenPricingOutput):
            pricing = self.pricing.to_dict()
        else:
            pricing = self.pricing

        structured_output: bool | Unset | None
        if isinstance(self.structured_output, Unset):
            structured_output = UNSET
        else:
            structured_output = self.structured_output

        supports_tools: bool | Unset | None
        if isinstance(self.supports_tools, Unset):
            supports_tools = UNSET
        else:
            supports_tools = self.supports_tools

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities
        if context_window_tokens is not UNSET:
            field_dict["context_window_tokens"] = context_window_tokens
        if pricing is not UNSET:
            field_dict["pricing"] = pricing
        if structured_output is not UNSET:
            field_dict["structured_output"] = structured_output
        if supports_tools is not UNSET:
            field_dict["supports_tools"] = supports_tools

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.token_pricing_output import TokenPricingOutput

        d = dict(src_dict)
        _capabilities = d.pop("capabilities", UNSET)
        capabilities: list[ModelCapability] | Unset = UNSET
        if _capabilities is not UNSET:
            capabilities = []
            for capabilities_item_data in _capabilities:
                capabilities_item = ModelCapability(capabilities_item_data)

                capabilities.append(capabilities_item)

        def _parse_context_window_tokens(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        context_window_tokens = _parse_context_window_tokens(d.pop("context_window_tokens", UNSET))

        def _parse_pricing(data: object) -> TokenPricingOutput | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pricing_type_0 = TokenPricingOutput.from_dict(data)

                return pricing_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(TokenPricingOutput | Unset | None, data)

        pricing = _parse_pricing(d.pop("pricing", UNSET))

        def _parse_structured_output(data: object) -> bool | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | Unset | None, data)

        structured_output = _parse_structured_output(d.pop("structured_output", UNSET))

        def _parse_supports_tools(data: object) -> bool | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | Unset | None, data)

        supports_tools = _parse_supports_tools(d.pop("supports_tools", UNSET))

        model_declarations_output = cls(
            capabilities=capabilities,
            context_window_tokens=context_window_tokens,
            pricing=pricing,
            structured_output=structured_output,
            supports_tools=supports_tools,
        )

        return model_declarations_output
