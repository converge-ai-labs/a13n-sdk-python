from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.startup_error_policy import StartupErrorPolicy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mcp_config_object_ref_tools import McpConfigObjectRefTools
    from ..models.o_auth_settings import OAuthSettings


T = TypeVar("T", bound="McpConfig")


@_attrs_define(repr=False)
class McpConfig:
    """
    Attributes:
        url (str):
        forward_context_headers (bool | Unset):
        headers (list[str] | Unset):
        oauth (None | OAuthSettings | Unset):
        object_ref_tools (McpConfigObjectRefTools | Unset): Object Reference Transport rules by original tool name; '*'
            matches any characters. Exact names win, then more literal characters, with false winning equally specific
            patterns. Use {'*': true} to enable all tools; unmatched tools retain native metadata, defaulting to false.
        on_error (StartupErrorPolicy | Unset):
        tools (list[str] | None | Unset):
    """

    url: str
    forward_context_headers: bool | Unset = UNSET
    headers: list[str] | Unset = UNSET
    oauth: OAuthSettings | Unset | None = UNSET
    object_ref_tools: McpConfigObjectRefTools | Unset = UNSET
    on_error: StartupErrorPolicy | Unset = UNSET
    tools: list[str] | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.o_auth_settings import OAuthSettings

        url = self.url

        forward_context_headers = self.forward_context_headers

        headers: list[str] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers

        oauth: dict[str, Any] | Unset | None
        if isinstance(self.oauth, Unset):
            oauth = UNSET
        elif isinstance(self.oauth, OAuthSettings):
            oauth = self.oauth.to_dict()
        else:
            oauth = self.oauth

        object_ref_tools: dict[str, Any] | Unset = UNSET
        if not isinstance(self.object_ref_tools, Unset):
            object_ref_tools = self.object_ref_tools.to_dict()

        on_error: str | Unset = UNSET
        if not isinstance(self.on_error, Unset):
            on_error = self.on_error.value

        tools: list[str] | Unset | None
        if isinstance(self.tools, Unset):
            tools = UNSET
        elif isinstance(self.tools, list):
            tools = self.tools

        else:
            tools = self.tools

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "url": url,
            }
        )
        if forward_context_headers is not UNSET:
            field_dict["forward_context_headers"] = forward_context_headers
        if headers is not UNSET:
            field_dict["headers"] = headers
        if oauth is not UNSET:
            field_dict["oauth"] = oauth
        if object_ref_tools is not UNSET:
            field_dict["object_ref_tools"] = object_ref_tools
        if on_error is not UNSET:
            field_dict["on_error"] = on_error
        if tools is not UNSET:
            field_dict["tools"] = tools

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mcp_config_object_ref_tools import McpConfigObjectRefTools
        from ..models.o_auth_settings import OAuthSettings

        d = dict(src_dict)
        url = d.pop("url")

        forward_context_headers = d.pop("forward_context_headers", UNSET)

        headers = cast(list[str], d.pop("headers", UNSET))

        def _parse_oauth(data: object) -> OAuthSettings | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                oauth_type_0 = OAuthSettings.from_dict(data)

                return oauth_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(OAuthSettings | Unset | None, data)

        oauth = _parse_oauth(d.pop("oauth", UNSET))

        _object_ref_tools = d.pop("object_ref_tools", UNSET)
        object_ref_tools: McpConfigObjectRefTools | Unset
        if isinstance(_object_ref_tools, Unset):
            object_ref_tools = UNSET
        else:
            object_ref_tools = McpConfigObjectRefTools.from_dict(_object_ref_tools)

        _on_error = d.pop("on_error", UNSET)
        on_error: StartupErrorPolicy | Unset
        if isinstance(_on_error, Unset):
            on_error = UNSET
        else:
            on_error = StartupErrorPolicy(_on_error)

        def _parse_tools(data: object) -> list[str] | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tools_type_0 = cast(list[str], data)

                return tools_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | Unset | None, data)

        tools = _parse_tools(d.pop("tools", UNSET))

        mcp_config = cls(
            url=url,
            forward_context_headers=forward_context_headers,
            headers=headers,
            oauth=oauth,
            object_ref_tools=object_ref_tools,
            on_error=on_error,
            tools=tools,
        )

        return mcp_config
