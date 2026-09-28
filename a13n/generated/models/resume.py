from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.resume_approvals import ResumeApprovals
    from ..models.resume_calls import ResumeCalls


T = TypeVar("T", bound="Resume")


@_attrs_define(repr=False)
class Resume:
    """The complete result batch, submitted and stored on the successor without omission defaults.

    Attributes:
        approvals (ResumeApprovals):
        calls (ResumeCalls):
    """

    approvals: ResumeApprovals
    calls: ResumeCalls

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
        from ..models.resume_approvals import ResumeApprovals
        from ..models.resume_calls import ResumeCalls

        d = dict(src_dict)
        approvals = ResumeApprovals.from_dict(d.pop("approvals"))

        calls = ResumeCalls.from_dict(d.pop("calls"))

        resume = cls(
            approvals=approvals,
            calls=calls,
        )

        return resume
