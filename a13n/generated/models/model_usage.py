from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelUsage")


@_attrs_define(repr=False)
class ModelUsage:
    """
    Attributes:
        cache_read_tokens (int):
        cache_write_tokens (int):
        cost (None | str):
        input_tokens (int):
        model_id (None | str):
        output_tokens (int):
        requests (int):
    """

    cache_read_tokens: int
    cache_write_tokens: int
    cost: str | None
    input_tokens: int
    model_id: str | None
    output_tokens: int
    requests: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cache_read_tokens = self.cache_read_tokens

        cache_write_tokens = self.cache_write_tokens

        cost: str | None
        cost = self.cost

        input_tokens = self.input_tokens

        model_id: str | None
        model_id = self.model_id

        output_tokens = self.output_tokens

        requests = self.requests

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cache_read_tokens": cache_read_tokens,
                "cache_write_tokens": cache_write_tokens,
                "cost": cost,
                "input_tokens": input_tokens,
                "model_id": model_id,
                "output_tokens": output_tokens,
                "requests": requests,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cache_read_tokens = d.pop("cache_read_tokens")

        cache_write_tokens = d.pop("cache_write_tokens")

        def _parse_cost(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        cost = _parse_cost(d.pop("cost"))

        input_tokens = d.pop("input_tokens")

        def _parse_model_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        model_id = _parse_model_id(d.pop("model_id"))

        output_tokens = d.pop("output_tokens")

        requests = d.pop("requests")

        model_usage = cls(
            cache_read_tokens=cache_read_tokens,
            cache_write_tokens=cache_write_tokens,
            cost=cost,
            input_tokens=input_tokens,
            model_id=model_id,
            output_tokens=output_tokens,
            requests=requests,
        )

        model_usage.additional_properties = d
        return model_usage

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
