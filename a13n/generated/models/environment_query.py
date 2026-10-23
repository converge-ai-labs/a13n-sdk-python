from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.environment_query_history import EnvironmentQueryHistory
from ..models.environment_query_metric_type_0 import EnvironmentQueryMetricType0
from ..models.environment_query_metric_type_1 import EnvironmentQueryMetricType1
from ..types import UNSET, Unset

T = TypeVar("T", bound="EnvironmentQuery")


@_attrs_define(repr=False)
class EnvironmentQuery:
    """
    Attributes:
        end (float):
        metric (EnvironmentQueryMetricType0 | EnvironmentQueryMetricType1):
        start (float):
        step (float):
        history (EnvironmentQueryHistory | Unset):
        include_snapshot (bool | Unset):
    """

    end: float
    metric: EnvironmentQueryMetricType0 | EnvironmentQueryMetricType1
    start: float
    step: float
    history: EnvironmentQueryHistory | Unset = UNSET
    include_snapshot: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        end = self.end

        metric: str
        if isinstance(self.metric, EnvironmentQueryMetricType0):
            metric = self.metric.value
        else:
            metric = self.metric.value

        start = self.start

        step = self.step

        history: str | Unset = UNSET
        if not isinstance(self.history, Unset):
            history = self.history.value

        include_snapshot = self.include_snapshot

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "end": end,
                "metric": metric,
                "start": start,
                "step": step,
            }
        )
        if history is not UNSET:
            field_dict["history"] = history
        if include_snapshot is not UNSET:
            field_dict["include_snapshot"] = include_snapshot

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        end = d.pop("end")

        def _parse_metric(data: object) -> EnvironmentQueryMetricType0 | EnvironmentQueryMetricType1:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                metric_type_0 = EnvironmentQueryMetricType0(data)

                return metric_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, str):
                raise TypeError()
            metric_type_1 = EnvironmentQueryMetricType1(data)

            return metric_type_1

        metric = _parse_metric(d.pop("metric"))

        start = d.pop("start")

        step = d.pop("step")

        _history = d.pop("history", UNSET)
        history: EnvironmentQueryHistory | Unset
        if isinstance(_history, Unset):
            history = UNSET
        else:
            history = EnvironmentQueryHistory(_history)

        include_snapshot = d.pop("include_snapshot", UNSET)

        environment_query = cls(
            end=end,
            metric=metric,
            start=start,
            step=step,
            history=history,
            include_snapshot=include_snapshot,
        )

        return environment_query
