from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="IsolatedSkillSync")


@_attrs_define(repr=False)
class IsolatedSkillSync:
    """Reuse immutable package directories, with a soft count budget.

    Attributes:
        cache_count (int | Unset):
        mode (Literal['isolated'] | Unset):
    """

    cache_count: int | Unset = UNSET
    mode: Literal["isolated"] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        cache_count = self.cache_count

        mode = self.mode

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if cache_count is not UNSET:
            field_dict["cache_count"] = cache_count
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cache_count = d.pop("cache_count", UNSET)

        mode = cast(Literal["isolated"] | Unset, d.pop("mode", UNSET))
        if mode != "isolated" and not isinstance(mode, Unset):
            raise ValueError(f"mode must match const 'isolated', got '{mode}'")

        isolated_skill_sync = cls(
            cache_count=cache_count,
            mode=mode,
        )

        return isolated_skill_sync
