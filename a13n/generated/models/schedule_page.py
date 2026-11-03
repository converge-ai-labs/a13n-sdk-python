from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schedule import Schedule
    from ..models.unavailable_configuration import UnavailableConfiguration


T = TypeVar("T", bound="SchedulePage")


@_attrs_define(repr=False)
class SchedulePage:
    """
    Attributes:
        items (list[Schedule]):
        next_cursor (None | str | Unset):
        unavailable (list[UnavailableConfiguration] | Unset):
    """

    items: list[Schedule]
    next_cursor: str | Unset | None = UNSET
    unavailable: list[UnavailableConfiguration] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        next_cursor: str | Unset | None
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor

        unavailable: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.unavailable, Unset):
            unavailable = []
            for unavailable_item_data in self.unavailable:
                unavailable_item = unavailable_item_data.to_dict()
                unavailable.append(unavailable_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "items": items,
            }
        )
        if next_cursor is not UNSET:
            field_dict["next_cursor"] = next_cursor
        if unavailable is not UNSET:
            field_dict["unavailable"] = unavailable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schedule import Schedule
        from ..models.unavailable_configuration import UnavailableConfiguration

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = Schedule.from_dict(items_item_data)

            items.append(items_item)

        def _parse_next_cursor(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor", UNSET))

        _unavailable = d.pop("unavailable", UNSET)
        unavailable: list[UnavailableConfiguration] | Unset = UNSET
        if _unavailable is not UNSET:
            unavailable = []
            for unavailable_item_data in _unavailable:
                unavailable_item = UnavailableConfiguration.from_dict(unavailable_item_data)

                unavailable.append(unavailable_item)

        schedule_page = cls(
            items=items,
            next_cursor=next_cursor,
            unavailable=unavailable,
        )

        return schedule_page
