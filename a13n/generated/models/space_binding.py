from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.memory_access import MemoryAccess
from ..types import UNSET, Unset

T = TypeVar("T", bound="SpaceBinding")


@_attrs_define(repr=False)
class SpaceBinding:
    """A named Space selected by the App or inherited from Agent defaults.

    Attributes:
        name (str):
        space_id (str):
        access (MemoryAccess | Unset):
    """

    name: str
    space_id: str
    access: MemoryAccess | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        space_id = self.space_id

        access: str | Unset = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "space_id": space_id,
            }
        )
        if access is not UNSET:
            field_dict["access"] = access

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        space_id = d.pop("space_id")

        _access = d.pop("access", UNSET)
        access: MemoryAccess | Unset
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = MemoryAccess(_access)

        space_binding = cls(
            name=name,
            space_id=space_id,
            access=access,
        )

        return space_binding
