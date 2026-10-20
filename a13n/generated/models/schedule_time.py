from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ScheduleTime")


@_attrs_define(repr=False)
class ScheduleTime:
    """
    Attributes:
        local (datetime.datetime):
        utc (datetime.datetime):
    """

    local: datetime.datetime
    utc: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        local = self.local.isoformat()

        utc = self.utc.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "local": local,
                "utc": utc,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        local = datetime.datetime.fromisoformat(d.pop("local"))

        utc = datetime.datetime.fromisoformat(d.pop("utc"))

        schedule_time = cls(
            local=local,
            utc=utc,
        )

        return schedule_time
