from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.busy_occurrence_page import BusyOccurrencePage


T = TypeVar("T", bound="ScheduleStatus")


@_attrs_define(repr=False)
class ScheduleStatus:
    """
    Attributes:
        busy_occurrences (BusyOccurrencePage):
        has_unfinished_work (bool):
        last_occurrence_id (None | str):
        next_fire_at (datetime.datetime | None):
        observed_at (datetime.datetime):
        pending_occurrence_id (None | str):
        schedule_id (str):
        session_id (str):
    """

    busy_occurrences: BusyOccurrencePage
    has_unfinished_work: bool
    last_occurrence_id: str | None
    next_fire_at: datetime.datetime | None
    observed_at: datetime.datetime
    pending_occurrence_id: str | None
    schedule_id: str
    session_id: str

    def to_dict(self) -> dict[str, Any]:
        busy_occurrences = self.busy_occurrences.to_dict()

        has_unfinished_work = self.has_unfinished_work

        last_occurrence_id: str | None
        last_occurrence_id = self.last_occurrence_id

        next_fire_at: str | None
        if isinstance(self.next_fire_at, datetime.datetime):
            next_fire_at = self.next_fire_at.isoformat()
        else:
            next_fire_at = self.next_fire_at

        observed_at = self.observed_at.isoformat()

        pending_occurrence_id: str | None
        pending_occurrence_id = self.pending_occurrence_id

        schedule_id = self.schedule_id

        session_id = self.session_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "busy_occurrences": busy_occurrences,
                "has_unfinished_work": has_unfinished_work,
                "last_occurrence_id": last_occurrence_id,
                "next_fire_at": next_fire_at,
                "observed_at": observed_at,
                "pending_occurrence_id": pending_occurrence_id,
                "schedule_id": schedule_id,
                "session_id": session_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.busy_occurrence_page import BusyOccurrencePage

        d = dict(src_dict)
        busy_occurrences = BusyOccurrencePage.from_dict(d.pop("busy_occurrences"))

        has_unfinished_work = d.pop("has_unfinished_work")

        def _parse_last_occurrence_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        last_occurrence_id = _parse_last_occurrence_id(d.pop("last_occurrence_id"))

        def _parse_next_fire_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_fire_at_type_0 = datetime.datetime.fromisoformat(data)

                return next_fire_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        next_fire_at = _parse_next_fire_at(d.pop("next_fire_at"))

        observed_at = datetime.datetime.fromisoformat(d.pop("observed_at"))

        def _parse_pending_occurrence_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        pending_occurrence_id = _parse_pending_occurrence_id(d.pop("pending_occurrence_id"))

        schedule_id = d.pop("schedule_id")

        session_id = d.pop("session_id")

        schedule_status = cls(
            busy_occurrences=busy_occurrences,
            has_unfinished_work=has_unfinished_work,
            last_occurrence_id=last_occurrence_id,
            next_fire_at=next_fire_at,
            observed_at=observed_at,
            pending_occurrence_id=pending_occurrence_id,
            schedule_id=schedule_id,
            session_id=session_id,
        )

        return schedule_status
