from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.run_status import RunStatus

T = TypeVar("T", bound="InitialRun")


@_attrs_define(repr=False)
class InitialRun:
    """
    Attributes:
        id (str):
        status (RunStatus):
    """

    id: str
    status: RunStatus

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        status = RunStatus(d.pop("status"))

        initial_run = cls(
            id=id,
            status=status,
        )

        return initial_run
