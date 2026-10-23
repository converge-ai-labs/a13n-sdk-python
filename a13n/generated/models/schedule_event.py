from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.progress import Progress
    from ..models.schedule_configuration import ScheduleConfiguration


T = TypeVar("T", bound="ScheduleEvent")


@_attrs_define(repr=False)
class ScheduleEvent:
    """
    Attributes:
        configuration (ScheduleConfiguration):
        progress (Progress):
        schedule_id (str):
        session_id (str):
    """

    configuration: ScheduleConfiguration
    progress: Progress
    schedule_id: str
    session_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configuration = self.configuration.to_dict()

        progress = self.progress.to_dict()

        schedule_id = self.schedule_id

        session_id = self.session_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "configuration": configuration,
                "progress": progress,
                "schedule_id": schedule_id,
                "session_id": session_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.progress import Progress
        from ..models.schedule_configuration import ScheduleConfiguration

        d = dict(src_dict)
        configuration = ScheduleConfiguration.from_dict(d.pop("configuration"))

        progress = Progress.from_dict(d.pop("progress"))

        schedule_id = d.pop("schedule_id")

        session_id = d.pop("session_id")

        schedule_event = cls(
            configuration=configuration,
            progress=progress,
            schedule_id=schedule_id,
            session_id=session_id,
        )

        schedule_event.additional_properties = d
        return schedule_event

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
