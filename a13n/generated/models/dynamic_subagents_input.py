from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DynamicSubagentsInput")


@_attrs_define(repr=False)
class DynamicSubagentsInput:
    """Root-only task-specific delegation within the parent's capability boundary.

    Attributes:
        allowed_models (list[str] | Unset):
        default_model (None | str | Unset):
        default_thinking (bool | None | str | Unset):
        enabled (bool | Unset):
    """

    allowed_models: list[str] | Unset = UNSET
    default_model: str | Unset | None = UNSET
    default_thinking: bool | str | Unset | None = UNSET
    enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        allowed_models: list[str] | Unset = UNSET
        if not isinstance(self.allowed_models, Unset):
            allowed_models = self.allowed_models

        default_model: str | Unset | None
        if isinstance(self.default_model, Unset):
            default_model = UNSET
        else:
            default_model = self.default_model

        default_thinking: bool | str | Unset | None
        if isinstance(self.default_thinking, Unset):
            default_thinking = UNSET
        else:
            default_thinking = self.default_thinking

        enabled = self.enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if allowed_models is not UNSET:
            field_dict["allowed_models"] = allowed_models
        if default_model is not UNSET:
            field_dict["default_model"] = default_model
        if default_thinking is not UNSET:
            field_dict["default_thinking"] = default_thinking
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allowed_models = cast(list[str], d.pop("allowed_models", UNSET))

        def _parse_default_model(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        default_model = _parse_default_model(d.pop("default_model", UNSET))

        def _parse_default_thinking(data: object) -> bool | str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | str | Unset | None, data)

        default_thinking = _parse_default_thinking(d.pop("default_thinking", UNSET))

        enabled = d.pop("enabled", UNSET)

        dynamic_subagents_input = cls(
            allowed_models=allowed_models,
            default_model=default_model,
            default_thinking=default_thinking,
            enabled=enabled,
        )

        return dynamic_subagents_input
