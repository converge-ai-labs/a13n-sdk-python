from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="BusyOccurrence")


@_attrs_define(repr=False)
class BusyOccurrence:
    """
    Attributes:
        entry_id (str):
        occurrence_id (str):
        root_thread_id (str):
    """

    entry_id: str
    occurrence_id: str
    root_thread_id: str

    def to_dict(self) -> dict[str, Any]:
        entry_id = self.entry_id

        occurrence_id = self.occurrence_id

        root_thread_id = self.root_thread_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "entry_id": entry_id,
                "occurrence_id": occurrence_id,
                "root_thread_id": root_thread_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entry_id = d.pop("entry_id")

        occurrence_id = d.pop("occurrence_id")

        root_thread_id = d.pop("root_thread_id")

        busy_occurrence = cls(
            entry_id=entry_id,
            occurrence_id=occurrence_id,
            root_thread_id=root_thread_id,
        )

        return busy_occurrence
