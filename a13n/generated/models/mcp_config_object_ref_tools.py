from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="McpConfigObjectRefTools")


@_attrs_define(repr=False)
class McpConfigObjectRefTools:
    """Object Reference Transport rules by original tool name; '*' matches any characters. Exact names win, then more
    literal characters, with false winning equally specific patterns. Use {'*': true} to enable all tools; unmatched
    tools retain native metadata, defaulting to false.

    """

    additional_properties: dict[str, bool] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mcp_config_object_ref_tools = cls()

        mcp_config_object_ref_tools.additional_properties = d
        return mcp_config_object_ref_tools

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> bool:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: bool) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
