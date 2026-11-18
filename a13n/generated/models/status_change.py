from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.status_change_status import StatusChangeStatus

T = TypeVar("T", bound="StatusChange")


@_attrs_define(repr=False)
class StatusChange:
    """
    Attributes:
        status (StatusChangeStatus):
    """

    status: StatusChangeStatus

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = StatusChangeStatus(d.pop("status"))

        status_change = cls(
            status=status,
        )

        return status_change
