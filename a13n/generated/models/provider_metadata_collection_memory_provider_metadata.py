from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.memory_provider_metadata import MemoryProviderMetadata


T = TypeVar("T", bound="ProviderMetadataCollectionMemoryProviderMetadata")


@_attrs_define(repr=False)
class ProviderMetadataCollectionMemoryProviderMetadata:
    """
    Attributes:
        items (list[MemoryProviderMetadata]):
    """

    items: list[MemoryProviderMetadata]

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
        from ..models.memory_provider_metadata import MemoryProviderMetadata

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = MemoryProviderMetadata.from_dict(items_item_data)

            items.append(items_item)

        provider_metadata_collection_memory_provider_metadata = cls(
            items=items,
        )

        return provider_metadata_collection_memory_provider_metadata
