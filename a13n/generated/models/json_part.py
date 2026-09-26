from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="JsonPart")


@_attrs_define(repr=False)
class JsonPart:
    """
    Attributes:
        type_ (Literal['json']):
        value (Any):
    """

    type_: Literal["json"]
    value: Any

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["json"], d.pop("type"))
        if type_ != "json":
            raise ValueError(f"type must match const 'json', got '{type_}'")

        value = d.pop("value")

        json_part = cls(
            type_=type_,
            value=value,
        )

        return json_part
