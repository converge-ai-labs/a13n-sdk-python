from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.git_hub_source import GitHubSource
    from ..models.upload_source import UploadSource


T = TypeVar("T", bound="SkillValidate")


@_attrs_define(repr=False)
class SkillValidate:
    """A package to read and check as creating a skill or revision would, storing nothing.

    Attributes:
        source (GitHubSource | UploadSource):
    """

    source: GitHubSource | UploadSource

    def to_dict(self) -> dict[str, Any]:
        from ..models.upload_source import UploadSource

        source: dict[str, Any]
        if isinstance(self.source, UploadSource):
            source = self.source.to_dict()
        else:
            source = self.source.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "source": source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.git_hub_source import GitHubSource
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

        skill_validate = cls(
            source=source,
        )

        return skill_validate
