from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.skill_manifest import SkillManifest


T = TypeVar("T", bound="SkillRevision")


@_attrs_define(repr=False)
class SkillRevision:
    """
    Attributes:
        config (SkillManifest): The frozen configuration of a skill revision: what its SKILL.md declares and the exact
            package bytes.
        created_at (datetime.datetime):
        created_by_id (str):
        digest (str):
        id (str):
        note (None | str):
        number (int):
        skill_id (str):
        workspace_id (str):
    """

    config: SkillManifest
    created_at: datetime.datetime
    created_by_id: str
    digest: str
    id: str
    note: str | None
    number: int
    skill_id: str
    workspace_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config = self.config.to_dict()

        created_at = self.created_at.isoformat()

        created_by_id = self.created_by_id

        digest = self.digest

        id = self.id

        note: str | None
        note = self.note

        number = self.number

        skill_id = self.skill_id

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config": config,
                "created_at": created_at,
                "created_by_id": created_by_id,
                "digest": digest,
                "id": id,
                "note": note,
                "number": number,
                "skill_id": skill_id,
                "workspace_id": workspace_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.skill_manifest import SkillManifest

        d = dict(src_dict)
        config = SkillManifest.from_dict(d.pop("config"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        created_by_id = d.pop("created_by_id")

        digest = d.pop("digest")

        id = d.pop("id")

        def _parse_note(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        note = _parse_note(d.pop("note"))

        number = d.pop("number")

        skill_id = d.pop("skill_id")

        workspace_id = d.pop("workspace_id")

        skill_revision = cls(
            config=config,
            created_at=created_at,
            created_by_id=created_by_id,
            digest=digest,
            id=id,
            note=note,
            number=number,
            skill_id=skill_id,
            workspace_id=workspace_id,
        )

        skill_revision.additional_properties = d
        return skill_revision

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
