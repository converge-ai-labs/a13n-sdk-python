from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ToolSearchGroup")


@_attrs_define(repr=False)
class ToolSearchGroup:
    """
    Attributes:
        description (str):
        connections (list[str] | Unset):
        platform (bool | Unset):
        plugins (list[str] | Unset):
    """

    description: str
    connections: list[str] | Unset = UNSET
    platform: bool | Unset = UNSET
    plugins: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        connections: list[str] | Unset = UNSET
        if not isinstance(self.connections, Unset):
            connections = self.connections

        platform = self.platform

        plugins: list[str] | Unset = UNSET
        if not isinstance(self.plugins, Unset):
            plugins = self.plugins

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "description": description,
            }
        )
        if connections is not UNSET:
            field_dict["connections"] = connections
        if platform is not UNSET:
            field_dict["platform"] = platform
        if plugins is not UNSET:
            field_dict["plugins"] = plugins

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description")

        connections = cast(list[str], d.pop("connections", UNSET))

        platform = d.pop("platform", UNSET)

        plugins = cast(list[str], d.pop("plugins", UNSET))

        tool_search_group = cls(
            description=description,
            connections=connections,
            platform=platform,
            plugins=plugins,
        )

        return tool_search_group
