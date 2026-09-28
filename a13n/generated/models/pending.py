from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.pending_call import PendingCall


T = TypeVar("T", bound="Pending")


@_attrs_define(repr=False)
class Pending:
    """Public projection; complete native requests and private metadata stay in the checkpoint.

    Attributes:
        approvals (list[PendingCall]):
        calls (list[PendingCall]):
    """

    approvals: list[PendingCall]
    calls: list[PendingCall]

    def to_dict(self) -> dict[str, Any]:
        approvals = []
        for approvals_item_data in self.approvals:
            approvals_item = approvals_item_data.to_dict()
            approvals.append(approvals_item)

        calls = []
        for calls_item_data in self.calls:
            calls_item = calls_item_data.to_dict()
            calls.append(calls_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "approvals": approvals,
                "calls": calls,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pending_call import PendingCall

        d = dict(src_dict)
        approvals = []
        _approvals = d.pop("approvals")
        for approvals_item_data in _approvals:
            approvals_item = PendingCall.from_dict(approvals_item_data)

            approvals.append(approvals_item)

        calls = []
        _calls = d.pop("calls")
        for calls_item_data in _calls:
            calls_item = PendingCall.from_dict(calls_item_data)

            calls.append(calls_item)

        pending = cls(
            approvals=approvals,
            calls=calls,
        )

        return pending
