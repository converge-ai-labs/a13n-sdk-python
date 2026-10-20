from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CatalogIndexItem")


@_attrs_define(repr=False)
class CatalogIndexItem:
    """
    Attributes:
        description (str):
        name (str):
        description_truncated (bool | Unset):
        provider_version (None | str | Unset):
        supported_tool_count (int | None | Unset):
        tool_count (int | None | Unset):
    """

    description: str
    name: str
    description_truncated: bool | Unset = UNSET
    provider_version: str | Unset | None = UNSET
    supported_tool_count: int | Unset | None = UNSET
    tool_count: int | Unset | None = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        name = self.name

        description_truncated = self.description_truncated

        provider_version: str | Unset | None
        if isinstance(self.provider_version, Unset):
            provider_version = UNSET
        else:
            provider_version = self.provider_version

        supported_tool_count: int | Unset | None
        if isinstance(self.supported_tool_count, Unset):
            supported_tool_count = UNSET
        else:
            supported_tool_count = self.supported_tool_count

        tool_count: int | Unset | None
        if isinstance(self.tool_count, Unset):
            tool_count = UNSET
        else:
            tool_count = self.tool_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "name": name,
            }
        )
        if description_truncated is not UNSET:
            field_dict["description_truncated"] = description_truncated
        if provider_version is not UNSET:
            field_dict["provider_version"] = provider_version
        if supported_tool_count is not UNSET:
            field_dict["supported_tool_count"] = supported_tool_count
        if tool_count is not UNSET:
            field_dict["tool_count"] = tool_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description")

        name = d.pop("name")

        description_truncated = d.pop("description_truncated", UNSET)

        def _parse_provider_version(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        provider_version = _parse_provider_version(d.pop("provider_version", UNSET))

        def _parse_supported_tool_count(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        supported_tool_count = _parse_supported_tool_count(d.pop("supported_tool_count", UNSET))

        def _parse_tool_count(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        tool_count = _parse_tool_count(d.pop("tool_count", UNSET))

        catalog_index_item = cls(
            description=description,
            name=name,
            description_truncated=description_truncated,
            provider_version=provider_version,
            supported_tool_count=supported_tool_count,
            tool_count=tool_count,
        )

        catalog_index_item.additional_properties = d
        return catalog_index_item

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
