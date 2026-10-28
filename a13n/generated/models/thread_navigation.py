from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.thread_navigation_origin import ThreadNavigationOrigin

if TYPE_CHECKING:
    from ..models.thread_reference import ThreadReference


T = TypeVar("T", bound="ThreadNavigation")


@_attrs_define(repr=False)
class ThreadNavigation:
    """Bounded navigation metadata; positions count the complete Session before filtering.

    Attributes:
        created_at (datetime.datetime):
        id (str):
        origin (ThreadNavigationOrigin):
        origin_count (int):
        origin_number (int):
        origin_thread (None | ThreadReference):
        session_id (str):
        subagent (None | str):
    """

    created_at: datetime.datetime
    id: str
    origin: ThreadNavigationOrigin
    origin_count: int
    origin_number: int
    origin_thread: ThreadReference | None
    session_id: str
    subagent: str | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.thread_reference import ThreadReference

        created_at = self.created_at.isoformat()

        id = self.id

        origin = self.origin.value

        origin_count = self.origin_count

        origin_number = self.origin_number

        origin_thread: dict[str, Any] | None
        if isinstance(self.origin_thread, ThreadReference):
            origin_thread = self.origin_thread.to_dict()
        else:
            origin_thread = self.origin_thread

        session_id = self.session_id

        subagent: str | None
        subagent = self.subagent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "id": id,
                "origin": origin,
                "origin_count": origin_count,
                "origin_number": origin_number,
                "origin_thread": origin_thread,
                "session_id": session_id,
                "subagent": subagent,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.thread_reference import ThreadReference

        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = d.pop("id")

        origin = ThreadNavigationOrigin(d.pop("origin"))

        origin_count = d.pop("origin_count")

        origin_number = d.pop("origin_number")

        def _parse_origin_thread(data: object) -> ThreadReference | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                origin_thread_type_0 = ThreadReference.from_dict(data)

                return origin_thread_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ThreadReference | None, data)

        origin_thread = _parse_origin_thread(d.pop("origin_thread"))

        session_id = d.pop("session_id")

        def _parse_subagent(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        subagent = _parse_subagent(d.pop("subagent"))

        thread_navigation = cls(
            created_at=created_at,
            id=id,
            origin=origin,
            origin_count=origin_count,
            origin_number=origin_number,
            origin_thread=origin_thread,
            session_id=session_id,
            subagent=subagent,
        )

        thread_navigation.additional_properties = d
        return thread_navigation

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
