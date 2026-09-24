from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SkillSelection")


@_attrs_define(repr=False)
class SkillSelection:
    """
    Attributes:
        skill_id (str):
        revision_id (None | str | Unset):
    """

    skill_id: str
    revision_id: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        skill_id = self.skill_id

        revision_id: str | Unset | None
        if isinstance(self.revision_id, Unset):
            revision_id = UNSET
        else:
            revision_id = self.revision_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "skill_id": skill_id,
            }
        )
        if revision_id is not UNSET:
            field_dict["revision_id"] = revision_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        skill_id = d.pop("skill_id")

        def _parse_revision_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        revision_id = _parse_revision_id(d.pop("revision_id", UNSET))

        skill_selection = cls(
            skill_id=skill_id,
            revision_id=revision_id,
        )

        return skill_selection
