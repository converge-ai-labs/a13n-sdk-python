from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.span_status import SpanStatus

if TYPE_CHECKING:
    from ..models.instrumentation_scope import InstrumentationScope
    from ..models.span_attributes import SpanAttributes
    from ..models.span_event import SpanEvent
    from ..models.span_link import SpanLink
    from ..models.span_resource_attributes import SpanResourceAttributes
    from ..models.span_usage import SpanUsage


T = TypeVar("T", bound="Span")


@_attrs_define(repr=False)
class Span:
    """One span as the backend stored it; `attributes` are its OpenTelemetry attributes.

    Fields a backend does not keep are null or empty.

        Attributes:
            attributes (SpanAttributes):
            cost_usd (None | str):
            ended_at (datetime.datetime | None):
            events (list[SpanEvent]):
            id (str):
            input_ (Any):
            kind (str):
            level (None | str):
            links (list[SpanLink]):
            model (None | str):
            name (str):
            output (Any):
            parent_id (None | str):
            resource_attributes (SpanResourceAttributes):
            scope (InstrumentationScope | None):
            source_url (None | str):
            started_at (datetime.datetime):
            status (SpanStatus):
            status_message (None | str):
            trace_id (str):
            usage (SpanUsage):
    """

    attributes: SpanAttributes
    cost_usd: str | None
    ended_at: datetime.datetime | None
    events: list[SpanEvent]
    id: str
    input_: Any
    kind: str
    level: str | None
    links: list[SpanLink]
    model: str | None
    name: str
    output: Any
    parent_id: str | None
    resource_attributes: SpanResourceAttributes
    scope: InstrumentationScope | None
    source_url: str | None
    started_at: datetime.datetime
    status: SpanStatus
    status_message: str | None
    trace_id: str
    usage: SpanUsage
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.instrumentation_scope import InstrumentationScope

        attributes = self.attributes.to_dict()

        cost_usd: str | None
        cost_usd = self.cost_usd

        ended_at: str | None
        if isinstance(self.ended_at, datetime.datetime):
            ended_at = self.ended_at.isoformat()
        else:
            ended_at = self.ended_at

        events = []
        for events_item_data in self.events:
            events_item = events_item_data.to_dict()
            events.append(events_item)

        id = self.id

        input_ = self.input_

        kind = self.kind

        level: str | None
        level = self.level

        links = []
        for links_item_data in self.links:
            links_item = links_item_data.to_dict()
            links.append(links_item)

        model: str | None
        model = self.model

        name = self.name

        output = self.output

        parent_id: str | None
        parent_id = self.parent_id

        resource_attributes = self.resource_attributes.to_dict()

        scope: dict[str, Any] | None
        if isinstance(self.scope, InstrumentationScope):
            scope = self.scope.to_dict()
        else:
            scope = self.scope

        source_url: str | None
        source_url = self.source_url

        started_at = self.started_at.isoformat()

        status = self.status.value

        status_message: str | None
        status_message = self.status_message

        trace_id = self.trace_id

        usage = self.usage.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attributes": attributes,
                "cost_usd": cost_usd,
                "ended_at": ended_at,
                "events": events,
                "id": id,
                "input": input_,
                "kind": kind,
                "level": level,
                "links": links,
                "model": model,
                "name": name,
                "output": output,
                "parent_id": parent_id,
                "resource_attributes": resource_attributes,
                "scope": scope,
                "source_url": source_url,
                "started_at": started_at,
                "status": status,
                "status_message": status_message,
                "trace_id": trace_id,
                "usage": usage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.instrumentation_scope import InstrumentationScope
        from ..models.span_attributes import SpanAttributes
        from ..models.span_event import SpanEvent
        from ..models.span_link import SpanLink
        from ..models.span_resource_attributes import SpanResourceAttributes
        from ..models.span_usage import SpanUsage

        d = dict(src_dict)
        attributes = SpanAttributes.from_dict(d.pop("attributes"))

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

        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = SpanEvent.from_dict(events_item_data)

            events.append(events_item)

        id = d.pop("id")

        input_ = d.pop("input")

        kind = d.pop("kind")

        def _parse_level(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        level = _parse_level(d.pop("level"))

        links = []
        _links = d.pop("links")
        for links_item_data in _links:
            links_item = SpanLink.from_dict(links_item_data)

            links.append(links_item)

        def _parse_model(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        model = _parse_model(d.pop("model"))

        name = d.pop("name")

        output = d.pop("output")

        def _parse_parent_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        parent_id = _parse_parent_id(d.pop("parent_id"))

        resource_attributes = SpanResourceAttributes.from_dict(d.pop("resource_attributes"))

        def _parse_scope(data: object) -> InstrumentationScope | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                scope_type_0 = InstrumentationScope.from_dict(data)

                return scope_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InstrumentationScope | None, data)

        scope = _parse_scope(d.pop("scope"))

        def _parse_source_url(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        source_url = _parse_source_url(d.pop("source_url"))

        started_at = datetime.datetime.fromisoformat(d.pop("started_at"))

        status = SpanStatus(d.pop("status"))

        def _parse_status_message(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        status_message = _parse_status_message(d.pop("status_message"))

        trace_id = d.pop("trace_id")

        usage = SpanUsage.from_dict(d.pop("usage"))

        span = cls(
            attributes=attributes,
            cost_usd=cost_usd,
            ended_at=ended_at,
            events=events,
            id=id,
            input_=input_,
            kind=kind,
            level=level,
            links=links,
            model=model,
            name=name,
            output=output,
            parent_id=parent_id,
            resource_attributes=resource_attributes,
            scope=scope,
            source_url=source_url,
            started_at=started_at,
            status=status,
            status_message=status_message,
            trace_id=trace_id,
            usage=usage,
        )

        span.additional_properties = d
        return span

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
