from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fragment_state_pending import FragmentStatePending


T = TypeVar("T", bound="FragmentState")


@_attrs_define(repr=False)
class FragmentState:
    """Incomplete custom payloads, not a journal of completed events.

    Attributes:
        gap (bool | Unset):
        max_bytes (int | Unset):
        max_pending (int | Unset):
        pending (FragmentStatePending | Unset):
    """

    gap: bool | Unset = UNSET
    max_bytes: int | Unset = UNSET
    max_pending: int | Unset = UNSET
    pending: FragmentStatePending | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        gap = self.gap

        max_bytes = self.max_bytes

        max_pending = self.max_pending

        pending: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pending, Unset):
            pending = self.pending.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if gap is not UNSET:
            field_dict["gap"] = gap
        if max_bytes is not UNSET:
            field_dict["max_bytes"] = max_bytes
        if max_pending is not UNSET:
            field_dict["max_pending"] = max_pending
        if pending is not UNSET:
            field_dict["pending"] = pending

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fragment_state_pending import FragmentStatePending

        d = dict(src_dict)
        gap = d.pop("gap", UNSET)

        max_bytes = d.pop("max_bytes", UNSET)

        max_pending = d.pop("max_pending", UNSET)

        _pending = d.pop("pending", UNSET)
        pending: FragmentStatePending | Unset
        if isinstance(_pending, Unset):
            pending = UNSET
        else:
            pending = FragmentStatePending.from_dict(_pending)

        fragment_state = cls(
            gap=gap,
            max_bytes=max_bytes,
            max_pending=max_pending,
            pending=pending,
        )

        return fragment_state
