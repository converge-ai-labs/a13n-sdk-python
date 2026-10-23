from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="UnlimitedCpuLimit")


@_attrs_define(repr=False)
class UnlimitedCpuLimit:
    """
    Attributes:
        kind (Literal['unlimited']):
    """

    kind: Literal["unlimited"]

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = cast(Literal["unlimited"], d.pop("kind"))
        if kind != "unlimited":
            raise ValueError(f"kind must match const 'unlimited', got '{kind}'")

        unlimited_cpu_limit = cls(
            kind=kind,
        )

        return unlimited_cpu_limit
