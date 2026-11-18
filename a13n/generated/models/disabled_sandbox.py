from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="DisabledSandbox")


@_attrs_define(repr=False)
class DisabledSandbox:
    """
    Attributes:
        mode (Literal['disabled']):
    """

    mode: Literal["disabled"]

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
        mode = cast(Literal["disabled"], d.pop("mode"))
        if mode != "disabled":
            raise ValueError(f"mode must match const 'disabled', got '{mode}'")

        disabled_sandbox = cls(
            mode=mode,
        )

        return disabled_sandbox
