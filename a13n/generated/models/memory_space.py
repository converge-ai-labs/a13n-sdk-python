from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.memory_space_labels import MemorySpaceLabels
    from ..models.organization_policy import OrganizationPolicy


T = TypeVar("T", bound="MemorySpace")


@_attrs_define(repr=False)
class MemorySpace:
    """
    Attributes:
        always_load (list[str]):
        content_bytes (int):
        created_at (datetime.datetime):
        created_by_id (str):
        description (None | str):
        enabled (bool):
        file_count (int):
        guide (None | str):
        history_bytes (int):
        id (str):
        labels (MemorySpaceLabels):
        memory_id (str):
        name (str):
        organization (OrganizationPolicy):
        organization_id (str):
        updated_at (datetime.datetime):
        updated_by_id (str):
        version (int):
        workspace_id (str):
    """

    always_load: list[str]
    content_bytes: int
    created_at: datetime.datetime
    created_by_id: str
    description: str | None
    enabled: bool
    file_count: int
    guide: str | None
    history_bytes: int
    id: str
    labels: MemorySpaceLabels
    memory_id: str
    name: str
    organization: OrganizationPolicy
    organization_id: str
    updated_at: datetime.datetime
    updated_by_id: str
    version: int
    workspace_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        always_load = self.always_load

        content_bytes = self.content_bytes

        created_at = self.created_at.isoformat()

        created_by_id = self.created_by_id

        description: str | None
        description = self.description

        enabled = self.enabled

        file_count = self.file_count

        guide: str | None
        guide = self.guide

        history_bytes = self.history_bytes

        id = self.id

        labels = self.labels.to_dict()

        memory_id = self.memory_id

        name = self.name

        organization = self.organization.to_dict()

        organization_id = self.organization_id

        updated_at = self.updated_at.isoformat()

        updated_by_id = self.updated_by_id

        version = self.version

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "always_load": always_load,
                "content_bytes": content_bytes,
                "created_at": created_at,
                "created_by_id": created_by_id,
                "description": description,
                "enabled": enabled,
                "file_count": file_count,
                "guide": guide,
                "history_bytes": history_bytes,
                "id": id,
                "labels": labels,
                "memory_id": memory_id,
                "name": name,
                "organization": organization,
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
        from ..models.memory_space_labels import MemorySpaceLabels
        from ..models.organization_policy import OrganizationPolicy

        d = dict(src_dict)
        always_load = cast(list[str], d.pop("always_load"))

        content_bytes = d.pop("content_bytes")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        created_by_id = d.pop("created_by_id")

        def _parse_description(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        description = _parse_description(d.pop("description"))

        enabled = d.pop("enabled")

        file_count = d.pop("file_count")

        def _parse_guide(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        guide = _parse_guide(d.pop("guide"))

        history_bytes = d.pop("history_bytes")

        id = d.pop("id")

        labels = MemorySpaceLabels.from_dict(d.pop("labels"))

        memory_id = d.pop("memory_id")

        name = d.pop("name")

        organization = OrganizationPolicy.from_dict(d.pop("organization"))

        organization_id = d.pop("organization_id")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        updated_by_id = d.pop("updated_by_id")

        version = d.pop("version")

        workspace_id = d.pop("workspace_id")

        memory_space = cls(
            always_load=always_load,
            content_bytes=content_bytes,
            created_at=created_at,
            created_by_id=created_by_id,
            description=description,
            enabled=enabled,
            file_count=file_count,
            guide=guide,
            history_bytes=history_bytes,
            id=id,
            labels=labels,
            memory_id=memory_id,
            name=name,
            organization=organization,
            organization_id=organization_id,
            updated_at=updated_at,
            updated_by_id=updated_by_id,
            version=version,
            workspace_id=workspace_id,
        )

        memory_space.additional_properties = d
        return memory_space

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
