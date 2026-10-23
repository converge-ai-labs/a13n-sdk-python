from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.span import Span
    from ..models.span_overview import SpanOverview
    from ..models.span_summary import SpanSummary


T = TypeVar("T", bound="SpanReadPage")


@_attrs_define(repr=False)
class SpanReadPage:
    """
    Attributes:
        items (list[Span | SpanOverview | SpanSummary]):
        next_cursor (None | str):
    """

    items: list[Span | SpanOverview | SpanSummary]
    next_cursor: str | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.span_overview import SpanOverview
        from ..models.span_summary import SpanSummary

        items = []
        for items_item_data in self.items:
            items_item: dict[str, Any]
            if isinstance(items_item_data, SpanSummary):
                items_item = items_item_data.to_dict()
            elif isinstance(items_item_data, SpanOverview):
                items_item = items_item_data.to_dict()
            else:
                items_item = items_item_data.to_dict()

            items.append(items_item)

        next_cursor: str | None
        next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "items": items,
                "next_cursor": next_cursor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.span import Span
        from ..models.span_overview import SpanOverview
        from ..models.span_summary import SpanSummary

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:

            def _parse_items_item(data: object) -> Span | SpanOverview | SpanSummary:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    items_item_type_0 = SpanSummary.from_dict(data)

                    return items_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    items_item_type_1 = SpanOverview.from_dict(data)

                    return items_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                items_item_type_2 = Span.from_dict(data)

                return items_item_type_2

            items_item = _parse_items_item(items_item_data)

            items.append(items_item)

        def _parse_next_cursor(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor"))

        span_read_page = cls(
            items=items,
            next_cursor=next_cursor,
        )

        span_read_page.additional_properties = d
        return span_read_page

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
