from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.recipe_overrides_volume_mounts import RecipeOverridesVolumeMounts


T = TypeVar("T", bound="RecipeOverrides")


@_attrs_define(repr=False)
class RecipeOverrides:
    """
    Attributes:
        volume_mounts (RecipeOverridesVolumeMounts | Unset):
    """

    volume_mounts: RecipeOverridesVolumeMounts | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        volume_mounts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.volume_mounts, Unset):
            volume_mounts = self.volume_mounts.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if volume_mounts is not UNSET:
            field_dict["volume_mounts"] = volume_mounts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.recipe_overrides_volume_mounts import RecipeOverridesVolumeMounts

        d = dict(src_dict)
        _volume_mounts = d.pop("volume_mounts", UNSET)
        volume_mounts: RecipeOverridesVolumeMounts | Unset
        if isinstance(_volume_mounts, Unset):
            volume_mounts = UNSET
        else:
            volume_mounts = RecipeOverridesVolumeMounts.from_dict(_volume_mounts)

        recipe_overrides = cls(
            volume_mounts=volume_mounts,
        )

        return recipe_overrides
