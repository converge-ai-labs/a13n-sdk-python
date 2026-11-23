from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.credential_state import CredentialState
from ..types import UNSET, Unset

T = TypeVar("T", bound="Credential")


@_attrs_define(repr=False)
class Credential:
    """
    Attributes:
        allowed_hosts (list[str]):
        created_at (datetime.datetime):
        created_by_id (str):
        credential_version (int):
        description (str):
        id (str):
        name (str):
        organization_id (str):
        revoked_at (datetime.datetime | None):
        state (CredentialState):
        updated_at (datetime.datetime):
        updated_by_id (str):
        version (int):
        workspace_id (str):
        owner_app_id (None | str | Unset):
    """

    allowed_hosts: list[str]
    created_at: datetime.datetime
    created_by_id: str
    credential_version: int
    description: str
    id: str
    name: str
    organization_id: str
    revoked_at: datetime.datetime | None
    state: CredentialState
    updated_at: datetime.datetime
    updated_by_id: str
    version: int
    workspace_id: str
    owner_app_id: str | Unset | None = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allowed_hosts = self.allowed_hosts

        created_at = self.created_at.isoformat()

        created_by_id = self.created_by_id

        credential_version = self.credential_version

        description = self.description

        id = self.id

        name = self.name

        organization_id = self.organization_id

        revoked_at: str | None
        if isinstance(self.revoked_at, datetime.datetime):
            revoked_at = self.revoked_at.isoformat()
        else:
            revoked_at = self.revoked_at

        state = self.state.value

        updated_at = self.updated_at.isoformat()

        updated_by_id = self.updated_by_id

        version = self.version

        workspace_id = self.workspace_id

        owner_app_id: str | Unset | None
        if isinstance(self.owner_app_id, Unset):
            owner_app_id = UNSET
        else:
            owner_app_id = self.owner_app_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allowed_hosts": allowed_hosts,
                "created_at": created_at,
                "created_by_id": created_by_id,
                "credential_version": credential_version,
                "description": description,
                "id": id,
                "name": name,
                "organization_id": organization_id,
                "revoked_at": revoked_at,
                "state": state,
                "updated_at": updated_at,
                "updated_by_id": updated_by_id,
                "version": version,
                "workspace_id": workspace_id,
            }
        )
        if owner_app_id is not UNSET:
            field_dict["owner_app_id"] = owner_app_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allowed_hosts = cast(list[str], d.pop("allowed_hosts"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        created_by_id = d.pop("created_by_id")

        credential_version = d.pop("credential_version")

        description = d.pop("description")

        id = d.pop("id")

        name = d.pop("name")

        organization_id = d.pop("organization_id")

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

        state = CredentialState(d.pop("state"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        updated_by_id = d.pop("updated_by_id")

        version = d.pop("version")

        workspace_id = d.pop("workspace_id")

        def _parse_owner_app_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        owner_app_id = _parse_owner_app_id(d.pop("owner_app_id", UNSET))

        credential = cls(
            allowed_hosts=allowed_hosts,
            created_at=created_at,
            created_by_id=created_by_id,
            credential_version=credential_version,
            description=description,
            id=id,
            name=name,
            organization_id=organization_id,
            revoked_at=revoked_at,
            state=state,
            updated_at=updated_at,
            updated_by_id=updated_by_id,
            version=version,
            workspace_id=workspace_id,
            owner_app_id=owner_app_id,
        )

        credential.additional_properties = d
        return credential

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
