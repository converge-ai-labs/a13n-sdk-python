from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.definition import Definition
    from ..models.definition_reference import DefinitionReference


T = TypeVar("T", bound="Definitions")


@_attrs_define(repr=False)
class Definitions:
    """
    Attributes:
        items (list[Definition] | Unset):
        missing (list[str] | Unset):
        oversized (list[DefinitionReference] | Unset):
    """

    items: list[Definition] | Unset = UNSET
    missing: list[str] | Unset = UNSET
    oversized: list[DefinitionReference] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        missing: list[str] | Unset = UNSET
        if not isinstance(self.missing, Unset):
            missing = self.missing

        oversized: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.oversized, Unset):
            oversized = []
            for oversized_item_data in self.oversized:
                oversized_item = oversized_item_data.to_dict()
                oversized.append(oversized_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if items is not UNSET:
            field_dict["items"] = items
        if missing is not UNSET:
            field_dict["missing"] = missing
        if oversized is not UNSET:
            field_dict["oversized"] = oversized

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.definition import Definition
        from ..models.definition_reference import DefinitionReference

        d = dict(src_dict)
        _items = d.pop("items", UNSET)
        items: list[Definition] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = Definition.from_dict(items_item_data)

                items.append(items_item)

        missing = cast(list[str], d.pop("missing", UNSET))

        _oversized = d.pop("oversized", UNSET)
        oversized: list[DefinitionReference] | Unset = UNSET
        if _oversized is not UNSET:
            oversized = []
            for oversized_item_data in _oversized:
                oversized_item = DefinitionReference.from_dict(oversized_item_data)

                oversized.append(oversized_item)

        definitions = cls(
            items=items,
            missing=missing,
            oversized=oversized,
        )

        definitions.additional_properties = d
        return definitions

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
