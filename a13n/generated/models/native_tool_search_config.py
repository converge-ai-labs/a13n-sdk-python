from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..._validation import validate_model
from ..models.native_tool_search_config_strategy_type_0 import NativeToolSearchConfigStrategyType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="NativeToolSearchConfig")


@_attrs_define(repr=False)
class NativeToolSearchConfig:
    """Provider-native discovery; omitted strategy uses the provider default.

    Attributes:
        mode (Literal['native']):
        strategy (NativeToolSearchConfigStrategyType0 | None | Unset):
    """

    mode: Literal["native"]
    strategy: NativeToolSearchConfigStrategyType0 | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        strategy: str | Unset | None
        if isinstance(self.strategy, Unset):
            strategy = UNSET
        elif isinstance(self.strategy, NativeToolSearchConfigStrategyType0):
            strategy = self.strategy.value
        else:
            strategy = self.strategy

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "mode": mode,
            }
        )
        if strategy is not UNSET:
            field_dict["strategy"] = strategy

        validate_model("NativeToolSearchConfig", field_dict)
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        validate_model("NativeToolSearchConfig", src_dict)
        d = dict(src_dict)
        mode = cast(Literal["native"], d.pop("mode"))
        if mode != "native":
            raise ValueError(f"mode must match const 'native', got '{mode}'")

        def _parse_strategy(data: object) -> NativeToolSearchConfigStrategyType0 | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                strategy_type_0 = NativeToolSearchConfigStrategyType0(data)

                return strategy_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NativeToolSearchConfigStrategyType0 | Unset | None, data)

        strategy = _parse_strategy(d.pop("strategy", UNSET))

        native_tool_search_config = cls(
            mode=mode,
            strategy=strategy,
        )

        return native_tool_search_config
