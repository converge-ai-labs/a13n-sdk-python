from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SessionLifecyclePolicy")


@_attrs_define(repr=False)
class SessionLifecyclePolicy:
    """
    Attributes:
        idle_timeout_ms (int):
        max_lifetime_ms (int | None | Unset):
    """

    idle_timeout_ms: int
    max_lifetime_ms: int | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        idle_timeout_ms = self.idle_timeout_ms

        max_lifetime_ms: int | Unset | None
        if isinstance(self.max_lifetime_ms, Unset):
            max_lifetime_ms = UNSET
        else:
            max_lifetime_ms = self.max_lifetime_ms

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "idle_timeout_ms": idle_timeout_ms,
            }
        )
        if max_lifetime_ms is not UNSET:
            field_dict["max_lifetime_ms"] = max_lifetime_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        idle_timeout_ms = d.pop("idle_timeout_ms")

        def _parse_max_lifetime_ms(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        max_lifetime_ms = _parse_max_lifetime_ms(d.pop("max_lifetime_ms", UNSET))

        session_lifecycle_policy = cls(
            idle_timeout_ms=idle_timeout_ms,
            max_lifetime_ms=max_lifetime_ms,
        )

        return session_lifecycle_policy
