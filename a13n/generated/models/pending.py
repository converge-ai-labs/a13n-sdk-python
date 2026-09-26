from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.pending_item import PendingItem


T = TypeVar("T", bound="Pending")


@_attrs_define(repr=False)
class Pending:
    """Public projection of the exact sealed pending set; the native requests live in the state object.

    Attributes:
        items (list[PendingItem]):
    """

    items: list[PendingItem]

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "items": items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pending_item import PendingItem

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = PendingItem.from_dict(items_item_data)

            items.append(items_item)

        pending = cls(
            items=items,
        )

        return pending
