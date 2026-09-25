from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MemoryRecordView")


@_attrs_define(repr=False)
class MemoryRecordView:
    """A record as the memory's provider returns it; `score` is its similarity to a search query.

    Attributes:
        id (str):
        text (str):
        score (float | None | Unset):
        updated_at (datetime.datetime | None | Unset):
    """

    id: str
    text: str
    score: float | Unset | None = UNSET
    updated_at: datetime.datetime | Unset | None = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        text = self.text

        score: float | Unset | None
        if isinstance(self.score, Unset):
            score = UNSET
        else:
            score = self.score

        updated_at: str | Unset | None
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "text": text,
            }
        )
        if score is not UNSET:
            field_dict["score"] = score
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        text = d.pop("text")

        def _parse_score(data: object) -> float | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | Unset | None, data)

        score = _parse_score(d.pop("score", UNSET))

        def _parse_updated_at(data: object) -> datetime.datetime | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | Unset | None, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        memory_record_view = cls(
            id=id,
            text=text,
            score=score,
            updated_at=updated_at,
        )

        memory_record_view.additional_properties = d
        return memory_record_view

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
