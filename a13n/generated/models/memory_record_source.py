from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MemoryRecordSource")


@_attrs_define(repr=False)
class MemoryRecordSource:
    """A platform-confirmed write, not an asserted source message or complete provider history.

    Attributes:
        attempt_id (None | str):
        confirmed_at (datetime.datetime):
        principal_id (None | str):
        run_id (None | str):
        tool_call_id (None | str):
        principal_name (None | str | Unset):
    """

    attempt_id: str | None
    confirmed_at: datetime.datetime
    principal_id: str | None
    run_id: str | None
    tool_call_id: str | None
    principal_name: str | Unset | None = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attempt_id: str | None
        attempt_id = self.attempt_id

        confirmed_at = self.confirmed_at.isoformat()

        principal_id: str | None
        principal_id = self.principal_id

        run_id: str | None
        run_id = self.run_id

        tool_call_id: str | None
        tool_call_id = self.tool_call_id

        principal_name: str | Unset | None
        if isinstance(self.principal_name, Unset):
            principal_name = UNSET
        else:
            principal_name = self.principal_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attempt_id": attempt_id,
                "confirmed_at": confirmed_at,
                "principal_id": principal_id,
                "run_id": run_id,
                "tool_call_id": tool_call_id,
            }
        )
        if principal_name is not UNSET:
            field_dict["principal_name"] = principal_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_attempt_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        attempt_id = _parse_attempt_id(d.pop("attempt_id"))

        confirmed_at = datetime.datetime.fromisoformat(d.pop("confirmed_at"))

        def _parse_principal_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        principal_id = _parse_principal_id(d.pop("principal_id"))

        def _parse_run_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        run_id = _parse_run_id(d.pop("run_id"))

        def _parse_tool_call_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        tool_call_id = _parse_tool_call_id(d.pop("tool_call_id"))

        def _parse_principal_name(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        principal_name = _parse_principal_name(d.pop("principal_name", UNSET))

        memory_record_source = cls(
            attempt_id=attempt_id,
            confirmed_at=confirmed_at,
            principal_id=principal_id,
            run_id=run_id,
            tool_call_id=tool_call_id,
            principal_name=principal_name,
        )

        memory_record_source.additional_properties = d
        return memory_record_source

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
