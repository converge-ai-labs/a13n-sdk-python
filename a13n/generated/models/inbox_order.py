from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="InboxOrder")


@_attrs_define(repr=False)
class InboxOrder:
    """
    Attributes:
        entry_ids (list[str]):
    """

    entry_ids: list[str]

    def to_dict(self) -> dict[str, Any]:
        entry_ids = self.entry_ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "entry_ids": entry_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entry_ids = cast(list[str], d.pop("entry_ids"))

        inbox_order = cls(
            entry_ids=entry_ids,
        )

        return inbox_order
