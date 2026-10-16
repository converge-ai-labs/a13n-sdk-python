from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pending_call import PendingCall


T = TypeVar("T", bound="Pending")


@_attrs_define(repr=False)
class Pending:
    """Public projection; complete native requests and private metadata stay in the checkpoint.

    Attributes:
        approvals (list[PendingCall]):
        calls (list[PendingCall]):
        desktop_control_id (None | str | Unset):
    """

    approvals: list[PendingCall]
    calls: list[PendingCall]
    desktop_control_id: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        approvals = []
        for approvals_item_data in self.approvals:
            approvals_item = approvals_item_data.to_dict()
            approvals.append(approvals_item)

        calls = []
        for calls_item_data in self.calls:
            calls_item = calls_item_data.to_dict()
            calls.append(calls_item)

        desktop_control_id: str | Unset | None
        if isinstance(self.desktop_control_id, Unset):
            desktop_control_id = UNSET
        else:
            desktop_control_id = self.desktop_control_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "approvals": approvals,
                "calls": calls,
            }
        )
        if desktop_control_id is not UNSET:
            field_dict["desktop_control_id"] = desktop_control_id

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

        def _parse_desktop_control_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        desktop_control_id = _parse_desktop_control_id(d.pop("desktop_control_id", UNSET))

        pending = cls(
            approvals=approvals,
            calls=calls,
            desktop_control_id=desktop_control_id,
        )

        return pending
