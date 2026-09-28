from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="Approve")


@_attrs_define(repr=False)
class Approve:
    """
    Attributes:
        action (Literal['approve']):
    """

    action: Literal["approve"]

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "action": action,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = cast(Literal["approve"], d.pop("action"))
        if action != "approve":
            raise ValueError(f"action must match const 'approve', got '{action}'")

        approve = cls(
            action=action,
        )

        return approve
