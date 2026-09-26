from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.audit_event_details import AuditEventDetails
    from ..models.principal_summary import PrincipalSummary


T = TypeVar("T", bound="AuditEvent")


@_attrs_define(repr=False)
class AuditEvent:
    """
    Attributes:
        action (str):
        actor (None | PrincipalSummary):
        actor_id (None | str):
        details (AuditEventDetails):
        id (str):
        occurred_at (datetime.datetime):
        organization_id (None | str):
        outcome (str):
        target_id (str):
        target_kind (str):
        workspace_id (None | str):
    """

    action: str
    actor: PrincipalSummary | None
    actor_id: str | None
    details: AuditEventDetails
    id: str
    occurred_at: datetime.datetime
    organization_id: str | None
    outcome: str
    target_id: str
    target_kind: str
    workspace_id: str | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.principal_summary import PrincipalSummary

        action = self.action

        actor: dict[str, Any] | None
        if isinstance(self.actor, PrincipalSummary):
            actor = self.actor.to_dict()
        else:
            actor = self.actor

        actor_id: str | None
        actor_id = self.actor_id

        details = self.details.to_dict()

        id = self.id

        occurred_at = self.occurred_at.isoformat()

        organization_id: str | None
        organization_id = self.organization_id

        outcome = self.outcome

        target_id = self.target_id

        target_kind = self.target_kind

        workspace_id: str | None
        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "actor": actor,
                "actor_id": actor_id,
                "details": details,
                "id": id,
                "occurred_at": occurred_at,
                "organization_id": organization_id,
                "outcome": outcome,
                "target_id": target_id,
                "target_kind": target_kind,
                "workspace_id": workspace_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audit_event_details import AuditEventDetails
        from ..models.principal_summary import PrincipalSummary

        d = dict(src_dict)
        action = d.pop("action")

        def _parse_actor(data: object) -> PrincipalSummary | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                actor_type_0 = PrincipalSummary.from_dict(data)

                return actor_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(PrincipalSummary | None, data)

        actor = _parse_actor(d.pop("actor"))

        def _parse_actor_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        actor_id = _parse_actor_id(d.pop("actor_id"))

        details = AuditEventDetails.from_dict(d.pop("details"))

        id = d.pop("id")

        occurred_at = datetime.datetime.fromisoformat(d.pop("occurred_at"))

        def _parse_organization_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        organization_id = _parse_organization_id(d.pop("organization_id"))

        outcome = d.pop("outcome")

        target_id = d.pop("target_id")

        target_kind = d.pop("target_kind")

        def _parse_workspace_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        workspace_id = _parse_workspace_id(d.pop("workspace_id"))

        audit_event = cls(
            action=action,
            actor=actor,
            actor_id=actor_id,
            details=details,
            id=id,
            occurred_at=occurred_at,
            organization_id=organization_id,
            outcome=outcome,
            target_id=target_id,
            target_kind=target_kind,
            workspace_id=workspace_id,
        )

        audit_event.additional_properties = d
        return audit_event

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
