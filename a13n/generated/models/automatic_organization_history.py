from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AutomaticOrganizationHistory")


@_attrs_define(repr=False)
class AutomaticOrganizationHistory:
    """Automatic history starts only at an explicitly chosen seal time.

    Attributes:
        session_ids (list[str]):
        after (datetime.datetime | None | Unset):
        before (datetime.datetime | None | Unset):
        max_runs (int | Unset):
    """

    session_ids: list[str]
    after: datetime.datetime | Unset | None = UNSET
    before: datetime.datetime | Unset | None = UNSET
    max_runs: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        session_ids = self.session_ids

        after: str | Unset | None
        if isinstance(self.after, Unset):
            after = UNSET
        elif isinstance(self.after, datetime.datetime):
            after = self.after.isoformat()
        else:
            after = self.after

        before: str | Unset | None
        if isinstance(self.before, Unset):
            before = UNSET
        elif isinstance(self.before, datetime.datetime):
            before = self.before.isoformat()
        else:
            before = self.before

        max_runs = self.max_runs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "session_ids": session_ids,
            }
        )
        if after is not UNSET:
            field_dict["after"] = after
        if before is not UNSET:
            field_dict["before"] = before
        if max_runs is not UNSET:
            field_dict["max_runs"] = max_runs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        session_ids = cast(list[str], d.pop("session_ids"))

        def _parse_after(data: object) -> datetime.datetime | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                after_type_0 = datetime.datetime.fromisoformat(data)

                return after_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | Unset | None, data)

        after = _parse_after(d.pop("after", UNSET))

        def _parse_before(data: object) -> datetime.datetime | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                before_type_0 = datetime.datetime.fromisoformat(data)

                return before_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | Unset | None, data)

        before = _parse_before(d.pop("before", UNSET))

        max_runs = d.pop("max_runs", UNSET)

        automatic_organization_history = cls(
            session_ids=session_ids,
            after=after,
            before=before,
            max_runs=max_runs,
        )

        automatic_organization_history.additional_properties = d
        return automatic_organization_history

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
