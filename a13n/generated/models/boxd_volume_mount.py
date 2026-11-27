from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="BoxdVolumeMount")


@_attrs_define(repr=False)
class BoxdVolumeMount:
    """
    Attributes:
        disk_id (str):
        mount_path (str):
        read_only (bool | Unset):
    """

    disk_id: str
    mount_path: str
    read_only: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        disk_id = self.disk_id

        mount_path = self.mount_path

        read_only = self.read_only

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "disk_id": disk_id,
                "mount_path": mount_path,
            }
        )
        if read_only is not UNSET:
            field_dict["read_only"] = read_only

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        disk_id = d.pop("disk_id")

        mount_path = d.pop("mount_path")

        read_only = d.pop("read_only", UNSET)

        boxd_volume_mount = cls(
            disk_id=disk_id,
            mount_path=mount_path,
            read_only=read_only,
        )

        return boxd_volume_mount
