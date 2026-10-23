from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportHealth")


@_attrs_define(repr=False)
class ExportHealth:
    """
    Attributes:
        dropped (int | Unset):
        exported (int | Unset):
        failed (int | Unset):
        last_success_at (datetime.datetime | None | Unset):
        queued (int | Unset):
    """

    dropped: int | Unset = UNSET
    exported: int | Unset = UNSET
    failed: int | Unset = UNSET
    last_success_at: datetime.datetime | Unset | None = UNSET
    queued: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dropped = self.dropped

        exported = self.exported

        failed = self.failed

        last_success_at: str | Unset | None
        if isinstance(self.last_success_at, Unset):
            last_success_at = UNSET
        elif isinstance(self.last_success_at, datetime.datetime):
            last_success_at = self.last_success_at.isoformat()
        else:
            last_success_at = self.last_success_at

        queued = self.queued

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dropped is not UNSET:
            field_dict["dropped"] = dropped
        if exported is not UNSET:
            field_dict["exported"] = exported
        if failed is not UNSET:
            field_dict["failed"] = failed
        if last_success_at is not UNSET:
            field_dict["last_success_at"] = last_success_at
        if queued is not UNSET:
            field_dict["queued"] = queued

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dropped = d.pop("dropped", UNSET)

        exported = d.pop("exported", UNSET)

        failed = d.pop("failed", UNSET)

        def _parse_last_success_at(data: object) -> datetime.datetime | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_success_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_success_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | Unset | None, data)

        last_success_at = _parse_last_success_at(d.pop("last_success_at", UNSET))

        queued = d.pop("queued", UNSET)

        export_health = cls(
            dropped=dropped,
            exported=exported,
            failed=failed,
            last_success_at=last_success_at,
            queued=queued,
        )

        export_health.additional_properties = d
        return export_health

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
