from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.entry_view import EntryView
    from ..models.run_view import RunView
    from ..models.thread_view import ThreadView


T = TypeVar("T", bound="ThreadState")


@_attrs_define(repr=False)
class ThreadState:
    """A thread's current state: the thread, the runs its pointers name and its open inbox entries.

    Attributes:
        current_run (None | RunView):
        entries (list[EntryView]):
        last_run (None | RunView):
        thread (ThreadView):
    """

    current_run: RunView | None
    entries: list[EntryView]
    last_run: RunView | None
    thread: ThreadView
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.run_view import RunView

        current_run: dict[str, Any] | None
        if isinstance(self.current_run, RunView):
            current_run = self.current_run.to_dict()
        else:
            current_run = self.current_run

        entries = []
        for entries_item_data in self.entries:
            entries_item = entries_item_data.to_dict()
            entries.append(entries_item)

        last_run: dict[str, Any] | None
        if isinstance(self.last_run, RunView):
            last_run = self.last_run.to_dict()
        else:
            last_run = self.last_run

        thread = self.thread.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "current_run": current_run,
                "entries": entries,
                "last_run": last_run,
                "thread": thread,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entry_view import EntryView
        from ..models.run_view import RunView
        from ..models.thread_view import ThreadView

        d = dict(src_dict)

        def _parse_current_run(data: object) -> RunView | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                current_run_type_0 = RunView.from_dict(data)

                return current_run_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(RunView | None, data)

        current_run = _parse_current_run(d.pop("current_run"))

        entries = []
        _entries = d.pop("entries")
        for entries_item_data in _entries:
            entries_item = EntryView.from_dict(entries_item_data)

            entries.append(entries_item)

        def _parse_last_run(data: object) -> RunView | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_run_type_0 = RunView.from_dict(data)

                return last_run_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(RunView | None, data)

        last_run = _parse_last_run(d.pop("last_run"))

        thread = ThreadView.from_dict(d.pop("thread"))

        thread_state = cls(
            current_run=current_run,
            entries=entries,
            last_run=last_run,
            thread=thread,
        )

        thread_state.additional_properties = d
        return thread_state

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
