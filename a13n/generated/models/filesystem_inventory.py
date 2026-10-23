from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filesystem_inventory_filesystems import FilesystemInventoryFilesystems


T = TypeVar("T", bound="FilesystemInventory")


@_attrs_define(repr=False)
class FilesystemInventory:
    """
    Attributes:
        truncated (bool):
        filesystems (FilesystemInventoryFilesystems | Unset):
    """

    truncated: bool
    filesystems: FilesystemInventoryFilesystems | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        truncated = self.truncated

        filesystems: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filesystems, Unset):
            filesystems = self.filesystems.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "truncated": truncated,
            }
        )
        if filesystems is not UNSET:
            field_dict["filesystems"] = filesystems

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filesystem_inventory_filesystems import FilesystemInventoryFilesystems

        d = dict(src_dict)
        truncated = d.pop("truncated")

        _filesystems = d.pop("filesystems", UNSET)
        filesystems: FilesystemInventoryFilesystems | Unset
        if isinstance(_filesystems, Unset):
            filesystems = UNSET
        else:
            filesystems = FilesystemInventoryFilesystems.from_dict(_filesystems)

        filesystem_inventory = cls(
            truncated=truncated,
            filesystems=filesystems,
        )

        return filesystem_inventory
