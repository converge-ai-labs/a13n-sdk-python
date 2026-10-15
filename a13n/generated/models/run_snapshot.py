from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.display_continuation import DisplayContinuation
    from ..models.item import Item


T = TypeVar("T", bound="RunSnapshot")


@_attrs_define(repr=False)
class RunSnapshot:
    """A run's committed items from ordinal `first` on. The receiver deletes the items it holds from `first` on and
    inserts these; earlier items are final. `complete` marks the run's final display.

        Attributes:
            complete (bool):
            continuation (DisplayContinuation | None):
            first (int):
            items (list[Item]):
            run_id (str):
            thread_id (str):
    """

    complete: bool
    continuation: DisplayContinuation | None
    first: int
    items: list[Item]
    run_id: str
    thread_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.display_continuation import DisplayContinuation

        complete = self.complete

        continuation: dict[str, Any] | None
        if isinstance(self.continuation, DisplayContinuation):
            continuation = self.continuation.to_dict()
        else:
            continuation = self.continuation

        first = self.first

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        run_id = self.run_id

        thread_id = self.thread_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "complete": complete,
                "continuation": continuation,
                "first": first,
                "items": items,
                "run_id": run_id,
                "thread_id": thread_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.display_continuation import DisplayContinuation
        from ..models.item import Item

        d = dict(src_dict)
        complete = d.pop("complete")

        def _parse_continuation(data: object) -> DisplayContinuation | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                continuation_type_0 = DisplayContinuation.from_dict(data)

                return continuation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DisplayContinuation | None, data)

        continuation = _parse_continuation(d.pop("continuation"))

        first = d.pop("first")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = Item.from_dict(items_item_data)

            items.append(items_item)

        run_id = d.pop("run_id")

        thread_id = d.pop("thread_id")

        run_snapshot = cls(
            complete=complete,
            continuation=continuation,
            first=first,
            items=items,
            run_id=run_id,
            thread_id=thread_id,
        )

        run_snapshot.additional_properties = d
        return run_snapshot

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
