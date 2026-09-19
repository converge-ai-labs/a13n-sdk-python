from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.directory_entry import DirectoryEntry


T = TypeVar("T", bound="DirectoryListResult")


@_attrs_define(repr=False)
class DirectoryListResult:
    """
    Attributes:
        path (str):
        entries (list[DirectoryEntry] | Unset):
        next_offset (int | None | Unset):
        parent_path (None | str | Unset):
    """

    path: str
    entries: list[DirectoryEntry] | Unset = UNSET
    next_offset: int | Unset | None = UNSET
    parent_path: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

        next_offset: int | Unset | None
        if isinstance(self.next_offset, Unset):
            next_offset = UNSET
        else:
            next_offset = self.next_offset

        parent_path: str | Unset | None
        if isinstance(self.parent_path, Unset):
            parent_path = UNSET
        else:
            parent_path = self.parent_path

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "path": path,
            }
        )
        if entries is not UNSET:
            field_dict["entries"] = entries
        if next_offset is not UNSET:
            field_dict["next_offset"] = next_offset
        if parent_path is not UNSET:
            field_dict["parent_path"] = parent_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.directory_entry import DirectoryEntry

        d = dict(src_dict)
        path = d.pop("path")

        _entries = d.pop("entries", UNSET)
        entries: list[DirectoryEntry] | Unset = UNSET
        if _entries is not UNSET:
            entries = []
            for entries_item_data in _entries:
                entries_item = DirectoryEntry.from_dict(entries_item_data)

                entries.append(entries_item)

        def _parse_next_offset(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        next_offset = _parse_next_offset(d.pop("next_offset", UNSET))

        def _parse_parent_path(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        parent_path = _parse_parent_path(d.pop("parent_path", UNSET))

        directory_list_result = cls(
            path=path,
            entries=entries,
            next_offset=next_offset,
            parent_path=parent_path,
        )

        return directory_list_result
