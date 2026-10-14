from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.platform_group import PlatformGroup
from ..models.platform_selection_read_permission import PlatformSelectionReadPermission
from ..models.platform_selection_write_permission import PlatformSelectionWritePermission
from ..types import UNSET, Unset

T = TypeVar("T", bound="PlatformSelection")


@_attrs_define(repr=False)
class PlatformSelection:
    """Platform MCP groups selected independently of local operating instructions.

    Attributes:
        groups (list[PlatformGroup] | Unset):
        read_permission (PlatformSelectionReadPermission | Unset):
        write_permission (PlatformSelectionWritePermission | Unset):
    """

    groups: list[PlatformGroup] | Unset = UNSET
    read_permission: PlatformSelectionReadPermission | Unset = UNSET
    write_permission: PlatformSelectionWritePermission | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        groups: list[str] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.value
                groups.append(groups_item)

        read_permission: str | Unset = UNSET
        if not isinstance(self.read_permission, Unset):
            read_permission = self.read_permission.value

        write_permission: str | Unset = UNSET
        if not isinstance(self.write_permission, Unset):
            write_permission = self.write_permission.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if groups is not UNSET:
            field_dict["groups"] = groups
        if read_permission is not UNSET:
            field_dict["read_permission"] = read_permission
        if write_permission is not UNSET:
            field_dict["write_permission"] = write_permission

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _groups = d.pop("groups", UNSET)
        groups: list[PlatformGroup] | Unset = UNSET
        if _groups is not UNSET:
            groups = []
            for groups_item_data in _groups:
                groups_item = PlatformGroup(groups_item_data)

                groups.append(groups_item)

        _read_permission = d.pop("read_permission", UNSET)
        read_permission: PlatformSelectionReadPermission | Unset
        if isinstance(_read_permission, Unset):
            read_permission = UNSET
        else:
            read_permission = PlatformSelectionReadPermission(_read_permission)

        _write_permission = d.pop("write_permission", UNSET)
        write_permission: PlatformSelectionWritePermission | Unset
        if isinstance(_write_permission, Unset):
            write_permission = UNSET
        else:
            write_permission = PlatformSelectionWritePermission(_write_permission)

        platform_selection = cls(
            groups=groups,
            read_permission=read_permission,
            write_permission=write_permission,
        )

        return platform_selection
