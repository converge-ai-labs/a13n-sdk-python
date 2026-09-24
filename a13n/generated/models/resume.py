from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.approve import Approve
    from ..models.complete import Complete
    from ..models.no_response import NoResponse
    from ..models.reject import Reject


T = TypeVar("T", bound="Resume")


@_attrs_define(repr=False)
class Resume:
    """The normalized batch stored on the successor: one answer per pending call of the exact wait.

    Attributes:
        answers (list[Approve | Complete | NoResponse | Reject]):
    """

    answers: list[Approve | Complete | NoResponse | Reject]

    def to_dict(self) -> dict[str, Any]:
        from ..models.approve import Approve
        from ..models.complete import Complete
        from ..models.reject import Reject

        answers = []
        for answers_item_data in self.answers:
            answers_item: dict[str, Any]
            if isinstance(answers_item_data, Approve):
                answers_item = answers_item_data.to_dict()
            elif isinstance(answers_item_data, Reject):
                answers_item = answers_item_data.to_dict()
            elif isinstance(answers_item_data, Complete):
                answers_item = answers_item_data.to_dict()
            else:
                answers_item = answers_item_data.to_dict()

            answers.append(answers_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "answers": answers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.approve import Approve
        from ..models.complete import Complete
        from ..models.no_response import NoResponse
        from ..models.reject import Reject

        d = dict(src_dict)
        answers = []
        _answers = d.pop("answers")
        for answers_item_data in _answers:

            def _parse_answers_item(data: object) -> Approve | Complete | NoResponse | Reject:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_normalized_answer_type_0 = Approve.from_dict(data)

                    return componentsschemas_normalized_answer_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_normalized_answer_type_1 = Reject.from_dict(data)

                    return componentsschemas_normalized_answer_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_normalized_answer_type_2 = Complete.from_dict(data)

                    return componentsschemas_normalized_answer_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_normalized_answer_type_3 = NoResponse.from_dict(data)

                return componentsschemas_normalized_answer_type_3

            answers_item = _parse_answers_item(answers_item_data)

            answers.append(answers_item)

        resume = cls(
            answers=answers,
        )

        return resume
