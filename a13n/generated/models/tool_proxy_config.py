from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ToolProxyConfig")


@_attrs_define(repr=False)
class ToolProxyConfig:
    """Names and bounded discovery settings for one Agent's proxy surface.

    Attributes:
        call_name (str | Unset):
        max_results (int | Unset):
        max_search_bytes (int | Unset):
        search_name (str | Unset):
    """

    call_name: str | Unset = UNSET
    max_results: int | Unset = UNSET
    max_search_bytes: int | Unset = UNSET
    search_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        call_name = self.call_name

        max_results = self.max_results

        max_search_bytes = self.max_search_bytes

        search_name = self.search_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if call_name is not UNSET:
            field_dict["call_name"] = call_name
        if max_results is not UNSET:
            field_dict["max_results"] = max_results
        if max_search_bytes is not UNSET:
            field_dict["max_search_bytes"] = max_search_bytes
        if search_name is not UNSET:
            field_dict["search_name"] = search_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        call_name = d.pop("call_name", UNSET)

        max_results = d.pop("max_results", UNSET)

        max_search_bytes = d.pop("max_search_bytes", UNSET)

        search_name = d.pop("search_name", UNSET)

        tool_proxy_config = cls(
            call_name=call_name,
            max_results=max_results,
            max_search_bytes=max_search_bytes,
            search_name=search_name,
        )

        tool_proxy_config.additional_properties = d
        return tool_proxy_config

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
