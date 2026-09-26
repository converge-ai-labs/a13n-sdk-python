from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trace_backend_type_type_0 import TraceBackendTypeType0

T = TypeVar("T", bound="TraceBackend")


@_attrs_define(repr=False)
class TraceBackend:
    """The trace backend queries read; `type` is null when trace query is not configured.

    Attributes:
        queryable_since (datetime.datetime | None):
        type_ (None | TraceBackendTypeType0):
    """

    queryable_since: datetime.datetime | None
    type_: TraceBackendTypeType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        queryable_since: str | None
        if isinstance(self.queryable_since, datetime.datetime):
            queryable_since = self.queryable_since.isoformat()
        else:
            queryable_since = self.queryable_since

        type_: str | None
        if isinstance(self.type_, TraceBackendTypeType0):
            type_ = self.type_.value
        else:
            type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "queryable_since": queryable_since,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_queryable_since(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                queryable_since_type_0 = datetime.datetime.fromisoformat(data)

                return queryable_since_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        queryable_since = _parse_queryable_since(d.pop("queryable_since"))

        def _parse_type_(data: object) -> TraceBackendTypeType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_0 = TraceBackendTypeType0(data)

                return type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(TraceBackendTypeType0 | None, data)

        type_ = _parse_type_(d.pop("type"))

        trace_backend = cls(
            queryable_since=queryable_since,
            type_=type_,
        )

        trace_backend.additional_properties = d
        return trace_backend

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
