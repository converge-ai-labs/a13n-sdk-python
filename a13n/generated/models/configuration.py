from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.schedule_state import ScheduleState

if TYPE_CHECKING:
    from ..models.cron_schedule import CronSchedule


T = TypeVar("T", bound="Configuration")


@_attrs_define(repr=False)
class Configuration:
    """
    Attributes:
        id (str):
        max_lateness_seconds (int):
        name (str):
        pause_reason (None | str):
        principal_id (str):
        schedule (CronSchedule):
        session_id (str):
        state (ScheduleState):
        version (int):
    """

    id: str
    max_lateness_seconds: int
    name: str
    pause_reason: str | None
    principal_id: str
    schedule: CronSchedule
    session_id: str
    state: ScheduleState
    version: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        max_lateness_seconds = self.max_lateness_seconds

        name = self.name

        pause_reason: str | None
        pause_reason = self.pause_reason

        principal_id = self.principal_id

        schedule = self.schedule.to_dict()

        session_id = self.session_id

        state = self.state.value

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "max_lateness_seconds": max_lateness_seconds,
                "name": name,
                "pause_reason": pause_reason,
                "principal_id": principal_id,
                "schedule": schedule,
                "session_id": session_id,
                "state": state,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cron_schedule import CronSchedule

        d = dict(src_dict)
        id = d.pop("id")

        max_lateness_seconds = d.pop("max_lateness_seconds")

        name = d.pop("name")

        def _parse_pause_reason(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        pause_reason = _parse_pause_reason(d.pop("pause_reason"))

        principal_id = d.pop("principal_id")

        schedule = CronSchedule.from_dict(d.pop("schedule"))

        session_id = d.pop("session_id")

        state = ScheduleState(d.pop("state"))

        version = d.pop("version")

        configuration = cls(
            id=id,
            max_lateness_seconds=max_lateness_seconds,
            name=name,
            pause_reason=pause_reason,
            principal_id=principal_id,
            schedule=schedule,
            session_id=session_id,
            state=state,
            version=version,
        )

        configuration.additional_properties = d
        return configuration

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
