from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.provider_config import ProviderConfig


T = TypeVar("T", bound="Provider")


@_attrs_define(repr=False)
class Provider:
    """
    Attributes:
        config (ProviderConfig):
        created_at (datetime.datetime):
        created_by_id (str):
        credential_configured (bool):
        enabled (bool):
        header_names (list[str]):
        id (str):
        name (str):
        organization_id (str):
        type_ (str):
        updated_at (datetime.datetime):
        updated_by_id (str):
        version (int):
        workspace_id (None | str):
    """

    config: ProviderConfig
    created_at: datetime.datetime
    created_by_id: str
    credential_configured: bool
    enabled: bool
    header_names: list[str]
    id: str
    name: str
    organization_id: str
    type_: str
    updated_at: datetime.datetime
    updated_by_id: str
    version: int
    workspace_id: str | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config = self.config.to_dict()

        created_at = self.created_at.isoformat()

        created_by_id = self.created_by_id

        credential_configured = self.credential_configured

        enabled = self.enabled

        header_names = self.header_names

        id = self.id

        name = self.name

        organization_id = self.organization_id

        type_ = self.type_

        updated_at = self.updated_at.isoformat()

        updated_by_id = self.updated_by_id

        version = self.version

        workspace_id: str | None
        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config": config,
                "created_at": created_at,
                "created_by_id": created_by_id,
                "credential_configured": credential_configured,
                "enabled": enabled,
                "header_names": header_names,
                "id": id,
                "name": name,
                "organization_id": organization_id,
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
        from ..models.provider_config import ProviderConfig

        d = dict(src_dict)
        config = ProviderConfig.from_dict(d.pop("config"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        created_by_id = d.pop("created_by_id")

        credential_configured = d.pop("credential_configured")

        enabled = d.pop("enabled")

        header_names = cast(list[str], d.pop("header_names"))

        id = d.pop("id")

        name = d.pop("name")

        organization_id = d.pop("organization_id")

        type_ = d.pop("type")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        updated_by_id = d.pop("updated_by_id")

        version = d.pop("version")

        def _parse_workspace_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        workspace_id = _parse_workspace_id(d.pop("workspace_id"))

        provider = cls(
            config=config,
            created_at=created_at,
            created_by_id=created_by_id,
            credential_configured=credential_configured,
            enabled=enabled,
            header_names=header_names,
            id=id,
            name=name,
            organization_id=organization_id,
            type_=type_,
            updated_at=updated_at,
            updated_by_id=updated_by_id,
            version=version,
            workspace_id=workspace_id,
        )

        provider.additional_properties = d
        return provider

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
