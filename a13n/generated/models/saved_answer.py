from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.pending_answer import PendingAnswer


T = TypeVar("T", bound="SavedAnswer")


@_attrs_define(repr=False)
class SavedAnswer:
    """
    Attributes:
        answer (PendingAnswer): One immutable answer to an exact waiting run; no accompanying input.
        answered_by_id (str):
        created_at (datetime.datetime):
    """

    answer: PendingAnswer
    answered_by_id: str
    created_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        answer = self.answer.to_dict()

        answered_by_id = self.answered_by_id

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "answer": answer,
                "answered_by_id": answered_by_id,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pending_answer import PendingAnswer

        d = dict(src_dict)
        answer = PendingAnswer.from_dict(d.pop("answer"))

        answered_by_id = d.pop("answered_by_id")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        saved_answer = cls(
            answer=answer,
            answered_by_id=answered_by_id,
            created_at=created_at,
        )

        return saved_answer
