from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="NativeIsolation")


@_attrs_define(repr=False)
class NativeIsolation:
    """
    Attributes:
        mode (Literal['native']):
    """

    mode: Literal["native"]

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "mode": mode,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mode = cast(Literal["native"], d.pop("mode"))
        if mode != "native":
            raise ValueError(f"mode must match const 'native', got '{mode}'")

        native_isolation = cls(
            mode=mode,
        )

        return native_isolation
