from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.secret_scope import SecretScope

T = TypeVar("T", bound="Secret")


@_attrs_define(repr=False)
class Secret:
    """
    Attributes:
        created_at (datetime.datetime):
        created_by_id (str):
        id (str):
        key (str):
        principal_id (None | str):
        scope (SecretScope):
        updated_at (datetime.datetime):
        updated_by_id (str):
        version (int):
        workspace_id (str):
    """

    created_at: datetime.datetime
    created_by_id: str
    id: str
    key: str
    principal_id: str | None
    scope: SecretScope
    updated_at: datetime.datetime
    updated_by_id: str
    version: int
    workspace_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        created_by_id = self.created_by_id

        id = self.id

        key = self.key

        principal_id: str | None
        principal_id = self.principal_id

        scope = self.scope.value

        updated_at = self.updated_at.isoformat()

        updated_by_id = self.updated_by_id

        version = self.version

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "created_by_id": created_by_id,
                "id": id,
                "key": key,
                "principal_id": principal_id,
                "scope": scope,
                "updated_at": updated_at,
                "updated_by_id": updated_by_id,
                "version": version,
                "workspace_id": workspace_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        created_by_id = d.pop("created_by_id")

        id = d.pop("id")

        key = d.pop("key")

        def _parse_principal_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        principal_id = _parse_principal_id(d.pop("principal_id"))

        scope = SecretScope(d.pop("scope"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        updated_by_id = d.pop("updated_by_id")

        version = d.pop("version")

        workspace_id = d.pop("workspace_id")

        secret = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            key=key,
            principal_id=principal_id,
            scope=scope,
            updated_at=updated_at,
            updated_by_id=updated_by_id,
            version=version,
            workspace_id=workspace_id,
        )

        secret.additional_properties = d
        return secret

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
