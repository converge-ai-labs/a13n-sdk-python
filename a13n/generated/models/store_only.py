from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="StoreOnly")


@_attrs_define(repr=False)
class StoreOnly:
    """
    Attributes:
        mode (Literal['store_only'] | Unset):
    """

    mode: Literal["store_only"] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mode = cast(Literal["store_only"] | Unset, d.pop("mode", UNSET))
        if mode != "store_only" and not isinstance(mode, Unset):
            raise ValueError(f"mode must match const 'store_only', got '{mode}'")

        store_only = cls(
            mode=mode,
        )

        return store_only
