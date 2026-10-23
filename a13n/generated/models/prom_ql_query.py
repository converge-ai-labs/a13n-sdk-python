from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PromQLQuery")


@_attrs_define(repr=False)
class PromQLQuery:
    """
    Attributes:
        expression (str):
        source_id (str):
        kind (Literal['promql'] | Unset):
    """

    expression: str
    source_id: str
    kind: Literal["promql"] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        expression = self.expression

        source_id = self.source_id

        kind = self.kind

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "expression": expression,
                "source_id": source_id,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expression = d.pop("expression")

        source_id = d.pop("source_id")

        kind = cast(Literal["promql"] | Unset, d.pop("kind", UNSET))
        if kind != "promql" and not isinstance(kind, Unset):
            raise ValueError(f"kind must match const 'promql', got '{kind}'")

        prom_ql_query = cls(
            expression=expression,
            source_id=source_id,
            kind=kind,
        )

        return prom_ql_query
