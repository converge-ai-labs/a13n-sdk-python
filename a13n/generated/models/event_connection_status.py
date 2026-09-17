from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.event_connection_status_state import EventConnectionStatusState
from ..models.event_connection_status_transport import EventConnectionStatusTransport
from ..types import UNSET, Unset

T = TypeVar("T", bound="EventConnectionStatus")


@_attrs_define(repr=False)
class EventConnectionStatus:
    """
    Attributes:
        state (EventConnectionStatusState):
        transport (EventConnectionStatusTransport):
        error_code (None | str | Unset):
        last_event_at (datetime.datetime | None | Unset):
        observed_at (datetime.datetime | None | Unset):
    """

    state: EventConnectionStatusState
    transport: EventConnectionStatusTransport
    error_code: str | Unset | None = UNSET
    last_event_at: datetime.datetime | Unset | None = UNSET
    observed_at: datetime.datetime | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        state = self.state.value

        transport = self.transport.value

        error_code: str | Unset | None
        if isinstance(self.error_code, Unset):
            error_code = UNSET
        else:
            error_code = self.error_code

        last_event_at: str | Unset | None
        if isinstance(self.last_event_at, Unset):
            last_event_at = UNSET
        elif isinstance(self.last_event_at, datetime.datetime):
            last_event_at = self.last_event_at.isoformat()
        else:
            last_event_at = self.last_event_at

        observed_at: str | Unset | None
        if isinstance(self.observed_at, Unset):
            observed_at = UNSET
        elif isinstance(self.observed_at, datetime.datetime):
            observed_at = self.observed_at.isoformat()
        else:
            observed_at = self.observed_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "state": state,
                "transport": transport,
            }
        )
        if error_code is not UNSET:
            field_dict["error_code"] = error_code
        if last_event_at is not UNSET:
            field_dict["last_event_at"] = last_event_at
        if observed_at is not UNSET:
            field_dict["observed_at"] = observed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        state = EventConnectionStatusState(d.pop("state"))

        transport = EventConnectionStatusTransport(d.pop("transport"))

        def _parse_error_code(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        error_code = _parse_error_code(d.pop("error_code", UNSET))

        def _parse_last_event_at(data: object) -> datetime.datetime | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_event_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_event_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | Unset | None, data)

        last_event_at = _parse_last_event_at(d.pop("last_event_at", UNSET))

        def _parse_observed_at(data: object) -> datetime.datetime | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                observed_at_type_0 = datetime.datetime.fromisoformat(data)

                return observed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | Unset | None, data)

        observed_at = _parse_observed_at(d.pop("observed_at", UNSET))

        event_connection_status = cls(
            state=state,
            transport=transport,
            error_code=error_code,
            last_event_at=last_event_at,
            observed_at=observed_at,
        )

        return event_connection_status
