from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigSummary")


@_attrs_define(repr=False)
class ConfigSummary:
    """
    Attributes:
        connection_count (int):
        model (str):
        skill_count (int):
        subagent_count (int):
        toolsets (list[str]):
        omitted_sections (list[str] | Unset):
    """

    connection_count: int
    model: str
    skill_count: int
    subagent_count: int
    toolsets: list[str]
    omitted_sections: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connection_count = self.connection_count

        model = self.model

        skill_count = self.skill_count

        subagent_count = self.subagent_count

        toolsets = self.toolsets

        omitted_sections: list[str] | Unset = UNSET
        if not isinstance(self.omitted_sections, Unset):
            omitted_sections = self.omitted_sections

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connection_count": connection_count,
                "model": model,
                "skill_count": skill_count,
                "subagent_count": subagent_count,
                "toolsets": toolsets,
            }
        )
        if omitted_sections is not UNSET:
            field_dict["omitted_sections"] = omitted_sections

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connection_count = d.pop("connection_count")

        model = d.pop("model")

        skill_count = d.pop("skill_count")

        subagent_count = d.pop("subagent_count")

        toolsets = cast(list[str], d.pop("toolsets"))

        omitted_sections = cast(list[str], d.pop("omitted_sections", UNSET))

        config_summary = cls(
            connection_count=connection_count,
            model=model,
            skill_count=skill_count,
            subagent_count=subagent_count,
            toolsets=toolsets,
            omitted_sections=omitted_sections,
        )

        config_summary.additional_properties = d
        return config_summary

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
