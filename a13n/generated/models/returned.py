from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="Returned")


@_attrs_define(repr=False)
class Returned:
    """A JSON tool result. Built-in question values are validated by the Harness.

    Attributes:
        status (Literal['returned']):
        value (Any):
    """

    status: Literal["returned"]
    value: Any

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = cast(Literal["returned"], d.pop("status"))
        if status != "returned":
            raise ValueError(f"status must match const 'returned', got '{status}'")

        value = d.pop("value")

        returned = cls(
            status=status,
            value=value,
        )

        return returned
