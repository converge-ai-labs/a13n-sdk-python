from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.span import Span


T = TypeVar("T", bound="TraceSearchItem")


@_attrs_define(repr=False)
class TraceSearchItem:
    """
    Attributes:
        cost_usd (None | str):
        duration_seconds (None | str):
        root (Span): One span as the backend stored it; `attributes` are its OpenTelemetry attributes.

            Fields a backend does not keep are null or empty.
    """

    cost_usd: str | None
    duration_seconds: str | None
    root: Span
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cost_usd: str | None
        cost_usd = self.cost_usd

        duration_seconds: str | None
        duration_seconds = self.duration_seconds

        root = self.root.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cost_usd": cost_usd,
                "duration_seconds": duration_seconds,
                "root": root,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.span import Span

        d = dict(src_dict)

        def _parse_cost_usd(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        cost_usd = _parse_cost_usd(d.pop("cost_usd"))

        def _parse_duration_seconds(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        duration_seconds = _parse_duration_seconds(d.pop("duration_seconds"))

        root = Span.from_dict(d.pop("root"))

        trace_search_item = cls(
            cost_usd=cost_usd,
            duration_seconds=duration_seconds,
            root=root,
        )

        trace_search_item.additional_properties = d
        return trace_search_item

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
