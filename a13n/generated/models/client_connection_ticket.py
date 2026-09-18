from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ClientConnectionTicket")


@_attrs_define(repr=False)
class ClientConnectionTicket:
    """
    Attributes:
        connection_id (str):
        expires_at (datetime.datetime):
        ticket (str):
        websocket_url (str):
    """

    connection_id: str
    expires_at: datetime.datetime
    ticket: str
    websocket_url: str

    def to_dict(self) -> dict[str, Any]:
        connection_id = self.connection_id

        expires_at = self.expires_at.isoformat()

        ticket = self.ticket

        websocket_url = self.websocket_url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "connection_id": connection_id,
                "expires_at": expires_at,
                "ticket": ticket,
                "websocket_url": websocket_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connection_id = d.pop("connection_id")

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        ticket = d.pop("ticket")

        websocket_url = d.pop("websocket_url")

        client_connection_ticket = cls(
            connection_id=connection_id,
            expires_at=expires_at,
            ticket=ticket,
            websocket_url=websocket_url,
        )

        return client_connection_ticket
