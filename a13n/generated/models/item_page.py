from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.item_page_view import ItemPageView
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item import Item
    from ..models.item_summary import ItemSummary
    from ..models.run_summary import RunSummary


T = TypeVar("T", bound="ItemPage")


@_attrs_define(repr=False)
class ItemPage:
    """
    Attributes:
        complete (bool):
        items (list[Item | ItemSummary]):
        run (RunSummary):
        view (ItemPageView):
        next_after (int | None | Unset):
        next_before (int | None | Unset):
    """

    complete: bool
    items: list[Item | ItemSummary]
    run: RunSummary
    view: ItemPageView
    next_after: int | Unset | None = UNSET
    next_before: int | Unset | None = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.item_summary import ItemSummary

        complete = self.complete

        items = []
        for items_item_data in self.items:
            items_item: dict[str, Any]
            if isinstance(items_item_data, ItemSummary):
                items_item = items_item_data.to_dict()
            else:
                items_item = items_item_data.to_dict()

            items.append(items_item)

        run = self.run.to_dict()

        view = self.view.value

        next_after: int | Unset | None
        if isinstance(self.next_after, Unset):
            next_after = UNSET
        else:
            next_after = self.next_after

        next_before: int | Unset | None
        if isinstance(self.next_before, Unset):
            next_before = UNSET
        else:
            next_before = self.next_before

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "complete": complete,
                "items": items,
                "run": run,
                "view": view,
            }
        )
        if next_after is not UNSET:
            field_dict["next_after"] = next_after
        if next_before is not UNSET:
            field_dict["next_before"] = next_before

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.item import Item
        from ..models.item_summary import ItemSummary
        from ..models.run_summary import RunSummary

        d = dict(src_dict)
        complete = d.pop("complete")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:

            def _parse_items_item(data: object) -> Item | ItemSummary:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    items_item_type_0 = ItemSummary.from_dict(data)

                    return items_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                items_item_type_1 = Item.from_dict(data)

                return items_item_type_1

            items_item = _parse_items_item(items_item_data)

            items.append(items_item)

        run = RunSummary.from_dict(d.pop("run"))

        view = ItemPageView(d.pop("view"))

        def _parse_next_after(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        next_after = _parse_next_after(d.pop("next_after", UNSET))

        def _parse_next_before(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        next_before = _parse_next_before(d.pop("next_before", UNSET))

        item_page = cls(
            complete=complete,
            items=items,
            run=run,
            view=view,
            next_after=next_after,
            next_before=next_before,
        )

        item_page.additional_properties = d
        return item_page

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
