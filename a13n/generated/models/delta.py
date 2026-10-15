from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.delta_event import DeltaEvent
    from ..models.item_ref import ItemRef


T = TypeVar("T", bound="Delta")


@_attrs_define(repr=False)
class Delta:
    """One raw AG-UI event, sequenced by the producer and correlated to its display item.

    Attributes:
        attempt (int):
        event (DeltaEvent):
        item (ItemRef | None):
        run_id (str):
        sequence (int):
        thread_id (str):
    """

    attempt: int
    event: DeltaEvent
    item: ItemRef | None
    run_id: str
    sequence: int
    thread_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.item_ref import ItemRef

        attempt = self.attempt

        event = self.event.to_dict()

        item: dict[str, Any] | None
        if isinstance(self.item, ItemRef):
            item = self.item.to_dict()
        else:
            item = self.item

        run_id = self.run_id

        sequence = self.sequence

        thread_id = self.thread_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attempt": attempt,
                "event": event,
                "item": item,
                "run_id": run_id,
                "sequence": sequence,
                "thread_id": thread_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.delta_event import DeltaEvent
        from ..models.item_ref import ItemRef

        d = dict(src_dict)
        attempt = d.pop("attempt")

        event = DeltaEvent.from_dict(d.pop("event"))

        def _parse_item(data: object) -> ItemRef | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                item_type_0 = ItemRef.from_dict(data)

                return item_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ItemRef | None, data)

        item = _parse_item(d.pop("item"))

        run_id = d.pop("run_id")

        sequence = d.pop("sequence")

        thread_id = d.pop("thread_id")

        delta = cls(
            attempt=attempt,
            event=event,
            item=item,
            run_id=run_id,
            sequence=sequence,
            thread_id=thread_id,
        )

        delta.additional_properties = d
        return delta

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
