from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.template_config import TemplateConfig
    from ..models.template_labels import TemplateLabels


T = TypeVar("T", bound="Template")


@_attrs_define(repr=False)
class Template:
    """
    Attributes:
        config (TemplateConfig):
        created_at (datetime.datetime):
        created_by_id (None | str):
        description (None | str):
        enabled (bool):
        id (str):
        labels (TemplateLabels):
        name (str):
        organization_id (str):
        provider_id (str):
        updated_at (datetime.datetime):
        updated_by_id (None | str):
        version (int):
        workspace_id (str):
    """

    config: TemplateConfig
    created_at: datetime.datetime
    created_by_id: str | None
    description: str | None
    enabled: bool
    id: str
    labels: TemplateLabels
    name: str
    organization_id: str
    provider_id: str
    updated_at: datetime.datetime
    updated_by_id: str | None
    version: int
    workspace_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config = self.config.to_dict()

        created_at = self.created_at.isoformat()

        created_by_id: str | None
        created_by_id = self.created_by_id

        description: str | None
        description = self.description

        enabled = self.enabled

        id = self.id

        labels = self.labels.to_dict()

        name = self.name

        organization_id = self.organization_id

        provider_id = self.provider_id

        updated_at = self.updated_at.isoformat()

        updated_by_id: str | None
        updated_by_id = self.updated_by_id

        version = self.version

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config": config,
                "created_at": created_at,
                "created_by_id": created_by_id,
                "description": description,
                "enabled": enabled,
                "id": id,
                "labels": labels,
                "name": name,
                "organization_id": organization_id,
                "provider_id": provider_id,
                "updated_at": updated_at,
                "updated_by_id": updated_by_id,
                "version": version,
                "workspace_id": workspace_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template_config import TemplateConfig
        from ..models.template_labels import TemplateLabels

        d = dict(src_dict)
        config = TemplateConfig.from_dict(d.pop("config"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_created_by_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        created_by_id = _parse_created_by_id(d.pop("created_by_id"))

        def _parse_description(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        description = _parse_description(d.pop("description"))

        enabled = d.pop("enabled")

        id = d.pop("id")

        labels = TemplateLabels.from_dict(d.pop("labels"))

        name = d.pop("name")

        organization_id = d.pop("organization_id")

        provider_id = d.pop("provider_id")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_updated_by_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        updated_by_id = _parse_updated_by_id(d.pop("updated_by_id"))

        version = d.pop("version")

        workspace_id = d.pop("workspace_id")

        template = cls(
            config=config,
            created_at=created_at,
            created_by_id=created_by_id,
            description=description,
            enabled=enabled,
            id=id,
            labels=labels,
            name=name,
            organization_id=organization_id,
            provider_id=provider_id,
            updated_at=updated_at,
            updated_by_id=updated_by_id,
            version=version,
            workspace_id=workspace_id,
        )

        template.additional_properties = d
        return template

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
