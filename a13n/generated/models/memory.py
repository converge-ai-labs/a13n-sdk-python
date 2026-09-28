from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.memory_kind import MemoryKind

if TYPE_CHECKING:
    from ..models.memory_labels import MemoryLabels


T = TypeVar("T", bound="Memory")


@_attrs_define(repr=False)
class Memory:
    """
    Attributes:
        always_load (list[str]):
        content_bytes (int | None):
        created_at (datetime.datetime):
        created_by_id (str):
        description (None | str):
        file_count (int | None):
        guide (None | str):
        history_bytes (int | None):
        id (str):
        inherited_guide (str):
        kind (MemoryKind):
        labels (MemoryLabels):
        name (str):
        namespace (None | str):
        organization_id (str):
        provider_id (None | str):
        type_ (str):
        updated_at (datetime.datetime):
        updated_by_id (str):
        version (int):
        workspace_id (str):
    """

    always_load: list[str]
    content_bytes: int | None
    created_at: datetime.datetime
    created_by_id: str
    description: str | None
    file_count: int | None
    guide: str | None
    history_bytes: int | None
    id: str
    inherited_guide: str
    kind: MemoryKind
    labels: MemoryLabels
    name: str
    namespace: str | None
    organization_id: str
    provider_id: str | None
    type_: str
    updated_at: datetime.datetime
    updated_by_id: str
    version: int
    workspace_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        always_load = self.always_load

        content_bytes: int | None
        content_bytes = self.content_bytes

        created_at = self.created_at.isoformat()

        created_by_id = self.created_by_id

        description: str | None
        description = self.description

        file_count: int | None
        file_count = self.file_count

        guide: str | None
        guide = self.guide

        history_bytes: int | None
        history_bytes = self.history_bytes

        id = self.id

        inherited_guide = self.inherited_guide

        kind = self.kind.value

        labels = self.labels.to_dict()

        name = self.name

        namespace: str | None
        namespace = self.namespace

        organization_id = self.organization_id

        provider_id: str | None
        provider_id = self.provider_id

        type_ = self.type_

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
                "file_count": file_count,
                "guide": guide,
                "history_bytes": history_bytes,
                "id": id,
                "inherited_guide": inherited_guide,
                "kind": kind,
                "labels": labels,
                "name": name,
                "namespace": namespace,
                "organization_id": organization_id,
                "provider_id": provider_id,
                "type": type_,
                "updated_at": updated_at,
                "updated_by_id": updated_by_id,
                "version": version,
                "workspace_id": workspace_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.memory_labels import MemoryLabels

        d = dict(src_dict)
        always_load = cast(list[str], d.pop("always_load"))

        def _parse_content_bytes(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        content_bytes = _parse_content_bytes(d.pop("content_bytes"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        created_by_id = d.pop("created_by_id")

        def _parse_description(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        description = _parse_description(d.pop("description"))

        def _parse_file_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        file_count = _parse_file_count(d.pop("file_count"))

        def _parse_guide(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        guide = _parse_guide(d.pop("guide"))

        def _parse_history_bytes(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        history_bytes = _parse_history_bytes(d.pop("history_bytes"))

        id = d.pop("id")

        inherited_guide = d.pop("inherited_guide")

        kind = MemoryKind(d.pop("kind"))

        labels = MemoryLabels.from_dict(d.pop("labels"))

        name = d.pop("name")

        def _parse_namespace(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        namespace = _parse_namespace(d.pop("namespace"))

        organization_id = d.pop("organization_id")

        def _parse_provider_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        provider_id = _parse_provider_id(d.pop("provider_id"))

        type_ = d.pop("type")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        updated_by_id = d.pop("updated_by_id")

        version = d.pop("version")

        workspace_id = d.pop("workspace_id")

        memory = cls(
            always_load=always_load,
            content_bytes=content_bytes,
            created_at=created_at,
            created_by_id=created_by_id,
            description=description,
            file_count=file_count,
            guide=guide,
            history_bytes=history_bytes,
            id=id,
            inherited_guide=inherited_guide,
            kind=kind,
            labels=labels,
            name=name,
            namespace=namespace,
            organization_id=organization_id,
            provider_id=provider_id,
            type_=type_,
            updated_at=updated_at,
            updated_by_id=updated_by_id,
            version=version,
            workspace_id=workspace_id,
        )

        memory.additional_properties = d
        return memory

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
