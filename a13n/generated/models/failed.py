from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="Failed")


@_attrs_define(repr=False)
class Failed:
    """An explicit external tool failure, including an intentional unanswered question.

    Attributes:
        message (str):
        status (Literal['failed']):
    """

    message: str
    status: Literal["failed"]

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        status = self.status

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "message": message,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message")

        status = cast(Literal["failed"], d.pop("status"))
        if status != "failed":
            raise ValueError(f"status must match const 'failed', got '{status}'")

        failed = cls(
            message=message,
            status=status,
        )

        return failed
