from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.connector_event_state import ConnectorEventState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connector_event_payload_type_0 import ConnectorEventPayloadType0


T = TypeVar("T", bound="ConnectorEvent")


@_attrs_define(repr=False)
class ConnectorEvent:
    """
    Attributes:
        attempts (int):
        created_at (datetime.datetime):
        event_type (str):
        failure (None | str):
        id (str):
        inbox_id (None | str):
        occurred_at (datetime.datetime):
        payload (ConnectorEventPayloadType0 | None):
        provider_id (str):
        source_id (str):
        state (ConnectorEventState):
        thread_id (None | str):
        trigger_id (None | str):
        version (int):
        retryable (bool | Unset):
    """

    attempts: int
    created_at: datetime.datetime
    event_type: str
    failure: str | None
    id: str
    inbox_id: str | None
    occurred_at: datetime.datetime
    payload: ConnectorEventPayloadType0 | None
    provider_id: str
    source_id: str
    state: ConnectorEventState
    thread_id: str | None
    trigger_id: str | None
    version: int
    retryable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.connector_event_payload_type_0 import ConnectorEventPayloadType0

        attempts = self.attempts

        created_at = self.created_at.isoformat()

        event_type = self.event_type

        failure: str | None
        failure = self.failure

        id = self.id

        inbox_id: str | None
        inbox_id = self.inbox_id

        occurred_at = self.occurred_at.isoformat()

        payload: dict[str, Any] | None
        if isinstance(self.payload, ConnectorEventPayloadType0):
            payload = self.payload.to_dict()
        else:
            payload = self.payload

        provider_id = self.provider_id

        source_id = self.source_id

        state = self.state.value

        thread_id: str | None
        thread_id = self.thread_id

        trigger_id: str | None
        trigger_id = self.trigger_id

        version = self.version

        retryable = self.retryable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attempts": attempts,
                "created_at": created_at,
                "event_type": event_type,
                "failure": failure,
                "id": id,
                "inbox_id": inbox_id,
                "occurred_at": occurred_at,
                "payload": payload,
                "provider_id": provider_id,
                "source_id": source_id,
                "state": state,
                "thread_id": thread_id,
                "trigger_id": trigger_id,
                "version": version,
            }
        )
        if retryable is not UNSET:
            field_dict["retryable"] = retryable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connector_event_payload_type_0 import ConnectorEventPayloadType0

        d = dict(src_dict)
        attempts = d.pop("attempts")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        event_type = d.pop("event_type")

        def _parse_failure(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        failure = _parse_failure(d.pop("failure"))

        id = d.pop("id")

        def _parse_inbox_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        inbox_id = _parse_inbox_id(d.pop("inbox_id"))

        occurred_at = datetime.datetime.fromisoformat(d.pop("occurred_at"))

        def _parse_payload(data: object) -> ConnectorEventPayloadType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payload_type_0 = ConnectorEventPayloadType0.from_dict(data)

                return payload_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConnectorEventPayloadType0 | None, data)

        payload = _parse_payload(d.pop("payload"))

        provider_id = d.pop("provider_id")

        source_id = d.pop("source_id")

        state = ConnectorEventState(d.pop("state"))

        def _parse_thread_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        thread_id = _parse_thread_id(d.pop("thread_id"))

        def _parse_trigger_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        trigger_id = _parse_trigger_id(d.pop("trigger_id"))

        version = d.pop("version")

        retryable = d.pop("retryable", UNSET)

        connector_event = cls(
            attempts=attempts,
            created_at=created_at,
            event_type=event_type,
            failure=failure,
            id=id,
            inbox_id=inbox_id,
            occurred_at=occurred_at,
            payload=payload,
            provider_id=provider_id,
            source_id=source_id,
            state=state,
            thread_id=thread_id,
            trigger_id=trigger_id,
            version=version,
            retryable=retryable,
        )

        connector_event.additional_properties = d
        return connector_event

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
