from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.lineage import Lineage
from ..models.run_status import RunStatus
from ..models.trigger import Trigger
from ..models.wait_reason import WaitReason

if TYPE_CHECKING:
    from ..models.run_input_preview import RunInputPreview


T = TypeVar("T", bound="RunListItem")


@_attrs_define(repr=False)
class RunListItem:
    """Run discovery metadata. Full input, results and execution settings belong to the Run detail read.

    Attributes:
        agent_id (str):
        agent_revision_id (str):
        attempts (int):
        created_at (datetime.datetime):
        current_attempt_id (None | str):
        id (str):
        input_preview (RunInputPreview):
        lineage (Lineage):
        max_attempts (int):
        parent_run_id (None | str):
        principal_id (str):
        sealed_at (datetime.datetime | None):
        session_id (str):
        source_entry_id (None | str):
        started_at (datetime.datetime | None):
        status (RunStatus):
        thread_id (str):
        trigger (Trigger):
        updated_at (datetime.datetime):
        version (int):
        wait_reason (None | WaitReason):
        workspace_id (str):
    """

    agent_id: str
    agent_revision_id: str
    attempts: int
    created_at: datetime.datetime
    current_attempt_id: str | None
    id: str
    input_preview: RunInputPreview
    lineage: Lineage
    max_attempts: int
    parent_run_id: str | None
    principal_id: str
    sealed_at: datetime.datetime | None
    session_id: str
    source_entry_id: str | None
    started_at: datetime.datetime | None
    status: RunStatus
    thread_id: str
    trigger: Trigger
    updated_at: datetime.datetime
    version: int
    wait_reason: WaitReason | None
    workspace_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_id = self.agent_id

        agent_revision_id = self.agent_revision_id

        attempts = self.attempts

        created_at = self.created_at.isoformat()

        current_attempt_id: str | None
        current_attempt_id = self.current_attempt_id

        id = self.id

        input_preview = self.input_preview.to_dict()

        lineage = self.lineage.value

        max_attempts = self.max_attempts

        parent_run_id: str | None
        parent_run_id = self.parent_run_id

        principal_id = self.principal_id

        sealed_at: str | None
        if isinstance(self.sealed_at, datetime.datetime):
            sealed_at = self.sealed_at.isoformat()
        else:
            sealed_at = self.sealed_at

        session_id = self.session_id

        source_entry_id: str | None
        source_entry_id = self.source_entry_id

        started_at: str | None
        if isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        status = self.status.value

        thread_id = self.thread_id

        trigger = self.trigger.value

        updated_at = self.updated_at.isoformat()

        version = self.version

        wait_reason: str | None
        if isinstance(self.wait_reason, WaitReason):
            wait_reason = self.wait_reason.value
        else:
            wait_reason = self.wait_reason

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_id": agent_id,
                "agent_revision_id": agent_revision_id,
                "attempts": attempts,
                "created_at": created_at,
                "current_attempt_id": current_attempt_id,
                "id": id,
                "input_preview": input_preview,
                "lineage": lineage,
                "max_attempts": max_attempts,
                "parent_run_id": parent_run_id,
                "principal_id": principal_id,
                "sealed_at": sealed_at,
                "session_id": session_id,
                "source_entry_id": source_entry_id,
                "started_at": started_at,
                "status": status,
                "thread_id": thread_id,
                "trigger": trigger,
                "updated_at": updated_at,
                "version": version,
                "wait_reason": wait_reason,
                "workspace_id": workspace_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_input_preview import RunInputPreview

        d = dict(src_dict)
        agent_id = d.pop("agent_id")

        agent_revision_id = d.pop("agent_revision_id")

        attempts = d.pop("attempts")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_current_attempt_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        current_attempt_id = _parse_current_attempt_id(d.pop("current_attempt_id"))

        id = d.pop("id")

        input_preview = RunInputPreview.from_dict(d.pop("input_preview"))

        lineage = Lineage(d.pop("lineage"))

        max_attempts = d.pop("max_attempts")

        def _parse_parent_run_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        parent_run_id = _parse_parent_run_id(d.pop("parent_run_id"))

        principal_id = d.pop("principal_id")

        def _parse_sealed_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sealed_at_type_0 = datetime.datetime.fromisoformat(data)

                return sealed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        sealed_at = _parse_sealed_at(d.pop("sealed_at"))

        session_id = d.pop("session_id")

        def _parse_source_entry_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        source_entry_id = _parse_source_entry_id(d.pop("source_entry_id"))

        def _parse_started_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_at_type_0 = datetime.datetime.fromisoformat(data)

                return started_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        started_at = _parse_started_at(d.pop("started_at"))

        status = RunStatus(d.pop("status"))

        thread_id = d.pop("thread_id")

        trigger = Trigger(d.pop("trigger"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        version = d.pop("version")

        def _parse_wait_reason(data: object) -> WaitReason | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                wait_reason_type_0 = WaitReason(data)

                return wait_reason_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(WaitReason | None, data)

        wait_reason = _parse_wait_reason(d.pop("wait_reason"))

        workspace_id = d.pop("workspace_id")

        run_list_item = cls(
            agent_id=agent_id,
            agent_revision_id=agent_revision_id,
            attempts=attempts,
            created_at=created_at,
            current_attempt_id=current_attempt_id,
            id=id,
            input_preview=input_preview,
            lineage=lineage,
            max_attempts=max_attempts,
            parent_run_id=parent_run_id,
            principal_id=principal_id,
            sealed_at=sealed_at,
            session_id=session_id,
            source_entry_id=source_entry_id,
            started_at=started_at,
            status=status,
            thread_id=thread_id,
            trigger=trigger,
            updated_at=updated_at,
            version=version,
            wait_reason=wait_reason,
            workspace_id=workspace_id,
        )

        run_list_item.additional_properties = d
        return run_list_item

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
