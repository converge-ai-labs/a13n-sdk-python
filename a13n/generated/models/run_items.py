from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.item import Item
    from ..models.run_view import RunView


T = TypeVar("T", bound="RunItems")


@_attrs_define(repr=False)
class RunItems:
    """A run's committed display with the run it describes. Live output continues after `position`.

    Attributes:
        complete (bool):
        dropped (int):
        items (list[Item]):
        position (None | str):
        run (RunView):
    """

    complete: bool
    dropped: int
    items: list[Item]
    position: str | None
    run: RunView
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        complete = self.complete

        dropped = self.dropped

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        position: str | None
        position = self.position

        run = self.run.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "complete": complete,
                "dropped": dropped,
                "items": items,
                "position": position,
                "run": run,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.item import Item
        from ..models.run_view import RunView

        d = dict(src_dict)
        complete = d.pop("complete")

        dropped = d.pop("dropped")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = Item.from_dict(items_item_data)

            items.append(items_item)

        def _parse_position(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        position = _parse_position(d.pop("position"))

        run = RunView.from_dict(d.pop("run"))

        run_items = cls(
            complete=complete,
            dropped=dropped,
            items=items,
            position=position,
            run=run,
        )

        run_items.additional_properties = d
        return run_items

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
