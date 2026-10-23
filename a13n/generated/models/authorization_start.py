from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthorizationStart")


@_attrs_define(repr=False)
class AuthorizationStart:
    """
    Attributes:
        attempt_id (str):
        authorization_url (str):
        expires_at (datetime.datetime):
        method (Literal['manual_callback'] | Unset):
    """

    attempt_id: str
    authorization_url: str
    expires_at: datetime.datetime
    method: Literal["manual_callback"] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attempt_id = self.attempt_id

        authorization_url = self.authorization_url

        expires_at = self.expires_at.isoformat()

        method = self.method

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attempt_id": attempt_id,
                "authorization_url": authorization_url,
                "expires_at": expires_at,
            }
        )
        if method is not UNSET:
            field_dict["method"] = method

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attempt_id = d.pop("attempt_id")

        authorization_url = d.pop("authorization_url")

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        method = cast(Literal["manual_callback"] | Unset, d.pop("method", UNSET))
        if method != "manual_callback" and not isinstance(method, Unset):
            raise ValueError(f"method must match const 'manual_callback', got '{method}'")

        authorization_start = cls(
            attempt_id=attempt_id,
            authorization_url=authorization_url,
            expires_at=expires_at,
            method=method,
        )

        authorization_start.additional_properties = d
        return authorization_start

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
