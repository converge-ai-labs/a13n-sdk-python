from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.thread_view_origin import ThreadViewOrigin

if TYPE_CHECKING:
    from ..models.message_history_item import MessageHistoryItem
    from ..models.thread_view_labels import ThreadViewLabels
    from ..models.thread_view_mcp_headers import ThreadViewMcpHeaders


T = TypeVar("T", bound="ThreadView")


@_attrs_define(repr=False)
class ThreadView:
    """
    Attributes:
        archived_at (datetime.datetime | None):
        created_at (datetime.datetime):
        current_run_id (None | str):
        id (str):
        labels (ThreadViewLabels):
        last_run_id (None | str):
        mcp_headers (ThreadViewMcpHeaders):
        message_history (list[MessageHistoryItem]): Pydantic AI ModelMessage JSON objects, validated by the Service.
            Imports completed user text, model text and closed tool-call/JSON-result exchanges; no instructions, media or
            suspended execution. At most 256 messages and 256 KiB of normalized JSON.
        origin (ThreadViewOrigin):
        origin_run_id (None | str):
        origin_thread_id (None | str):
        origin_tool_call_id (None | str):
        session_id (str):
        subagent (None | str):
        updated_at (datetime.datetime):
        version (int):
        workspace_id (str):
    """

    archived_at: datetime.datetime | None
    created_at: datetime.datetime
    current_run_id: str | None
    id: str
    labels: ThreadViewLabels
    last_run_id: str | None
    mcp_headers: ThreadViewMcpHeaders
    message_history: list[MessageHistoryItem]
    origin: ThreadViewOrigin
    origin_run_id: str | None
    origin_thread_id: str | None
    origin_tool_call_id: str | None
    session_id: str
    subagent: str | None
    updated_at: datetime.datetime
    version: int
    workspace_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        archived_at: str | None
        if isinstance(self.archived_at, datetime.datetime):
            archived_at = self.archived_at.isoformat()
        else:
            archived_at = self.archived_at

        created_at = self.created_at.isoformat()

        current_run_id: str | None
        current_run_id = self.current_run_id

        id = self.id

        labels = self.labels.to_dict()

        last_run_id: str | None
        last_run_id = self.last_run_id

        mcp_headers = self.mcp_headers.to_dict()

        message_history = []
        for componentsschemas_message_history_item_data in self.message_history:
            componentsschemas_message_history_item = componentsschemas_message_history_item_data.to_dict()
            message_history.append(componentsschemas_message_history_item)

        origin = self.origin.value

        origin_run_id: str | None
        origin_run_id = self.origin_run_id

        origin_thread_id: str | None
        origin_thread_id = self.origin_thread_id

        origin_tool_call_id: str | None
        origin_tool_call_id = self.origin_tool_call_id

        session_id = self.session_id

        subagent: str | None
        subagent = self.subagent

        updated_at = self.updated_at.isoformat()

        version = self.version

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "archived_at": archived_at,
                "created_at": created_at,
                "current_run_id": current_run_id,
                "id": id,
                "labels": labels,
                "last_run_id": last_run_id,
                "mcp_headers": mcp_headers,
                "message_history": message_history,
                "origin": origin,
                "origin_run_id": origin_run_id,
                "origin_thread_id": origin_thread_id,
                "origin_tool_call_id": origin_tool_call_id,
                "session_id": session_id,
                "subagent": subagent,
                "updated_at": updated_at,
                "version": version,
                "workspace_id": workspace_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_history_item import MessageHistoryItem
        from ..models.thread_view_labels import ThreadViewLabels
        from ..models.thread_view_mcp_headers import ThreadViewMcpHeaders

        d = dict(src_dict)

        def _parse_archived_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                archived_at_type_0 = datetime.datetime.fromisoformat(data)

                return archived_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        archived_at = _parse_archived_at(d.pop("archived_at"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_current_run_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        current_run_id = _parse_current_run_id(d.pop("current_run_id"))

        id = d.pop("id")

        labels = ThreadViewLabels.from_dict(d.pop("labels"))

        def _parse_last_run_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        last_run_id = _parse_last_run_id(d.pop("last_run_id"))

        mcp_headers = ThreadViewMcpHeaders.from_dict(d.pop("mcp_headers"))

        message_history = []
        _message_history = d.pop("message_history")
        for componentsschemas_message_history_item_data in _message_history:
            componentsschemas_message_history_item = MessageHistoryItem.from_dict(
                componentsschemas_message_history_item_data
            )

            message_history.append(componentsschemas_message_history_item)

        origin = ThreadViewOrigin(d.pop("origin"))

        def _parse_origin_run_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        origin_run_id = _parse_origin_run_id(d.pop("origin_run_id"))

        def _parse_origin_thread_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        origin_thread_id = _parse_origin_thread_id(d.pop("origin_thread_id"))

        def _parse_origin_tool_call_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        origin_tool_call_id = _parse_origin_tool_call_id(d.pop("origin_tool_call_id"))

        session_id = d.pop("session_id")

        def _parse_subagent(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        subagent = _parse_subagent(d.pop("subagent"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        version = d.pop("version")

        workspace_id = d.pop("workspace_id")

        thread_view = cls(
            archived_at=archived_at,
            created_at=created_at,
            current_run_id=current_run_id,
            id=id,
            labels=labels,
            last_run_id=last_run_id,
            mcp_headers=mcp_headers,
            message_history=message_history,
            origin=origin,
            origin_run_id=origin_run_id,
            origin_thread_id=origin_thread_id,
            origin_tool_call_id=origin_tool_call_id,
            session_id=session_id,
            subagent=subagent,
            updated_at=updated_at,
            version=version,
            workspace_id=workspace_id,
        )

        thread_view.additional_properties = d
        return thread_view

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
