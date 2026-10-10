from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.assessment import Assessment
from ..types import UNSET, Unset

T = TypeVar("T", bound="FindingUpdate")


@_attrs_define(repr=False)
class FindingUpdate:
    """
    Attributes:
        assessment (Assessment | None | Unset):
        assessment_note (None | str | Unset):
        closed (bool | None | Unset):
    """

    assessment: Assessment | Unset | None = UNSET
    assessment_note: str | Unset | None = UNSET
    closed: bool | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        assessment: str | Unset | None
        if isinstance(self.assessment, Unset):
            assessment = UNSET
        elif isinstance(self.assessment, Assessment):
            assessment = self.assessment.value
        else:
            assessment = self.assessment

        assessment_note: str | Unset | None
        if isinstance(self.assessment_note, Unset):
            assessment_note = UNSET
        else:
            assessment_note = self.assessment_note

        closed: bool | Unset | None
        if isinstance(self.closed, Unset):
            closed = UNSET
        else:
            closed = self.closed

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if assessment is not UNSET:
            field_dict["assessment"] = assessment
        if assessment_note is not UNSET:
            field_dict["assessment_note"] = assessment_note
        if closed is not UNSET:
            field_dict["closed"] = closed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_assessment(data: object) -> Assessment | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                assessment_type_0 = Assessment(data)

                return assessment_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Assessment | Unset | None, data)

        assessment = _parse_assessment(d.pop("assessment", UNSET))

        def _parse_assessment_note(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        assessment_note = _parse_assessment_note(d.pop("assessment_note", UNSET))

        def _parse_closed(data: object) -> bool | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | Unset | None, data)

        closed = _parse_closed(d.pop("closed", UNSET))

        finding_update = cls(
            assessment=assessment,
            assessment_note=assessment_note,
            closed=closed,
        )

        return finding_update
