from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..._validation import validate_model

T = TypeVar("T", bound="ContextUsage")


@_attrs_define(repr=False)
class ContextUsage:
    """One reported generation, compared with its currently configured window.

    Attributes:
        context_window_tokens (int | None):
        input_tokens (int | None):
        output_tokens (int | None):
        record_id (str):
        run_id (str):
    """

    context_window_tokens: int | None
    input_tokens: int | None
    output_tokens: int | None
    record_id: str
    run_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        context_window_tokens: int | None
        context_window_tokens = self.context_window_tokens

        input_tokens: int | None
        input_tokens = self.input_tokens

        output_tokens: int | None
        output_tokens = self.output_tokens

        record_id = self.record_id

        run_id = self.run_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "context_window_tokens": context_window_tokens,
                "input_tokens": input_tokens,
                "output_tokens": output_tokens,
                "record_id": record_id,
                "run_id": run_id,
            }
        )

        validate_model("ContextUsage", field_dict)
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        validate_model("ContextUsage", src_dict)
        d = dict(src_dict)

        def _parse_context_window_tokens(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        context_window_tokens = _parse_context_window_tokens(d.pop("context_window_tokens"))

        def _parse_input_tokens(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        input_tokens = _parse_input_tokens(d.pop("input_tokens"))

        def _parse_output_tokens(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        output_tokens = _parse_output_tokens(d.pop("output_tokens"))

        record_id = d.pop("record_id")

        run_id = d.pop("run_id")

        context_usage = cls(
            context_window_tokens=context_window_tokens,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            record_id=record_id,
            run_id=run_id,
        )

        context_usage.additional_properties = d
        return context_usage

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
