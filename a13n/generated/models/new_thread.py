from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..models.delivery import Delivery
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mcp_headers import McpHeaders
    from ..models.memory_mount import MemoryMount
    from ..models.message_payload import MessagePayload
    from ..models.mount_create import MountCreate
    from ..models.run_options_input import RunOptionsInput


T = TypeVar("T", bound="NewThread")


@_attrs_define(repr=False)
class NewThread:
    """
    Attributes:
        agent_id (str):
        payload (MessagePayload):
        agent_revision_id (None | str | Unset):
        delivery (Delivery | Unset):
        environments (list[MountCreate] | Unset):
        kind (Literal['message'] | Unset):
        mcp_headers (McpHeaders | Unset):
        memories (list[MemoryMount] | Unset):
        options (RunOptionsInput | Unset): What a message may choose for the run it starts. A steer joins a run with the
            defaults or equal options.
        session_id (None | str | Unset):
    """

    agent_id: str
    payload: MessagePayload
    agent_revision_id: str | Unset | None = UNSET
    delivery: Delivery | Unset = UNSET
    environments: list[MountCreate] | Unset = UNSET
    kind: Literal["message"] | Unset = UNSET
    mcp_headers: McpHeaders | Unset = UNSET
    memories: list[MemoryMount] | Unset = UNSET
    options: RunOptionsInput | Unset = UNSET
    session_id: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        agent_id = self.agent_id

        payload = self.payload.to_dict()

        agent_revision_id: str | Unset | None
        if isinstance(self.agent_revision_id, Unset):
            agent_revision_id = UNSET
        else:
            agent_revision_id = self.agent_revision_id

        delivery: str | Unset = UNSET
        if not isinstance(self.delivery, Unset):
            delivery = self.delivery.value

        environments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.environments, Unset):
            environments = []
            for componentsschemas_initial_mounts_item_data in self.environments:
                componentsschemas_initial_mounts_item = componentsschemas_initial_mounts_item_data.to_dict()
                environments.append(componentsschemas_initial_mounts_item)

        kind = self.kind

        mcp_headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mcp_headers, Unset):
            mcp_headers = self.mcp_headers.to_dict()

        memories: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.memories, Unset):
            memories = []
            for memories_item_data in self.memories:
                memories_item = memories_item_data.to_dict()
                memories.append(memories_item)

        options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        session_id: str | Unset | None
        if isinstance(self.session_id, Unset):
            session_id = UNSET
        else:
            session_id = self.session_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "agent_id": agent_id,
                "payload": payload,
            }
        )
        if agent_revision_id is not UNSET:
            field_dict["agent_revision_id"] = agent_revision_id
        if delivery is not UNSET:
            field_dict["delivery"] = delivery
        if environments is not UNSET:
            field_dict["environments"] = environments
        if kind is not UNSET:
            field_dict["kind"] = kind
        if mcp_headers is not UNSET:
            field_dict["mcp_headers"] = mcp_headers
        if memories is not UNSET:
            field_dict["memories"] = memories
        if options is not UNSET:
            field_dict["options"] = options
        if session_id is not UNSET:
            field_dict["session_id"] = session_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mcp_headers import McpHeaders
        from ..models.memory_mount import MemoryMount
        from ..models.message_payload import MessagePayload
        from ..models.mount_create import MountCreate
        from ..models.run_options_input import RunOptionsInput

        d = dict(src_dict)
        agent_id = d.pop("agent_id")

        payload = MessagePayload.from_dict(d.pop("payload"))

        def _parse_agent_revision_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        agent_revision_id = _parse_agent_revision_id(d.pop("agent_revision_id", UNSET))

        _delivery = d.pop("delivery", UNSET)
        delivery: Delivery | Unset
        if isinstance(_delivery, Unset):
            delivery = UNSET
        else:
            delivery = Delivery(_delivery)

        _environments = d.pop("environments", UNSET)
        environments: list[MountCreate] | Unset = UNSET
        if _environments is not UNSET:
            environments = []
            for componentsschemas_initial_mounts_item_data in _environments:
                componentsschemas_initial_mounts_item = MountCreate.from_dict(
                    componentsschemas_initial_mounts_item_data
                )

                environments.append(componentsschemas_initial_mounts_item)

        kind = cast(Literal["message"] | Unset, d.pop("kind", UNSET))
        if kind != "message" and not isinstance(kind, Unset):
            raise ValueError(f"kind must match const 'message', got '{kind}'")

        _mcp_headers = d.pop("mcp_headers", UNSET)
        mcp_headers: McpHeaders | Unset
        if isinstance(_mcp_headers, Unset):
            mcp_headers = UNSET
        else:
            mcp_headers = McpHeaders.from_dict(_mcp_headers)

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

        def _parse_session_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        session_id = _parse_session_id(d.pop("session_id", UNSET))

        new_thread = cls(
            agent_id=agent_id,
            payload=payload,
            agent_revision_id=agent_revision_id,
            delivery=delivery,
            environments=environments,
            kind=kind,
            mcp_headers=mcp_headers,
            memories=memories,
            options=options,
            session_id=session_id,
        )

        return new_thread
