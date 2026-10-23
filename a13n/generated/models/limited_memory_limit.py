from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="LimitedMemoryLimit")


@_attrs_define(repr=False)
class LimitedMemoryLimit:
    """
    Attributes:
        bytes_ (int):
        kind (Literal['limited']):
    """

    bytes_: int
    kind: Literal["limited"]

    def to_dict(self) -> dict[str, Any]:
        bytes_ = self.bytes_

        kind = self.kind

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "bytes": bytes_,
                "kind": kind,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bytes_ = d.pop("bytes")

        kind = cast(Literal["limited"], d.pop("kind"))
        if kind != "limited":
            raise ValueError(f"kind must match const 'limited', got '{kind}'")

        limited_memory_limit = cls(
            bytes_=bytes_,
            kind=kind,
        )

        return limited_memory_limit
