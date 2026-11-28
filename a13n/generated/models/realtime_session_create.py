from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.transport import Transport
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.memory_mount import MemoryMount
    from ..models.mount_create import MountCreate
    from ..models.run_options_input import RunOptionsInput
    from ..models.session_memory_settings import SessionMemorySettings
    from ..models.usage_limit import UsageLimit


T = TypeVar("T", bound="RealtimeSessionCreate")


@_attrs_define(repr=False)
class RealtimeSessionCreate:
    """
    Attributes:
        agent_id (str):
        agent_revision_id (None | str | Unset):
        audio (bool | Unset):
        draft (str | Unset):
        environments (list[MountCreate] | Unset):
        fork_run_id (None | str | Unset):
        fresh_environments (bool | Unset):
        max_usage (None | Unset | UsageLimit):
        memories (list[MemoryMount] | Unset):
        memory (None | SessionMemorySettings | Unset):
        options (RunOptionsInput | Unset): What a message may choose for the run it starts. A steer joins a run with the
            defaults or equal options.
        thread_id (None | str | Unset):
        transport (Transport | Unset):
    """

    agent_id: str
    agent_revision_id: str | Unset | None = UNSET
    audio: bool | Unset = UNSET
    draft: str | Unset = UNSET
    environments: list[MountCreate] | Unset = UNSET
    fork_run_id: str | Unset | None = UNSET
    fresh_environments: bool | Unset = UNSET
    max_usage: Unset | UsageLimit | None = UNSET
    memories: list[MemoryMount] | Unset = UNSET
    memory: SessionMemorySettings | Unset | None = UNSET
    options: RunOptionsInput | Unset = UNSET
    thread_id: str | Unset | None = UNSET
    transport: Transport | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.session_memory_settings import SessionMemorySettings
        from ..models.usage_limit import UsageLimit

        agent_id = self.agent_id

        agent_revision_id: str | Unset | None
        if isinstance(self.agent_revision_id, Unset):
            agent_revision_id = UNSET
        else:
            agent_revision_id = self.agent_revision_id

        audio = self.audio

        draft = self.draft

        environments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.environments, Unset):
            environments = []
            for componentsschemas_initial_mounts_item_data in self.environments:
                componentsschemas_initial_mounts_item = componentsschemas_initial_mounts_item_data.to_dict()
                environments.append(componentsschemas_initial_mounts_item)

        fork_run_id: str | Unset | None
        if isinstance(self.fork_run_id, Unset):
            fork_run_id = UNSET
        else:
            fork_run_id = self.fork_run_id

        fresh_environments = self.fresh_environments

        max_usage: dict[str, Any] | Unset | None
        if isinstance(self.max_usage, Unset):
            max_usage = UNSET
        elif isinstance(self.max_usage, UsageLimit):
            max_usage = self.max_usage.to_dict()
        else:
            max_usage = self.max_usage

        memories: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.memories, Unset):
            memories = []
            for memories_item_data in self.memories:
                memories_item = memories_item_data.to_dict()
                memories.append(memories_item)

        memory: dict[str, Any] | Unset | None
        if isinstance(self.memory, Unset):
            memory = UNSET
        elif isinstance(self.memory, SessionMemorySettings):
            memory = self.memory.to_dict()
        else:
            memory = self.memory

        options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        thread_id: str | Unset | None
        if isinstance(self.thread_id, Unset):
            thread_id = UNSET
        else:
            thread_id = self.thread_id

        transport: str | Unset = UNSET
        if not isinstance(self.transport, Unset):
            transport = self.transport.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "agent_id": agent_id,
            }
        )
        if agent_revision_id is not UNSET:
            field_dict["agent_revision_id"] = agent_revision_id
        if audio is not UNSET:
            field_dict["audio"] = audio
        if draft is not UNSET:
            field_dict["draft"] = draft
        if environments is not UNSET:
            field_dict["environments"] = environments
        if fork_run_id is not UNSET:
            field_dict["fork_run_id"] = fork_run_id
        if fresh_environments is not UNSET:
            field_dict["fresh_environments"] = fresh_environments
        if max_usage is not UNSET:
            field_dict["max_usage"] = max_usage
        if memories is not UNSET:
            field_dict["memories"] = memories
        if memory is not UNSET:
            field_dict["memory"] = memory
        if options is not UNSET:
            field_dict["options"] = options
        if thread_id is not UNSET:
            field_dict["thread_id"] = thread_id
        if transport is not UNSET:
            field_dict["transport"] = transport

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.memory_mount import MemoryMount
        from ..models.mount_create import MountCreate
        from ..models.run_options_input import RunOptionsInput
        from ..models.session_memory_settings import SessionMemorySettings
        from ..models.usage_limit import UsageLimit

        d = dict(src_dict)
        agent_id = d.pop("agent_id")

        def _parse_agent_revision_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        agent_revision_id = _parse_agent_revision_id(d.pop("agent_revision_id", UNSET))

        audio = d.pop("audio", UNSET)

        draft = d.pop("draft", UNSET)

        _environments = d.pop("environments", UNSET)
        environments: list[MountCreate] | Unset = UNSET
        if _environments is not UNSET:
            environments = []
            for componentsschemas_initial_mounts_item_data in _environments:
                componentsschemas_initial_mounts_item = MountCreate.from_dict(
                    componentsschemas_initial_mounts_item_data
                )

                environments.append(componentsschemas_initial_mounts_item)

        def _parse_fork_run_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        fork_run_id = _parse_fork_run_id(d.pop("fork_run_id", UNSET))

        fresh_environments = d.pop("fresh_environments", UNSET)

        def _parse_max_usage(data: object) -> Unset | UsageLimit | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                max_usage_type_0 = UsageLimit.from_dict(data)

                return max_usage_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Unset | UsageLimit | None, data)

        max_usage = _parse_max_usage(d.pop("max_usage", UNSET))

        _memories = d.pop("memories", UNSET)
        memories: list[MemoryMount] | Unset = UNSET
        if _memories is not UNSET:
            memories = []
            for memories_item_data in _memories:
                memories_item = MemoryMount.from_dict(memories_item_data)

                memories.append(memories_item)

        def _parse_memory(data: object) -> SessionMemorySettings | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                memory_type_0 = SessionMemorySettings.from_dict(data)

                return memory_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(SessionMemorySettings | Unset | None, data)

        memory = _parse_memory(d.pop("memory", UNSET))

        _options = d.pop("options", UNSET)
        options: RunOptionsInput | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = RunOptionsInput.from_dict(_options)

        def _parse_thread_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        thread_id = _parse_thread_id(d.pop("thread_id", UNSET))

        _transport = d.pop("transport", UNSET)
        transport: Transport | Unset
        if isinstance(_transport, Unset):
            transport = UNSET
        else:
            transport = Transport(_transport)

        realtime_session_create = cls(
            agent_id=agent_id,
            agent_revision_id=agent_revision_id,
            audio=audio,
            draft=draft,
            environments=environments,
            fork_run_id=fork_run_id,
            fresh_environments=fresh_environments,
            max_usage=max_usage,
            memories=memories,
            memory=memory,
            options=options,
            thread_id=thread_id,
            transport=transport,
        )

        return realtime_session_create
