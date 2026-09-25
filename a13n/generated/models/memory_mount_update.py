from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.memory_access import MemoryAccess
from ..types import UNSET, Unset

T = TypeVar("T", bound="MemoryMountUpdate")


@_attrs_define(repr=False)
class MemoryMountUpdate:
    """Fields left out stay unchanged.

    Attributes:
        access (MemoryAccess | None | Unset):
        recall (bool | None | Unset):
    """

    access: MemoryAccess | Unset | None = UNSET
    recall: bool | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        access: str | Unset | None
        if isinstance(self.access, Unset):
            access = UNSET
        elif isinstance(self.access, MemoryAccess):
            access = self.access.value
        else:
            access = self.access

        recall: bool | Unset | None
        if isinstance(self.recall, Unset):
            recall = UNSET
        else:
            recall = self.recall

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if access is not UNSET:
            field_dict["access"] = access
        if recall is not UNSET:
            field_dict["recall"] = recall

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_access(data: object) -> MemoryAccess | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                access_type_0 = MemoryAccess(data)

                return access_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MemoryAccess | Unset | None, data)

        access = _parse_access(d.pop("access", UNSET))

        def _parse_recall(data: object) -> bool | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | Unset | None, data)

        recall = _parse_recall(d.pop("recall", UNSET))

        memory_mount_update = cls(
            access=access,
            recall=recall,
        )

        return memory_mount_update
