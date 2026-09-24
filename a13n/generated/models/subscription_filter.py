from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriptionFilter")


@_attrs_define(repr=False)
class SubscriptionFilter:
    """Absent fields match every run.

    Attributes:
        agent_id (None | str | Unset):
        session_id (None | str | Unset):
        thread_id (None | str | Unset):
    """

    agent_id: str | Unset | None = UNSET
    session_id: str | Unset | None = UNSET
    thread_id: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        agent_id: str | Unset | None
        if isinstance(self.agent_id, Unset):
            agent_id = UNSET
        else:
            agent_id = self.agent_id

        session_id: str | Unset | None
        if isinstance(self.session_id, Unset):
            session_id = UNSET
        else:
            session_id = self.session_id

        thread_id: str | Unset | None
        if isinstance(self.thread_id, Unset):
            thread_id = UNSET
        else:
            thread_id = self.thread_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if agent_id is not UNSET:
            field_dict["agent_id"] = agent_id
        if session_id is not UNSET:
            field_dict["session_id"] = session_id
        if thread_id is not UNSET:
            field_dict["thread_id"] = thread_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_agent_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        agent_id = _parse_agent_id(d.pop("agent_id", UNSET))

        def _parse_session_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        session_id = _parse_session_id(d.pop("session_id", UNSET))

        def _parse_thread_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        thread_id = _parse_thread_id(d.pop("thread_id", UNSET))

        subscription_filter = cls(
            agent_id=agent_id,
            session_id=session_id,
            thread_id=thread_id,
        )

        return subscription_filter
