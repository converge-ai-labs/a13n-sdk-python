from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.candidate_apply_mode import CandidateApplyMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="CandidateApply")


@_attrs_define(repr=False)
class CandidateApply:
    """
    Attributes:
        candidate_seq (int):
        target_seq (int):
        mode (CandidateApplyMode | Unset):
    """

    candidate_seq: int
    target_seq: int
    mode: CandidateApplyMode | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        candidate_seq = self.candidate_seq

        target_seq = self.target_seq

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "candidate_seq": candidate_seq,
                "target_seq": target_seq,
            }
        )
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        candidate_seq = d.pop("candidate_seq")

        target_seq = d.pop("target_seq")

        _mode = d.pop("mode", UNSET)
        mode: CandidateApplyMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = CandidateApplyMode(_mode)

        candidate_apply = cls(
            candidate_seq=candidate_seq,
            target_seq=target_seq,
            mode=mode,
        )

        return candidate_apply
