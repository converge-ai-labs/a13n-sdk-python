from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.verb import Verb

T = TypeVar("T", bound="Organization")


@_attrs_define(repr=False)
class Organization:
    """
    Attributes:
        created_at (datetime.datetime):
        id (str):
        image_url (None | str):
        key (str):
        name (str):
        permissions (list[Verb]):
        updated_at (datetime.datetime):
        version (int):
    """

    created_at: datetime.datetime
    id: str
    image_url: str | None
    key: str
    name: str
    permissions: list[Verb]
    updated_at: datetime.datetime
    version: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = self.id

        image_url: str | None
        image_url = self.image_url

        key = self.key

        name = self.name

        permissions = []
        for permissions_item_data in self.permissions:
            permissions_item = permissions_item_data.value
            permissions.append(permissions_item)

        updated_at = self.updated_at.isoformat()

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "id": id,
                "image_url": image_url,
                "key": key,
                "name": name,
                "permissions": permissions,
                "updated_at": updated_at,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = d.pop("id")

        def _parse_image_url(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        image_url = _parse_image_url(d.pop("image_url"))

        key = d.pop("key")

        name = d.pop("name")

        permissions = []
        _permissions = d.pop("permissions")
        for permissions_item_data in _permissions:
            permissions_item = Verb(permissions_item_data)

            permissions.append(permissions_item)

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        version = d.pop("version")

        organization = cls(
            created_at=created_at,
            id=id,
            image_url=image_url,
            key=key,
            name=name,
            permissions=permissions,
            updated_at=updated_at,
            version=version,
        )

        organization.additional_properties = d
        return organization

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
