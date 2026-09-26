from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.span_event_attributes import SpanEventAttributes


T = TypeVar("T", bound="SpanEvent")


@_attrs_define(repr=False)
class SpanEvent:
    """Something the span recorded at one moment, such as an exception.

    Attributes:
        attributes (SpanEventAttributes):
        name (str):
        timestamp (datetime.datetime):
    """

    attributes: SpanEventAttributes
    name: str
    timestamp: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attributes = self.attributes.to_dict()

        name = self.name

        timestamp = self.timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attributes": attributes,
                "name": name,
                "timestamp": timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.span_event_attributes import SpanEventAttributes

        d = dict(src_dict)
        attributes = SpanEventAttributes.from_dict(d.pop("attributes"))

        name = d.pop("name")

        timestamp = datetime.datetime.fromisoformat(d.pop("timestamp"))

        span_event = cls(
            attributes=attributes,
            name=name,
            timestamp=timestamp,
        )

        span_event.additional_properties = d
        return span_event

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
