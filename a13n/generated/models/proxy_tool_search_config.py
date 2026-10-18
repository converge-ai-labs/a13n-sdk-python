from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProxyToolSearchConfig")


@_attrs_define(repr=False)
class ProxyToolSearchConfig:
    """Names and bounded discovery settings for one Agent's proxy surface.

    Attributes:
        mode (Literal['proxy']):
        call_name (str | Unset):
        max_results (int | Unset):
        max_search_bytes (int | Unset):
        search_name (str | Unset):
    """

    mode: Literal["proxy"]
    call_name: str | Unset = UNSET
    max_results: int | Unset = UNSET
    max_search_bytes: int | Unset = UNSET
    search_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        call_name = self.call_name

        max_results = self.max_results

        max_search_bytes = self.max_search_bytes

        search_name = self.search_name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "mode": mode,
            }
        )
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
        mode = cast(Literal["proxy"], d.pop("mode"))
        if mode != "proxy":
            raise ValueError(f"mode must match const 'proxy', got '{mode}'")

        call_name = d.pop("call_name", UNSET)

        max_results = d.pop("max_results", UNSET)

        max_search_bytes = d.pop("max_search_bytes", UNSET)

        search_name = d.pop("search_name", UNSET)

        proxy_tool_search_config = cls(
            mode=mode,
            call_name=call_name,
            max_results=max_results,
            max_search_bytes=max_search_bytes,
            search_name=search_name,
        )

        return proxy_tool_search_config
