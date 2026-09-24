from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.approve import Approve
    from ..models.complete import Complete
    from ..models.reject import Reject


T = TypeVar("T", bound="ResumeRequest")


@_attrs_define(repr=False)
class ResumeRequest:
    """
    Attributes:
        answers (list[Approve | Complete | Reject] | Unset):
    """

    answers: list[Approve | Complete | Reject] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.approve import Approve
        from ..models.reject import Reject

        answers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.answers, Unset):
            answers = []
            for answers_item_data in self.answers:
                answers_item: dict[str, Any]
                if isinstance(answers_item_data, Approve):
                    answers_item = answers_item_data.to_dict()
                elif isinstance(answers_item_data, Reject):
                    answers_item = answers_item_data.to_dict()
                else:
                    answers_item = answers_item_data.to_dict()

                answers.append(answers_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if answers is not UNSET:
            field_dict["answers"] = answers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.approve import Approve
        from ..models.complete import Complete
        from ..models.reject import Reject

        d = dict(src_dict)
        _answers = d.pop("answers", UNSET)
        answers: list[Approve | Complete | Reject] | Unset = UNSET
        if _answers is not UNSET:
            answers = []
            for answers_item_data in _answers:

                def _parse_answers_item(data: object) -> Approve | Complete | Reject:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_answer_type_0 = Approve.from_dict(data)

                        return componentsschemas_answer_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_answer_type_1 = Reject.from_dict(data)

                        return componentsschemas_answer_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_answer_type_2 = Complete.from_dict(data)

                    return componentsschemas_answer_type_2

                answers_item = _parse_answers_item(answers_item_data)

                answers.append(answers_item)

        resume_request = cls(
            answers=answers,
        )

        return resume_request
