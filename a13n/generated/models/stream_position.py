from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="StreamPosition")


@_attrs_define(repr=False)
class StreamPosition:
    """
    Attributes:
        attempt (int):
        sequence (int):
    """

    attempt: int
    sequence: int

    def to_dict(self) -> dict[str, Any]:
        attempt = self.attempt

        sequence = self.sequence

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "attempt": attempt,
                "sequence": sequence,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attempt = d.pop("attempt")

        sequence = d.pop("sequence")

        stream_position = cls(
            attempt=attempt,
            sequence=sequence,
        )

        return stream_position
