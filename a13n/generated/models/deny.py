from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Deny")


@_attrs_define(repr=False)
class Deny:
    """
    Attributes:
        action (Literal['deny']):
        reason (None | str | Unset):
    """

    action: Literal["deny"]
    reason: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        reason: str | Unset | None
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "action": action,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = cast(Literal["deny"], d.pop("action"))
        if action != "deny":
            raise ValueError(f"action must match const 'deny', got '{action}'")

        def _parse_reason(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        deny = cls(
            action=action,
            reason=reason,
        )

        return deny
