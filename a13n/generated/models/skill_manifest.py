from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.git_hub_source import GitHubSource
    from ..models.skill_file import SkillFile
    from ..models.upload_source import UploadSource


T = TypeVar("T", bound="SkillManifest")


@_attrs_define(repr=False)
class SkillManifest:
    """The frozen configuration of a skill revision: what its SKILL.md declares and the exact package bytes.

    Attributes:
        description (str):
        files (list[SkillFile]):
        name (str):
        package_digest (str):
        package_size (int):
        root (str): The archive directory holding SKILL.md: "" or "<directory>/"
        size (int): Expanded bytes of all files
        source (GitHubSource | UploadSource):
    """

    description: str
    files: list[SkillFile]
    name: str
    package_digest: str
    package_size: int
    root: str
    size: int
    source: GitHubSource | UploadSource

    def to_dict(self) -> dict[str, Any]:
        from ..models.upload_source import UploadSource

        description = self.description

        files = []
        for files_item_data in self.files:
            files_item = files_item_data.to_dict()
            files.append(files_item)

        name = self.name

        package_digest = self.package_digest

        package_size = self.package_size

        root = self.root

        size = self.size

        source: dict[str, Any]
        if isinstance(self.source, UploadSource):
            source = self.source.to_dict()
        else:
            source = self.source.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "description": description,
                "files": files,
                "name": name,
                "package_digest": package_digest,
                "package_size": package_size,
                "root": root,
                "size": size,
                "source": source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.git_hub_source import GitHubSource
        from ..models.skill_file import SkillFile
        from ..models.upload_source import UploadSource

        d = dict(src_dict)
        description = d.pop("description")

        files = []
        _files = d.pop("files")
        for files_item_data in _files:
            files_item = SkillFile.from_dict(files_item_data)

            files.append(files_item)

        name = d.pop("name")

        package_digest = d.pop("package_digest")

        package_size = d.pop("package_size")

        root = d.pop("root")

        size = d.pop("size")

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

        skill_manifest = cls(
            description=description,
            files=files,
            name=name,
            package_digest=package_digest,
            package_size=package_size,
            root=root,
            size=size,
            source=source,
        )

        return skill_manifest
