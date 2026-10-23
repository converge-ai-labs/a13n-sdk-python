from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ScheduleOrigin")


@_attrs_define(repr=False)
class ScheduleOrigin:
    """
    Attributes:
        occurrence_id (str):
        schedule_id (str):
    """

    occurrence_id: str
    schedule_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        occurrence_id = self.occurrence_id

        schedule_id = self.schedule_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "occurrence_id": occurrence_id,
                "schedule_id": schedule_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        occurrence_id = d.pop("occurrence_id")

        schedule_id = d.pop("schedule_id")

        schedule_origin = cls(
            occurrence_id=occurrence_id,
            schedule_id=schedule_id,
        )

        schedule_origin.additional_properties = d
        return schedule_origin

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
