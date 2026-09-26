from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.git_hub_source import GitHubSource
    from ..models.upload_source import UploadSource


T = TypeVar("T", bound="SkillRevisionCreate")


@_attrs_define(repr=False)
class SkillRevisionCreate:
    """
    Attributes:
        source (GitHubSource | UploadSource):
        make_default (bool | Unset):
        note (None | str | Unset):
    """

    source: GitHubSource | UploadSource
    make_default: bool | Unset = UNSET
    note: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.upload_source import UploadSource

        source: dict[str, Any]
        if isinstance(self.source, UploadSource):
            source = self.source.to_dict()
        else:
            source = self.source.to_dict()

        make_default = self.make_default

        note: str | Unset | None
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "source": source,
            }
        )
        if make_default is not UNSET:
            field_dict["make_default"] = make_default
        if note is not UNSET:
            field_dict["note"] = note

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

        make_default = d.pop("make_default", UNSET)

        def _parse_note(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        note = _parse_note(d.pop("note", UNSET))

        skill_revision_create = cls(
            source=source,
            make_default=make_default,
            note=note,
        )

        return skill_revision_create
