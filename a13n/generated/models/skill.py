from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.skill_labels import SkillLabels
    from ..models.skill_revision_summary import SkillRevisionSummary


T = TypeVar("T", bound="Skill")


@_attrs_define(repr=False)
class Skill:
    """
    Attributes:
        archived_at (datetime.datetime | None):
        created_at (datetime.datetime):
        created_by_id (str):
        default_revision (None | SkillRevisionSummary):
        default_revision_id (None | str):
        description (str):
        id (str):
        labels (SkillLabels):
        name (str):
        organization_id (str):
        updated_at (datetime.datetime):
        updated_by_id (str):
        version (int):
        workspace_id (str):
    """

    archived_at: datetime.datetime | None
    created_at: datetime.datetime
    created_by_id: str
    default_revision: SkillRevisionSummary | None
    default_revision_id: str | None
    description: str
    id: str
    labels: SkillLabels
    name: str
    organization_id: str
    updated_at: datetime.datetime
    updated_by_id: str
    version: int
    workspace_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.skill_revision_summary import SkillRevisionSummary

        archived_at: str | None
        if isinstance(self.archived_at, datetime.datetime):
            archived_at = self.archived_at.isoformat()
        else:
            archived_at = self.archived_at

        created_at = self.created_at.isoformat()

        created_by_id = self.created_by_id

        default_revision: dict[str, Any] | None
        if isinstance(self.default_revision, SkillRevisionSummary):
            default_revision = self.default_revision.to_dict()
        else:
            default_revision = self.default_revision

        default_revision_id: str | None
        default_revision_id = self.default_revision_id

        description = self.description

        id = self.id

        labels = self.labels.to_dict()

        name = self.name

        organization_id = self.organization_id

        updated_at = self.updated_at.isoformat()

        updated_by_id = self.updated_by_id

        version = self.version

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "archived_at": archived_at,
                "created_at": created_at,
                "created_by_id": created_by_id,
                "default_revision": default_revision,
                "default_revision_id": default_revision_id,
                "description": description,
                "id": id,
                "labels": labels,
                "name": name,
                "organization_id": organization_id,
                "updated_at": updated_at,
                "updated_by_id": updated_by_id,
                "version": version,
                "workspace_id": workspace_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.skill_labels import SkillLabels
        from ..models.skill_revision_summary import SkillRevisionSummary

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

        created_by_id = d.pop("created_by_id")

        def _parse_default_revision(data: object) -> SkillRevisionSummary | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                default_revision_type_0 = SkillRevisionSummary.from_dict(data)

                return default_revision_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(SkillRevisionSummary | None, data)

        default_revision = _parse_default_revision(d.pop("default_revision"))

        def _parse_default_revision_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        default_revision_id = _parse_default_revision_id(d.pop("default_revision_id"))

        description = d.pop("description")

        id = d.pop("id")

        labels = SkillLabels.from_dict(d.pop("labels"))

        name = d.pop("name")

        organization_id = d.pop("organization_id")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        updated_by_id = d.pop("updated_by_id")

        version = d.pop("version")

        workspace_id = d.pop("workspace_id")

        skill = cls(
            archived_at=archived_at,
            created_at=created_at,
            created_by_id=created_by_id,
            default_revision=default_revision,
            default_revision_id=default_revision_id,
            description=description,
            id=id,
            labels=labels,
            name=name,
            organization_id=organization_id,
            updated_at=updated_at,
            updated_by_id=updated_by_id,
            version=version,
            workspace_id=workspace_id,
        )

        skill.additional_properties = d
        return skill

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
