from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.observer_state import ObserverState


T = TypeVar("T", bound="ObserverContinuation")


@_attrs_define(repr=False)
class ObserverContinuation:
    """Native conversion cursors required to resume mid-part, without raw history.

    Attributes:
        run_id (None | str | Unset):
        state (ObserverState | Unset):
        thread_id (None | str | Unset):
    """

    run_id: str | Unset | None = UNSET
    state: ObserverState | Unset = UNSET
    thread_id: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        run_id: str | Unset | None
        if isinstance(self.run_id, Unset):
            run_id = UNSET
        else:
            run_id = self.run_id

        state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.to_dict()

        thread_id: str | Unset | None
        if isinstance(self.thread_id, Unset):
            thread_id = UNSET
        else:
            thread_id = self.thread_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if run_id is not UNSET:
            field_dict["run_id"] = run_id
        if state is not UNSET:
            field_dict["state"] = state
        if thread_id is not UNSET:
            field_dict["thread_id"] = thread_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.observer_state import ObserverState

        d = dict(src_dict)

        def _parse_run_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        run_id = _parse_run_id(d.pop("run_id", UNSET))

        _state = d.pop("state", UNSET)
        state: ObserverState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = ObserverState.from_dict(_state)

        def _parse_thread_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        thread_id = _parse_thread_id(d.pop("thread_id", UNSET))

        observer_continuation = cls(
            run_id=run_id,
            state=state,
            thread_id=thread_id,
        )

        return observer_continuation
