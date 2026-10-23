from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RangeQuery")


@_attrs_define(repr=False)
class RangeQuery:
    """
    Attributes:
        end (float):
        expression (str):
        start (float):
        step (float):
        kind (Literal['range'] | Unset):
    """

    end: float
    expression: str
    start: float
    step: float
    kind: Literal["range"] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        end = self.end

        expression = self.expression

        start = self.start

        step = self.step

        kind = self.kind

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "end": end,
                "expression": expression,
                "start": start,
                "step": step,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        end = d.pop("end")

        expression = d.pop("expression")

        start = d.pop("start")

        step = d.pop("step")

        kind = cast(Literal["range"] | Unset, d.pop("kind", UNSET))
        if kind != "range" and not isinstance(kind, Unset):
            raise ValueError(f"kind must match const 'range', got '{kind}'")

        range_query = cls(
            end=end,
            expression=expression,
            start=start,
            step=step,
            kind=kind,
        )

        return range_query
