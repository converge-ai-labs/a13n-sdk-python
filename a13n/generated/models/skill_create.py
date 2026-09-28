from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.git_hub_source import GitHubSource
    from ..models.skill_create_labels import SkillCreateLabels
    from ..models.upload_source import UploadSource


T = TypeVar("T", bound="SkillCreate")


@_attrs_define(repr=False)
class SkillCreate:
    """`name` and `description` default to what the package's SKILL.md declares.

    Attributes:
        source (GitHubSource | UploadSource):
        description (None | str | Unset):
        labels (SkillCreateLabels | Unset):
        name (None | str | Unset):
    """

    source: GitHubSource | UploadSource
    description: str | Unset | None = UNSET
    labels: SkillCreateLabels | Unset = UNSET
    name: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.upload_source import UploadSource

        source: dict[str, Any]
        if isinstance(self.source, UploadSource):
            source = self.source.to_dict()
        else:
            source = self.source.to_dict()

        description: str | Unset | None
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        name: str | Unset | None
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "source": source,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if labels is not UNSET:
            field_dict["labels"] = labels
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.git_hub_source import GitHubSource
        from ..models.skill_create_labels import SkillCreateLabels
        from ..models.upload_source import UploadSource

        d = dict(src_dict)

        def _parse_source(data: object) -> GitHubSource | UploadSource:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_type_0 = UploadSource.from_dict(data)

                return source_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            source_type_1 = GitHubSource.from_dict(data)

            return source_type_1

        source = _parse_source(d.pop("source"))

        def _parse_description(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        description = _parse_description(d.pop("description", UNSET))

        _labels = d.pop("labels", UNSET)
        labels: SkillCreateLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = SkillCreateLabels.from_dict(_labels)

        def _parse_name(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        name = _parse_name(d.pop("name", UNSET))

        skill_create = cls(
            source=source,
            description=description,
            labels=labels,
            name=name,
        )

        return skill_create
