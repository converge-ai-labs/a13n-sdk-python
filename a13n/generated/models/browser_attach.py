from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.browser_attach_headers import BrowserAttachHeaders


T = TypeVar("T", bound="BrowserAttach")


@_attrs_define(repr=False)
class BrowserAttach:
    """
    Attributes:
        cdp_url (str):
        name (str):
        headers (BrowserAttachHeaders | Unset):
        idle_seconds (int | None | Unset):
        prepare (bool | Unset):
    """

    cdp_url: str
    name: str
    headers: BrowserAttachHeaders | Unset = UNSET
    idle_seconds: int | Unset | None = UNSET
    prepare: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        cdp_url = self.cdp_url

        name = self.name

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        idle_seconds: int | Unset | None
        if isinstance(self.idle_seconds, Unset):
            idle_seconds = UNSET
        else:
            idle_seconds = self.idle_seconds

        prepare = self.prepare

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "cdp_url": cdp_url,
                "name": name,
            }
        )
        if headers is not UNSET:
            field_dict["headers"] = headers
        if idle_seconds is not UNSET:
            field_dict["idle_seconds"] = idle_seconds
        if prepare is not UNSET:
            field_dict["prepare"] = prepare

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.browser_attach_headers import BrowserAttachHeaders

        d = dict(src_dict)
        cdp_url = d.pop("cdp_url")

        name = d.pop("name")

        _headers = d.pop("headers", UNSET)
        headers: BrowserAttachHeaders | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = BrowserAttachHeaders.from_dict(_headers)

        def _parse_idle_seconds(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        idle_seconds = _parse_idle_seconds(d.pop("idle_seconds", UNSET))

        prepare = d.pop("prepare", UNSET)

        browser_attach = cls(
            cdp_url=cdp_url,
            name=name,
            headers=headers,
            idle_seconds=idle_seconds,
            prepare=prepare,
        )

        return browser_attach
