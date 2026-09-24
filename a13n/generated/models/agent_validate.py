from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_config_input import AgentConfigInput


T = TypeVar("T", bound="AgentValidate")


@_attrs_define(repr=False)
class AgentValidate:
    """A configuration to check as creating a revision would, storing nothing.

    `agent_id` names the agent it would become a revision of, whose inline subagents may not lead back to it;
    omit it for a new agent.

        Attributes:
            config (AgentConfigInput):
            agent_id (None | str | Unset):
    """

    config: AgentConfigInput
    agent_id: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        config = self.config.to_dict()

        agent_id: str | Unset | None
        if isinstance(self.agent_id, Unset):
            agent_id = UNSET
        else:
            agent_id = self.agent_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "config": config,
            }
        )
        if agent_id is not UNSET:
            field_dict["agent_id"] = agent_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_config_input import AgentConfigInput

        d = dict(src_dict)
        config = AgentConfigInput.from_dict(d.pop("config"))

        def _parse_agent_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        agent_id = _parse_agent_id(d.pop("agent_id", UNSET))

        agent_validate = cls(
            config=config,
            agent_id=agent_id,
        )

        return agent_validate
