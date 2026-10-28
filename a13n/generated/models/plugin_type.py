from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.plugin_type_config_schema_type_0 import PluginTypeConfigSchemaType0


T = TypeVar("T", bound="PluginType")


@_attrs_define(repr=False)
class PluginType:
    """
    Attributes:
        config_schema (None | PluginTypeConfigSchemaType0):
        description (str):
        display_name (str):
        distribution_name (None | str):
        distribution_version (None | str):
        plugin_key (str):
    """

    config_schema: PluginTypeConfigSchemaType0 | None
    description: str
    display_name: str
    distribution_name: str | None
    distribution_version: str | None
    plugin_key: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.plugin_type_config_schema_type_0 import PluginTypeConfigSchemaType0

        config_schema: dict[str, Any] | None
        if isinstance(self.config_schema, PluginTypeConfigSchemaType0):
            config_schema = self.config_schema.to_dict()
        else:
            config_schema = self.config_schema

        description = self.description

        display_name = self.display_name

        distribution_name: str | None
        distribution_name = self.distribution_name

        distribution_version: str | None
        distribution_version = self.distribution_version

        plugin_key = self.plugin_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config_schema": config_schema,
                "description": description,
                "display_name": display_name,
                "distribution_name": distribution_name,
                "distribution_version": distribution_version,
                "plugin_key": plugin_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plugin_type_config_schema_type_0 import PluginTypeConfigSchemaType0

        d = dict(src_dict)

        def _parse_config_schema(data: object) -> PluginTypeConfigSchemaType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_schema_type_0 = PluginTypeConfigSchemaType0.from_dict(data)

                return config_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(PluginTypeConfigSchemaType0 | None, data)

        config_schema = _parse_config_schema(d.pop("config_schema"))

        description = d.pop("description")

        display_name = d.pop("display_name")

        def _parse_distribution_name(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        distribution_name = _parse_distribution_name(d.pop("distribution_name"))

        def _parse_distribution_version(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        distribution_version = _parse_distribution_version(d.pop("distribution_version"))

        plugin_key = d.pop("plugin_key")

        plugin_type = cls(
            config_schema=config_schema,
            description=description,
            display_name=display_name,
            distribution_name=distribution_name,
            distribution_version=distribution_version,
            plugin_key=plugin_key,
        )

        plugin_type.additional_properties = d
        return plugin_type

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
