from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="FilesystemMetrics")


@_attrs_define(repr=False)
class FilesystemMetrics:
    """
    Attributes:
        available_bytes (int):
        free_bytes (int):
        total_bytes (int):
        available_inodes (int | None | Unset):
        free_inodes (int | None | Unset):
        total_inodes (int | None | Unset):
    """

    available_bytes: int
    free_bytes: int
    total_bytes: int
    available_inodes: int | Unset | None = UNSET
    free_inodes: int | Unset | None = UNSET
    total_inodes: int | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        available_bytes = self.available_bytes

        free_bytes = self.free_bytes

        total_bytes = self.total_bytes

        available_inodes: int | Unset | None
        if isinstance(self.available_inodes, Unset):
            available_inodes = UNSET
        else:
            available_inodes = self.available_inodes

        free_inodes: int | Unset | None
        if isinstance(self.free_inodes, Unset):
            free_inodes = UNSET
        else:
            free_inodes = self.free_inodes

        total_inodes: int | Unset | None
        if isinstance(self.total_inodes, Unset):
            total_inodes = UNSET
        else:
            total_inodes = self.total_inodes

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "available_bytes": available_bytes,
                "free_bytes": free_bytes,
                "total_bytes": total_bytes,
            }
        )
        if available_inodes is not UNSET:
            field_dict["available_inodes"] = available_inodes
        if free_inodes is not UNSET:
            field_dict["free_inodes"] = free_inodes
        if total_inodes is not UNSET:
            field_dict["total_inodes"] = total_inodes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        available_bytes = d.pop("available_bytes")

        free_bytes = d.pop("free_bytes")

        total_bytes = d.pop("total_bytes")

        def _parse_available_inodes(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        available_inodes = _parse_available_inodes(d.pop("available_inodes", UNSET))

        def _parse_free_inodes(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        free_inodes = _parse_free_inodes(d.pop("free_inodes", UNSET))

        def _parse_total_inodes(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        total_inodes = _parse_total_inodes(d.pop("total_inodes", UNSET))

        filesystem_metrics = cls(
            available_bytes=available_bytes,
            free_bytes=free_bytes,
            total_bytes=total_bytes,
            available_inodes=available_inodes,
            free_inodes=free_inodes,
            total_inodes=total_inodes,
        )

        return filesystem_metrics
