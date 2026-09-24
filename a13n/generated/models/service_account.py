from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_account_status import ServiceAccountStatus

T = TypeVar("T", bound="ServiceAccount")


@_attrs_define(repr=False)
class ServiceAccount:
    """
    Attributes:
        created_at (datetime.datetime):
        description (str):
        id (str):
        name (str):
        organization_id (str):
        role (None | str):
        status (ServiceAccountStatus):
        updated_at (datetime.datetime):
        version (int):
        workspace_id (str):
    """

    created_at: datetime.datetime
    description: str
    id: str
    name: str
    organization_id: str
    role: str | None
    status: ServiceAccountStatus
    updated_at: datetime.datetime
    version: int
    workspace_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        description = self.description

        id = self.id

        name = self.name

        organization_id = self.organization_id

        role: str | None
        role = self.role

        status = self.status.value

        updated_at = self.updated_at.isoformat()

        version = self.version

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "description": description,
                "id": id,
                "name": name,
                "organization_id": organization_id,
                "role": role,
                "status": status,
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

        description = d.pop("description")

        id = d.pop("id")

        name = d.pop("name")

        organization_id = d.pop("organization_id")

        def _parse_role(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        role = _parse_role(d.pop("role"))

        status = ServiceAccountStatus(d.pop("status"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        version = d.pop("version")

        workspace_id = d.pop("workspace_id")

        service_account = cls(
            created_at=created_at,
            description=description,
            id=id,
            name=name,
            organization_id=organization_id,
            role=role,
            status=status,
            updated_at=updated_at,
            version=version,
            workspace_id=workspace_id,
        )

        service_account.additional_properties = d
        return service_account

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
