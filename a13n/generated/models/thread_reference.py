from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.thread_reference_origin import ThreadReferenceOrigin

T = TypeVar("T", bound="ThreadReference")


@_attrs_define(repr=False)
class ThreadReference:
    """
    Attributes:
        id (str):
        origin (ThreadReferenceOrigin):
        origin_count (int):
        origin_number (int):
        subagent (None | str):
    """

    id: str
    origin: ThreadReferenceOrigin
    origin_count: int
    origin_number: int
    subagent: str | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        origin = self.origin.value

        origin_count = self.origin_count

        origin_number = self.origin_number

        subagent: str | None
        subagent = self.subagent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "origin": origin,
                "origin_count": origin_count,
                "origin_number": origin_number,
                "subagent": subagent,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        origin = ThreadReferenceOrigin(d.pop("origin"))

        origin_count = d.pop("origin_count")

        origin_number = d.pop("origin_number")

        def _parse_subagent(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        subagent = _parse_subagent(d.pop("subagent"))

        thread_reference = cls(
            id=id,
            origin=origin,
            origin_count=origin_count,
            origin_number=origin_number,
            subagent=subagent,
        )

        thread_reference.additional_properties = d
        return thread_reference

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
