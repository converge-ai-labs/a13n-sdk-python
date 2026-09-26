from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Profile")


@_attrs_define(repr=False)
class Profile:
    """
    Attributes:
        created_at (datetime.datetime):
        email (None | str):
        id (str):
        image_url (None | str):
        kind (str):
        name (str):
        status (str):
        updated_at (datetime.datetime):
        version (int):
    """

    created_at: datetime.datetime
    email: str | None
    id: str
    image_url: str | None
    kind: str
    name: str
    status: str
    updated_at: datetime.datetime
    version: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        email: str | None
        email = self.email

        id = self.id

        image_url: str | None
        image_url = self.image_url

        kind = self.kind

        name = self.name

        status = self.status

        updated_at = self.updated_at.isoformat()

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "email": email,
                "id": id,
                "image_url": image_url,
                "kind": kind,
                "name": name,
                "status": status,
                "updated_at": updated_at,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_email(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        email = _parse_email(d.pop("email"))

        id = d.pop("id")

        def _parse_image_url(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        image_url = _parse_image_url(d.pop("image_url"))

        kind = d.pop("kind")

        name = d.pop("name")

        status = d.pop("status")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        version = d.pop("version")

        profile = cls(
            created_at=created_at,
            email=email,
            id=id,
            image_url=image_url,
            kind=kind,
            name=name,
            status=status,
            updated_at=updated_at,
            version=version,
        )

        profile.additional_properties = d
        return profile

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
