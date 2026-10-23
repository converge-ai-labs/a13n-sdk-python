from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="InstantQuery")


@_attrs_define(repr=False)
class InstantQuery:
    """
    Attributes:
        expression (str):
        kind (Literal['instant'] | Unset):
        time (float | None | Unset):
    """

    expression: str
    kind: Literal["instant"] | Unset = UNSET
    time: float | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        expression = self.expression

        kind = self.kind

        time: float | Unset | None
        if isinstance(self.time, Unset):
            time = UNSET
        else:
            time = self.time

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "expression": expression,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expression = d.pop("expression")

        kind = cast(Literal["instant"] | Unset, d.pop("kind", UNSET))
        if kind != "instant" and not isinstance(kind, Unset):
            raise ValueError(f"kind must match const 'instant', got '{kind}'")

        def _parse_time(data: object) -> float | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | Unset | None, data)

        time = _parse_time(d.pop("time", UNSET))

        instant_query = cls(
            expression=expression,
            kind=kind,
            time=time,
        )

        return instant_query
