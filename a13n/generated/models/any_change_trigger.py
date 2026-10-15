from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnyChangeTrigger")


@_attrs_define(repr=False)
class AnyChangeTrigger:
    """
    Attributes:
        type_ (Literal['any_change'] | Unset):
    """

    type_: Literal["any_change"] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["any_change"] | Unset, d.pop("type", UNSET))
        if type_ != "any_change" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'any_change', got '{type_}'")

        any_change_trigger = cls(
            type_=type_,
        )

        return any_change_trigger
