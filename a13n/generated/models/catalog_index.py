from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_index_item import CatalogIndexItem


T = TypeVar("T", bound="CatalogIndex")


@_attrs_define(repr=False)
class CatalogIndex:
    """
    Attributes:
        items (list[CatalogIndexItem]):
        next_cursor (None | str):
        omitted_sections (list[str] | Unset):
    """

    items: list[CatalogIndexItem]
    next_cursor: str | None
    omitted_sections: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        next_cursor: str | None
        next_cursor = self.next_cursor

        omitted_sections: list[str] | Unset = UNSET
        if not isinstance(self.omitted_sections, Unset):
            omitted_sections = self.omitted_sections

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "items": items,
                "next_cursor": next_cursor,
            }
        )
        if omitted_sections is not UNSET:
            field_dict["omitted_sections"] = omitted_sections

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.catalog_index_item import CatalogIndexItem

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = CatalogIndexItem.from_dict(items_item_data)

            items.append(items_item)

        def _parse_next_cursor(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor"))

        omitted_sections = cast(list[str], d.pop("omitted_sections", UNSET))

        catalog_index = cls(
            items=items,
            next_cursor=next_cursor,
            omitted_sections=omitted_sections,
        )

        catalog_index.additional_properties = d
        return catalog_index

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
