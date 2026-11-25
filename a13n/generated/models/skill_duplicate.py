from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.skill_duplicate_labels_type_0 import SkillDuplicateLabelsType0


T = TypeVar("T", bound="SkillDuplicate")


@_attrs_define(repr=False)
class SkillDuplicate:
    """
    Attributes:
        description (None | str | Unset):
        labels (None | SkillDuplicateLabelsType0 | Unset):
        name (None | str | Unset):
        revision_id (None | str | Unset):
    """

    description: str | Unset | None = UNSET
    labels: SkillDuplicateLabelsType0 | Unset | None = UNSET
    name: str | Unset | None = UNSET
    revision_id: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.skill_duplicate_labels_type_0 import SkillDuplicateLabelsType0

        description: str | Unset | None
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        labels: dict[str, Any] | Unset | None
        if isinstance(self.labels, Unset):
            labels = UNSET
        elif isinstance(self.labels, SkillDuplicateLabelsType0):
            labels = self.labels.to_dict()
        else:
            labels = self.labels

        name: str | Unset | None
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        revision_id: str | Unset | None
        if isinstance(self.revision_id, Unset):
            revision_id = UNSET
        else:
            revision_id = self.revision_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if labels is not UNSET:
            field_dict["labels"] = labels
        if name is not UNSET:
            field_dict["name"] = name
        if revision_id is not UNSET:
            field_dict["revision_id"] = revision_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.skill_duplicate_labels_type_0 import SkillDuplicateLabelsType0

        d = dict(src_dict)

        def _parse_description(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_labels(data: object) -> SkillDuplicateLabelsType0 | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                labels_type_0 = SkillDuplicateLabelsType0.from_dict(data)

                return labels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(SkillDuplicateLabelsType0 | Unset | None, data)

        labels = _parse_labels(d.pop("labels", UNSET))

        def _parse_name(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_revision_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        revision_id = _parse_revision_id(d.pop("revision_id", UNSET))

        skill_duplicate = cls(
            description=description,
            labels=labels,
            name=name,
            revision_id=revision_id,
        )

        return skill_duplicate
