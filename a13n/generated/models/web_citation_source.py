from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebCitationSource")


@_attrs_define(repr=False)
class WebCitationSource:
    """
    Attributes:
        url (str):
        excerpts (list[str] | Unset):
        kind (Literal['web'] | Unset):
        title (None | str | Unset):
    """

    url: str
    excerpts: list[str] | Unset = UNSET
    kind: Literal["web"] | Unset = UNSET
    title: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        excerpts: list[str] | Unset = UNSET
        if not isinstance(self.excerpts, Unset):
            excerpts = self.excerpts

        kind = self.kind

        title: str | Unset | None
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "url": url,
            }
        )
        if excerpts is not UNSET:
            field_dict["excerpts"] = excerpts
        if kind is not UNSET:
            field_dict["kind"] = kind
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        excerpts = cast(list[str], d.pop("excerpts", UNSET))

        kind = cast(Literal["web"] | Unset, d.pop("kind", UNSET))
        if kind != "web" and not isinstance(kind, Unset):
            raise ValueError(f"kind must match const 'web', got '{kind}'")

        def _parse_title(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        title = _parse_title(d.pop("title", UNSET))

        web_citation_source = cls(
            url=url,
            excerpts=excerpts,
            kind=kind,
            title=title,
        )

        return web_citation_source
