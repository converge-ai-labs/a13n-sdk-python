from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="Request")


@_attrs_define(repr=False)
class Request:
    """
    Attributes:
        mount (str):
        reason (str):
    """

    mount: str
    reason: str

    def to_dict(self) -> dict[str, Any]:
        mount = self.mount

        reason = self.reason

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "mount": mount,
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mount = d.pop("mount")

        reason = d.pop("reason")

        request = cls(
            mount=mount,
            reason=reason,
        )

        return request
