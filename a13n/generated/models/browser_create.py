from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.browser_create_recipe import BrowserCreateRecipe


T = TypeVar("T", bound="BrowserCreate")


@_attrs_define(repr=False)
class BrowserCreate:
    """
    Attributes:
        name (str):
        provider_id (str):
        idle_seconds (int | None | Unset):
        prepare (bool | Unset):
        recipe (BrowserCreateRecipe | Unset):
    """

    name: str
    provider_id: str
    idle_seconds: int | Unset | None = UNSET
    prepare: bool | Unset = UNSET
    recipe: BrowserCreateRecipe | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        provider_id = self.provider_id

        idle_seconds: int | Unset | None
        if isinstance(self.idle_seconds, Unset):
            idle_seconds = UNSET
        else:
            idle_seconds = self.idle_seconds

        prepare = self.prepare

        recipe: dict[str, Any] | Unset = UNSET
        if not isinstance(self.recipe, Unset):
            recipe = self.recipe.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "provider_id": provider_id,
            }
        )
        if idle_seconds is not UNSET:
            field_dict["idle_seconds"] = idle_seconds
        if prepare is not UNSET:
            field_dict["prepare"] = prepare
        if recipe is not UNSET:
            field_dict["recipe"] = recipe

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.browser_create_recipe import BrowserCreateRecipe

        d = dict(src_dict)
        name = d.pop("name")

        provider_id = d.pop("provider_id")

        def _parse_idle_seconds(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        idle_seconds = _parse_idle_seconds(d.pop("idle_seconds", UNSET))

        prepare = d.pop("prepare", UNSET)

        _recipe = d.pop("recipe", UNSET)
        recipe: BrowserCreateRecipe | Unset
        if isinstance(_recipe, Unset):
            recipe = UNSET
        else:
            recipe = BrowserCreateRecipe.from_dict(_recipe)

        browser_create = cls(
            name=name,
            provider_id=provider_id,
            idle_seconds=idle_seconds,
            prepare=prepare,
            recipe=recipe,
        )

        return browser_create
