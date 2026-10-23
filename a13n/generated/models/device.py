from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Device")


@_attrs_define(repr=False)
class Device:
    """
    Attributes:
        created_at (datetime.datetime):
        device_id (str):
        enabled (bool):
        id (str):
        metrics_data_source_id (None | str):
        name (str):
        organization_id (str):
        updated_at (datetime.datetime):
        version (int):
        workspace_id (str):
    """

    created_at: datetime.datetime
    device_id: str
    enabled: bool
    id: str
    metrics_data_source_id: str | None
    name: str
    organization_id: str
    updated_at: datetime.datetime
    version: int
    workspace_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        device_id = self.device_id

        enabled = self.enabled

        id = self.id

        metrics_data_source_id: str | None
        metrics_data_source_id = self.metrics_data_source_id

        name = self.name

        organization_id = self.organization_id

        updated_at = self.updated_at.isoformat()

        version = self.version

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "device_id": device_id,
                "enabled": enabled,
                "id": id,
                "metrics_data_source_id": metrics_data_source_id,
                "name": name,
                "organization_id": organization_id,
                "updated_at": updated_at,
                "version": version,
                "workspace_id": workspace_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        device_id = d.pop("device_id")

        enabled = d.pop("enabled")

        id = d.pop("id")

        def _parse_metrics_data_source_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        metrics_data_source_id = _parse_metrics_data_source_id(d.pop("metrics_data_source_id"))

        name = d.pop("name")

        organization_id = d.pop("organization_id")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        version = d.pop("version")

        workspace_id = d.pop("workspace_id")

        device = cls(
            created_at=created_at,
            device_id=device_id,
            enabled=enabled,
            id=id,
            metrics_data_source_id=metrics_data_source_id,
            name=name,
            organization_id=organization_id,
            updated_at=updated_at,
            version=version,
            workspace_id=workspace_id,
        )

        device.additional_properties = d
        return device

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
