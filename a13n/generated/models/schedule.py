from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.schedule_pause_reason_type_0 import SchedulePauseReasonType0
from ..models.schedule_state import ScheduleState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cron_schedule import CronSchedule
    from ..models.once_schedule import OnceSchedule
    from ..models.schedule_invocation_output import ScheduleInvocationOutput
    from ..models.schedule_labels import ScheduleLabels


T = TypeVar("T", bound="Schedule")


@_attrs_define(repr=False)
class Schedule:
    """
    Attributes:
        archived_at (datetime.datetime | None):
        created_at (datetime.datetime):
        created_by_id (str):
        id (str):
        invocation (ScheduleInvocationOutput):
        name (str):
        pause_reason (None | SchedulePauseReasonType0):
        principal_id (str):
        schedule (CronSchedule | OnceSchedule):
        session_id (str):
        state (ScheduleState):
        stream_url (str):
        updated_at (datetime.datetime):
        updated_by_id (str):
        version (int):
        workspace_id (str):
        description (None | str | Unset):
        labels (ScheduleLabels | Unset):
        max_lateness_seconds (int | Unset):
    """

    archived_at: datetime.datetime | None
    created_at: datetime.datetime
    created_by_id: str
    id: str
    invocation: ScheduleInvocationOutput
    name: str
    pause_reason: SchedulePauseReasonType0 | None
    principal_id: str
    schedule: CronSchedule | OnceSchedule
    session_id: str
    state: ScheduleState
    stream_url: str
    updated_at: datetime.datetime
    updated_by_id: str
    version: int
    workspace_id: str
    description: str | Unset | None = UNSET
    labels: ScheduleLabels | Unset = UNSET
    max_lateness_seconds: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.cron_schedule import CronSchedule

        archived_at: str | None
        if isinstance(self.archived_at, datetime.datetime):
            archived_at = self.archived_at.isoformat()
        else:
            archived_at = self.archived_at

        created_at = self.created_at.isoformat()

        created_by_id = self.created_by_id

        id = self.id

        invocation = self.invocation.to_dict()

        name = self.name

        pause_reason: str | None
        if isinstance(self.pause_reason, SchedulePauseReasonType0):
            pause_reason = self.pause_reason.value
        else:
            pause_reason = self.pause_reason

        principal_id = self.principal_id

        schedule: dict[str, Any]
        if isinstance(self.schedule, CronSchedule):
            schedule = self.schedule.to_dict()
        else:
            schedule = self.schedule.to_dict()

        session_id = self.session_id

        state = self.state.value

        stream_url = self.stream_url

        updated_at = self.updated_at.isoformat()

        updated_by_id = self.updated_by_id

        version = self.version

        workspace_id = self.workspace_id

        description: str | Unset | None
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        max_lateness_seconds = self.max_lateness_seconds

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "archived_at": archived_at,
                "created_at": created_at,
                "created_by_id": created_by_id,
                "id": id,
                "invocation": invocation,
                "name": name,
                "pause_reason": pause_reason,
                "principal_id": principal_id,
                "schedule": schedule,
                "session_id": session_id,
                "state": state,
                "stream_url": stream_url,
                "updated_at": updated_at,
                "updated_by_id": updated_by_id,
                "version": version,
                "workspace_id": workspace_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if labels is not UNSET:
            field_dict["labels"] = labels
        if max_lateness_seconds is not UNSET:
            field_dict["max_lateness_seconds"] = max_lateness_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cron_schedule import CronSchedule
        from ..models.once_schedule import OnceSchedule
        from ..models.schedule_invocation_output import ScheduleInvocationOutput
        from ..models.schedule_labels import ScheduleLabels

        d = dict(src_dict)

        def _parse_archived_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                archived_at_type_0 = datetime.datetime.fromisoformat(data)

                return archived_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        archived_at = _parse_archived_at(d.pop("archived_at"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        created_by_id = d.pop("created_by_id")

        id = d.pop("id")

        invocation = ScheduleInvocationOutput.from_dict(d.pop("invocation"))

        name = d.pop("name")

        def _parse_pause_reason(data: object) -> SchedulePauseReasonType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                pause_reason_type_0 = SchedulePauseReasonType0(data)

                return pause_reason_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(SchedulePauseReasonType0 | None, data)

        pause_reason = _parse_pause_reason(d.pop("pause_reason"))

        principal_id = d.pop("principal_id")

        def _parse_schedule(data: object) -> CronSchedule | OnceSchedule:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_schedule_rule_type_0 = CronSchedule.from_dict(data)

                return componentsschemas_schedule_rule_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_schedule_rule_type_1 = OnceSchedule.from_dict(data)

            return componentsschemas_schedule_rule_type_1

        schedule = _parse_schedule(d.pop("schedule"))

        session_id = d.pop("session_id")

        state = ScheduleState(d.pop("state"))

        stream_url = d.pop("stream_url")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        updated_by_id = d.pop("updated_by_id")

        version = d.pop("version")

        workspace_id = d.pop("workspace_id")

        def _parse_description(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        description = _parse_description(d.pop("description", UNSET))

        _labels = d.pop("labels", UNSET)
        labels: ScheduleLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = ScheduleLabels.from_dict(_labels)

        max_lateness_seconds = d.pop("max_lateness_seconds", UNSET)

        schedule = cls(
            archived_at=archived_at,
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            invocation=invocation,
            name=name,
            pause_reason=pause_reason,
            principal_id=principal_id,
            schedule=schedule,
            session_id=session_id,
            state=state,
            stream_url=stream_url,
            updated_at=updated_at,
            updated_by_id=updated_by_id,
            version=version,
            workspace_id=workspace_id,
            description=description,
            labels=labels,
            max_lateness_seconds=max_lateness_seconds,
        )

        return schedule
