from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.mcp_auth import McpAuth
from ..types import UNSET, Unset

T = TypeVar("T", bound="McpServer")


@_attrs_define(repr=False)
class McpServer:
    """
    Attributes:
        auth (McpAuth):
        description (str):
        key (str):
        name (str):
        url (str):
        documentation_url (None | str | Unset):
        header_names (list[str] | Unset):
        logo_url (None | str | Unset):
        requirements (str | Unset):
    """

    auth: McpAuth
    description: str
    key: str
    name: str
    url: str
    documentation_url: str | Unset | None = UNSET
    header_names: list[str] | Unset = UNSET
    logo_url: str | Unset | None = UNSET
    requirements: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        auth = self.auth.value

        description = self.description

        key = self.key

        name = self.name

        url = self.url

        documentation_url: str | Unset | None
        if isinstance(self.documentation_url, Unset):
            documentation_url = UNSET
        else:
            documentation_url = self.documentation_url

        header_names: list[str] | Unset = UNSET
        if not isinstance(self.header_names, Unset):
            header_names = self.header_names

        logo_url: str | Unset | None
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        requirements = self.requirements

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "auth": auth,
                "description": description,
                "key": key,
                "name": name,
                "url": url,
            }
        )
        if documentation_url is not UNSET:
            field_dict["documentation_url"] = documentation_url
        if header_names is not UNSET:
            field_dict["header_names"] = header_names
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if requirements is not UNSET:
            field_dict["requirements"] = requirements

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auth = McpAuth(d.pop("auth"))

        description = d.pop("description")

        key = d.pop("key")

        name = d.pop("name")

        url = d.pop("url")

        def _parse_documentation_url(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        documentation_url = _parse_documentation_url(d.pop("documentation_url", UNSET))

        header_names = cast(list[str], d.pop("header_names", UNSET))

        def _parse_logo_url(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        logo_url = _parse_logo_url(d.pop("logo_url", UNSET))

        requirements = d.pop("requirements", UNSET)

        mcp_server = cls(
            auth=auth,
            description=description,
            key=key,
            name=name,
            url=url,
            documentation_url=documentation_url,
            header_names=header_names,
            logo_url=logo_url,
            requirements=requirements,
        )

        return mcp_server
