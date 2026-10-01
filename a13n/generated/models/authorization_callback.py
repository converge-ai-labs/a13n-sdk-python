from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="AuthorizationCallback")


@_attrs_define(repr=False)
class AuthorizationCallback:
    """
    Attributes:
        attempt_id (str):
        callback_url (str):
    """

    attempt_id: str
    callback_url: str

    def to_dict(self) -> dict[str, Any]:
        attempt_id = self.attempt_id

        callback_url = self.callback_url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "attempt_id": attempt_id,
                "callback_url": callback_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attempt_id = d.pop("attempt_id")

        callback_url = d.pop("callback_url")

        authorization_callback = cls(
            attempt_id=attempt_id,
            callback_url=callback_url,
        )

        return authorization_callback
