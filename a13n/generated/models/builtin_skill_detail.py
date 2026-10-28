from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.skill_file import SkillFile


T = TypeVar("T", bound="BuiltinSkillDetail")


@_attrs_define(repr=False)
class BuiltinSkillDetail:
    """The current process's bundled package, without a workspace resource or revision.

    Attributes:
        description (str):
        files (list[SkillFile]):
        name (Literal['platform-operations']):
        package_digest (str):
        package_size (int):
        root (str):
    """

    description: str
    files: list[SkillFile]
    name: Literal["platform-operations"]
    package_digest: str
    package_size: int
    root: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        files = []
        for files_item_data in self.files:
            files_item = files_item_data.to_dict()
            files.append(files_item)

        name = self.name

        package_digest = self.package_digest

        package_size = self.package_size

        root = self.root

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "files": files,
                "name": name,
                "package_digest": package_digest,
                "package_size": package_size,
                "root": root,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.skill_file import SkillFile

        d = dict(src_dict)
        description = d.pop("description")

        files = []
        _files = d.pop("files")
        for files_item_data in _files:
            files_item = SkillFile.from_dict(files_item_data)

            files.append(files_item)

        name = cast(Literal["platform-operations"], d.pop("name"))
        if name != "platform-operations":
            raise ValueError(f"name must match const 'platform-operations', got '{name}'")

        package_digest = d.pop("package_digest")

        package_size = d.pop("package_size")

        root = d.pop("root")

        builtin_skill_detail = cls(
            description=description,
            files=files,
            name=name,
            package_digest=package_digest,
            package_size=package_size,
            root=root,
        )

        builtin_skill_detail.additional_properties = d
        return builtin_skill_detail

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
