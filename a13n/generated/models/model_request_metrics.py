from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelRequestMetrics")


@_attrs_define(repr=False)
class ModelRequestMetrics:
    """Derived from the current model contribution.

    Attributes:
        output_tokens_per_second (float | None):
        request_duration_seconds (float | None):
        time_to_first_chunk_seconds (float | None):
    """

    output_tokens_per_second: float | None
    request_duration_seconds: float | None
    time_to_first_chunk_seconds: float | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        output_tokens_per_second: float | None
        output_tokens_per_second = self.output_tokens_per_second

        request_duration_seconds: float | None
        request_duration_seconds = self.request_duration_seconds

        time_to_first_chunk_seconds: float | None
        time_to_first_chunk_seconds = self.time_to_first_chunk_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "output_tokens_per_second": output_tokens_per_second,
                "request_duration_seconds": request_duration_seconds,
                "time_to_first_chunk_seconds": time_to_first_chunk_seconds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_output_tokens_per_second(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        output_tokens_per_second = _parse_output_tokens_per_second(d.pop("output_tokens_per_second"))

        def _parse_request_duration_seconds(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        request_duration_seconds = _parse_request_duration_seconds(d.pop("request_duration_seconds"))

        def _parse_time_to_first_chunk_seconds(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        time_to_first_chunk_seconds = _parse_time_to_first_chunk_seconds(d.pop("time_to_first_chunk_seconds"))

        model_request_metrics = cls(
            output_tokens_per_second=output_tokens_per_second,
            request_duration_seconds=request_duration_seconds,
            time_to_first_chunk_seconds=time_to_first_chunk_seconds,
        )

        model_request_metrics.additional_properties = d
        return model_request_metrics

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
