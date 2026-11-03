from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.builtin_toolset_key import BuiltinToolsetKey
from ..types import UNSET, Unset

T = TypeVar("T", bound="AutomaticToolSearch")


@_attrs_define(repr=False)
class AutomaticToolSearch:
    """Group Service-owned sources individually, following the agent's selections.

    Attributes:
        capabilities (list[BuiltinToolsetKey] | Unset):
        connections (bool | Unset):
        exclude_connections (list[str] | Unset):
        exclude_platform (bool | Unset):
    """

    capabilities: list[BuiltinToolsetKey] | Unset = UNSET
    connections: bool | Unset = UNSET
    exclude_connections: list[str] | Unset = UNSET
    exclude_platform: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        capabilities: list[str] | Unset = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = []
            for capabilities_item_data in self.capabilities:
                capabilities_item = capabilities_item_data.value
                capabilities.append(capabilities_item)

        connections = self.connections

        exclude_connections: list[str] | Unset = UNSET
        if not isinstance(self.exclude_connections, Unset):
            exclude_connections = self.exclude_connections

        exclude_platform = self.exclude_platform

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities
        if connections is not UNSET:
            field_dict["connections"] = connections
        if exclude_connections is not UNSET:
            field_dict["exclude_connections"] = exclude_connections
        if exclude_platform is not UNSET:
            field_dict["exclude_platform"] = exclude_platform

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _capabilities = d.pop("capabilities", UNSET)
        capabilities: list[BuiltinToolsetKey] | Unset = UNSET
        if _capabilities is not UNSET:
            capabilities = []
            for capabilities_item_data in _capabilities:
                capabilities_item = BuiltinToolsetKey(capabilities_item_data)

                capabilities.append(capabilities_item)

        connections = d.pop("connections", UNSET)

        exclude_connections = cast(list[str], d.pop("exclude_connections", UNSET))

        exclude_platform = d.pop("exclude_platform", UNSET)

        automatic_tool_search = cls(
            capabilities=capabilities,
            connections=connections,
            exclude_connections=exclude_connections,
            exclude_platform=exclude_platform,
        )

        return automatic_tool_search
