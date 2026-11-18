from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileMemoryTarget")


@_attrs_define(repr=False)
class FileMemoryTarget:
    """
    Attributes:
        id (str):
        kind (Literal['memory'] | Unset):
    """

    id: str
    kind: Literal["memory"] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        kind = self.kind

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        kind = cast(Literal["memory"] | Unset, d.pop("kind", UNSET))
        if kind != "memory" and not isinstance(kind, Unset):
            raise ValueError(f"kind must match const 'memory', got '{kind}'")

        file_memory_target = cls(
            id=id,
            kind=kind,
        )

        return file_memory_target
