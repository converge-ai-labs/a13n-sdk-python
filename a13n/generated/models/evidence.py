from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Evidence")


@_attrs_define(repr=False)
class Evidence:
    """
    Attributes:
        run_id (str):
        trace_id (str):
        span_ids (list[str] | Unset):
    """

    run_id: str
    trace_id: str
    span_ids: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        run_id = self.run_id

        trace_id = self.trace_id

        span_ids: list[str] | Unset = UNSET
        if not isinstance(self.span_ids, Unset):
            span_ids = self.span_ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "run_id": run_id,
                "trace_id": trace_id,
            }
        )
        if span_ids is not UNSET:
            field_dict["span_ids"] = span_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        run_id = d.pop("run_id")

        trace_id = d.pop("trace_id")

        span_ids = cast(list[str], d.pop("span_ids", UNSET))

        evidence = cls(
            run_id=run_id,
            trace_id=trace_id,
            span_ids=span_ids,
        )

        return evidence
