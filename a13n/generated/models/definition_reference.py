from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DefinitionReference")


@_attrs_define(repr=False)
class DefinitionReference:
    """
    Attributes:
        name (str):
        size_chars (int):
        version (str):
        instruction (str | Unset):
    """

    name: str
    size_chars: int
    version: str
    instruction: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        size_chars = self.size_chars

        version = self.version

        instruction = self.instruction

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "size_chars": size_chars,
                "version": version,
            }
        )
        if instruction is not UNSET:
            field_dict["instruction"] = instruction

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        size_chars = d.pop("size_chars")

        version = d.pop("version")

        instruction = d.pop("instruction", UNSET)

        definition_reference = cls(
            name=name,
            size_chars=size_chars,
            version=version,
            instruction=instruction,
        )

        definition_reference.additional_properties = d
        return definition_reference

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
