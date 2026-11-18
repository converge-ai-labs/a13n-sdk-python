from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CandidateReplacement")


@_attrs_define(repr=False)
class CandidateReplacement:
    """
    Attributes:
        candidate_seq (int):
        deletions (list[str]):
        overwrites (list[str]):
        restorations (list[str]):
        target_seq (int):
    """

    candidate_seq: int
    deletions: list[str]
    overwrites: list[str]
    restorations: list[str]
    target_seq: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        candidate_seq = self.candidate_seq

        deletions = self.deletions

        overwrites = self.overwrites

        restorations = self.restorations

        target_seq = self.target_seq

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "candidate_seq": candidate_seq,
                "deletions": deletions,
                "overwrites": overwrites,
                "restorations": restorations,
                "target_seq": target_seq,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        candidate_seq = d.pop("candidate_seq")

        deletions = cast(list[str], d.pop("deletions"))

        overwrites = cast(list[str], d.pop("overwrites"))

        restorations = cast(list[str], d.pop("restorations"))

        target_seq = d.pop("target_seq")

        candidate_replacement = cls(
            candidate_seq=candidate_seq,
            deletions=deletions,
            overwrites=overwrites,
            restorations=restorations,
            target_seq=target_seq,
        )

        candidate_replacement.additional_properties = d
        return candidate_replacement

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
