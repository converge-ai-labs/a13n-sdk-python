from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RealtimeSessionTicket")


@_attrs_define(repr=False)
class RealtimeSessionTicket:
    """
    Attributes:
        expires_in (int): Ticket lifetime in seconds.
        run_id (str):
        session_id (str):
        subprotocol (Literal['a13n.realtime.v1']): Offer this protocol first and the ticket second.
        thread_id (str):
        ticket (str): Single-use connection credential. Pass it as the second WebSocket subprotocol.
        websocket_path (str): WebSocket path relative to the Service origin.
    """

    expires_in: int
    run_id: str
    session_id: str
    subprotocol: Literal["a13n.realtime.v1"]
    thread_id: str
    ticket: str
    websocket_path: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expires_in = self.expires_in

        run_id = self.run_id

        session_id = self.session_id

        subprotocol = self.subprotocol

        thread_id = self.thread_id

        ticket = self.ticket

        websocket_path = self.websocket_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expires_in": expires_in,
                "run_id": run_id,
                "session_id": session_id,
                "subprotocol": subprotocol,
                "thread_id": thread_id,
                "ticket": ticket,
                "websocket_path": websocket_path,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expires_in = d.pop("expires_in")

        run_id = d.pop("run_id")

        session_id = d.pop("session_id")

        subprotocol = cast(Literal["a13n.realtime.v1"], d.pop("subprotocol"))
        if subprotocol != "a13n.realtime.v1":
            raise ValueError(f"subprotocol must match const 'a13n.realtime.v1', got '{subprotocol}'")

        thread_id = d.pop("thread_id")

        ticket = d.pop("ticket")

        websocket_path = d.pop("websocket_path")

        realtime_session_ticket = cls(
            expires_in=expires_in,
            run_id=run_id,
            session_id=session_id,
            subprotocol=subprotocol,
            thread_id=thread_id,
            ticket=ticket,
            websocket_path=websocket_path,
        )

        realtime_session_ticket.additional_properties = d
        return realtime_session_ticket

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
