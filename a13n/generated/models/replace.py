from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="Replace")


@_attrs_define(repr=False)
class Replace:
    """
    Attributes:
        text (str):
        type_ (Literal['replace']):
    """

    text: str
    type_: Literal["replace"]

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        type_ = self.type_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "text": text,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text = d.pop("text")

        type_ = cast(Literal["replace"], d.pop("type"))
        if type_ != "replace":
            raise ValueError(f"type must match const 'replace', got '{type_}'")

        replace = cls(
            text=text,
            type_=type_,
        )

        return replace
