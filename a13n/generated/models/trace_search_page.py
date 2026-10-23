from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.trace_search_item import TraceSearchItem


T = TypeVar("T", bound="TraceSearchPage")


@_attrs_define(repr=False)
class TraceSearchPage:
    """
    Attributes:
        collected_at (datetime.datetime):
        items (list[TraceSearchItem]):
        next_cursor (None | str):
        total (int):
    """

    collected_at: datetime.datetime
    items: list[TraceSearchItem]
    next_cursor: str | None
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collected_at = self.collected_at.isoformat()

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        next_cursor: str | None
        next_cursor = self.next_cursor

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collected_at": collected_at,
                "items": items,
                "next_cursor": next_cursor,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trace_search_item import TraceSearchItem

        d = dict(src_dict)
        collected_at = datetime.datetime.fromisoformat(d.pop("collected_at"))

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = TraceSearchItem.from_dict(items_item_data)

            items.append(items_item)

        def _parse_next_cursor(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor"))

        total = d.pop("total")

        trace_search_page = cls(
            collected_at=collected_at,
            items=items,
            next_cursor=next_cursor,
            total=total,
        )

        trace_search_page.additional_properties = d
        return trace_search_page

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
