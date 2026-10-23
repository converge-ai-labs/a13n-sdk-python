from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vercel_option import VercelOption


T = TypeVar("T", bound="VercelOptions")


@_attrs_define(repr=False)
class VercelOptions:
    """
    Attributes:
        items (list[VercelOption]):
        cursor (int | None | Unset):
    """

    items: list[VercelOption]
    cursor: int | Unset | None = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        cursor: int | Unset | None
        if isinstance(self.cursor, Unset):
            cursor = UNSET
        else:
            cursor = self.cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "items": items,
            }
        )
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vercel_option import VercelOption

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = VercelOption.from_dict(items_item_data)

            items.append(items_item)

        def _parse_cursor(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        cursor = _parse_cursor(d.pop("cursor", UNSET))

        vercel_options = cls(
            items=items,
            cursor=cursor,
        )

        vercel_options.additional_properties = d
        return vercel_options

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
