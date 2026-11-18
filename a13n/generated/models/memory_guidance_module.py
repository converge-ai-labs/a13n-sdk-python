from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.guide_module import GuideModule

T = TypeVar("T", bound="MemoryGuidanceModule")


@_attrs_define(repr=False)
class MemoryGuidanceModule:
    """
    Attributes:
        description (str):
        guide (str):
        id (GuideModule):
        name (str):
    """

    description: str
    guide: str
    id: GuideModule
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        guide = self.guide

        id = self.id.value

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "guide": guide,
                "id": id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description")

        guide = d.pop("guide")

        id = GuideModule(d.pop("id"))

        name = d.pop("name")

        memory_guidance_module = cls(
            description=description,
            guide=guide,
            id=id,
            name=name,
        )

        memory_guidance_module.additional_properties = d
        return memory_guidance_module

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
