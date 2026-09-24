from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.git_hub_source import GitHubSource
    from ..models.upload_source import UploadSource


T = TypeVar("T", bound="SkillRevisionSummary")


@_attrs_define(repr=False)
class SkillRevisionSummary:
    """What a skill's representation shows of its default revision.

    Attributes:
        id (str):
        number (int):
        source (GitHubSource | UploadSource):
    """

    id: str
    number: int
    source: GitHubSource | UploadSource
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.upload_source import UploadSource

        id = self.id

        number = self.number

        source: dict[str, Any]
        if isinstance(self.source, UploadSource):
            source = self.source.to_dict()
        else:
            source = self.source.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "number": number,
                "source": source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.git_hub_source import GitHubSource
        from ..models.upload_source import UploadSource

        d = dict(src_dict)
        id = d.pop("id")

        number = d.pop("number")

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

        skill_revision_summary = cls(
            id=id,
            number=number,
            source=source,
        )

        skill_revision_summary.additional_properties = d
        return skill_revision_summary

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
