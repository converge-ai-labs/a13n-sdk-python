from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProviderAuthorizationRequest")


@_attrs_define(repr=False)
class ProviderAuthorizationRequest:
    """
    Attributes:
        new_registration (bool | Unset):
    """

    new_registration: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        new_registration = self.new_registration

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if new_registration is not UNSET:
            field_dict["new_registration"] = new_registration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        new_registration = d.pop("new_registration", UNSET)

        provider_authorization_request = cls(
            new_registration=new_registration,
        )

        return provider_authorization_request
