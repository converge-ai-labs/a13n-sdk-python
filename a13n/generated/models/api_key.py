from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.principal_summary import PrincipalSummary


T = TypeVar("T", bound="ApiKey")


@_attrs_define(repr=False)
class ApiKey:
    """
    Attributes:
        created_at (datetime.datetime):
        created_by_id (str):
        expires_at (datetime.datetime | None):
        id (str):
        last_used_at (datetime.datetime | None):
        name (str):
        organization_id (str):
        principal (PrincipalSummary):
        revoked_at (datetime.datetime | None):
        version (int):
        workspace_id (str):
    """

    created_at: datetime.datetime
    created_by_id: str
    expires_at: datetime.datetime | None
    id: str
    last_used_at: datetime.datetime | None
    name: str
    organization_id: str
    principal: PrincipalSummary
    revoked_at: datetime.datetime | None
    version: int
    workspace_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        created_by_id = self.created_by_id

        expires_at: str | None
        if isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        id = self.id

        last_used_at: str | None
        if isinstance(self.last_used_at, datetime.datetime):
            last_used_at = self.last_used_at.isoformat()
        else:
            last_used_at = self.last_used_at

        name = self.name

        organization_id = self.organization_id

        principal = self.principal.to_dict()

        revoked_at: str | None
        if isinstance(self.revoked_at, datetime.datetime):
            revoked_at = self.revoked_at.isoformat()
        else:
            revoked_at = self.revoked_at

        version = self.version

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "created_by_id": created_by_id,
                "expires_at": expires_at,
                "id": id,
                "last_used_at": last_used_at,
                "name": name,
                "organization_id": organization_id,
                "principal": principal,
                "revoked_at": revoked_at,
                "version": version,
                "workspace_id": workspace_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.principal_summary import PrincipalSummary

        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        created_by_id = d.pop("created_by_id")

        def _parse_expires_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = datetime.datetime.fromisoformat(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        expires_at = _parse_expires_at(d.pop("expires_at"))

        id = d.pop("id")

        def _parse_last_used_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_used_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_used_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_used_at = _parse_last_used_at(d.pop("last_used_at"))

        name = d.pop("name")

        organization_id = d.pop("organization_id")

        principal = PrincipalSummary.from_dict(d.pop("principal"))

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

        version = d.pop("version")

        workspace_id = d.pop("workspace_id")

        api_key = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            expires_at=expires_at,
            id=id,
            last_used_at=last_used_at,
            name=name,
            organization_id=organization_id,
            principal=principal,
            revoked_at=revoked_at,
            version=version,
            workspace_id=workspace_id,
        )

        api_key.additional_properties = d
        return api_key

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
