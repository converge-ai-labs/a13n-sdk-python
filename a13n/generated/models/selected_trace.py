from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SelectedTrace")


@_attrs_define(repr=False)
class SelectedTrace:
    """
    Attributes:
        run_id (str):
        trace_id (str):
    """

    run_id: str
    trace_id: str

    def to_dict(self) -> dict[str, Any]:
        run_id = self.run_id

        trace_id = self.trace_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "run_id": run_id,
                "trace_id": trace_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        run_id = d.pop("run_id")

        trace_id = d.pop("trace_id")

        selected_trace = cls(
            run_id=run_id,
            trace_id=trace_id,
        )

        return selected_trace
