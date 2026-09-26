from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="Complete")


@_attrs_define(repr=False)
class Complete:
    """
    Attributes:
        action (Literal['complete']):
        result (Any):
        tool_call_id (str):
    """

    action: Literal["complete"]
    result: Any
    tool_call_id: str

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        result = self.result

        tool_call_id = self.tool_call_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "action": action,
                "result": result,
                "tool_call_id": tool_call_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = cast(Literal["complete"], d.pop("action"))
        if action != "complete":
            raise ValueError(f"action must match const 'complete', got '{action}'")

        result = d.pop("result")

        tool_call_id = d.pop("tool_call_id")

        complete = cls(
            action=action,
            result=result,
            tool_call_id=tool_call_id,
        )

        return complete
