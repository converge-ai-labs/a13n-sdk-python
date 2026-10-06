from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.display_continuation import DisplayContinuation
    from ..models.item import Item
    from ..models.run_view import RunView


T = TypeVar("T", bound="RunItems")


@_attrs_define(repr=False)
class RunItems:
    """Items of a run's committed display, in ordinal order, with the run they describe. Ordinals are dense from 1,
    so the first item's ordinal tells whether earlier ones exist. Live output continues after `position`.

        Attributes:
            baseline (bool):
            complete (bool):
            items (list[Item]):
            position (None | str):
            run (RunView):
            continuation (DisplayContinuation | None | Unset):
            resume_after (None | str | Unset):
    """

    baseline: bool
    complete: bool
    items: list[Item]
    position: str | None
    run: RunView
    continuation: DisplayContinuation | Unset | None = UNSET
    resume_after: str | Unset | None = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.display_continuation import DisplayContinuation

        baseline = self.baseline

        complete = self.complete

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        position: str | None
        position = self.position

        run = self.run.to_dict()

        continuation: dict[str, Any] | Unset | None
        if isinstance(self.continuation, Unset):
            continuation = UNSET
        elif isinstance(self.continuation, DisplayContinuation):
            continuation = self.continuation.to_dict()
        else:
            continuation = self.continuation

        resume_after: str | Unset | None
        if isinstance(self.resume_after, Unset):
            resume_after = UNSET
        else:
            resume_after = self.resume_after

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "baseline": baseline,
                "complete": complete,
                "items": items,
                "position": position,
                "run": run,
            }
        )
        if continuation is not UNSET:
            field_dict["continuation"] = continuation
        if resume_after is not UNSET:
            field_dict["resume_after"] = resume_after

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.display_continuation import DisplayContinuation
        from ..models.item import Item
        from ..models.run_view import RunView

        d = dict(src_dict)
        baseline = d.pop("baseline")

        complete = d.pop("complete")

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

        def _parse_continuation(data: object) -> DisplayContinuation | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                continuation_type_0 = DisplayContinuation.from_dict(data)

                return continuation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DisplayContinuation | Unset | None, data)

        continuation = _parse_continuation(d.pop("continuation", UNSET))

        def _parse_resume_after(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        resume_after = _parse_resume_after(d.pop("resume_after", UNSET))

        run_items = cls(
            baseline=baseline,
            complete=complete,
            items=items,
            position=position,
            run=run,
            continuation=continuation,
            resume_after=resume_after,
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
