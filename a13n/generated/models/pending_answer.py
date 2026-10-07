from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.pending_answer_approvals import PendingAnswerApprovals
    from ..models.pending_answer_calls import PendingAnswerCalls


T = TypeVar("T", bound="PendingAnswer")


@_attrs_define(repr=False)
class PendingAnswer:
    """One immutable answer to an exact waiting run; no accompanying input.

    Attributes:
        approvals (PendingAnswerApprovals):
        calls (PendingAnswerCalls):
    """

    approvals: PendingAnswerApprovals
    calls: PendingAnswerCalls

    def to_dict(self) -> dict[str, Any]:
        approvals = self.approvals.to_dict()

        calls = self.calls.to_dict()

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
        from ..models.pending_answer_approvals import PendingAnswerApprovals
        from ..models.pending_answer_calls import PendingAnswerCalls

        d = dict(src_dict)
        approvals = PendingAnswerApprovals.from_dict(d.pop("approvals"))

        calls = PendingAnswerCalls.from_dict(d.pop("calls"))

        pending_answer = cls(
            approvals=approvals,
            calls=calls,
        )

        return pending_answer
