from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.entry_view import EntryView
    from ..models.run_view import RunView
    from ..models.thread_view import ThreadView


T = TypeVar("T", bound="Submitted")


@_attrs_define(repr=False)
class Submitted:
    """A submission receipt: the entry and, when the thread was idle, the run it started.

    Attributes:
        entry (EntryView):
        run (None | RunView):
        thread (ThreadView):
    """

    entry: EntryView
    run: RunView | None
    thread: ThreadView
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.run_view import RunView

        entry = self.entry.to_dict()

        run: dict[str, Any] | None
        if isinstance(self.run, RunView):
            run = self.run.to_dict()
        else:
            run = self.run

        thread = self.thread.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entry": entry,
                "run": run,
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
        entry = EntryView.from_dict(d.pop("entry"))

        def _parse_run(data: object) -> RunView | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                run_type_0 = RunView.from_dict(data)

                return run_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(RunView | None, data)

        run = _parse_run(d.pop("run"))

        thread = ThreadView.from_dict(d.pop("thread"))

        submitted = cls(
            entry=entry,
            run=run,
            thread=thread,
        )

        submitted.additional_properties = d
        return submitted

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
