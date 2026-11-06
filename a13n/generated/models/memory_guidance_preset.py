from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.system_preset import SystemPreset

T = TypeVar("T", bound="MemoryGuidancePreset")


@_attrs_define(repr=False)
class MemoryGuidancePreset:
    """
    Attributes:
        description (str):
        id (SystemPreset):
        name (str):
        system_guide (str):
    """

    description: str
    id: SystemPreset
    name: str
    system_guide: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        id = self.id.value

        name = self.name

        system_guide = self.system_guide

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "id": id,
                "name": name,
                "system_guide": system_guide,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description")

        id = SystemPreset(d.pop("id"))

        name = d.pop("name")

        system_guide = d.pop("system_guide")

        memory_guidance_preset = cls(
            description=description,
            id=id,
            name=name,
            system_guide=system_guide,
        )

        memory_guidance_preset.additional_properties = d
        return memory_guidance_preset

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
