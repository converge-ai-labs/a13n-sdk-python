from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..models.typed_query_history import TypedQueryHistory
from ..models.typed_query_metric_type_0 import TypedQueryMetricType0
from ..models.typed_query_metric_type_1 import TypedQueryMetricType1
from ..types import UNSET, Unset

T = TypeVar("T", bound="TypedQuery")


@_attrs_define(repr=False)
class TypedQuery:
    """
    Attributes:
        metric (TypedQueryMetricType0 | TypedQueryMetricType1):
        history (TypedQueryHistory | Unset):
        kind (Literal['metric'] | Unset):
    """

    metric: TypedQueryMetricType0 | TypedQueryMetricType1
    history: TypedQueryHistory | Unset = UNSET
    kind: Literal["metric"] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        metric: str
        if isinstance(self.metric, TypedQueryMetricType0):
            metric = self.metric.value
        else:
            metric = self.metric.value

        history: str | Unset = UNSET
        if not isinstance(self.history, Unset):
            history = self.history.value

        kind = self.kind

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "metric": metric,
            }
        )
        if history is not UNSET:
            field_dict["history"] = history
        if kind is not UNSET:
            field_dict["kind"] = kind

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_metric(data: object) -> TypedQueryMetricType0 | TypedQueryMetricType1:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                metric_type_0 = TypedQueryMetricType0(data)

                return metric_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, str):
                raise TypeError()
            metric_type_1 = TypedQueryMetricType1(data)

            return metric_type_1

        metric = _parse_metric(d.pop("metric"))

        _history = d.pop("history", UNSET)
        history: TypedQueryHistory | Unset
        if isinstance(_history, Unset):
            history = UNSET
        else:
            history = TypedQueryHistory(_history)

        kind = cast(Literal["metric"] | Unset, d.pop("kind", UNSET))
        if kind != "metric" and not isinstance(kind, Unset):
            raise ValueError(f"kind must match const 'metric', got '{kind}'")

        typed_query = cls(
            metric=metric,
            history=history,
            kind=kind,
        )

        return typed_query
