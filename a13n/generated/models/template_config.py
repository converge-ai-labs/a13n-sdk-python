from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.template_config_recipe import TemplateConfigRecipe


T = TypeVar("T", bound="TemplateConfig")


@_attrs_define(repr=False)
class TemplateConfig:
    """
    Attributes:
        delete_after_seconds (int | None | Unset):
        recipe (TemplateConfigRecipe | Unset):
        stop_after_seconds (int | None | Unset):
    """

    delete_after_seconds: int | Unset | None = UNSET
    recipe: TemplateConfigRecipe | Unset = UNSET
    stop_after_seconds: int | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        delete_after_seconds: int | Unset | None
        if isinstance(self.delete_after_seconds, Unset):
            delete_after_seconds = UNSET
        else:
            delete_after_seconds = self.delete_after_seconds

        recipe: dict[str, Any] | Unset = UNSET
        if not isinstance(self.recipe, Unset):
            recipe = self.recipe.to_dict()

        stop_after_seconds: int | Unset | None
        if isinstance(self.stop_after_seconds, Unset):
            stop_after_seconds = UNSET
        else:
            stop_after_seconds = self.stop_after_seconds

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if delete_after_seconds is not UNSET:
            field_dict["delete_after_seconds"] = delete_after_seconds
        if recipe is not UNSET:
            field_dict["recipe"] = recipe
        if stop_after_seconds is not UNSET:
            field_dict["stop_after_seconds"] = stop_after_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template_config_recipe import TemplateConfigRecipe

        d = dict(src_dict)

        def _parse_delete_after_seconds(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        delete_after_seconds = _parse_delete_after_seconds(d.pop("delete_after_seconds", UNSET))

        _recipe = d.pop("recipe", UNSET)
        recipe: TemplateConfigRecipe | Unset
        if isinstance(_recipe, Unset):
            recipe = UNSET
        else:
            recipe = TemplateConfigRecipe.from_dict(_recipe)

        def _parse_stop_after_seconds(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        stop_after_seconds = _parse_stop_after_seconds(d.pop("stop_after_seconds", UNSET))

        template_config = cls(
            delete_after_seconds=delete_after_seconds,
            recipe=recipe,
            stop_after_seconds=stop_after_seconds,
        )

        return template_config
