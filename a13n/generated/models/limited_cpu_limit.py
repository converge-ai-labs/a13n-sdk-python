from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="LimitedCpuLimit")


@_attrs_define(repr=False)
class LimitedCpuLimit:
    """
    Attributes:
        kind (Literal['limited']):
        period_usec (int):
        quota_usec (int):
    """

    kind: Literal["limited"]
    period_usec: int
    quota_usec: int

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        period_usec = self.period_usec

        quota_usec = self.quota_usec

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
                "period_usec": period_usec,
                "quota_usec": quota_usec,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = cast(Literal["limited"], d.pop("kind"))
        if kind != "limited":
            raise ValueError(f"kind must match const 'limited', got '{kind}'")

        period_usec = d.pop("period_usec")

        quota_usec = d.pop("quota_usec")

        limited_cpu_limit = cls(
            kind=kind,
            period_usec=period_usec,
            quota_usec=quota_usec,
        )

        return limited_cpu_limit
