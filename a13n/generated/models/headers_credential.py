from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.headers_credential_headers import HeadersCredentialHeaders


T = TypeVar("T", bound="HeadersCredential")


@_attrs_define(repr=False)
class HeadersCredential:
    """
    Attributes:
        headers (HeadersCredentialHeaders):
    """

    headers: HeadersCredentialHeaders

    def to_dict(self) -> dict[str, Any]:
        headers = self.headers.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "headers": headers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.headers_credential_headers import HeadersCredentialHeaders

        d = dict(src_dict)
        headers = HeadersCredentialHeaders.from_dict(d.pop("headers"))

        headers_credential = cls(
            headers=headers,
        )

        return headers_credential
