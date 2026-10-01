from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.authorization_status_state import AuthorizationStatusState
from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthorizationStatus")


@_attrs_define(repr=False)
class AuthorizationStatus:
    """
    Attributes:
        provider_id (str):
        state (AuthorizationStatusState):
        client_id (None | str | Unset):
        email (None | str | Unset):
        expires_at (datetime.datetime | None | Unset):
        message (None | str | Unset):
        pending (bool | Unset):
        subject (None | str | Unset):
    """

    provider_id: str
    state: AuthorizationStatusState
    client_id: str | Unset | None = UNSET
    email: str | Unset | None = UNSET
    expires_at: datetime.datetime | Unset | None = UNSET
    message: str | Unset | None = UNSET
    pending: bool | Unset = UNSET
    subject: str | Unset | None = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider_id = self.provider_id

        state = self.state.value

        client_id: str | Unset | None
        if isinstance(self.client_id, Unset):
            client_id = UNSET
        else:
            client_id = self.client_id

        email: str | Unset | None
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        expires_at: str | Unset | None
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        message: str | Unset | None
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        pending = self.pending

        subject: str | Unset | None
        if isinstance(self.subject, Unset):
            subject = UNSET
        else:
            subject = self.subject

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider_id": provider_id,
                "state": state,
            }
        )
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if email is not UNSET:
            field_dict["email"] = email
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if message is not UNSET:
            field_dict["message"] = message
        if pending is not UNSET:
            field_dict["pending"] = pending
        if subject is not UNSET:
            field_dict["subject"] = subject

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider_id = d.pop("provider_id")

        state = AuthorizationStatusState(d.pop("state"))

        def _parse_client_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        client_id = _parse_client_id(d.pop("client_id", UNSET))

        def _parse_email(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_expires_at(data: object) -> datetime.datetime | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = datetime.datetime.fromisoformat(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | Unset | None, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        def _parse_message(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        message = _parse_message(d.pop("message", UNSET))

        pending = d.pop("pending", UNSET)

        def _parse_subject(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        subject = _parse_subject(d.pop("subject", UNSET))

        authorization_status = cls(
            provider_id=provider_id,
            state=state,
            client_id=client_id,
            email=email,
            expires_at=expires_at,
            message=message,
            pending=pending,
            subject=subject,
        )

        authorization_status.additional_properties = d
        return authorization_status

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
