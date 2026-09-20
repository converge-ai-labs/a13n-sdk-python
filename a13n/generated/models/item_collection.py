from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_resource import ItemResource


T = TypeVar("T", bound="ItemCollection")


@_attrs_define(repr=False)
class ItemCollection:
    """
    Attributes:
        complete (bool):
        finalized (bool):
        incomplete_reason (None | str):
        items (list[ItemResource]):
        next_cursor (None | str):
        projection_cursor (None | str):
        snapshot_version (int):
        recovery_exhausted (bool | Unset):
    """

    complete: bool
    finalized: bool
    incomplete_reason: str | None
    items: list[ItemResource]
    next_cursor: str | None
    projection_cursor: str | None
    snapshot_version: int
    recovery_exhausted: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        complete = self.complete

        finalized = self.finalized

        incomplete_reason: str | None
        incomplete_reason = self.incomplete_reason

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        next_cursor: str | None
        next_cursor = self.next_cursor

        projection_cursor: str | None
        projection_cursor = self.projection_cursor

        snapshot_version = self.snapshot_version

        recovery_exhausted = self.recovery_exhausted

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "complete": complete,
                "finalized": finalized,
                "incomplete_reason": incomplete_reason,
                "items": items,
                "next_cursor": next_cursor,
                "projection_cursor": projection_cursor,
                "snapshot_version": snapshot_version,
            }
        )
        if recovery_exhausted is not UNSET:
            field_dict["recovery_exhausted"] = recovery_exhausted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.item_resource import ItemResource

        d = dict(src_dict)
        complete = d.pop("complete")

        finalized = d.pop("finalized")

        def _parse_incomplete_reason(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        incomplete_reason = _parse_incomplete_reason(d.pop("incomplete_reason"))

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = ItemResource.from_dict(items_item_data)

            items.append(items_item)

        def _parse_next_cursor(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor"))

        def _parse_projection_cursor(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        projection_cursor = _parse_projection_cursor(d.pop("projection_cursor"))

        snapshot_version = d.pop("snapshot_version")

        recovery_exhausted = d.pop("recovery_exhausted", UNSET)

        item_collection = cls(
            complete=complete,
            finalized=finalized,
            incomplete_reason=incomplete_reason,
            items=items,
            next_cursor=next_cursor,
            projection_cursor=projection_cursor,
            snapshot_version=snapshot_version,
            recovery_exhausted=recovery_exhausted,
        )

        return item_collection
