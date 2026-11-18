from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.app_view import AppView


T = TypeVar("T", bound="AppPlugins")


@_attrs_define(repr=False)
class AppPlugins:
    """
    Attributes:
        id (str):
        items (list[AppView]):
        permissions (list[str]):
        version (int):
    """

    id: str
    items: list[AppView]
    permissions: list[str]
    version: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        permissions = self.permissions

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "items": items,
                "permissions": permissions,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_view import AppView

        d = dict(src_dict)
        id = d.pop("id")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = AppView.from_dict(items_item_data)

            items.append(items_item)

        permissions = cast(list[str], d.pop("permissions"))

        version = d.pop("version")

        app_plugins = cls(
            id=id,
            items=items,
            permissions=permissions,
            version=version,
        )

        app_plugins.additional_properties = d
        return app_plugins

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
