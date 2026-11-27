from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModalVolumeMount")


@_attrs_define(repr=False)
class ModalVolumeMount:
    """
    Attributes:
        mount_path (str):
        volume_name (str):
        read_only (bool | Unset):
        sub_path (None | str | Unset):
    """

    mount_path: str
    volume_name: str
    read_only: bool | Unset = UNSET
    sub_path: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        mount_path = self.mount_path

        volume_name = self.volume_name

        read_only = self.read_only

        sub_path: str | Unset | None
        if isinstance(self.sub_path, Unset):
            sub_path = UNSET
        else:
            sub_path = self.sub_path

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "mount_path": mount_path,
                "volume_name": volume_name,
            }
        )
        if read_only is not UNSET:
            field_dict["read_only"] = read_only
        if sub_path is not UNSET:
            field_dict["sub_path"] = sub_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mount_path = d.pop("mount_path")

        volume_name = d.pop("volume_name")

        read_only = d.pop("read_only", UNSET)

        def _parse_sub_path(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        sub_path = _parse_sub_path(d.pop("sub_path", UNSET))

        modal_volume_mount = cls(
            mount_path=mount_path,
            volume_name=volume_name,
            read_only=read_only,
            sub_path=sub_path,
        )

        return modal_volume_mount
