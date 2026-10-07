from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.pending_answers_status import PendingAnswersStatus

if TYPE_CHECKING:
    from ..models.run_view import RunView
    from ..models.saved_answer import SavedAnswer


T = TypeVar("T", bound="PendingAnswers")


@_attrs_define(repr=False)
class PendingAnswers:
    """
    Attributes:
        answers (list[SavedAnswer]):
        run_id (str):
        status (PendingAnswersStatus):
        successor (None | RunView):
    """

    answers: list[SavedAnswer]
    run_id: str
    status: PendingAnswersStatus
    successor: RunView | None

    def to_dict(self) -> dict[str, Any]:
        from ..models.run_view import RunView

        answers = []
        for answers_item_data in self.answers:
            answers_item = answers_item_data.to_dict()
            answers.append(answers_item)

        run_id = self.run_id

        status = self.status.value

        successor: dict[str, Any] | None
        if isinstance(self.successor, RunView):
            successor = self.successor.to_dict()
        else:
            successor = self.successor

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "answers": answers,
                "run_id": run_id,
                "status": status,
                "successor": successor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_view import RunView
        from ..models.saved_answer import SavedAnswer

        d = dict(src_dict)
        answers = []
        _answers = d.pop("answers")
        for answers_item_data in _answers:
            answers_item = SavedAnswer.from_dict(answers_item_data)

            answers.append(answers_item)

        run_id = d.pop("run_id")

        status = PendingAnswersStatus(d.pop("status"))

        def _parse_successor(data: object) -> RunView | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                successor_type_0 = RunView.from_dict(data)

                return successor_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(RunView | None, data)

        successor = _parse_successor(d.pop("successor"))

        pending_answers = cls(
            answers=answers,
            run_id=run_id,
            status=status,
            successor=successor,
        )

        return pending_answers
