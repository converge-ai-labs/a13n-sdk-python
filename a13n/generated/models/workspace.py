from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.verb import Verb

if TYPE_CHECKING:
    from ..models.workspace_settings import WorkspaceSettings


T = TypeVar("T", bound="Workspace")


@_attrs_define(repr=False)
class Workspace:
    """
    Attributes:
        archived_at (datetime.datetime | None):
        created_at (datetime.datetime):
        id (str):
        image_url (None | str):
        key (str):
        name (str):
        organization_id (str):
        permissions (list[Verb]):
        settings (WorkspaceSettings):
        updated_at (datetime.datetime):
        version (int):
    """

    archived_at: datetime.datetime | None
    created_at: datetime.datetime
    id: str
    image_url: str | None
    key: str
    name: str
    organization_id: str
    permissions: list[Verb]
    settings: WorkspaceSettings
    updated_at: datetime.datetime
    version: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        archived_at: str | None
        if isinstance(self.archived_at, datetime.datetime):
            archived_at = self.archived_at.isoformat()
        else:
            archived_at = self.archived_at

        created_at = self.created_at.isoformat()

        id = self.id

        image_url: str | None
        image_url = self.image_url

        key = self.key

        name = self.name

        organization_id = self.organization_id

        permissions = []
        for permissions_item_data in self.permissions:
            permissions_item = permissions_item_data.value
            permissions.append(permissions_item)

        settings = self.settings.to_dict()

        updated_at = self.updated_at.isoformat()

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "archived_at": archived_at,
                "created_at": created_at,
                "id": id,
                "image_url": image_url,
                "key": key,
                "name": name,
                "organization_id": organization_id,
                "permissions": permissions,
                "settings": settings,
                "updated_at": updated_at,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workspace_settings import WorkspaceSettings

        d = dict(src_dict)

        def _parse_archived_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                archived_at_type_0 = datetime.datetime.fromisoformat(data)

                return archived_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        archived_at = _parse_archived_at(d.pop("archived_at"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = d.pop("id")

        def _parse_image_url(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        image_url = _parse_image_url(d.pop("image_url"))

        key = d.pop("key")

        name = d.pop("name")

        organization_id = d.pop("organization_id")

        permissions = []
        _permissions = d.pop("permissions")
        for permissions_item_data in _permissions:
            permissions_item = Verb(permissions_item_data)

            permissions.append(permissions_item)

        settings = WorkspaceSettings.from_dict(d.pop("settings"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        version = d.pop("version")

        workspace = cls(
            archived_at=archived_at,
            created_at=created_at,
            id=id,
            image_url=image_url,
            key=key,
            name=name,
            organization_id=organization_id,
            permissions=permissions,
            settings=settings,
            updated_at=updated_at,
            version=version,
        )

        workspace.additional_properties = d
        return workspace

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
