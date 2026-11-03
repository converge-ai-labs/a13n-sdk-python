from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..._validation import validate_model

if TYPE_CHECKING:
    from ..models.pending_call import PendingCall


T = TypeVar("T", bound="HistoricalDesktopPending")


@_attrs_define(repr=False)
class HistoricalDesktopPending:
    """Read-only projection of sealed desktop suspensions predating Computer-scoped control.

    Attributes:
        approvals (list[PendingCall]):
        calls (list[PendingCall]):
        desktop_control_id (str):
    """

    approvals: list[PendingCall]
    calls: list[PendingCall]
    desktop_control_id: str

    def to_dict(self) -> dict[str, Any]:
        approvals = []
        for approvals_item_data in self.approvals:
            approvals_item = approvals_item_data.to_dict()
            approvals.append(approvals_item)

        calls = []
        for calls_item_data in self.calls:
            calls_item = calls_item_data.to_dict()
            calls.append(calls_item)

        desktop_control_id = self.desktop_control_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "approvals": approvals,
                "calls": calls,
                "desktop_control_id": desktop_control_id,
            }
        )

        validate_model("HistoricalDesktopPending", field_dict)
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        validate_model("HistoricalDesktopPending", src_dict)
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

        desktop_control_id = d.pop("desktop_control_id")

        historical_desktop_pending = cls(
            approvals=approvals,
            calls=calls,
            desktop_control_id=desktop_control_id,
        )

        return historical_desktop_pending
