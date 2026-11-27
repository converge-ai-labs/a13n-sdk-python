from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.boxd_volume_mount import BoxdVolumeMount
    from ..models.daytona_volume_mount import DaytonaVolumeMount
    from ..models.modal_volume_mount import ModalVolumeMount
    from ..models.recipe_overrides_volume_mounts import RecipeOverridesVolumeMounts


T = TypeVar("T", bound="RecipeOverrides")


@_attrs_define(repr=False)
class RecipeOverrides:
    """
    Attributes:
        volume_mounts (RecipeOverridesVolumeMounts | Unset):
        volumes (list[BoxdVolumeMount] | list[DaytonaVolumeMount] | list[ModalVolumeMount] | Unset):
    """

    volume_mounts: RecipeOverridesVolumeMounts | Unset = UNSET
    volumes: list[BoxdVolumeMount] | list[DaytonaVolumeMount] | list[ModalVolumeMount] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        volume_mounts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.volume_mounts, Unset):
            volume_mounts = self.volume_mounts.to_dict()

        volumes: list[dict[str, Any]] | Unset
        if isinstance(self.volumes, Unset):
            volumes = UNSET
        else:
            volumes = []
            for volumes_type_0_item_data in self.volumes:
                volumes_type_0_item = volumes_type_0_item_data.to_dict()
                volumes.append(volumes_type_0_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if volume_mounts is not UNSET:
            field_dict["volume_mounts"] = volume_mounts
        if volumes is not UNSET:
            field_dict["volumes"] = volumes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.boxd_volume_mount import BoxdVolumeMount
        from ..models.daytona_volume_mount import DaytonaVolumeMount
        from ..models.modal_volume_mount import ModalVolumeMount
        from ..models.recipe_overrides_volume_mounts import RecipeOverridesVolumeMounts

        d = dict(src_dict)
        _volume_mounts = d.pop("volume_mounts", UNSET)
        volume_mounts: RecipeOverridesVolumeMounts | Unset
        if isinstance(_volume_mounts, Unset):
            volume_mounts = UNSET
        else:
            volume_mounts = RecipeOverridesVolumeMounts.from_dict(_volume_mounts)

        def _parse_volumes(
            data: object,
        ) -> list[BoxdVolumeMount] | list[DaytonaVolumeMount] | list[ModalVolumeMount] | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                volumes_type_0 = []
                _volumes_type_0 = data
                for volumes_type_0_item_data in _volumes_type_0:
                    volumes_type_0_item = DaytonaVolumeMount.from_dict(volumes_type_0_item_data)

                    volumes_type_0.append(volumes_type_0_item)

                return volumes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                volumes_type_1 = []
                _volumes_type_1 = data
                for volumes_type_1_item_data in _volumes_type_1:
                    volumes_type_1_item = ModalVolumeMount.from_dict(volumes_type_1_item_data)

                    volumes_type_1.append(volumes_type_1_item)

                return volumes_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, list):
                raise TypeError()
            volumes_type_2 = []
            _volumes_type_2 = data
            for volumes_type_2_item_data in _volumes_type_2:
                volumes_type_2_item = BoxdVolumeMount.from_dict(volumes_type_2_item_data)

                volumes_type_2.append(volumes_type_2_item)

            return volumes_type_2

        volumes = _parse_volumes(d.pop("volumes", UNSET))

        recipe_overrides = cls(
            volume_mounts=volume_mounts,
            volumes=volumes,
        )

        return recipe_overrides
