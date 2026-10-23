from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.memory_mount import MemoryMount
    from ..models.message_payload import MessagePayload
    from ..models.run_options_input import RunOptionsInput


T = TypeVar("T", bound="ScheduleInvocationInput")


@_attrs_define(repr=False)
class ScheduleInvocationInput:
    """
    Attributes:
        agent_id (str):
        agent_revision_id (None | str):
        payload (MessagePayload):
        memories (list[MemoryMount] | Unset):
        options (RunOptionsInput | Unset): What a message may choose for the run it starts. A steer joins a run with the
            defaults or equal options.
    """

    agent_id: str
    agent_revision_id: str | None
    payload: MessagePayload
    memories: list[MemoryMount] | Unset = UNSET
    options: RunOptionsInput | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        agent_id = self.agent_id

        agent_revision_id: str | None
        agent_revision_id = self.agent_revision_id

        payload = self.payload.to_dict()

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
        if memories is not UNSET:
            field_dict["memories"] = memories
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.memory_mount import MemoryMount
        from ..models.message_payload import MessagePayload
        from ..models.run_options_input import RunOptionsInput

        d = dict(src_dict)
        agent_id = d.pop("agent_id")

        def _parse_agent_revision_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        agent_revision_id = _parse_agent_revision_id(d.pop("agent_revision_id"))

        payload = MessagePayload.from_dict(d.pop("payload"))

        _memories = d.pop("memories", UNSET)
        memories: list[MemoryMount] | Unset = UNSET
        if _memories is not UNSET:
            memories = []
            for memories_item_data in _memories:
                memories_item = MemoryMount.from_dict(memories_item_data)

                memories.append(memories_item)

        _options = d.pop("options", UNSET)
        options: RunOptionsInput | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = RunOptionsInput.from_dict(_options)

        schedule_invocation_input = cls(
            agent_id=agent_id,
            agent_revision_id=agent_revision_id,
            payload=payload,
            memories=memories,
            options=options,
        )

        return schedule_invocation_input
