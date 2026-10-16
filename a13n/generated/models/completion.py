from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.completion_outcome import CompletionOutcome
from ..types import UNSET, Unset

T = TypeVar("T", bound="Completion")


@_attrs_define(repr=False)
class Completion:
    """
    Attributes:
        epoch (int):
        session_id (str):
        note (str | Unset):
        outcome (CompletionOutcome | Unset):
    """

    epoch: int
    session_id: str
    note: str | Unset = UNSET
    outcome: CompletionOutcome | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        epoch = self.epoch

        session_id = self.session_id

        note = self.note

        outcome: str | Unset = UNSET
        if not isinstance(self.outcome, Unset):
            outcome = self.outcome.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "epoch": epoch,
                "session_id": session_id,
            }
        )
        if note is not UNSET:
            field_dict["note"] = note
        if outcome is not UNSET:
            field_dict["outcome"] = outcome

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        epoch = d.pop("epoch")

        session_id = d.pop("session_id")

        note = d.pop("note", UNSET)

        _outcome = d.pop("outcome", UNSET)
        outcome: CompletionOutcome | Unset
        if isinstance(_outcome, Unset):
            outcome = UNSET
        else:
            outcome = CompletionOutcome(_outcome)

        completion = cls(
            epoch=epoch,
            session_id=session_id,
            note=note,
            outcome=outcome,
        )

        return completion
