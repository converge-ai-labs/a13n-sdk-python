from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Reclamation")


@_attrs_define(repr=False)
class Reclamation:
    """Instance-scoped reclamation settings copied at reservation; no stop/resume semantics.

    Attributes:
        failed_retention_seconds (int | Unset):
        idle_delete_seconds (int | None | Unset):
        preparation_seconds (int | Unset):
    """

    failed_retention_seconds: int | Unset = UNSET
    idle_delete_seconds: int | Unset | None = UNSET
    preparation_seconds: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        failed_retention_seconds = self.failed_retention_seconds

        idle_delete_seconds: int | Unset | None
        if isinstance(self.idle_delete_seconds, Unset):
            idle_delete_seconds = UNSET
        else:
            idle_delete_seconds = self.idle_delete_seconds

        preparation_seconds = self.preparation_seconds

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if failed_retention_seconds is not UNSET:
            field_dict["failed_retention_seconds"] = failed_retention_seconds
        if idle_delete_seconds is not UNSET:
            field_dict["idle_delete_seconds"] = idle_delete_seconds
        if preparation_seconds is not UNSET:
            field_dict["preparation_seconds"] = preparation_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        failed_retention_seconds = d.pop("failed_retention_seconds", UNSET)

        def _parse_idle_delete_seconds(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        idle_delete_seconds = _parse_idle_delete_seconds(d.pop("idle_delete_seconds", UNSET))

        preparation_seconds = d.pop("preparation_seconds", UNSET)

        reclamation = cls(
            failed_retention_seconds=failed_retention_seconds,
            idle_delete_seconds=idle_delete_seconds,
            preparation_seconds=preparation_seconds,
        )

        return reclamation
