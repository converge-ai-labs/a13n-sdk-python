from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.memory_source_kind import MemorySourceKind
from ..models.memory_source_status import MemorySourceStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_source import FileSource
    from ..models.record_source import RecordSource


T = TypeVar("T", bound="MemorySource")


@_attrs_define(repr=False)
class MemorySource:
    """One automatic delivery in this Run; content remains in the memory or execution archive.

    Attributes:
        kind (MemorySourceKind):
        memory (str):
        status (MemorySourceStatus):
        cursor (None | str | Unset):
        files (list[FileSource] | Unset):
        memory_id (None | str | Unset):
        records (list[RecordSource] | Unset):
        sources_truncated (bool | Unset):
    """

    kind: MemorySourceKind
    memory: str
    status: MemorySourceStatus
    cursor: str | Unset | None = UNSET
    files: list[FileSource] | Unset = UNSET
    memory_id: str | Unset | None = UNSET
    records: list[RecordSource] | Unset = UNSET
    sources_truncated: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        memory = self.memory

        status = self.status.value

        cursor: str | Unset | None
        if isinstance(self.cursor, Unset):
            cursor = UNSET
        else:
            cursor = self.cursor

        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        memory_id: str | Unset | None
        if isinstance(self.memory_id, Unset):
            memory_id = UNSET
        else:
            memory_id = self.memory_id

        records: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.records, Unset):
            records = []
            for records_item_data in self.records:
                records_item = records_item_data.to_dict()
                records.append(records_item)

        sources_truncated = self.sources_truncated

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
                "memory": memory,
                "status": status,
            }
        )
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if files is not UNSET:
            field_dict["files"] = files
        if memory_id is not UNSET:
            field_dict["memory_id"] = memory_id
        if records is not UNSET:
            field_dict["records"] = records
        if sources_truncated is not UNSET:
            field_dict["sources_truncated"] = sources_truncated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_source import FileSource
        from ..models.record_source import RecordSource

        d = dict(src_dict)
        kind = MemorySourceKind(d.pop("kind"))

        memory = d.pop("memory")

        status = MemorySourceStatus(d.pop("status"))

        def _parse_cursor(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        cursor = _parse_cursor(d.pop("cursor", UNSET))

        _files = d.pop("files", UNSET)
        files: list[FileSource] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = FileSource.from_dict(files_item_data)

                files.append(files_item)

        def _parse_memory_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        memory_id = _parse_memory_id(d.pop("memory_id", UNSET))

        _records = d.pop("records", UNSET)
        records: list[RecordSource] | Unset = UNSET
        if _records is not UNSET:
            records = []
            for records_item_data in _records:
                records_item = RecordSource.from_dict(records_item_data)

                records.append(records_item)

        sources_truncated = d.pop("sources_truncated", UNSET)

        memory_source = cls(
            kind=kind,
            memory=memory,
            status=status,
            cursor=cursor,
            files=files,
            memory_id=memory_id,
            records=records,
            sources_truncated=sources_truncated,
        )

        return memory_source
