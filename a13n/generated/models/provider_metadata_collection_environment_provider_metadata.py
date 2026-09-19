from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.environment_provider_metadata import EnvironmentProviderMetadata


T = TypeVar("T", bound="ProviderMetadataCollectionEnvironmentProviderMetadata")


@_attrs_define(repr=False)
class ProviderMetadataCollectionEnvironmentProviderMetadata:
    """
    Attributes:
        items (list[EnvironmentProviderMetadata]):
    """

    items: list[EnvironmentProviderMetadata]

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
        from ..models.environment_provider_metadata import EnvironmentProviderMetadata

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = EnvironmentProviderMetadata.from_dict(items_item_data)

            items.append(items_item)

        provider_metadata_collection_environment_provider_metadata = cls(
            items=items,
        )

        return provider_metadata_collection_environment_provider_metadata
