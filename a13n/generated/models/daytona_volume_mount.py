from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DaytonaVolumeMount")


@_attrs_define(repr=False)
class DaytonaVolumeMount:
    """
    Attributes:
        mount_path (str):
        volume_id (str):
        subpath (None | str | Unset):
    """

    mount_path: str
    volume_id: str
    subpath: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        mount_path = self.mount_path

        volume_id = self.volume_id

        subpath: str | Unset | None
        if isinstance(self.subpath, Unset):
            subpath = UNSET
        else:
            subpath = self.subpath

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "mount_path": mount_path,
                "volume_id": volume_id,
            }
        )
        if subpath is not UNSET:
            field_dict["subpath"] = subpath

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mount_path = d.pop("mount_path")

        volume_id = d.pop("volume_id")

        def _parse_subpath(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        subpath = _parse_subpath(d.pop("subpath", UNSET))

        daytona_volume_mount = cls(
            mount_path=mount_path,
            volume_id=volume_id,
            subpath=subpath,
        )

        return daytona_volume_mount
