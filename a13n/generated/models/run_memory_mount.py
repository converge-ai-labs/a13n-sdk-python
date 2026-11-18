from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.memory_access import MemoryAccess
from ..types import UNSET, Unset

T = TypeVar("T", bound="RunMemoryMount")


@_attrs_define(repr=False)
class RunMemoryMount:
    """Host-resolved Space identity and roots, never accepted from a mount request.

    Attributes:
        access (MemoryAccess):
        memory_id (str):
        name (str):
        recall (bool | Unset):
        roots (list[str] | Unset):
        space_id (None | str | Unset):
    """

    access: MemoryAccess
    memory_id: str
    name: str
    recall: bool | Unset = UNSET
    roots: list[str] | Unset = UNSET
    space_id: str | Unset | None = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access = self.access.value

        memory_id = self.memory_id

        name = self.name

        recall = self.recall

        roots: list[str] | Unset = UNSET
        if not isinstance(self.roots, Unset):
            roots = self.roots

        space_id: str | Unset | None
        if isinstance(self.space_id, Unset):
            space_id = UNSET
        else:
            space_id = self.space_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "access": access,
                "memory_id": memory_id,
                "name": name,
            }
        )
        if recall is not UNSET:
            field_dict["recall"] = recall
        if roots is not UNSET:
            field_dict["roots"] = roots
        if space_id is not UNSET:
            field_dict["space_id"] = space_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access = MemoryAccess(d.pop("access"))

        memory_id = d.pop("memory_id")

        name = d.pop("name")

        recall = d.pop("recall", UNSET)

        roots = cast(list[str], d.pop("roots", UNSET))

        def _parse_space_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        space_id = _parse_space_id(d.pop("space_id", UNSET))

        run_memory_mount = cls(
            access=access,
            memory_id=memory_id,
            name=name,
            recall=recall,
            roots=roots,
            space_id=space_id,
        )

        run_memory_mount.additional_properties = d
        return run_memory_mount

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
