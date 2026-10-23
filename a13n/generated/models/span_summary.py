from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.span_summary_status import SpanSummaryStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.preview import Preview


T = TypeVar("T", bound="SpanSummary")


@_attrs_define(repr=False)
class SpanSummary:
    """
    Attributes:
        cost_usd (None | str):
        duration_ms (float | None):
        ended_at (datetime.datetime | None):
        error (Preview):
        id (str):
        kind (str):
        model (Preview):
        name (Preview):
        parent_id (None | str):
        started_at (datetime.datetime):
        status (SpanSummaryStatus):
        trace_id (str):
        usage (Preview):
        omitted_sections (list[str] | Unset):
        view (Literal['compact'] | Unset):
    """

    cost_usd: str | None
    duration_ms: float | None
    ended_at: datetime.datetime | None
    error: Preview
    id: str
    kind: str
    model: Preview
    name: Preview
    parent_id: str | None
    started_at: datetime.datetime
    status: SpanSummaryStatus
    trace_id: str
    usage: Preview
    omitted_sections: list[str] | Unset = UNSET
    view: Literal["compact"] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cost_usd: str | None
        cost_usd = self.cost_usd

        duration_ms: float | None
        duration_ms = self.duration_ms

        ended_at: str | None
        if isinstance(self.ended_at, datetime.datetime):
            ended_at = self.ended_at.isoformat()
        else:
            ended_at = self.ended_at

        error = self.error.to_dict()

        id = self.id

        kind = self.kind

        model = self.model.to_dict()

        name = self.name.to_dict()

        parent_id: str | None
        parent_id = self.parent_id

        started_at = self.started_at.isoformat()

        status = self.status.value

        trace_id = self.trace_id

        usage = self.usage.to_dict()

        omitted_sections: list[str] | Unset = UNSET
        if not isinstance(self.omitted_sections, Unset):
            omitted_sections = self.omitted_sections

        view = self.view

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cost_usd": cost_usd,
                "duration_ms": duration_ms,
                "ended_at": ended_at,
                "error": error,
                "id": id,
                "kind": kind,
                "model": model,
                "name": name,
                "parent_id": parent_id,
                "started_at": started_at,
                "status": status,
                "trace_id": trace_id,
                "usage": usage,
            }
        )
        if omitted_sections is not UNSET:
            field_dict["omitted_sections"] = omitted_sections
        if view is not UNSET:
            field_dict["view"] = view

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.preview import Preview

        d = dict(src_dict)

        def _parse_cost_usd(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        cost_usd = _parse_cost_usd(d.pop("cost_usd"))

        def _parse_duration_ms(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        duration_ms = _parse_duration_ms(d.pop("duration_ms"))

        def _parse_ended_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ended_at_type_0 = datetime.datetime.fromisoformat(data)

                return ended_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        ended_at = _parse_ended_at(d.pop("ended_at"))

        error = Preview.from_dict(d.pop("error"))

        id = d.pop("id")

        kind = d.pop("kind")

        model = Preview.from_dict(d.pop("model"))

        name = Preview.from_dict(d.pop("name"))

        def _parse_parent_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        parent_id = _parse_parent_id(d.pop("parent_id"))

        started_at = datetime.datetime.fromisoformat(d.pop("started_at"))

        status = SpanSummaryStatus(d.pop("status"))

        trace_id = d.pop("trace_id")

        usage = Preview.from_dict(d.pop("usage"))

        omitted_sections = cast(list[str], d.pop("omitted_sections", UNSET))

        view = cast(Literal["compact"] | Unset, d.pop("view", UNSET))
        if view != "compact" and not isinstance(view, Unset):
            raise ValueError(f"view must match const 'compact', got '{view}'")

        span_summary = cls(
            cost_usd=cost_usd,
            duration_ms=duration_ms,
            ended_at=ended_at,
            error=error,
            id=id,
            kind=kind,
            model=model,
            name=name,
            parent_id=parent_id,
            started_at=started_at,
            status=status,
            trace_id=trace_id,
            usage=usage,
            omitted_sections=omitted_sections,
            view=view,
        )

        span_summary.additional_properties = d
        return span_summary

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
