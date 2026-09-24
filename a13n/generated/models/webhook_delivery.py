from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_delivery_status import WebhookDeliveryStatus

if TYPE_CHECKING:
    from ..models.webhook_delivery_payload import WebhookDeliveryPayload


T = TypeVar("T", bound="WebhookDelivery")


@_attrs_define(repr=False)
class WebhookDelivery:
    """One webhook outbox row; its ID is the delivery ID receivers deduplicate by.

    Attributes:
        attempts (int):
        available_at (datetime.datetime):
        created_at (datetime.datetime):
        delivered_at (datetime.datetime | None):
        id (str):
        last_error (None | str):
        payload (WebhookDeliveryPayload):
        status (WebhookDeliveryStatus):
        subscription_id (str):
        url (str):
    """

    attempts: int
    available_at: datetime.datetime
    created_at: datetime.datetime
    delivered_at: datetime.datetime | None
    id: str
    last_error: str | None
    payload: WebhookDeliveryPayload
    status: WebhookDeliveryStatus
    subscription_id: str
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attempts = self.attempts

        available_at = self.available_at.isoformat()

        created_at = self.created_at.isoformat()

        delivered_at: str | None
        if isinstance(self.delivered_at, datetime.datetime):
            delivered_at = self.delivered_at.isoformat()
        else:
            delivered_at = self.delivered_at

        id = self.id

        last_error: str | None
        last_error = self.last_error

        payload = self.payload.to_dict()

        status = self.status.value

        subscription_id = self.subscription_id

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attempts": attempts,
                "available_at": available_at,
                "created_at": created_at,
                "delivered_at": delivered_at,
                "id": id,
                "last_error": last_error,
                "payload": payload,
                "status": status,
                "subscription_id": subscription_id,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_delivery_payload import WebhookDeliveryPayload

        d = dict(src_dict)
        attempts = d.pop("attempts")

        available_at = datetime.datetime.fromisoformat(d.pop("available_at"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_delivered_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                delivered_at_type_0 = datetime.datetime.fromisoformat(data)

                return delivered_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        delivered_at = _parse_delivered_at(d.pop("delivered_at"))

        id = d.pop("id")

        def _parse_last_error(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        last_error = _parse_last_error(d.pop("last_error"))

        payload = WebhookDeliveryPayload.from_dict(d.pop("payload"))

        status = WebhookDeliveryStatus(d.pop("status"))

        subscription_id = d.pop("subscription_id")

        url = d.pop("url")

        webhook_delivery = cls(
            attempts=attempts,
            available_at=available_at,
            created_at=created_at,
            delivered_at=delivered_at,
            id=id,
            last_error=last_error,
            payload=payload,
            status=status,
            subscription_id=subscription_id,
            url=url,
        )

        webhook_delivery.additional_properties = d
        return webhook_delivery

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
