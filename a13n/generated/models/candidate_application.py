from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.candidate_apply import CandidateApply


T = TypeVar("T", bound="CandidateApplication")


@_attrs_define(repr=False)
class CandidateApplication:
    """
    Attributes:
        applied_at (datetime.datetime):
        applied_by_id (str):
        request (CandidateApply):
        result_seq (int):
    """

    applied_at: datetime.datetime
    applied_by_id: str
    request: CandidateApply
    result_seq: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        applied_at = self.applied_at.isoformat()

        applied_by_id = self.applied_by_id

        request = self.request.to_dict()

        result_seq = self.result_seq

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "applied_at": applied_at,
                "applied_by_id": applied_by_id,
                "request": request,
                "result_seq": result_seq,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.candidate_apply import CandidateApply

        d = dict(src_dict)
        applied_at = datetime.datetime.fromisoformat(d.pop("applied_at"))

        applied_by_id = d.pop("applied_by_id")

        request = CandidateApply.from_dict(d.pop("request"))

        result_seq = d.pop("result_seq")

        candidate_application = cls(
            applied_at=applied_at,
            applied_by_id=applied_by_id,
            request=request,
            result_seq=result_seq,
        )

        candidate_application.additional_properties = d
        return candidate_application

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
