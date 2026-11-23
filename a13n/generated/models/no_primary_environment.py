from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="NoPrimaryEnvironment")


@_attrs_define(repr=False)
class NoPrimaryEnvironment:
    """Skip the primary mount for this Run. Named mounts remain available.

    Attributes:
        mode (Literal['none']):
    """

    mode: Literal["none"]

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
        mode = cast(Literal["none"], d.pop("mode"))
        if mode != "none":
            raise ValueError(f"mode must match const 'none', got '{mode}'")

        no_primary_environment = cls(
            mode=mode,
        )

        return no_primary_environment
