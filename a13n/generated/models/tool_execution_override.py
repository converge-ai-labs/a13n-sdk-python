from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.tool_execution_override_mode_type_0 import ToolExecutionOverrideModeType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="ToolExecutionOverride")


@_attrs_define(repr=False)
class ToolExecutionOverride:
    """
    Attributes:
        foreground_wait_seconds (float | None | Unset):
        mode (None | ToolExecutionOverrideModeType0 | Unset):
    """

    foreground_wait_seconds: float | Unset | None = UNSET
    mode: ToolExecutionOverrideModeType0 | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        foreground_wait_seconds: float | Unset | None
        if isinstance(self.foreground_wait_seconds, Unset):
            foreground_wait_seconds = UNSET
        else:
            foreground_wait_seconds = self.foreground_wait_seconds

        mode: str | Unset | None
        if isinstance(self.mode, Unset):
            mode = UNSET
        elif isinstance(self.mode, ToolExecutionOverrideModeType0):
            mode = self.mode.value
        else:
            mode = self.mode

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if foreground_wait_seconds is not UNSET:
            field_dict["foreground_wait_seconds"] = foreground_wait_seconds
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_foreground_wait_seconds(data: object) -> float | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | Unset | None, data)

        foreground_wait_seconds = _parse_foreground_wait_seconds(d.pop("foreground_wait_seconds", UNSET))

        def _parse_mode(data: object) -> ToolExecutionOverrideModeType0 | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mode_type_0 = ToolExecutionOverrideModeType0(data)

                return mode_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ToolExecutionOverrideModeType0 | Unset | None, data)

        mode = _parse_mode(d.pop("mode", UNSET))

        tool_execution_override = cls(
            foreground_wait_seconds=foreground_wait_seconds,
            mode=mode,
        )

        return tool_execution_override
