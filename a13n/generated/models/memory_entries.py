from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.memory_entry_selection import MemoryEntrySelection


T = TypeVar("T", bound="MemoryEntries")


@_attrs_define(repr=False)
class MemoryEntries:
    """
    Attributes:
        entries (list[MemoryEntrySelection]):
    """

    entries: list[MemoryEntrySelection]

    def to_dict(self) -> dict[str, Any]:
        entries = []
        for entries_item_data in self.entries:
            entries_item = entries_item_data.to_dict()
            entries.append(entries_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "entries": entries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.memory_entry_selection import MemoryEntrySelection

        d = dict(src_dict)
        entries = []
        _entries = d.pop("entries")
        for entries_item_data in _entries:
            entries_item = MemoryEntrySelection.from_dict(entries_item_data)

            entries.append(entries_item)

        memory_entries = cls(
            entries=entries,
        )

        return memory_entries
