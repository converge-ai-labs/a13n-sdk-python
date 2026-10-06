from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.lineage import Lineage
from ..models.run_status import RunStatus
from ..models.run_view_revision_selection import RunViewRevisionSelection
from ..models.trigger import Trigger
from ..models.wait_reason import WaitReason
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.environment_mount import EnvironmentMount
    from ..models.failure import Failure
    from ..models.memory_mount import MemoryMount
    from ..models.pending import Pending
    from ..models.resume import Resume
    from ..models.run_options_output import RunOptionsOutput
    from ..models.run_view_input_type_0 import RunViewInputType0
    from ..models.run_view_labels import RunViewLabels
    from ..models.run_view_usage_at_seal_type_0 import RunViewUsageAtSealType0


T = TypeVar("T", bound="RunView")


@_attrs_define(repr=False)
class RunView:
    """
    Attributes:
        agent_id (str):
        agent_revision_id (str):
        attempts (int):
        cancel_requested_at (datetime.datetime | None):
        created_at (datetime.datetime):
        current_attempt_id (None | str):
        environment_mounts (list[EnvironmentMount]):
        failure (Failure | None):
        id (str):
        labels (RunViewLabels):
        lineage (Lineage):
        max_attempts (int):
        memory_mounts (list[MemoryMount]):
        options (RunOptionsOutput): What a message may choose for the run it starts. A steer joins a run with the
            defaults or equal options.
        output (Any | None):
        parent_run_id (None | str):
        pending (None | Pending):
        principal_id (str):
        resume (None | Resume):
        resumed_by_id (None | str):
        revision_selection (RunViewRevisionSelection):
        sealed_at (datetime.datetime | None):
        session_id (str):
        source_entry_id (None | str):
        started_at (datetime.datetime | None):
        status (RunStatus):
        thread_id (str):
        trigger (Trigger):
        updated_at (datetime.datetime):
        usage_at_seal (None | RunViewUsageAtSealType0):
        version (int):
        wait_reason (None | WaitReason):
        workspace_id (str):
        display_position (None | str | Unset):
        input_ (None | RunViewInputType0 | Unset):
    """

    agent_id: str
    agent_revision_id: str
    attempts: int
    cancel_requested_at: datetime.datetime | None
    created_at: datetime.datetime
    current_attempt_id: str | None
    environment_mounts: list[EnvironmentMount]
    failure: Failure | None
    id: str
    labels: RunViewLabels
    lineage: Lineage
    max_attempts: int
    memory_mounts: list[MemoryMount]
    options: RunOptionsOutput
    output: Any | None
    parent_run_id: str | None
    pending: Pending | None
    principal_id: str
    resume: Resume | None
    resumed_by_id: str | None
    revision_selection: RunViewRevisionSelection
    sealed_at: datetime.datetime | None
    session_id: str
    source_entry_id: str | None
    started_at: datetime.datetime | None
    status: RunStatus
    thread_id: str
    trigger: Trigger
    updated_at: datetime.datetime
    usage_at_seal: RunViewUsageAtSealType0 | None
    version: int
    wait_reason: WaitReason | None
    workspace_id: str
    display_position: str | Unset | None = UNSET
    input_: RunViewInputType0 | Unset | None = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.failure import Failure
        from ..models.pending import Pending
        from ..models.resume import Resume
        from ..models.run_view_input_type_0 import RunViewInputType0
        from ..models.run_view_usage_at_seal_type_0 import RunViewUsageAtSealType0

        agent_id = self.agent_id

        agent_revision_id = self.agent_revision_id

        attempts = self.attempts

        cancel_requested_at: str | None
        if isinstance(self.cancel_requested_at, datetime.datetime):
            cancel_requested_at = self.cancel_requested_at.isoformat()
        else:
            cancel_requested_at = self.cancel_requested_at

        created_at = self.created_at.isoformat()

        current_attempt_id: str | None
        current_attempt_id = self.current_attempt_id

        environment_mounts = []
        for environment_mounts_item_data in self.environment_mounts:
            environment_mounts_item = environment_mounts_item_data.to_dict()
            environment_mounts.append(environment_mounts_item)

        failure: dict[str, Any] | None
        if isinstance(self.failure, Failure):
            failure = self.failure.to_dict()
        else:
            failure = self.failure

        id = self.id

        labels = self.labels.to_dict()

        lineage = self.lineage.value

        max_attempts = self.max_attempts

        memory_mounts = []
        for memory_mounts_item_data in self.memory_mounts:
            memory_mounts_item = memory_mounts_item_data.to_dict()
            memory_mounts.append(memory_mounts_item)

        options = self.options.to_dict()

        output: Any | None
        output = self.output

        parent_run_id: str | None
        parent_run_id = self.parent_run_id

        pending: dict[str, Any] | None
        if isinstance(self.pending, Pending):
            pending = self.pending.to_dict()
        else:
            pending = self.pending

        principal_id = self.principal_id

        resume: dict[str, Any] | None
        if isinstance(self.resume, Resume):
            resume = self.resume.to_dict()
        else:
            resume = self.resume

        resumed_by_id: str | None
        resumed_by_id = self.resumed_by_id

        revision_selection = self.revision_selection.value

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

        usage_at_seal: dict[str, Any] | None
        if isinstance(self.usage_at_seal, RunViewUsageAtSealType0):
            usage_at_seal = self.usage_at_seal.to_dict()
        else:
            usage_at_seal = self.usage_at_seal

        version = self.version

        wait_reason: str | None
        if isinstance(self.wait_reason, WaitReason):
            wait_reason = self.wait_reason.value
        else:
            wait_reason = self.wait_reason

        workspace_id = self.workspace_id

        display_position: str | Unset | None
        if isinstance(self.display_position, Unset):
            display_position = UNSET
        else:
            display_position = self.display_position

        input_: dict[str, Any] | Unset | None
        if isinstance(self.input_, Unset):
            input_ = UNSET
        elif isinstance(self.input_, RunViewInputType0):
            input_ = self.input_.to_dict()
        else:
            input_ = self.input_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_id": agent_id,
                "agent_revision_id": agent_revision_id,
                "attempts": attempts,
                "cancel_requested_at": cancel_requested_at,
                "created_at": created_at,
                "current_attempt_id": current_attempt_id,
                "environment_mounts": environment_mounts,
                "failure": failure,
                "id": id,
                "labels": labels,
                "lineage": lineage,
                "max_attempts": max_attempts,
                "memory_mounts": memory_mounts,
                "options": options,
                "output": output,
                "parent_run_id": parent_run_id,
                "pending": pending,
                "principal_id": principal_id,
                "resume": resume,
                "resumed_by_id": resumed_by_id,
                "revision_selection": revision_selection,
                "sealed_at": sealed_at,
                "session_id": session_id,
                "source_entry_id": source_entry_id,
                "started_at": started_at,
                "status": status,
                "thread_id": thread_id,
                "trigger": trigger,
                "updated_at": updated_at,
                "usage_at_seal": usage_at_seal,
                "version": version,
                "wait_reason": wait_reason,
                "workspace_id": workspace_id,
            }
        )
        if display_position is not UNSET:
            field_dict["display_position"] = display_position
        if input_ is not UNSET:
            field_dict["input"] = input_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.environment_mount import EnvironmentMount
        from ..models.failure import Failure
        from ..models.memory_mount import MemoryMount
        from ..models.pending import Pending
        from ..models.resume import Resume
        from ..models.run_options_output import RunOptionsOutput
        from ..models.run_view_input_type_0 import RunViewInputType0
        from ..models.run_view_labels import RunViewLabels
        from ..models.run_view_usage_at_seal_type_0 import RunViewUsageAtSealType0

        d = dict(src_dict)
        agent_id = d.pop("agent_id")

        agent_revision_id = d.pop("agent_revision_id")

        attempts = d.pop("attempts")

        def _parse_cancel_requested_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cancel_requested_at_type_0 = datetime.datetime.fromisoformat(data)

                return cancel_requested_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        cancel_requested_at = _parse_cancel_requested_at(d.pop("cancel_requested_at"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_current_attempt_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        current_attempt_id = _parse_current_attempt_id(d.pop("current_attempt_id"))

        environment_mounts = []
        _environment_mounts = d.pop("environment_mounts")
        for environment_mounts_item_data in _environment_mounts:
            environment_mounts_item = EnvironmentMount.from_dict(environment_mounts_item_data)

            environment_mounts.append(environment_mounts_item)

        def _parse_failure(data: object) -> Failure | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                failure_type_0 = Failure.from_dict(data)

                return failure_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Failure | None, data)

        failure = _parse_failure(d.pop("failure"))

        id = d.pop("id")

        labels = RunViewLabels.from_dict(d.pop("labels"))

        lineage = Lineage(d.pop("lineage"))

        max_attempts = d.pop("max_attempts")

        memory_mounts = []
        _memory_mounts = d.pop("memory_mounts")
        for memory_mounts_item_data in _memory_mounts:
            memory_mounts_item = MemoryMount.from_dict(memory_mounts_item_data)

            memory_mounts.append(memory_mounts_item)

        options = RunOptionsOutput.from_dict(d.pop("options"))

        def _parse_output(data: object) -> Any | None:
            if data is None:
                return data
            return cast(Any | None, data)

        output = _parse_output(d.pop("output"))

        def _parse_parent_run_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        parent_run_id = _parse_parent_run_id(d.pop("parent_run_id"))

        def _parse_pending(data: object) -> Pending | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pending_type_0 = Pending.from_dict(data)

                return pending_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Pending | None, data)

        pending = _parse_pending(d.pop("pending"))

        principal_id = d.pop("principal_id")

        def _parse_resume(data: object) -> Resume | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                resume_type_0 = Resume.from_dict(data)

                return resume_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Resume | None, data)

        resume = _parse_resume(d.pop("resume"))

        def _parse_resumed_by_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        resumed_by_id = _parse_resumed_by_id(d.pop("resumed_by_id"))

        revision_selection = RunViewRevisionSelection(d.pop("revision_selection"))

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

        def _parse_usage_at_seal(data: object) -> RunViewUsageAtSealType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                usage_at_seal_type_0 = RunViewUsageAtSealType0.from_dict(data)

                return usage_at_seal_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(RunViewUsageAtSealType0 | None, data)

        usage_at_seal = _parse_usage_at_seal(d.pop("usage_at_seal"))

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

        def _parse_display_position(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        display_position = _parse_display_position(d.pop("display_position", UNSET))

        def _parse_input_(data: object) -> RunViewInputType0 | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                input_type_0 = RunViewInputType0.from_dict(data)

                return input_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(RunViewInputType0 | Unset | None, data)

        input_ = _parse_input_(d.pop("input", UNSET))

        run_view = cls(
            agent_id=agent_id,
            agent_revision_id=agent_revision_id,
            attempts=attempts,
            cancel_requested_at=cancel_requested_at,
            created_at=created_at,
            current_attempt_id=current_attempt_id,
            environment_mounts=environment_mounts,
            failure=failure,
            id=id,
            labels=labels,
            lineage=lineage,
            max_attempts=max_attempts,
            memory_mounts=memory_mounts,
            options=options,
            output=output,
            parent_run_id=parent_run_id,
            pending=pending,
            principal_id=principal_id,
            resume=resume,
            resumed_by_id=resumed_by_id,
            revision_selection=revision_selection,
            sealed_at=sealed_at,
            session_id=session_id,
            source_entry_id=source_entry_id,
            started_at=started_at,
            status=status,
            thread_id=thread_id,
            trigger=trigger,
            updated_at=updated_at,
            usage_at_seal=usage_at_seal,
            version=version,
            wait_reason=wait_reason,
            workspace_id=workspace_id,
            display_position=display_position,
            input_=input_,
        )

        run_view.additional_properties = d
        return run_view

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
