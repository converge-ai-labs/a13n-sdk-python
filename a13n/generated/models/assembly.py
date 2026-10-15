from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Assembly")


@_attrs_define(repr=False)
class Assembly:
    """
    Attributes:
        count (int):
        parts (list[str] | Unset):
        size (int | Unset):
    """

    count: int
    parts: list[str] | Unset = UNSET
    size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        parts: list[str] | Unset = UNSET
        if not isinstance(self.parts, Unset):
            parts = self.parts

        size = self.size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
            }
        )
        if parts is not UNSET:
            field_dict["parts"] = parts
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count")

        parts = cast(list[str], d.pop("parts", UNSET))

        size = d.pop("size", UNSET)

        assembly = cls(
            count=count,
            parts=parts,
            size=size,
        )

        assembly.additional_properties = d
        return assembly

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
