from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="MemoryFileMove")


@_attrs_define(repr=False)
class MemoryFileMove:
    """Moves the file `If-Match` names to a free path; it keeps its ID.

    Attributes:
        destination (str):
        source (str):
    """

    destination: str
    source: str

    def to_dict(self) -> dict[str, Any]:
        destination = self.destination

        source = self.source

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "destination": destination,
                "source": source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        destination = d.pop("destination")

        source = d.pop("source")

        memory_file_move = cls(
            destination=destination,
            source=source,
        )

        return memory_file_move
