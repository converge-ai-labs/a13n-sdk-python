from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="OnceSchedule")


@_attrs_define(repr=False)
class OnceSchedule:
    """
    Attributes:
        run_at (datetime.datetime):
        type_ (Literal['once']):
    """

    run_at: datetime.datetime
    type_: Literal["once"]

    def to_dict(self) -> dict[str, Any]:
        run_at = self.run_at.isoformat()

        type_ = self.type_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "run_at": run_at,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        run_at = datetime.datetime.fromisoformat(d.pop("run_at"))

        type_ = cast(Literal["once"], d.pop("type"))
        if type_ != "once":
            raise ValueError(f"type must match const 'once', got '{type_}'")

        once_schedule = cls(
            run_at=run_at,
            type_=type_,
        )

        return once_schedule
