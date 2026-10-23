from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.run_list_item import RunListItem


T = TypeVar("T", bound="ThreadRunPage")


@_attrs_define(repr=False)
class ThreadRunPage:
    """Newest first; first_number is the first item's 1-based chronological position in the thread.

    Attributes:
        first_number (int):
        items (list[RunListItem]):
        next_cursor (None | str):
        previous_cursor (None | str):
        total (int):
    """

    first_number: int
    items: list[RunListItem]
    next_cursor: str | None
    previous_cursor: str | None
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first_number = self.first_number

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        next_cursor: str | None
        next_cursor = self.next_cursor

        previous_cursor: str | None
        previous_cursor = self.previous_cursor

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "first_number": first_number,
                "items": items,
                "next_cursor": next_cursor,
                "previous_cursor": previous_cursor,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_list_item import RunListItem

        d = dict(src_dict)
        first_number = d.pop("first_number")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = RunListItem.from_dict(items_item_data)

            items.append(items_item)

        def _parse_next_cursor(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor"))

        def _parse_previous_cursor(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        previous_cursor = _parse_previous_cursor(d.pop("previous_cursor"))

        total = d.pop("total")

        thread_run_page = cls(
            first_number=first_number,
            items=items,
            next_cursor=next_cursor,
            previous_cursor=previous_cursor,
            total=total,
        )

        thread_run_page.additional_properties = d
        return thread_run_page

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
