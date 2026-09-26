from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.memory_access import MemoryAccess
from ..types import UNSET, Unset

T = TypeVar("T", bound="MemoryMount")


@_attrs_define(repr=False)
class MemoryMount:
    """A memory under the name the model addresses it by, exposing the tools its access allows. `recall` lets a
    record memory recall records into each run's first input; file memories ignore it.

        Attributes:
            access (MemoryAccess):
            memory_id (str):
            name (str):
            recall (bool | Unset):
    """

    access: MemoryAccess
    memory_id: str
    name: str
    recall: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        access = self.access.value

        memory_id = self.memory_id

        name = self.name

        recall = self.recall

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "access": access,
                "memory_id": memory_id,
                "name": name,
            }
        )
        if recall is not UNSET:
            field_dict["recall"] = recall

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access = MemoryAccess(d.pop("access"))

        memory_id = d.pop("memory_id")

        name = d.pop("name")

        recall = d.pop("recall", UNSET)

        memory_mount = cls(
            access=access,
            memory_id=memory_id,
            name=name,
            recall=recall,
        )

        return memory_mount
