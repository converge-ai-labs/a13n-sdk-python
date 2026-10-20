from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ScheduleCommand")


@_attrs_define(repr=False)
class ScheduleCommand:
    """Commands accept no configuration or authority overrides."""

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        schedule_command = cls()

        return schedule_command
