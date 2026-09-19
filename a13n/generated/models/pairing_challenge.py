from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PairingChallenge")


@_attrs_define(repr=False)
class PairingChallenge:
    """Safe details shown to both the registering operator and approving user.

    Attributes:
        device_id (str):
        expires_at (datetime.datetime):
        name (str):
        pairing_id (str):
        verification_code (str):
    """

    device_id: str
    expires_at: datetime.datetime
    name: str
    pairing_id: str
    verification_code: str

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        expires_at = self.expires_at.isoformat()

        name = self.name

        pairing_id = self.pairing_id

        verification_code = self.verification_code

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "device_id": device_id,
                "expires_at": expires_at,
                "name": name,
                "pairing_id": pairing_id,
                "verification_code": verification_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        device_id = d.pop("device_id")

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        name = d.pop("name")

        pairing_id = d.pop("pairing_id")

        verification_code = d.pop("verification_code")

        pairing_challenge = cls(
            device_id=device_id,
            expires_at=expires_at,
            name=name,
            pairing_id=pairing_id,
            verification_code=verification_code,
        )

        return pairing_challenge
