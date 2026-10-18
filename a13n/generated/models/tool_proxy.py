from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tool_proxy_config import ToolProxyConfig
    from ..models.tool_proxy_groups import ToolProxyGroups


T = TypeVar("T", bound="ToolProxy")


@_attrs_define(repr=False)
class ToolProxy:
    """Presentation of already-selected sources, composed by Harness once per agent.

    Attributes:
        config (ToolProxyConfig | Unset): Names and bounded discovery settings for one Agent's proxy surface.
        groups (ToolProxyGroups | Unset):
        native_search (bool | Unset):
    """

    config: ToolProxyConfig | Unset = UNSET
    groups: ToolProxyGroups | Unset = UNSET
    native_search: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        groups: dict[str, Any] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups.to_dict()

        native_search = self.native_search

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if groups is not UNSET:
            field_dict["groups"] = groups
        if native_search is not UNSET:
            field_dict["native_search"] = native_search

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tool_proxy_config import ToolProxyConfig
        from ..models.tool_proxy_groups import ToolProxyGroups

        d = dict(src_dict)
        _config = d.pop("config", UNSET)
        config: ToolProxyConfig | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = ToolProxyConfig.from_dict(_config)

        _groups = d.pop("groups", UNSET)
        groups: ToolProxyGroups | Unset
        if isinstance(_groups, Unset):
            groups = UNSET
        else:
            groups = ToolProxyGroups.from_dict(_groups)

        native_search = d.pop("native_search", UNSET)

        tool_proxy = cls(
            config=config,
            groups=groups,
            native_search=native_search,
        )

        return tool_proxy
