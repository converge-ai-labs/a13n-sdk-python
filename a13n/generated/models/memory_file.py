from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MemoryFile")


@_attrs_define(repr=False)
class MemoryFile:
    """
    Attributes:
        content (str):
        created_at (datetime.datetime):
        description (None | str):
        id (str):
        path (str):
        size (int):
        updated_at (datetime.datetime):
        updated_by_principal_id (None | str):
        updated_by_run_id (None | str):
        version (int):
    """

    content: str
    created_at: datetime.datetime
    description: str | None
    id: str
    path: str
    size: int
    updated_at: datetime.datetime
    updated_by_principal_id: str | None
    updated_by_run_id: str | None
    version: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        created_at = self.created_at.isoformat()

        description: str | None
        description = self.description

        id = self.id

        path = self.path

        size = self.size

        updated_at = self.updated_at.isoformat()

        updated_by_principal_id: str | None
        updated_by_principal_id = self.updated_by_principal_id

        updated_by_run_id: str | None
        updated_by_run_id = self.updated_by_run_id

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "created_at": created_at,
                "description": description,
                "id": id,
                "path": path,
                "size": size,
                "updated_at": updated_at,
                "updated_by_principal_id": updated_by_principal_id,
                "updated_by_run_id": updated_by_run_id,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = d.pop("content")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_description(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        description = _parse_description(d.pop("description"))

        id = d.pop("id")

        path = d.pop("path")

        size = d.pop("size")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_updated_by_principal_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        updated_by_principal_id = _parse_updated_by_principal_id(d.pop("updated_by_principal_id"))

        def _parse_updated_by_run_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        updated_by_run_id = _parse_updated_by_run_id(d.pop("updated_by_run_id"))

        version = d.pop("version")

        memory_file = cls(
            content=content,
            created_at=created_at,
            description=description,
            id=id,
            path=path,
            size=size,
            updated_at=updated_at,
            updated_by_principal_id=updated_by_principal_id,
            updated_by_run_id=updated_by_run_id,
            version=version,
        )

        memory_file.additional_properties = d
        return memory_file

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
