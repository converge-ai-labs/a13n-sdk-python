from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.occurrence_status import OccurrenceStatus
from ..models.schedule_trigger import ScheduleTrigger
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.occurrence_execution import OccurrenceExecution
    from ..models.occurrence_snapshot import OccurrenceSnapshot


T = TypeVar("T", bound="Occurrence")


@_attrs_define(repr=False)
class Occurrence:
    """
    Attributes:
        covered_from_at (datetime.datetime | None):
        created_at (datetime.datetime):
        deadline_at (datetime.datetime):
        dispatch_attempts (int):
        entry_id (None | str):
        finished_at (datetime.datetime | None):
        id (str):
        last_error (None | str):
        next_attempt_at (datetime.datetime | None):
        principal_id (str):
        reason (None | str):
        requested_by_id (None | str):
        schedule_id (str):
        schedule_version (int):
        scheduled_at (datetime.datetime | None):
        session_id (str):
        snapshot (OccurrenceSnapshot):
        status (OccurrenceStatus):
        thread_id (None | str):
        trigger (ScheduleTrigger):
        updated_at (datetime.datetime):
        version (int):
        execution (None | OccurrenceExecution | Unset):
    """

    covered_from_at: datetime.datetime | None
    created_at: datetime.datetime
    deadline_at: datetime.datetime
    dispatch_attempts: int
    entry_id: str | None
    finished_at: datetime.datetime | None
    id: str
    last_error: str | None
    next_attempt_at: datetime.datetime | None
    principal_id: str
    reason: str | None
    requested_by_id: str | None
    schedule_id: str
    schedule_version: int
    scheduled_at: datetime.datetime | None
    session_id: str
    snapshot: OccurrenceSnapshot
    status: OccurrenceStatus
    thread_id: str | None
    trigger: ScheduleTrigger
    updated_at: datetime.datetime
    version: int
    execution: OccurrenceExecution | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.occurrence_execution import OccurrenceExecution

        covered_from_at: str | None
        if isinstance(self.covered_from_at, datetime.datetime):
            covered_from_at = self.covered_from_at.isoformat()
        else:
            covered_from_at = self.covered_from_at

        created_at = self.created_at.isoformat()

        deadline_at = self.deadline_at.isoformat()

        dispatch_attempts = self.dispatch_attempts

        entry_id: str | None
        entry_id = self.entry_id

        finished_at: str | None
        if isinstance(self.finished_at, datetime.datetime):
            finished_at = self.finished_at.isoformat()
        else:
            finished_at = self.finished_at

        id = self.id

        last_error: str | None
        last_error = self.last_error

        next_attempt_at: str | None
        if isinstance(self.next_attempt_at, datetime.datetime):
            next_attempt_at = self.next_attempt_at.isoformat()
        else:
            next_attempt_at = self.next_attempt_at

        principal_id = self.principal_id

        reason: str | None
        reason = self.reason

        requested_by_id: str | None
        requested_by_id = self.requested_by_id

        schedule_id = self.schedule_id

        schedule_version = self.schedule_version

        scheduled_at: str | None
        if isinstance(self.scheduled_at, datetime.datetime):
            scheduled_at = self.scheduled_at.isoformat()
        else:
            scheduled_at = self.scheduled_at

        session_id = self.session_id

        snapshot = self.snapshot.to_dict()

        status = self.status.value

        thread_id: str | None
        thread_id = self.thread_id

        trigger = self.trigger.value

        updated_at = self.updated_at.isoformat()

        version = self.version

        execution: dict[str, Any] | Unset | None
        if isinstance(self.execution, Unset):
            execution = UNSET
        elif isinstance(self.execution, OccurrenceExecution):
            execution = self.execution.to_dict()
        else:
            execution = self.execution

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "covered_from_at": covered_from_at,
                "created_at": created_at,
                "deadline_at": deadline_at,
                "dispatch_attempts": dispatch_attempts,
                "entry_id": entry_id,
                "finished_at": finished_at,
                "id": id,
                "last_error": last_error,
                "next_attempt_at": next_attempt_at,
                "principal_id": principal_id,
                "reason": reason,
                "requested_by_id": requested_by_id,
                "schedule_id": schedule_id,
                "schedule_version": schedule_version,
                "scheduled_at": scheduled_at,
                "session_id": session_id,
                "snapshot": snapshot,
                "status": status,
                "thread_id": thread_id,
                "trigger": trigger,
                "updated_at": updated_at,
                "version": version,
            }
        )
        if execution is not UNSET:
            field_dict["execution"] = execution

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.occurrence_execution import OccurrenceExecution
        from ..models.occurrence_snapshot import OccurrenceSnapshot

        d = dict(src_dict)

        def _parse_covered_from_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                covered_from_at_type_0 = datetime.datetime.fromisoformat(data)

                return covered_from_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        covered_from_at = _parse_covered_from_at(d.pop("covered_from_at"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        deadline_at = datetime.datetime.fromisoformat(d.pop("deadline_at"))

        dispatch_attempts = d.pop("dispatch_attempts")

        def _parse_entry_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        entry_id = _parse_entry_id(d.pop("entry_id"))

        def _parse_finished_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                finished_at_type_0 = datetime.datetime.fromisoformat(data)

                return finished_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        finished_at = _parse_finished_at(d.pop("finished_at"))

        id = d.pop("id")

        def _parse_last_error(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        last_error = _parse_last_error(d.pop("last_error"))

        def _parse_next_attempt_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_attempt_at_type_0 = datetime.datetime.fromisoformat(data)

                return next_attempt_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        next_attempt_at = _parse_next_attempt_at(d.pop("next_attempt_at"))

        principal_id = d.pop("principal_id")

        def _parse_reason(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        reason = _parse_reason(d.pop("reason"))

        def _parse_requested_by_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        requested_by_id = _parse_requested_by_id(d.pop("requested_by_id"))

        schedule_id = d.pop("schedule_id")

        schedule_version = d.pop("schedule_version")

        def _parse_scheduled_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scheduled_at_type_0 = datetime.datetime.fromisoformat(data)

                return scheduled_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        scheduled_at = _parse_scheduled_at(d.pop("scheduled_at"))

        session_id = d.pop("session_id")

        snapshot = OccurrenceSnapshot.from_dict(d.pop("snapshot"))

        status = OccurrenceStatus(d.pop("status"))

        def _parse_thread_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        thread_id = _parse_thread_id(d.pop("thread_id"))

        trigger = ScheduleTrigger(d.pop("trigger"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        version = d.pop("version")

        def _parse_execution(data: object) -> OccurrenceExecution | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                execution_type_0 = OccurrenceExecution.from_dict(data)

                return execution_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(OccurrenceExecution | Unset | None, data)

        execution = _parse_execution(d.pop("execution", UNSET))

        occurrence = cls(
            covered_from_at=covered_from_at,
            created_at=created_at,
            deadline_at=deadline_at,
            dispatch_attempts=dispatch_attempts,
            entry_id=entry_id,
            finished_at=finished_at,
            id=id,
            last_error=last_error,
            next_attempt_at=next_attempt_at,
            principal_id=principal_id,
            reason=reason,
            requested_by_id=requested_by_id,
            schedule_id=schedule_id,
            schedule_version=schedule_version,
            scheduled_at=scheduled_at,
            session_id=session_id,
            snapshot=snapshot,
            status=status,
            thread_id=thread_id,
            trigger=trigger,
            updated_at=updated_at,
            version=version,
            execution=execution,
        )

        return occurrence
