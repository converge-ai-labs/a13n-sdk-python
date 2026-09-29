from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message_payload import MessagePayload
    from ..models.resume_approvals import ResumeApprovals
    from ..models.resume_calls import ResumeCalls


T = TypeVar("T", bound="Resume")


@_attrs_define(repr=False)
class Resume:
    """The complete result batch, submitted and stored on the successor without omission defaults.

    Attributes:
        approvals (ResumeApprovals):
        calls (ResumeCalls):
        input_ (MessagePayload | None | Unset):
    """

    approvals: ResumeApprovals
    calls: ResumeCalls
    input_: MessagePayload | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.message_payload import MessagePayload

        approvals = self.approvals.to_dict()

        calls = self.calls.to_dict()

        input_: dict[str, Any] | Unset | None
        if isinstance(self.input_, Unset):
            input_ = UNSET
        elif isinstance(self.input_, MessagePayload):
            input_ = self.input_.to_dict()
        else:
            input_ = self.input_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "approvals": approvals,
                "calls": calls,
            }
        )
        if input_ is not UNSET:
            field_dict["input"] = input_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_payload import MessagePayload
        from ..models.resume_approvals import ResumeApprovals
        from ..models.resume_calls import ResumeCalls

        d = dict(src_dict)
        approvals = ResumeApprovals.from_dict(d.pop("approvals"))

        calls = ResumeCalls.from_dict(d.pop("calls"))

        def _parse_input_(data: object) -> MessagePayload | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                input_type_0 = MessagePayload.from_dict(data)

                return input_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MessagePayload | Unset | None, data)

        input_ = _parse_input_(d.pop("input", UNSET))

        resume = cls(
            approvals=approvals,
            calls=calls,
            input_=input_,
        )

        return resume
