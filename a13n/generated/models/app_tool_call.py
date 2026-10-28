from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_tool_call_arguments import AppToolCallArguments


T = TypeVar("T", bound="AppToolCall")


@_attrs_define(repr=False)
class AppToolCall:
    """
    Attributes:
        name (str):
        arguments (AppToolCallArguments | Unset):
    """

    name: str
    arguments: AppToolCallArguments | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        arguments: dict[str, Any] | Unset = UNSET
        if not isinstance(self.arguments, Unset):
            arguments = self.arguments.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if arguments is not UNSET:
            field_dict["arguments"] = arguments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_tool_call_arguments import AppToolCallArguments

        d = dict(src_dict)
        name = d.pop("name")

        _arguments = d.pop("arguments", UNSET)
        arguments: AppToolCallArguments | Unset
        if isinstance(_arguments, Unset):
            arguments = UNSET
        else:
            arguments = AppToolCallArguments.from_dict(_arguments)

        app_tool_call = cls(
            name=name,
            arguments=arguments,
        )

        return app_tool_call
