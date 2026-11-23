from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PasswordResetReceipt")


@_attrs_define(repr=False)
class PasswordResetReceipt:
    """
    Attributes:
        email_queued (bool):
        reset_url (None | str | Unset):
    """

    email_queued: bool
    reset_url: str | Unset | None = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email_queued = self.email_queued

        reset_url: str | Unset | None
        if isinstance(self.reset_url, Unset):
            reset_url = UNSET
        else:
            reset_url = self.reset_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email_queued": email_queued,
            }
        )
        if reset_url is not UNSET:
            field_dict["reset_url"] = reset_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email_queued = d.pop("email_queued")

        def _parse_reset_url(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        reset_url = _parse_reset_url(d.pop("reset_url", UNSET))

        password_reset_receipt = cls(
            email_queued=email_queued,
            reset_url=reset_url,
        )

        password_reset_receipt.additional_properties = d
        return password_reset_receipt

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
