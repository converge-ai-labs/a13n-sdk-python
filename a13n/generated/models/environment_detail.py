from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.environment_access import EnvironmentAccess
from ..models.environment_detail_ownership import EnvironmentDetailOwnership
from ..models.environment_detail_retention_condition import EnvironmentDetailRetentionCondition
from ..models.environment_status import EnvironmentStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.environment_detail_labels import EnvironmentDetailLabels
    from ..models.retention_policy import RetentionPolicy


T = TypeVar("T", bound="EnvironmentDetail")


@_attrs_define(repr=False)
class EnvironmentDetail:
    """
    Attributes:
        access (EnvironmentAccess):
        condition_since (datetime.datetime):
        created_at (datetime.datetime):
        generation (int):
        id (str):
        name (str):
        organization_id (str):
        ownership (EnvironmentDetailOwnership):
        provider_id (str):
        retention (None | RetentionPolicy):
        retention_condition (EnvironmentDetailRetentionCondition):
        status (EnvironmentStatus):
        supports_destroy (bool):
        supports_stop (bool):
        template_revision_id (None | str):
        updated_at (datetime.datetime):
        workspace_id (str):
        labels (EnvironmentDetailLabels | Unset):
    """

    access: EnvironmentAccess
    condition_since: datetime.datetime
    created_at: datetime.datetime
    generation: int
    id: str
    name: str
    organization_id: str
    ownership: EnvironmentDetailOwnership
    provider_id: str
    retention: RetentionPolicy | None
    retention_condition: EnvironmentDetailRetentionCondition
    status: EnvironmentStatus
    supports_destroy: bool
    supports_stop: bool
    template_revision_id: str | None
    updated_at: datetime.datetime
    workspace_id: str
    labels: EnvironmentDetailLabels | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.retention_policy import RetentionPolicy

        access = self.access.value

        condition_since = self.condition_since.isoformat()

        created_at = self.created_at.isoformat()

        generation = self.generation

        id = self.id

        name = self.name

        organization_id = self.organization_id

        ownership = self.ownership.value

        provider_id = self.provider_id

        retention: dict[str, Any] | None
        if isinstance(self.retention, RetentionPolicy):
            retention = self.retention.to_dict()
        else:
            retention = self.retention

        retention_condition = self.retention_condition.value

        status = self.status.value

        supports_destroy = self.supports_destroy

        supports_stop = self.supports_stop

        template_revision_id: str | None
        template_revision_id = self.template_revision_id

        updated_at = self.updated_at.isoformat()

        workspace_id = self.workspace_id

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "access": access,
                "condition_since": condition_since,
                "created_at": created_at,
                "generation": generation,
                "id": id,
                "name": name,
                "organization_id": organization_id,
                "ownership": ownership,
                "provider_id": provider_id,
                "retention": retention,
                "retention_condition": retention_condition,
                "status": status,
                "supports_destroy": supports_destroy,
                "supports_stop": supports_stop,
                "template_revision_id": template_revision_id,
                "updated_at": updated_at,
                "workspace_id": workspace_id,
            }
        )
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.environment_detail_labels import EnvironmentDetailLabels
        from ..models.retention_policy import RetentionPolicy

        d = dict(src_dict)
        access = EnvironmentAccess(d.pop("access"))

        condition_since = datetime.datetime.fromisoformat(d.pop("condition_since"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        generation = d.pop("generation")

        id = d.pop("id")

        name = d.pop("name")

        organization_id = d.pop("organization_id")

        ownership = EnvironmentDetailOwnership(d.pop("ownership"))

        provider_id = d.pop("provider_id")

        def _parse_retention(data: object) -> RetentionPolicy | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                retention_type_0 = RetentionPolicy.from_dict(data)

                return retention_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(RetentionPolicy | None, data)

        retention = _parse_retention(d.pop("retention"))

        retention_condition = EnvironmentDetailRetentionCondition(d.pop("retention_condition"))

        status = EnvironmentStatus(d.pop("status"))

        supports_destroy = d.pop("supports_destroy")

        supports_stop = d.pop("supports_stop")

        def _parse_template_revision_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        template_revision_id = _parse_template_revision_id(d.pop("template_revision_id"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        workspace_id = d.pop("workspace_id")

        _labels = d.pop("labels", UNSET)
        labels: EnvironmentDetailLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = EnvironmentDetailLabels.from_dict(_labels)

        environment_detail = cls(
            access=access,
            condition_since=condition_since,
            created_at=created_at,
            generation=generation,
            id=id,
            name=name,
            organization_id=organization_id,
            ownership=ownership,
            provider_id=provider_id,
            retention=retention,
            retention_condition=retention_condition,
            status=status,
            supports_destroy=supports_destroy,
            supports_stop=supports_stop,
            template_revision_id=template_revision_id,
            updated_at=updated_at,
            workspace_id=workspace_id,
            labels=labels,
        )

        return environment_detail
