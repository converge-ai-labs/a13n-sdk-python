from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.request_context_headers import RequestContextHeaders


T = TypeVar("T", bound="RequestContext")


@_attrs_define(repr=False)
class RequestContext:
    """Explicit business headers, frozen in accepted Run options and kept out of model projections.

    Attributes:
        headers (RequestContextHeaders | Unset):
    """

    headers: RequestContextHeaders | Unset = UNSET

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
        from ..models.request_context_headers import RequestContextHeaders

        d = dict(src_dict)
        _headers = d.pop("headers", UNSET)
        headers: RequestContextHeaders | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = RequestContextHeaders.from_dict(_headers)

        request_context = cls(
            headers=headers,
        )

        return request_context
