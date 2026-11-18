from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CandidateFile")


@_attrs_define(repr=False)
class CandidateFile:
    """
    Attributes:
        baseline (None | str):
        candidate (None | str):
        candidate_seq (int):
        path (str):
    """

    baseline: str | None
    candidate: str | None
    candidate_seq: int
    path: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        baseline: str | None
        baseline = self.baseline

        candidate: str | None
        candidate = self.candidate

        candidate_seq = self.candidate_seq

        path = self.path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "baseline": baseline,
                "candidate": candidate,
                "candidate_seq": candidate_seq,
                "path": path,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_baseline(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        baseline = _parse_baseline(d.pop("baseline"))

        def _parse_candidate(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        candidate = _parse_candidate(d.pop("candidate"))

        candidate_seq = d.pop("candidate_seq")

        path = d.pop("path")

        candidate_file = cls(
            baseline=baseline,
            candidate=candidate,
            candidate_seq=candidate_seq,
            path=path,
        )

        candidate_file.additional_properties = d
        return candidate_file

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
