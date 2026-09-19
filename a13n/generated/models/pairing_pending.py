from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pairing_challenge import PairingChallenge


T = TypeVar("T", bound="PairingPending")


@_attrs_define(repr=False)
class PairingPending:
    """
    Attributes:
        challenge (PairingChallenge): Safe details shown to both the registering operator and approving user.
        approval_url (None | str | Unset):
        poll_after_seconds (int | Unset):
        status (Literal['pending'] | Unset):
    """

    challenge: PairingChallenge
    approval_url: str | Unset | None = UNSET
    poll_after_seconds: int | Unset = UNSET
    status: Literal["pending"] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        challenge = self.challenge.to_dict()

        approval_url: str | Unset | None
        if isinstance(self.approval_url, Unset):
            approval_url = UNSET
        else:
            approval_url = self.approval_url

        poll_after_seconds = self.poll_after_seconds

        status = self.status

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "challenge": challenge,
            }
        )
        if approval_url is not UNSET:
            field_dict["approval_url"] = approval_url
        if poll_after_seconds is not UNSET:
            field_dict["poll_after_seconds"] = poll_after_seconds
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pairing_challenge import PairingChallenge

        d = dict(src_dict)
        challenge = PairingChallenge.from_dict(d.pop("challenge"))

        def _parse_approval_url(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        approval_url = _parse_approval_url(d.pop("approval_url", UNSET))

        poll_after_seconds = d.pop("poll_after_seconds", UNSET)

        status = cast(Literal["pending"] | Unset, d.pop("status", UNSET))
        if status != "pending" and not isinstance(status, Unset):
            raise ValueError(f"status must match const 'pending', got '{status}'")

        pairing_pending = cls(
            challenge=challenge,
            approval_url=approval_url,
            poll_after_seconds=poll_after_seconds,
            status=status,
        )

        return pairing_pending
