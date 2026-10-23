from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OutputPreview")


@_attrs_define(repr=False)
class OutputPreview:
    """
    Attributes:
        observation_closed (bool):
        produced_bytes (int | None):
        text (str):
        truncated (bool):
    """

    observation_closed: bool
    produced_bytes: int | None
    text: str
    truncated: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        observation_closed = self.observation_closed

        produced_bytes: int | None
        produced_bytes = self.produced_bytes

        text = self.text

        truncated = self.truncated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "observation_closed": observation_closed,
                "produced_bytes": produced_bytes,
                "text": text,
                "truncated": truncated,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        observation_closed = d.pop("observation_closed")

        def _parse_produced_bytes(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        produced_bytes = _parse_produced_bytes(d.pop("produced_bytes"))

        text = d.pop("text")

        truncated = d.pop("truncated")

        output_preview = cls(
            observation_closed=observation_closed,
            produced_bytes=produced_bytes,
            text=text,
            truncated=truncated,
        )

        output_preview.additional_properties = d
        return output_preview

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
