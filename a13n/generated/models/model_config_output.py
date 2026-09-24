from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.harness_model_characteristics_output import HarnessModelCharacteristicsOutput


T = TypeVar("T", bound="ModelConfigOutput")


@_attrs_define(repr=False)
class ModelConfigOutput:
    """
    Attributes:
        model_api (str):
        model_name (str):
        characteristics (HarnessModelCharacteristicsOutput | Unset): Resolved Harness characteristics of the active
            Agent model.
        max_tokens (int | None | Unset):
        temperature (float | None | Unset):
        top_p (float | None | Unset):
    """

    model_api: str
    model_name: str
    characteristics: HarnessModelCharacteristicsOutput | Unset = UNSET
    max_tokens: int | Unset | None = UNSET
    temperature: float | Unset | None = UNSET
    top_p: float | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        model_api = self.model_api

        model_name = self.model_name

        characteristics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.characteristics, Unset):
            characteristics = self.characteristics.to_dict()

        max_tokens: int | Unset | None
        if isinstance(self.max_tokens, Unset):
            max_tokens = UNSET
        else:
            max_tokens = self.max_tokens

        temperature: float | Unset | None
        if isinstance(self.temperature, Unset):
            temperature = UNSET
        else:
            temperature = self.temperature

        top_p: float | Unset | None
        if isinstance(self.top_p, Unset):
            top_p = UNSET
        else:
            top_p = self.top_p

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "model_api": model_api,
                "model_name": model_name,
            }
        )
        if characteristics is not UNSET:
            field_dict["characteristics"] = characteristics
        if max_tokens is not UNSET:
            field_dict["max_tokens"] = max_tokens
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if top_p is not UNSET:
            field_dict["top_p"] = top_p

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.harness_model_characteristics_output import HarnessModelCharacteristicsOutput

        d = dict(src_dict)
        model_api = d.pop("model_api")

        model_name = d.pop("model_name")

        _characteristics = d.pop("characteristics", UNSET)
        characteristics: HarnessModelCharacteristicsOutput | Unset
        if isinstance(_characteristics, Unset):
            characteristics = UNSET
        else:
            characteristics = HarnessModelCharacteristicsOutput.from_dict(_characteristics)

        def _parse_max_tokens(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        max_tokens = _parse_max_tokens(d.pop("max_tokens", UNSET))

        def _parse_temperature(data: object) -> float | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | Unset | None, data)

        temperature = _parse_temperature(d.pop("temperature", UNSET))

        def _parse_top_p(data: object) -> float | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | Unset | None, data)

        top_p = _parse_top_p(d.pop("top_p", UNSET))

        model_config_output = cls(
            model_api=model_api,
            model_name=model_name,
            characteristics=characteristics,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
        )

        return model_config_output
