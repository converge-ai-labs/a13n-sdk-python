from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="Patch")


@_attrs_define(repr=False)
class Patch:
    """
    Attributes:
        patch (str):
        type_ (Literal['patch']):
    """

    patch: str
    type_: Literal["patch"]

    def to_dict(self) -> dict[str, Any]:
        patch = self.patch

        type_ = self.type_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "patch": patch,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        patch = d.pop("patch")

        type_ = cast(Literal["patch"], d.pop("type"))
        if type_ != "patch":
            raise ValueError(f"type must match const 'patch', got '{type_}'")

        patch = cls(
            patch=patch,
            type_=type_,
        )

        return patch
