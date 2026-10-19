from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.platform_group import PlatformGroup
from ..models.toolset_key_type_0 import ToolsetKeyType0
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tool_definition import ToolDefinition
    from ..models.toolset_definition_config_schema import ToolsetDefinitionConfigSchema


T = TypeVar("T", bound="ToolsetDefinition")


@_attrs_define(repr=False)
class ToolsetDefinition:
    """
    Attributes:
        config_schema (ToolsetDefinitionConfigSchema):
        default_enabled (bool):
        display_name (str):
        key (PlatformGroup | ToolsetKeyType0):
        tools (list[ToolDefinition]):
        description (str | Unset):
        platform (bool | Unset):
    """

    config_schema: ToolsetDefinitionConfigSchema
    default_enabled: bool
    display_name: str
    key: PlatformGroup | ToolsetKeyType0
    tools: list[ToolDefinition]
    description: str | Unset = UNSET
    platform: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        config_schema = self.config_schema.to_dict()

        default_enabled = self.default_enabled

        display_name = self.display_name

        key: str
        if isinstance(self.key, ToolsetKeyType0):
            key = self.key.value
        else:
            key = self.key.value

        tools = []
        for tools_item_data in self.tools:
            tools_item = tools_item_data.to_dict()
            tools.append(tools_item)

        description = self.description

        platform = self.platform

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "config_schema": config_schema,
                "default_enabled": default_enabled,
                "display_name": display_name,
                "key": key,
                "tools": tools,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if platform is not UNSET:
            field_dict["platform"] = platform

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tool_definition import ToolDefinition
        from ..models.toolset_definition_config_schema import ToolsetDefinitionConfigSchema

        d = dict(src_dict)
        config_schema = ToolsetDefinitionConfigSchema.from_dict(d.pop("config_schema"))

        default_enabled = d.pop("default_enabled")

        display_name = d.pop("display_name")

        def _parse_key(data: object) -> PlatformGroup | ToolsetKeyType0:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_toolset_key_type_0 = ToolsetKeyType0(data)

                return componentsschemas_toolset_key_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, str):
                raise TypeError()
            componentsschemas_toolset_key_type_1 = PlatformGroup(data)

            return componentsschemas_toolset_key_type_1

        key = _parse_key(d.pop("key"))

        tools = []
        _tools = d.pop("tools")
        for tools_item_data in _tools:
            tools_item = ToolDefinition.from_dict(tools_item_data)

            tools.append(tools_item)

        description = d.pop("description", UNSET)

        platform = d.pop("platform", UNSET)

        toolset_definition = cls(
            config_schema=config_schema,
            default_enabled=default_enabled,
            display_name=display_name,
            key=key,
            tools=tools,
            description=description,
            platform=platform,
        )

        return toolset_definition
