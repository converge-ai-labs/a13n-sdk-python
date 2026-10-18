from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..._validation import validate_model
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.native_tool_search_config import NativeToolSearchConfig
    from ..models.proxy_tool_search_config import ProxyToolSearchConfig
    from ..models.tool_search_groups import ToolSearchGroups


T = TypeVar("T", bound="ToolSearch")


@_attrs_define(repr=False)
class ToolSearch:
    """Presentation of already-selected sources, composed by Harness once per agent.

    Attributes:
        config (NativeToolSearchConfig | ProxyToolSearchConfig | Unset):
        groups (ToolSearchGroups | Unset):
    """

    config: NativeToolSearchConfig | ProxyToolSearchConfig | Unset = UNSET
    groups: ToolSearchGroups | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.proxy_tool_search_config import ProxyToolSearchConfig

        config: dict[str, Any] | Unset
        if isinstance(self.config, Unset):
            config = UNSET
        elif isinstance(self.config, ProxyToolSearchConfig):
            config = self.config.to_dict()
        else:
            config = self.config.to_dict()

        groups: dict[str, Any] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if groups is not UNSET:
            field_dict["groups"] = groups

        validate_model("ToolSearch", field_dict)
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        validate_model("ToolSearch", src_dict)
        from ..models.native_tool_search_config import NativeToolSearchConfig
        from ..models.proxy_tool_search_config import ProxyToolSearchConfig
        from ..models.tool_search_groups import ToolSearchGroups

        d = dict(src_dict)

        def _parse_config(data: object) -> NativeToolSearchConfig | ProxyToolSearchConfig | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_tool_search_config_type_0 = ProxyToolSearchConfig.from_dict(data)

                return componentsschemas_tool_search_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_tool_search_config_type_1 = NativeToolSearchConfig.from_dict(data)

            return componentsschemas_tool_search_config_type_1

        config = _parse_config(d.pop("config", UNSET))

        _groups = d.pop("groups", UNSET)
        groups: ToolSearchGroups | Unset
        if isinstance(_groups, Unset):
            groups = UNSET
        else:
            groups = ToolSearchGroups.from_dict(_groups)

        tool_search = cls(
            config=config,
            groups=groups,
        )

        return tool_search
