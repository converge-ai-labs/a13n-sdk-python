from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credentials_headers import CredentialsHeaders


T = TypeVar("T", bound="Credentials")


@_attrs_define(repr=False)
class Credentials:
    """
    Attributes:
        headers (CredentialsHeaders | Unset):
    """

    headers: CredentialsHeaders | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if headers is not UNSET:
            field_dict["headers"] = headers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credentials_headers import CredentialsHeaders

        d = dict(src_dict)
        _headers = d.pop("headers", UNSET)
        headers: CredentialsHeaders | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = CredentialsHeaders.from_dict(_headers)

        credentials = cls(
            headers=headers,
        )

        return credentials
