from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.o_auth_settings import OAuthSettings


T = TypeVar("T", bound="McpConfig")


@_attrs_define(repr=False)
class McpConfig:
    """
    Attributes:
        url (str):
        headers (list[str] | Unset):
        oauth (None | OAuthSettings | Unset):
        tools (list[str] | None | Unset):
    """

    url: str
    headers: list[str] | Unset = UNSET
    oauth: OAuthSettings | Unset | None = UNSET
    tools: list[str] | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.o_auth_settings import OAuthSettings

        url = self.url

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
        if headers is not UNSET:
            field_dict["headers"] = headers
        if oauth is not UNSET:
            field_dict["oauth"] = oauth
        if tools is not UNSET:
            field_dict["tools"] = tools

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.o_auth_settings import OAuthSettings

        d = dict(src_dict)
        url = d.pop("url")

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
            headers=headers,
            oauth=oauth,
            tools=tools,
        )

        return mcp_config
