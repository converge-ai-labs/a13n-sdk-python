from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Progress")


@_attrs_define(repr=False)
class Progress:
    """
    Attributes:
        last_occurrence_id (None | str):
        next_fire_at (datetime.datetime | None):
        pending_occurrence_id (None | str):
    """

    last_occurrence_id: str | None
    next_fire_at: datetime.datetime | None
    pending_occurrence_id: str | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_occurrence_id: str | None
        last_occurrence_id = self.last_occurrence_id

        next_fire_at: str | None
        if isinstance(self.next_fire_at, datetime.datetime):
            next_fire_at = self.next_fire_at.isoformat()
        else:
            next_fire_at = self.next_fire_at

        pending_occurrence_id: str | None
        pending_occurrence_id = self.pending_occurrence_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "last_occurrence_id": last_occurrence_id,
                "next_fire_at": next_fire_at,
                "pending_occurrence_id": pending_occurrence_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_last_occurrence_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        last_occurrence_id = _parse_last_occurrence_id(d.pop("last_occurrence_id"))

        def _parse_next_fire_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_fire_at_type_0 = datetime.datetime.fromisoformat(data)

                return next_fire_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        next_fire_at = _parse_next_fire_at(d.pop("next_fire_at"))

        def _parse_pending_occurrence_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        pending_occurrence_id = _parse_pending_occurrence_id(d.pop("pending_occurrence_id"))

        progress = cls(
            last_occurrence_id=last_occurrence_id,
            next_fire_at=next_fire_at,
            pending_occurrence_id=pending_occurrence_id,
        )

        progress.additional_properties = d
        return progress

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
