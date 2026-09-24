from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.span_link_attributes import SpanLinkAttributes


T = TypeVar("T", bound="SpanLink")


@_attrs_define(repr=False)
class SpanLink:
    """Another span this one relates to, in its own trace or another.

    Attributes:
        attributes (SpanLinkAttributes):
        span_id (str):
        trace_id (str):
    """

    attributes: SpanLinkAttributes
    span_id: str
    trace_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attributes = self.attributes.to_dict()

        span_id = self.span_id

        trace_id = self.trace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attributes": attributes,
                "span_id": span_id,
                "trace_id": trace_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.span_link_attributes import SpanLinkAttributes

        d = dict(src_dict)
        attributes = SpanLinkAttributes.from_dict(d.pop("attributes"))

        span_id = d.pop("span_id")

        trace_id = d.pop("trace_id")

        span_link = cls(
            attributes=attributes,
            span_id=span_id,
            trace_id=trace_id,
        )

        span_link.additional_properties = d
        return span_link

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
