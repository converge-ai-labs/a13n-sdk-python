from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.steering import Steering
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tool_execution_override import ToolExecutionOverride


T = TypeVar("T", bound="ExecutionOverride")


@_attrs_define(repr=False)
class ExecutionOverride:
    """Sparse choices: null inherits; Thread PATCH distinguishes omission from null.

    Attributes:
        steering (None | Steering | Unset):
        tools (None | ToolExecutionOverride | Unset):
    """

    steering: Steering | Unset | None = UNSET
    tools: ToolExecutionOverride | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.tool_execution_override import ToolExecutionOverride

        steering: str | Unset | None
        if isinstance(self.steering, Unset):
            steering = UNSET
        elif isinstance(self.steering, Steering):
            steering = self.steering.value
        else:
            steering = self.steering

        tools: dict[str, Any] | Unset | None
        if isinstance(self.tools, Unset):
            tools = UNSET
        elif isinstance(self.tools, ToolExecutionOverride):
            tools = self.tools.to_dict()
        else:
            tools = self.tools

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if steering is not UNSET:
            field_dict["steering"] = steering
        if tools is not UNSET:
            field_dict["tools"] = tools

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tool_execution_override import ToolExecutionOverride

        d = dict(src_dict)

        def _parse_steering(data: object) -> Steering | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                steering_type_0 = Steering(data)

                return steering_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Steering | Unset | None, data)

        steering = _parse_steering(d.pop("steering", UNSET))

        def _parse_tools(data: object) -> ToolExecutionOverride | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tools_type_0 = ToolExecutionOverride.from_dict(data)

                return tools_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ToolExecutionOverride | Unset | None, data)

        tools = _parse_tools(d.pop("tools", UNSET))

        execution_override = cls(
            steering=steering,
            tools=tools,
        )

        return execution_override
