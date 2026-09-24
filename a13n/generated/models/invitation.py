from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Invitation")


@_attrs_define(repr=False)
class Invitation:
    """
    Attributes:
        accepted_at (datetime.datetime | None):
        created_at (datetime.datetime):
        email (str):
        expires_at (datetime.datetime):
        id (str):
        invited_by_id (str):
        organization_id (str):
        principal_id (None | str):
        revoked_at (datetime.datetime | None):
        role (str):
        updated_at (datetime.datetime):
        version (int):
        workspace_id (None | str):
    """

    accepted_at: datetime.datetime | None
    created_at: datetime.datetime
    email: str
    expires_at: datetime.datetime
    id: str
    invited_by_id: str
    organization_id: str
    principal_id: str | None
    revoked_at: datetime.datetime | None
    role: str
    updated_at: datetime.datetime
    version: int
    workspace_id: str | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accepted_at: str | None
        if isinstance(self.accepted_at, datetime.datetime):
            accepted_at = self.accepted_at.isoformat()
        else:
            accepted_at = self.accepted_at

        created_at = self.created_at.isoformat()

        email = self.email

        expires_at = self.expires_at.isoformat()

        id = self.id

        invited_by_id = self.invited_by_id

        organization_id = self.organization_id

        principal_id: str | None
        principal_id = self.principal_id

        revoked_at: str | None
        if isinstance(self.revoked_at, datetime.datetime):
            revoked_at = self.revoked_at.isoformat()
        else:
            revoked_at = self.revoked_at

        role = self.role

        updated_at = self.updated_at.isoformat()

        version = self.version

        workspace_id: str | None
        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accepted_at": accepted_at,
                "created_at": created_at,
                "email": email,
                "expires_at": expires_at,
                "id": id,
                "invited_by_id": invited_by_id,
                "organization_id": organization_id,
                "principal_id": principal_id,
                "revoked_at": revoked_at,
                "role": role,
                "updated_at": updated_at,
                "version": version,
                "workspace_id": workspace_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_accepted_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                accepted_at_type_0 = datetime.datetime.fromisoformat(data)

                return accepted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        accepted_at = _parse_accepted_at(d.pop("accepted_at"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        email = d.pop("email")

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        id = d.pop("id")

        invited_by_id = d.pop("invited_by_id")

        organization_id = d.pop("organization_id")

        def _parse_principal_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        principal_id = _parse_principal_id(d.pop("principal_id"))

        def _parse_revoked_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                revoked_at_type_0 = datetime.datetime.fromisoformat(data)

                return revoked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        revoked_at = _parse_revoked_at(d.pop("revoked_at"))

        role = d.pop("role")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        version = d.pop("version")

        def _parse_workspace_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        workspace_id = _parse_workspace_id(d.pop("workspace_id"))

        invitation = cls(
            accepted_at=accepted_at,
            created_at=created_at,
            email=email,
            expires_at=expires_at,
            id=id,
            invited_by_id=invited_by_id,
            organization_id=organization_id,
            principal_id=principal_id,
            revoked_at=revoked_at,
            role=role,
            updated_at=updated_at,
            version=version,
            workspace_id=workspace_id,
        )

        invitation.additional_properties = d
        return invitation

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
