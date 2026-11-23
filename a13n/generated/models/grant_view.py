from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.grant_view_source import GrantViewSource
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.principal_summary import PrincipalSummary


T = TypeVar("T", bound="GrantView")


@_attrs_define(repr=False)
class GrantView:
    """
    Attributes:
        created_at (datetime.datetime):
        created_by_id (str):
        id (str):
        organization_id (str):
        principal (PrincipalSummary):
        role (str):
        workspace_id (None | str):
        overrides_sso (bool | Unset): The manual grant overrides an SSO default at this scope.
        source (GrantViewSource | Unset):
    """

    created_at: datetime.datetime
    created_by_id: str
    id: str
    organization_id: str
    principal: PrincipalSummary
    role: str
    workspace_id: str | None
    overrides_sso: bool | Unset = UNSET
    source: GrantViewSource | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        created_by_id = self.created_by_id

        id = self.id

        organization_id = self.organization_id

        principal = self.principal.to_dict()

        role = self.role

        workspace_id: str | None
        workspace_id = self.workspace_id

        overrides_sso = self.overrides_sso

        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "created_by_id": created_by_id,
                "id": id,
                "organization_id": organization_id,
                "principal": principal,
                "role": role,
                "workspace_id": workspace_id,
            }
        )
        if overrides_sso is not UNSET:
            field_dict["overrides_sso"] = overrides_sso
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.principal_summary import PrincipalSummary

        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        created_by_id = d.pop("created_by_id")

        id = d.pop("id")

        organization_id = d.pop("organization_id")

        principal = PrincipalSummary.from_dict(d.pop("principal"))

        role = d.pop("role")

        def _parse_workspace_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        workspace_id = _parse_workspace_id(d.pop("workspace_id"))

        overrides_sso = d.pop("overrides_sso", UNSET)

        _source = d.pop("source", UNSET)
        source: GrantViewSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = GrantViewSource(_source)

        grant_view = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            organization_id=organization_id,
            principal=principal,
            role=role,
            workspace_id=workspace_id,
            overrides_sso=overrides_sso,
            source=source,
        )

        grant_view.additional_properties = d
        return grant_view

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
