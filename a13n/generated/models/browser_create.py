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
        delete_after_seconds (int | None | Unset):
        idle_seconds (int | None | Unset):
        prepare (bool | Unset):
        recipe (BrowserCreateRecipe | Unset):
        stop_after_seconds (int | None | Unset):
    """

    name: str
    provider_id: str
    delete_after_seconds: int | Unset | None = UNSET
    idle_seconds: int | Unset | None = UNSET
    prepare: bool | Unset = UNSET
    recipe: BrowserCreateRecipe | Unset = UNSET
    stop_after_seconds: int | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        provider_id = self.provider_id

        delete_after_seconds: int | Unset | None
        if isinstance(self.delete_after_seconds, Unset):
            delete_after_seconds = UNSET
        else:
            delete_after_seconds = self.delete_after_seconds

        idle_seconds: int | Unset | None
        if isinstance(self.idle_seconds, Unset):
            idle_seconds = UNSET
        else:
            idle_seconds = self.idle_seconds

        prepare = self.prepare

        recipe: dict[str, Any] | Unset = UNSET
        if not isinstance(self.recipe, Unset):
            recipe = self.recipe.to_dict()

        stop_after_seconds: int | Unset | None
        if isinstance(self.stop_after_seconds, Unset):
            stop_after_seconds = UNSET
        else:
            stop_after_seconds = self.stop_after_seconds

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "provider_id": provider_id,
            }
        )
        if delete_after_seconds is not UNSET:
            field_dict["delete_after_seconds"] = delete_after_seconds
        if idle_seconds is not UNSET:
            field_dict["idle_seconds"] = idle_seconds
        if prepare is not UNSET:
            field_dict["prepare"] = prepare
        if recipe is not UNSET:
            field_dict["recipe"] = recipe
        if stop_after_seconds is not UNSET:
            field_dict["stop_after_seconds"] = stop_after_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.browser_create_recipe import BrowserCreateRecipe

        d = dict(src_dict)
        name = d.pop("name")

        provider_id = d.pop("provider_id")

        def _parse_delete_after_seconds(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        delete_after_seconds = _parse_delete_after_seconds(d.pop("delete_after_seconds", UNSET))

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

        def _parse_stop_after_seconds(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        stop_after_seconds = _parse_stop_after_seconds(d.pop("stop_after_seconds", UNSET))

        browser_create = cls(
            name=name,
            provider_id=provider_id,
            delete_after_seconds=delete_after_seconds,
            idle_seconds=idle_seconds,
            prepare=prepare,
            recipe=recipe,
            stop_after_seconds=stop_after_seconds,
        )

        return browser_create
