from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelMetrics")


@_attrs_define(repr=False)
class ModelMetrics:
    """
    Attributes:
        cache_hit_rate (float | None):
        cache_read_tokens (int):
        cost (None | str):
        input_tokens (int):
        output_tokens (int):
        requests (int):
        unpriced_requests (int):
    """

    cache_hit_rate: float | None
    cache_read_tokens: int
    cost: str | None
    input_tokens: int
    output_tokens: int
    requests: int
    unpriced_requests: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cache_hit_rate: float | None
        cache_hit_rate = self.cache_hit_rate

        cache_read_tokens = self.cache_read_tokens

        cost: str | None
        cost = self.cost

        input_tokens = self.input_tokens

        output_tokens = self.output_tokens

        requests = self.requests

        unpriced_requests = self.unpriced_requests

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cache_hit_rate": cache_hit_rate,
                "cache_read_tokens": cache_read_tokens,
                "cost": cost,
                "input_tokens": input_tokens,
                "output_tokens": output_tokens,
                "requests": requests,
                "unpriced_requests": unpriced_requests,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_cache_hit_rate(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        cache_hit_rate = _parse_cache_hit_rate(d.pop("cache_hit_rate"))

        cache_read_tokens = d.pop("cache_read_tokens")

        def _parse_cost(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        cost = _parse_cost(d.pop("cost"))

        input_tokens = d.pop("input_tokens")

        output_tokens = d.pop("output_tokens")

        requests = d.pop("requests")

        unpriced_requests = d.pop("unpriced_requests")

        model_metrics = cls(
            cache_hit_rate=cache_hit_rate,
            cache_read_tokens=cache_read_tokens,
            cost=cost,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            requests=requests,
            unpriced_requests=unpriced_requests,
        )

        model_metrics.additional_properties = d
        return model_metrics

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
