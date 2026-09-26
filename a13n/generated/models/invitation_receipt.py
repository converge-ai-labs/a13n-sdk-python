from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invitation_receipt_delivery import InvitationReceiptDelivery

if TYPE_CHECKING:
    from ..models.invitation import Invitation


T = TypeVar("T", bound="InvitationReceipt")


@_attrs_define(repr=False)
class InvitationReceipt:
    """
    Attributes:
        delivery (InvitationReceiptDelivery):
        invitation (Invitation):
        invitation_url (None | str):
    """

    delivery: InvitationReceiptDelivery
    invitation: Invitation
    invitation_url: str | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delivery = self.delivery.value

        invitation = self.invitation.to_dict()

        invitation_url: str | None
        invitation_url = self.invitation_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "delivery": delivery,
                "invitation": invitation,
                "invitation_url": invitation_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invitation import Invitation

        d = dict(src_dict)
        delivery = InvitationReceiptDelivery(d.pop("delivery"))

        invitation = Invitation.from_dict(d.pop("invitation"))

        def _parse_invitation_url(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        invitation_url = _parse_invitation_url(d.pop("invitation_url"))

        invitation_receipt = cls(
            delivery=delivery,
            invitation=invitation,
            invitation_url=invitation_url,
        )

        invitation_receipt.additional_properties = d
        return invitation_receipt

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
