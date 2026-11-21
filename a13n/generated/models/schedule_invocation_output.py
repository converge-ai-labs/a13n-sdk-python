from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.browser_binding import BrowserBinding
    from ..models.memory_mount import MemoryMount
    from ..models.message_payload import MessagePayload
    from ..models.mount_create import MountCreate
    from ..models.run_options_output import RunOptionsOutput


T = TypeVar("T", bound="ScheduleInvocationOutput")


@_attrs_define(repr=False)
class ScheduleInvocationOutput:
    """
    Attributes:
        agent_id (str):
        agent_revision_id (None | str):
        payload (MessagePayload):
        browser_binding (BrowserBinding | None | Unset):
        environments (list[MountCreate] | Unset):
        memories (list[MemoryMount] | Unset):
        options (RunOptionsOutput | Unset): What a message may choose for the run it starts. A steer joins a run with
            the defaults or equal options.
    """

    agent_id: str
    agent_revision_id: str | None
    payload: MessagePayload
    browser_binding: BrowserBinding | Unset | None = UNSET
    environments: list[MountCreate] | Unset = UNSET
    memories: list[MemoryMount] | Unset = UNSET
    options: RunOptionsOutput | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.browser_binding import BrowserBinding

        agent_id = self.agent_id

        agent_revision_id: str | None
        agent_revision_id = self.agent_revision_id

        payload = self.payload.to_dict()

        browser_binding: dict[str, Any] | Unset | None
        if isinstance(self.browser_binding, Unset):
            browser_binding = UNSET
        elif isinstance(self.browser_binding, BrowserBinding):
            browser_binding = self.browser_binding.to_dict()
        else:
            browser_binding = self.browser_binding

        environments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.environments, Unset):
            environments = []
            for componentsschemas_initial_mounts_item_data in self.environments:
                componentsschemas_initial_mounts_item = componentsschemas_initial_mounts_item_data.to_dict()
                environments.append(componentsschemas_initial_mounts_item)

        memories: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.memories, Unset):
            memories = []
            for memories_item_data in self.memories:
                memories_item = memories_item_data.to_dict()
                memories.append(memories_item)

        options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "agent_id": agent_id,
                "agent_revision_id": agent_revision_id,
                "payload": payload,
            }
        )
        if browser_binding is not UNSET:
            field_dict["browser_binding"] = browser_binding
        if environments is not UNSET:
            field_dict["environments"] = environments
        if memories is not UNSET:
            field_dict["memories"] = memories
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.browser_binding import BrowserBinding
        from ..models.memory_mount import MemoryMount
        from ..models.message_payload import MessagePayload
        from ..models.mount_create import MountCreate
        from ..models.run_options_output import RunOptionsOutput

        d = dict(src_dict)
        agent_id = d.pop("agent_id")

        def _parse_agent_revision_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        agent_revision_id = _parse_agent_revision_id(d.pop("agent_revision_id"))

        payload = MessagePayload.from_dict(d.pop("payload"))

        def _parse_browser_binding(data: object) -> BrowserBinding | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                browser_binding_type_0 = BrowserBinding.from_dict(data)

                return browser_binding_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BrowserBinding | Unset | None, data)

        browser_binding = _parse_browser_binding(d.pop("browser_binding", UNSET))

        _environments = d.pop("environments", UNSET)
        environments: list[MountCreate] | Unset = UNSET
        if _environments is not UNSET:
            environments = []
            for componentsschemas_initial_mounts_item_data in _environments:
                componentsschemas_initial_mounts_item = MountCreate.from_dict(
                    componentsschemas_initial_mounts_item_data
                )

                environments.append(componentsschemas_initial_mounts_item)

        _memories = d.pop("memories", UNSET)
        memories: list[MemoryMount] | Unset = UNSET
        if _memories is not UNSET:
            memories = []
            for memories_item_data in _memories:
                memories_item = MemoryMount.from_dict(memories_item_data)

                memories.append(memories_item)

        _options = d.pop("options", UNSET)
        options: RunOptionsOutput | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = RunOptionsOutput.from_dict(_options)

        schedule_invocation_output = cls(
            agent_id=agent_id,
            agent_revision_id=agent_revision_id,
            payload=payload,
            browser_binding=browser_binding,
            environments=environments,
            memories=memories,
            options=options,
        )

        return schedule_invocation_output
