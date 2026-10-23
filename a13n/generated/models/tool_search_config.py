from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..._validation import validate_model
from ..types import UNSET, Unset

T = TypeVar("T", bound="ToolSearchConfig")


@_attrs_define(repr=False)
class ToolSearchConfig:
    """Names and bounded discovery settings for one Agent's proxy surface.

    Attributes:
        call_name (str | Unset):
        describe_name (str | Unset):
        groups_name (str | Unset):
        list_name (str | Unset):
        max_results (int | Unset):
        max_search_bytes (int | Unset):
        mode (Literal['proxy'] | Unset):
        search_name (str | Unset):
    """

    call_name: str | Unset = UNSET
    describe_name: str | Unset = UNSET
    groups_name: str | Unset = UNSET
    list_name: str | Unset = UNSET
    max_results: int | Unset = UNSET
    max_search_bytes: int | Unset = UNSET
    mode: Literal["proxy"] | Unset = UNSET
    search_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        call_name = self.call_name

        describe_name = self.describe_name

        groups_name = self.groups_name

        list_name = self.list_name

        max_results = self.max_results

        max_search_bytes = self.max_search_bytes

        mode = self.mode

        search_name = self.search_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if call_name is not UNSET:
            field_dict["call_name"] = call_name
        if describe_name is not UNSET:
            field_dict["describe_name"] = describe_name
        if groups_name is not UNSET:
            field_dict["groups_name"] = groups_name
        if list_name is not UNSET:
            field_dict["list_name"] = list_name
        if max_results is not UNSET:
            field_dict["max_results"] = max_results
        if max_search_bytes is not UNSET:
            field_dict["max_search_bytes"] = max_search_bytes
        if mode is not UNSET:
            field_dict["mode"] = mode
        if search_name is not UNSET:
            field_dict["search_name"] = search_name

        validate_model("ToolSearchConfig", field_dict)
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        validate_model("ToolSearchConfig", src_dict)
        d = dict(src_dict)
        call_name = d.pop("call_name", UNSET)

        describe_name = d.pop("describe_name", UNSET)

        groups_name = d.pop("groups_name", UNSET)

        list_name = d.pop("list_name", UNSET)

        max_results = d.pop("max_results", UNSET)

        max_search_bytes = d.pop("max_search_bytes", UNSET)

        mode = cast(Literal["proxy"] | Unset, d.pop("mode", UNSET))
        if mode != "proxy" and not isinstance(mode, Unset):
            raise ValueError(f"mode must match const 'proxy', got '{mode}'")

        search_name = d.pop("search_name", UNSET)

        tool_search_config = cls(
            call_name=call_name,
            describe_name=describe_name,
            groups_name=groups_name,
            list_name=list_name,
            max_results=max_results,
            max_search_bytes=max_search_bytes,
            mode=mode,
            search_name=search_name,
        )

        return tool_search_config
