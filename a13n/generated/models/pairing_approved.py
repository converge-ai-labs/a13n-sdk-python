from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PairingApproved")


@_attrs_define(repr=False)
class PairingApproved:
    """
    Attributes:
        resource_id (str):
        websocket_url (str):
        status (Literal['approved'] | Unset):
    """

    resource_id: str
    websocket_url: str
    status: Literal["approved"] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        resource_id = self.resource_id

        websocket_url = self.websocket_url

        status = self.status

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "resource_id": resource_id,
                "websocket_url": websocket_url,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource_id = d.pop("resource_id")

        websocket_url = d.pop("websocket_url")

        status = cast(Literal["approved"] | Unset, d.pop("status", UNSET))
        if status != "approved" and not isinstance(status, Unset):
            raise ValueError(f"status must match const 'approved', got '{status}'")

        pairing_approved = cls(
            resource_id=resource_id,
            websocket_url=websocket_url,
            status=status,
        )

        return pairing_approved
