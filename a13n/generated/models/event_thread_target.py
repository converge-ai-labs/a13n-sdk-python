from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventThreadTarget")


@_attrs_define(repr=False)
class EventThreadTarget:
    """
    Attributes:
        agent_id (str):
        principal_id (str):
        agent_revision_id (None | str | Unset):
        instruction (str | Unset):
        mode (Literal['new_thread'] | Unset):
    """

    agent_id: str
    principal_id: str
    agent_revision_id: str | Unset | None = UNSET
    instruction: str | Unset = UNSET
    mode: Literal["new_thread"] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        agent_id = self.agent_id

        principal_id = self.principal_id

        agent_revision_id: str | Unset | None
        if isinstance(self.agent_revision_id, Unset):
            agent_revision_id = UNSET
        else:
            agent_revision_id = self.agent_revision_id

        instruction = self.instruction

        mode = self.mode

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "agent_id": agent_id,
                "principal_id": principal_id,
            }
        )
        if agent_revision_id is not UNSET:
            field_dict["agent_revision_id"] = agent_revision_id
        if instruction is not UNSET:
            field_dict["instruction"] = instruction
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        agent_id = d.pop("agent_id")

        principal_id = d.pop("principal_id")

        def _parse_agent_revision_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        agent_revision_id = _parse_agent_revision_id(d.pop("agent_revision_id", UNSET))

        instruction = d.pop("instruction", UNSET)

        mode = cast(Literal["new_thread"] | Unset, d.pop("mode", UNSET))
        if mode != "new_thread" and not isinstance(mode, Unset):
            raise ValueError(f"mode must match const 'new_thread', got '{mode}'")

        event_thread_target = cls(
            agent_id=agent_id,
            principal_id=principal_id,
            agent_revision_id=agent_revision_id,
            instruction=instruction,
            mode=mode,
        )

        return event_thread_target
