from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cron_schedule import CronSchedule


T = TypeVar("T", bound="SchedulePreviewRequest")


@_attrs_define(repr=False)
class SchedulePreviewRequest:
    """
    Attributes:
        after (datetime.datetime):
        schedule (CronSchedule):
        count (int | Unset):
    """

    after: datetime.datetime
    schedule: CronSchedule
    count: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        after = self.after.isoformat()

        schedule = self.schedule.to_dict()

        count = self.count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "after": after,
                "schedule": schedule,
            }
        )
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cron_schedule import CronSchedule

        d = dict(src_dict)
        after = datetime.datetime.fromisoformat(d.pop("after"))

        schedule = CronSchedule.from_dict(d.pop("schedule"))

        count = d.pop("count", UNSET)

        schedule_preview_request = cls(
            after=after,
            schedule=schedule,
            count=count,
        )

        return schedule_preview_request
