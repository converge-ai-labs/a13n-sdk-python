from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.provider_reference import ProviderReference


T = TypeVar("T", bound="EnvironmentProviderReferences")


@_attrs_define(repr=False)
class EnvironmentProviderReferences:
    """
    Attributes:
        environment_count (int):
        environments (list[ProviderReference]):
        template_count (int):
        templates (list[ProviderReference]):
    """

    environment_count: int
    environments: list[ProviderReference]
    template_count: int
    templates: list[ProviderReference]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        environment_count = self.environment_count

        environments = []
        for environments_item_data in self.environments:
            environments_item = environments_item_data.to_dict()
            environments.append(environments_item)

        template_count = self.template_count

        templates = []
        for templates_item_data in self.templates:
            templates_item = templates_item_data.to_dict()
            templates.append(templates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "environment_count": environment_count,
                "environments": environments,
                "template_count": template_count,
                "templates": templates,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.provider_reference import ProviderReference

        d = dict(src_dict)
        environment_count = d.pop("environment_count")

        environments = []
        _environments = d.pop("environments")
        for environments_item_data in _environments:
            environments_item = ProviderReference.from_dict(environments_item_data)

            environments.append(environments_item)

        template_count = d.pop("template_count")

        templates = []
        _templates = d.pop("templates")
        for templates_item_data in _templates:
            templates_item = ProviderReference.from_dict(templates_item_data)

            templates.append(templates_item)

        environment_provider_references = cls(
            environment_count=environment_count,
            environments=environments,
            template_count=template_count,
            templates=templates,
        )

        environment_provider_references.additional_properties = d
        return environment_provider_references

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
