from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthorizationRequest")


@_attrs_define(repr=False)
class AuthorizationRequest:
    """
    Attributes:
        return_url (None | str | Unset):
    """

    return_url: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        return_url: str | Unset | None
        if isinstance(self.return_url, Unset):
            return_url = UNSET
        else:
            return_url = self.return_url

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if return_url is not UNSET:
            field_dict["return_url"] = return_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_return_url(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        return_url = _parse_return_url(d.pop("return_url", UNSET))

        authorization_request = cls(
            return_url=return_url,
        )

        return authorization_request
