from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.cron_schedule import CronSchedule
    from ..models.schedule_invocation_output import ScheduleInvocationOutput


T = TypeVar("T", bound="OccurrenceSnapshot")


@_attrs_define(repr=False)
class OccurrenceSnapshot:
    """
    Attributes:
        invocation (ScheduleInvocationOutput):
        max_lateness_seconds (int):
        name (str):
        schedule (CronSchedule):
        timezone_data_version (str):
        utc_offset_seconds (int | None):
    """

    invocation: ScheduleInvocationOutput
    max_lateness_seconds: int
    name: str
    schedule: CronSchedule
    timezone_data_version: str
    utc_offset_seconds: int | None

    def to_dict(self) -> dict[str, Any]:
        invocation = self.invocation.to_dict()

        max_lateness_seconds = self.max_lateness_seconds

        name = self.name

        schedule = self.schedule.to_dict()

        timezone_data_version = self.timezone_data_version

        utc_offset_seconds: int | None
        utc_offset_seconds = self.utc_offset_seconds

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "invocation": invocation,
                "max_lateness_seconds": max_lateness_seconds,
                "name": name,
                "schedule": schedule,
                "timezone_data_version": timezone_data_version,
                "utc_offset_seconds": utc_offset_seconds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cron_schedule import CronSchedule
        from ..models.schedule_invocation_output import ScheduleInvocationOutput

        d = dict(src_dict)
        invocation = ScheduleInvocationOutput.from_dict(d.pop("invocation"))

        max_lateness_seconds = d.pop("max_lateness_seconds")

        name = d.pop("name")

        schedule = CronSchedule.from_dict(d.pop("schedule"))

        timezone_data_version = d.pop("timezone_data_version")

        def _parse_utc_offset_seconds(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        utc_offset_seconds = _parse_utc_offset_seconds(d.pop("utc_offset_seconds"))

        occurrence_snapshot = cls(
            invocation=invocation,
            max_lateness_seconds=max_lateness_seconds,
            name=name,
            schedule=schedule,
            timezone_data_version=timezone_data_version,
            utc_offset_seconds=utc_offset_seconds,
        )

        return occurrence_snapshot
