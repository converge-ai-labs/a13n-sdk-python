from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.span_overview_status import SpanOverviewStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="SpanOverview")


@_attrs_define(repr=False)
class SpanOverview:
    """Exact timeline and cost fields; payloads are read from the individual span.

    Attributes:
        cost_usd (None | str):
        ended_at (datetime.datetime | None):
        id (str):
        kind (str):
        level (None | str):
        model (None | str):
        name (str):
        parent_id (None | str):
        started_at (datetime.datetime):
        status (SpanOverviewStatus):
        trace_id (str):
        view (Literal['overview'] | Unset):
    """

    cost_usd: str | None
    ended_at: datetime.datetime | None
    id: str
    kind: str
    level: str | None
    model: str | None
    name: str
    parent_id: str | None
    started_at: datetime.datetime
    status: SpanOverviewStatus
    trace_id: str
    view: Literal["overview"] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cost_usd: str | None
        cost_usd = self.cost_usd

        ended_at: str | None
        if isinstance(self.ended_at, datetime.datetime):
            ended_at = self.ended_at.isoformat()
        else:
            ended_at = self.ended_at

        id = self.id

        kind = self.kind

        level: str | None
        level = self.level

        model: str | None
        model = self.model

        name = self.name

        parent_id: str | None
        parent_id = self.parent_id

        started_at = self.started_at.isoformat()

        status = self.status.value

        trace_id = self.trace_id

        view = self.view

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cost_usd": cost_usd,
                "ended_at": ended_at,
                "id": id,
                "kind": kind,
                "level": level,
                "model": model,
                "name": name,
                "parent_id": parent_id,
                "started_at": started_at,
                "status": status,
                "trace_id": trace_id,
            }
        )
        if view is not UNSET:
            field_dict["view"] = view

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_cost_usd(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        cost_usd = _parse_cost_usd(d.pop("cost_usd"))

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

        id = d.pop("id")

        kind = d.pop("kind")

        def _parse_level(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        level = _parse_level(d.pop("level"))

        def _parse_model(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        model = _parse_model(d.pop("model"))

        name = d.pop("name")

        def _parse_parent_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        parent_id = _parse_parent_id(d.pop("parent_id"))

        started_at = datetime.datetime.fromisoformat(d.pop("started_at"))

        status = SpanOverviewStatus(d.pop("status"))

        trace_id = d.pop("trace_id")

        view = cast(Literal["overview"] | Unset, d.pop("view", UNSET))
        if view != "overview" and not isinstance(view, Unset):
            raise ValueError(f"view must match const 'overview', got '{view}'")

        span_overview = cls(
            cost_usd=cost_usd,
            ended_at=ended_at,
            id=id,
            kind=kind,
            level=level,
            model=model,
            name=name,
            parent_id=parent_id,
            started_at=started_at,
            status=status,
            trace_id=trace_id,
            view=view,
        )

        span_overview.additional_properties = d
        return span_overview

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
