from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.configuration import Configuration


T = TypeVar("T", bound="DataSource")


@_attrs_define(repr=False)
class DataSource:
    """
    Attributes:
        builtin (bool):
        config (Configuration):
        created_at (datetime.datetime):
        created_by_id (str):
        enabled (bool):
        has_export_credentials (bool):
        has_query_credentials (bool):
        id (str):
        name (str):
        organization_id (str):
        updated_at (datetime.datetime):
        updated_by_id (str):
        version (int):
        workspace_id (str):
    """

    builtin: bool
    config: Configuration
    created_at: datetime.datetime
    created_by_id: str
    enabled: bool
    has_export_credentials: bool
    has_query_credentials: bool
    id: str
    name: str
    organization_id: str
    updated_at: datetime.datetime
    updated_by_id: str
    version: int
    workspace_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        builtin = self.builtin

        config = self.config.to_dict()

        created_at = self.created_at.isoformat()

        created_by_id = self.created_by_id

        enabled = self.enabled

        has_export_credentials = self.has_export_credentials

        has_query_credentials = self.has_query_credentials

        id = self.id

        name = self.name

        organization_id = self.organization_id

        updated_at = self.updated_at.isoformat()

        updated_by_id = self.updated_by_id

        version = self.version

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "builtin": builtin,
                "config": config,
                "created_at": created_at,
                "created_by_id": created_by_id,
                "enabled": enabled,
                "has_export_credentials": has_export_credentials,
                "has_query_credentials": has_query_credentials,
                "id": id,
                "name": name,
                "organization_id": organization_id,
                "updated_at": updated_at,
                "updated_by_id": updated_by_id,
                "version": version,
                "workspace_id": workspace_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.configuration import Configuration

        d = dict(src_dict)
        builtin = d.pop("builtin")

        config = Configuration.from_dict(d.pop("config"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        created_by_id = d.pop("created_by_id")

        enabled = d.pop("enabled")

        has_export_credentials = d.pop("has_export_credentials")

        has_query_credentials = d.pop("has_query_credentials")

        id = d.pop("id")

        name = d.pop("name")

        organization_id = d.pop("organization_id")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        updated_by_id = d.pop("updated_by_id")

        version = d.pop("version")

        workspace_id = d.pop("workspace_id")

        data_source = cls(
            builtin=builtin,
            config=config,
            created_at=created_at,
            created_by_id=created_by_id,
            enabled=enabled,
            has_export_credentials=has_export_credentials,
            has_query_credentials=has_query_credentials,
            id=id,
            name=name,
            organization_id=organization_id,
            updated_at=updated_at,
            updated_by_id=updated_by_id,
            version=version,
            workspace_id=workspace_id,
        )

        data_source.additional_properties = d
        return data_source

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
