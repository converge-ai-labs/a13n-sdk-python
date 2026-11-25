from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.daytona_volume_mount import DaytonaVolumeMount
    from ..models.recipe_overrides_volume_mounts import RecipeOverridesVolumeMounts


T = TypeVar("T", bound="RecipeOverrides")


@_attrs_define(repr=False)
class RecipeOverrides:
    """
    Attributes:
        volume_mounts (RecipeOverridesVolumeMounts | Unset):
        volumes (list[DaytonaVolumeMount] | Unset):
    """

    volume_mounts: RecipeOverridesVolumeMounts | Unset = UNSET
    volumes: list[DaytonaVolumeMount] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        volume_mounts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.volume_mounts, Unset):
            volume_mounts = self.volume_mounts.to_dict()

        volumes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.volumes, Unset):
            volumes = []
            for volumes_item_data in self.volumes:
                volumes_item = volumes_item_data.to_dict()
                volumes.append(volumes_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if volume_mounts is not UNSET:
            field_dict["volume_mounts"] = volume_mounts
        if volumes is not UNSET:
            field_dict["volumes"] = volumes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.daytona_volume_mount import DaytonaVolumeMount
        from ..models.recipe_overrides_volume_mounts import RecipeOverridesVolumeMounts

        d = dict(src_dict)
        _volume_mounts = d.pop("volume_mounts", UNSET)
        volume_mounts: RecipeOverridesVolumeMounts | Unset
        if isinstance(_volume_mounts, Unset):
            volume_mounts = UNSET
        else:
            volume_mounts = RecipeOverridesVolumeMounts.from_dict(_volume_mounts)

        _volumes = d.pop("volumes", UNSET)
        volumes: list[DaytonaVolumeMount] | Unset = UNSET
        if _volumes is not UNSET:
            volumes = []
            for volumes_item_data in _volumes:
                volumes_item = DaytonaVolumeMount.from_dict(volumes_item_data)

                volumes.append(volumes_item)

        recipe_overrides = cls(
            volume_mounts=volume_mounts,
            volumes=volumes,
        )

        return recipe_overrides
