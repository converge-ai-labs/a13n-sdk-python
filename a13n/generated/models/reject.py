from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Reject")


@_attrs_define(repr=False)
class Reject:
    """
    Attributes:
        action (Literal['reject']):
        tool_call_id (str):
        reason (None | str | Unset):
    """

    action: Literal["reject"]
    tool_call_id: str
    reason: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        tool_call_id = self.tool_call_id

        reason: str | Unset | None
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "action": action,
                "tool_call_id": tool_call_id,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = cast(Literal["reject"], d.pop("action"))
        if action != "reject":
            raise ValueError(f"action must match const 'reject', got '{action}'")

        tool_call_id = d.pop("tool_call_id")

        def _parse_reason(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        reject = cls(
            action=action,
            tool_call_id=tool_call_id,
            reason=reason,
        )

        return reject
