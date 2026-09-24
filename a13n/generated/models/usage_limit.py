from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="UsageLimit")


@_attrs_define(repr=False)
class UsageLimit:
    """
    Attributes:
        requests (int):
    """

    requests: int

    def to_dict(self) -> dict[str, Any]:
        requests = self.requests

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "requests": requests,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        requests = d.pop("requests")

        usage_limit = cls(
            requests=requests,
        )

        return usage_limit
