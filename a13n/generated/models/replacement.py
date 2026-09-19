from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Replacement")


@_attrs_define(repr=False)
class Replacement:
    """
    Attributes:
        new_string (str):
        old_string (str):
        replace_all (bool | Unset):
    """

    new_string: str
    old_string: str
    replace_all: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        new_string = self.new_string

        old_string = self.old_string

        replace_all = self.replace_all

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "new_string": new_string,
                "old_string": old_string,
            }
        )
        if replace_all is not UNSET:
            field_dict["replace_all"] = replace_all

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        new_string = d.pop("new_string")

        old_string = d.pop("old_string")

        replace_all = d.pop("replace_all", UNSET)

        replacement = cls(
            new_string=new_string,
            old_string=old_string,
            replace_all=replace_all,
        )

        return replacement
