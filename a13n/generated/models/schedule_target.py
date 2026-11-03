from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.schedule_target_mode import ScheduleTargetMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="ScheduleTarget")


@_attrs_define(repr=False)
class ScheduleTarget:
    """Omitted IDs create a session and, for thread mode, one empty reusable thread.

    Attributes:
        mode (ScheduleTargetMode | Unset):
        session_id (None | str | Unset):
        thread_id (None | str | Unset):
    """

    mode: ScheduleTargetMode | Unset = UNSET
    session_id: str | Unset | None = UNSET
    thread_id: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        session_id: str | Unset | None
        if isinstance(self.session_id, Unset):
            session_id = UNSET
        else:
            session_id = self.session_id

        thread_id: str | Unset | None
        if isinstance(self.thread_id, Unset):
            thread_id = UNSET
        else:
            thread_id = self.thread_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if mode is not UNSET:
            field_dict["mode"] = mode
        if session_id is not UNSET:
            field_dict["session_id"] = session_id
        if thread_id is not UNSET:
            field_dict["thread_id"] = thread_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _mode = d.pop("mode", UNSET)
        mode: ScheduleTargetMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = ScheduleTargetMode(_mode)

        def _parse_session_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        session_id = _parse_session_id(d.pop("session_id", UNSET))

        def _parse_thread_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        thread_id = _parse_thread_id(d.pop("thread_id", UNSET))

        schedule_target = cls(
            mode=mode,
            session_id=session_id,
            thread_id=thread_id,
        )

        return schedule_target
