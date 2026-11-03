from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.automatic_tool_search import AutomaticToolSearch
    from ..models.discovery_source import DiscoverySource
    from ..models.toolset_definition import ToolsetDefinition


T = TypeVar("T", bound="ToolsetCatalog")


@_attrs_define(repr=False)
class ToolsetCatalog:
    """
    Attributes:
        discovery_defaults (AutomaticToolSearch): Group Service-owned sources individually, following the agent's
            selections.
        discovery_sources (list[DiscoverySource]):
        items (list[ToolsetDefinition]):
    """

    discovery_defaults: AutomaticToolSearch
    discovery_sources: list[DiscoverySource]
    items: list[ToolsetDefinition]

    def to_dict(self) -> dict[str, Any]:
        discovery_defaults = self.discovery_defaults.to_dict()

        discovery_sources = []
        for discovery_sources_item_data in self.discovery_sources:
            discovery_sources_item = discovery_sources_item_data.to_dict()
            discovery_sources.append(discovery_sources_item)

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "discovery_defaults": discovery_defaults,
                "discovery_sources": discovery_sources,
                "items": items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.automatic_tool_search import AutomaticToolSearch
        from ..models.discovery_source import DiscoverySource
        from ..models.toolset_definition import ToolsetDefinition

        d = dict(src_dict)
        discovery_defaults = AutomaticToolSearch.from_dict(d.pop("discovery_defaults"))

        discovery_sources = []
        _discovery_sources = d.pop("discovery_sources")
        for discovery_sources_item_data in _discovery_sources:
            discovery_sources_item = DiscoverySource.from_dict(discovery_sources_item_data)

            discovery_sources.append(discovery_sources_item)

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = ToolsetDefinition.from_dict(items_item_data)

            items.append(items_item)

        toolset_catalog = cls(
            discovery_defaults=discovery_defaults,
            discovery_sources=discovery_sources,
            items=items,
        )

        return toolset_catalog
