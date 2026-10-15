from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChangeCountTrigger")


@_attrs_define(repr=False)
class ChangeCountTrigger:
    """
    Attributes:
        count (int):
        type_ (Literal['change_count'] | Unset):
    """

    count: int
    type_: Literal["change_count"] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        type_ = self.type_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "count": count,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count")

        type_ = cast(Literal["change_count"] | Unset, d.pop("type", UNSET))
        if type_ != "change_count" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'change_count', got '{type_}'")

        change_count_trigger = cls(
            count=count,
            type_=type_,
        )

        return change_count_trigger
