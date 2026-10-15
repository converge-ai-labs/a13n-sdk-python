from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.arguments_event_type_0 import ArgumentsEventType0


T = TypeVar("T", bound="Arguments")


@_attrs_define(repr=False)
class Arguments:
    """A tool-call part's streamed arguments so far and the one observation item that holds them.

    Attributes:
        at (datetime.datetime):
        event (ArgumentsEventType0 | None):
        key (str):
        sequence (int):
        size (int):
        stream (Any):
    """

    at: datetime.datetime
    event: ArgumentsEventType0 | None
    key: str
    sequence: int
    size: int
    stream: Any
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.arguments_event_type_0 import ArgumentsEventType0

        at = self.at.isoformat()

        event: dict[str, Any] | None
        if isinstance(self.event, ArgumentsEventType0):
            event = self.event.to_dict()
        else:
            event = self.event

        key = self.key

        sequence = self.sequence

        size = self.size

        stream = self.stream

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "at": at,
                "event": event,
                "key": key,
                "sequence": sequence,
                "size": size,
                "stream": stream,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.arguments_event_type_0 import ArgumentsEventType0

        d = dict(src_dict)
        at = datetime.datetime.fromisoformat(d.pop("at"))

        def _parse_event(data: object) -> ArgumentsEventType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                event_type_0 = ArgumentsEventType0.from_dict(data)

                return event_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ArgumentsEventType0 | None, data)

        event = _parse_event(d.pop("event"))

        key = d.pop("key")

        sequence = d.pop("sequence")

        size = d.pop("size")

        stream = d.pop("stream")

        arguments = cls(
            at=at,
            event=event,
            key=key,
            sequence=sequence,
            size=size,
            stream=stream,
        )

        arguments.additional_properties = d
        return arguments

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
