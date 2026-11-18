from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SelectedTrace")


@_attrs_define(repr=False)
class SelectedTrace:
    """
    Attributes:
        run_id (str):
        trace_id (str):
        session_id (None | str | Unset):
    """

    run_id: str
    trace_id: str
    session_id: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        run_id = self.run_id

        trace_id = self.trace_id

        session_id: str | Unset | None
        if isinstance(self.session_id, Unset):
            session_id = UNSET
        else:
            session_id = self.session_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "run_id": run_id,
                "trace_id": trace_id,
            }
        )
        if session_id is not UNSET:
            field_dict["session_id"] = session_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        run_id = d.pop("run_id")

        trace_id = d.pop("trace_id")

        def _parse_session_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        session_id = _parse_session_id(d.pop("session_id", UNSET))

        selected_trace = cls(
            run_id=run_id,
            trace_id=trace_id,
            session_id=session_id,
        )

        return selected_trace
