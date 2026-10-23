from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DiskIoMetrics")


@_attrs_define(repr=False)
class DiskIoMetrics:
    """
    Attributes:
        identity (str):
        busy_time_ms (int | None | Unset):
        in_progress (int | None | Unset):
        read_bytes (int | None | Unset):
        read_operations (int | None | Unset):
        read_time_ms (int | None | Unset):
        weighted_time_ms (int | None | Unset):
        write_operations (int | None | Unset):
        write_time_ms (int | None | Unset):
        written_bytes (int | None | Unset):
    """

    identity: str
    busy_time_ms: int | Unset | None = UNSET
    in_progress: int | Unset | None = UNSET
    read_bytes: int | Unset | None = UNSET
    read_operations: int | Unset | None = UNSET
    read_time_ms: int | Unset | None = UNSET
    weighted_time_ms: int | Unset | None = UNSET
    write_operations: int | Unset | None = UNSET
    write_time_ms: int | Unset | None = UNSET
    written_bytes: int | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        identity = self.identity

        busy_time_ms: int | Unset | None
        if isinstance(self.busy_time_ms, Unset):
            busy_time_ms = UNSET
        else:
            busy_time_ms = self.busy_time_ms

        in_progress: int | Unset | None
        if isinstance(self.in_progress, Unset):
            in_progress = UNSET
        else:
            in_progress = self.in_progress

        read_bytes: int | Unset | None
        if isinstance(self.read_bytes, Unset):
            read_bytes = UNSET
        else:
            read_bytes = self.read_bytes

        read_operations: int | Unset | None
        if isinstance(self.read_operations, Unset):
            read_operations = UNSET
        else:
            read_operations = self.read_operations

        read_time_ms: int | Unset | None
        if isinstance(self.read_time_ms, Unset):
            read_time_ms = UNSET
        else:
            read_time_ms = self.read_time_ms

        weighted_time_ms: int | Unset | None
        if isinstance(self.weighted_time_ms, Unset):
            weighted_time_ms = UNSET
        else:
            weighted_time_ms = self.weighted_time_ms

        write_operations: int | Unset | None
        if isinstance(self.write_operations, Unset):
            write_operations = UNSET
        else:
            write_operations = self.write_operations

        write_time_ms: int | Unset | None
        if isinstance(self.write_time_ms, Unset):
            write_time_ms = UNSET
        else:
            write_time_ms = self.write_time_ms

        written_bytes: int | Unset | None
        if isinstance(self.written_bytes, Unset):
            written_bytes = UNSET
        else:
            written_bytes = self.written_bytes

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "identity": identity,
            }
        )
        if busy_time_ms is not UNSET:
            field_dict["busy_time_ms"] = busy_time_ms
        if in_progress is not UNSET:
            field_dict["in_progress"] = in_progress
        if read_bytes is not UNSET:
            field_dict["read_bytes"] = read_bytes
        if read_operations is not UNSET:
            field_dict["read_operations"] = read_operations
        if read_time_ms is not UNSET:
            field_dict["read_time_ms"] = read_time_ms
        if weighted_time_ms is not UNSET:
            field_dict["weighted_time_ms"] = weighted_time_ms
        if write_operations is not UNSET:
            field_dict["write_operations"] = write_operations
        if write_time_ms is not UNSET:
            field_dict["write_time_ms"] = write_time_ms
        if written_bytes is not UNSET:
            field_dict["written_bytes"] = written_bytes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identity = d.pop("identity")

        def _parse_busy_time_ms(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        busy_time_ms = _parse_busy_time_ms(d.pop("busy_time_ms", UNSET))

        def _parse_in_progress(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        in_progress = _parse_in_progress(d.pop("in_progress", UNSET))

        def _parse_read_bytes(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        read_bytes = _parse_read_bytes(d.pop("read_bytes", UNSET))

        def _parse_read_operations(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        read_operations = _parse_read_operations(d.pop("read_operations", UNSET))

        def _parse_read_time_ms(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        read_time_ms = _parse_read_time_ms(d.pop("read_time_ms", UNSET))

        def _parse_weighted_time_ms(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        weighted_time_ms = _parse_weighted_time_ms(d.pop("weighted_time_ms", UNSET))

        def _parse_write_operations(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        write_operations = _parse_write_operations(d.pop("write_operations", UNSET))

        def _parse_write_time_ms(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        write_time_ms = _parse_write_time_ms(d.pop("write_time_ms", UNSET))

        def _parse_written_bytes(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        written_bytes = _parse_written_bytes(d.pop("written_bytes", UNSET))

        disk_io_metrics = cls(
            identity=identity,
            busy_time_ms=busy_time_ms,
            in_progress=in_progress,
            read_bytes=read_bytes,
            read_operations=read_operations,
            read_time_ms=read_time_ms,
            weighted_time_ms=weighted_time_ms,
            write_operations=write_operations,
            write_time_ms=write_time_ms,
            written_bytes=written_bytes,
        )

        return disk_io_metrics
