from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="MemoryFileCreate")


@_attrs_define(repr=False)
class MemoryFileCreate:
    """
    Attributes:
        content (str):
        path (str):
    """

    content: str
    path: str

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        path = self.path

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "content": content,
                "path": path,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = d.pop("content")

        path = d.pop("path")

        memory_file_create = cls(
            content=content,
            path=path,
        )

        return memory_file_create
