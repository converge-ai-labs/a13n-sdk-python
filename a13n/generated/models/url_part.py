from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="UrlPart")


@_attrs_define(repr=False)
class UrlPart:
    """
    Attributes:
        type_ (Literal['url']):
        url (str):
    """

    type_: Literal["url"]
    url: str

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        url = self.url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["url"], d.pop("type"))
        if type_ != "url":
            raise ValueError(f"type must match const 'url', got '{type_}'")

        url = d.pop("url")

        url_part = cls(
            type_=type_,
            url=url,
        )

        return url_part
