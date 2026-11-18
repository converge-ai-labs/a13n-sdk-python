from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SessionApplicationSummary")


@_attrs_define(repr=False)
class SessionApplicationSummary:
    """All matching binding versions, counted once each independently of page size and cursor.

    Attributes:
        applied (int):
        on_create (int):
        on_next_use (int):
        pending (int):
        retry (int):
        unknown (int):
    """

    applied: int
    on_create: int
    on_next_use: int
    pending: int
    retry: int
    unknown: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        applied = self.applied

        on_create = self.on_create

        on_next_use = self.on_next_use

        pending = self.pending

        retry = self.retry

        unknown = self.unknown

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "applied": applied,
                "on_create": on_create,
                "on_next_use": on_next_use,
                "pending": pending,
                "retry": retry,
                "unknown": unknown,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        applied = d.pop("applied")

        on_create = d.pop("on_create")

        on_next_use = d.pop("on_next_use")

        pending = d.pop("pending")

        retry = d.pop("retry")

        unknown = d.pop("unknown")

        session_application_summary = cls(
            applied=applied,
            on_create=on_create,
            on_next_use=on_next_use,
            pending=pending,
            retry=retry,
            unknown=unknown,
        )

        session_application_summary.additional_properties = d
        return session_application_summary

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
