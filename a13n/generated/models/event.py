from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Event")


@_attrs_define(repr=False)
class Event:
    """
    Attributes:
        resource_uid (str):
        count (int | None | Unset):
        first_timestamp (None | str | Unset):
        last_timestamp (None | str | Unset):
        message (None | str | Unset):
        reason (None | str | Unset):
        type_ (None | str | Unset):
    """

    resource_uid: str
    count: int | Unset | None = UNSET
    first_timestamp: str | Unset | None = UNSET
    last_timestamp: str | Unset | None = UNSET
    message: str | Unset | None = UNSET
    reason: str | Unset | None = UNSET
    type_: str | Unset | None = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_uid = self.resource_uid

        count: int | Unset | None
        if isinstance(self.count, Unset):
            count = UNSET
        else:
            count = self.count

        first_timestamp: str | Unset | None
        if isinstance(self.first_timestamp, Unset):
            first_timestamp = UNSET
        else:
            first_timestamp = self.first_timestamp

        last_timestamp: str | Unset | None
        if isinstance(self.last_timestamp, Unset):
            last_timestamp = UNSET
        else:
            last_timestamp = self.last_timestamp

        message: str | Unset | None
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        reason: str | Unset | None
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        type_: str | Unset | None
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource_uid": resource_uid,
            }
        )
        if count is not UNSET:
            field_dict["count"] = count
        if first_timestamp is not UNSET:
            field_dict["first_timestamp"] = first_timestamp
        if last_timestamp is not UNSET:
            field_dict["last_timestamp"] = last_timestamp
        if message is not UNSET:
            field_dict["message"] = message
        if reason is not UNSET:
            field_dict["reason"] = reason
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource_uid = d.pop("resource_uid")

        def _parse_count(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        count = _parse_count(d.pop("count", UNSET))

        def _parse_first_timestamp(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        first_timestamp = _parse_first_timestamp(d.pop("first_timestamp", UNSET))

        def _parse_last_timestamp(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        last_timestamp = _parse_last_timestamp(d.pop("last_timestamp", UNSET))

        def _parse_message(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        message = _parse_message(d.pop("message", UNSET))

        def _parse_reason(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        def _parse_type_(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        event = cls(
            resource_uid=resource_uid,
            count=count,
            first_timestamp=first_timestamp,
            last_timestamp=last_timestamp,
            message=message,
            reason=reason,
            type_=type_,
        )

        event.additional_properties = d
        return event

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
