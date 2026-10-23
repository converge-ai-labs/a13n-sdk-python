from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MemoryEvents")


@_attrs_define(repr=False)
class MemoryEvents:
    """
    Attributes:
        high (int | None | Unset):
        low (int | None | Unset):
        max_ (int | None | Unset):
        oom (int | None | Unset):
        oom_group_kill (int | None | Unset):
        oom_kill (int | None | Unset):
    """

    high: int | Unset | None = UNSET
    low: int | Unset | None = UNSET
    max_: int | Unset | None = UNSET
    oom: int | Unset | None = UNSET
    oom_group_kill: int | Unset | None = UNSET
    oom_kill: int | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        high: int | Unset | None
        if isinstance(self.high, Unset):
            high = UNSET
        else:
            high = self.high

        low: int | Unset | None
        if isinstance(self.low, Unset):
            low = UNSET
        else:
            low = self.low

        max_: int | Unset | None
        if isinstance(self.max_, Unset):
            max_ = UNSET
        else:
            max_ = self.max_

        oom: int | Unset | None
        if isinstance(self.oom, Unset):
            oom = UNSET
        else:
            oom = self.oom

        oom_group_kill: int | Unset | None
        if isinstance(self.oom_group_kill, Unset):
            oom_group_kill = UNSET
        else:
            oom_group_kill = self.oom_group_kill

        oom_kill: int | Unset | None
        if isinstance(self.oom_kill, Unset):
            oom_kill = UNSET
        else:
            oom_kill = self.oom_kill

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if high is not UNSET:
            field_dict["high"] = high
        if low is not UNSET:
            field_dict["low"] = low
        if max_ is not UNSET:
            field_dict["max"] = max_
        if oom is not UNSET:
            field_dict["oom"] = oom
        if oom_group_kill is not UNSET:
            field_dict["oom_group_kill"] = oom_group_kill
        if oom_kill is not UNSET:
            field_dict["oom_kill"] = oom_kill

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_high(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        high = _parse_high(d.pop("high", UNSET))

        def _parse_low(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        low = _parse_low(d.pop("low", UNSET))

        def _parse_max_(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        max_ = _parse_max_(d.pop("max", UNSET))

        def _parse_oom(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        oom = _parse_oom(d.pop("oom", UNSET))

        def _parse_oom_group_kill(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        oom_group_kill = _parse_oom_group_kill(d.pop("oom_group_kill", UNSET))

        def _parse_oom_kill(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        oom_kill = _parse_oom_kill(d.pop("oom_kill", UNSET))

        memory_events = cls(
            high=high,
            low=low,
            max_=max_,
            oom=oom,
            oom_group_kill=oom_group_kill,
            oom_kill=oom_kill,
        )

        return memory_events
