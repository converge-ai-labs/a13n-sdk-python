from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NoResponse")


@_attrs_define(repr=False)
class NoResponse:
    """
    Attributes:
        tool_call_id (str):
        action (Literal['no_response'] | Unset):
    """

    tool_call_id: str
    action: Literal["no_response"] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        tool_call_id = self.tool_call_id

        action = self.action

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "tool_call_id": tool_call_id,
            }
        )
        if action is not UNSET:
            field_dict["action"] = action

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tool_call_id = d.pop("tool_call_id")

        action = cast(Literal["no_response"] | Unset, d.pop("action", UNSET))
        if action != "no_response" and not isinstance(action, Unset):
            raise ValueError(f"action must match const 'no_response', got '{action}'")

        no_response = cls(
            tool_call_id=tool_call_id,
            action=action,
        )

        return no_response
