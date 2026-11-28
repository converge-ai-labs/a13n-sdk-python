from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transport import Transport
from ..types import UNSET, Unset

T = TypeVar("T", bound="RealtimeAvailability")


@_attrs_define(repr=False)
class RealtimeAvailability:
    """
    Attributes:
        accepts_text (bool | Unset):
        can_start (bool | Unset):
        realtime (bool | Unset):
        reason (None | str | Unset):
        transports (list[Transport] | Unset):
    """

    accepts_text: bool | Unset = UNSET
    can_start: bool | Unset = UNSET
    realtime: bool | Unset = UNSET
    reason: str | Unset | None = UNSET
    transports: list[Transport] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accepts_text = self.accepts_text

        can_start = self.can_start

        realtime = self.realtime

        reason: str | Unset | None
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        transports: list[str] | Unset = UNSET
        if not isinstance(self.transports, Unset):
            transports = []
            for transports_item_data in self.transports:
                transports_item = transports_item_data.value
                transports.append(transports_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accepts_text is not UNSET:
            field_dict["accepts_text"] = accepts_text
        if can_start is not UNSET:
            field_dict["can_start"] = can_start
        if realtime is not UNSET:
            field_dict["realtime"] = realtime
        if reason is not UNSET:
            field_dict["reason"] = reason
        if transports is not UNSET:
            field_dict["transports"] = transports

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accepts_text = d.pop("accepts_text", UNSET)

        can_start = d.pop("can_start", UNSET)

        realtime = d.pop("realtime", UNSET)

        def _parse_reason(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        _transports = d.pop("transports", UNSET)
        transports: list[Transport] | Unset = UNSET
        if _transports is not UNSET:
            transports = []
            for transports_item_data in _transports:
                transports_item = Transport(transports_item_data)

                transports.append(transports_item)

        realtime_availability = cls(
            accepts_text=accepts_text,
            can_start=can_start,
            realtime=realtime,
            reason=reason,
            transports=transports,
        )

        realtime_availability.additional_properties = d
        return realtime_availability

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
