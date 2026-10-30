from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Takeover")


@_attrs_define(repr=False)
class Takeover:
    """
    Attributes:
        thread_id (str):
        lease_seconds (int | None | Unset):
    """

    thread_id: str
    lease_seconds: int | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        thread_id = self.thread_id

        lease_seconds: int | Unset | None
        if isinstance(self.lease_seconds, Unset):
            lease_seconds = UNSET
        else:
            lease_seconds = self.lease_seconds

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "thread_id": thread_id,
            }
        )
        if lease_seconds is not UNSET:
            field_dict["lease_seconds"] = lease_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        thread_id = d.pop("thread_id")

        def _parse_lease_seconds(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        lease_seconds = _parse_lease_seconds(d.pop("lease_seconds", UNSET))

        takeover = cls(
            thread_id=thread_id,
            lease_seconds=lease_seconds,
        )

        return takeover
