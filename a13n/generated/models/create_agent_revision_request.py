from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_config_input import AgentConfigInput


T = TypeVar("T", bound="CreateAgentRevisionRequest")


@_attrs_define(repr=False)
class CreateAgentRevisionRequest:
    """
    Attributes:
        config (AgentConfigInput):
        change_summary (None | str | Unset):
    """

    config: AgentConfigInput
    change_summary: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        config = self.config.to_dict()

        change_summary: str | Unset | None
        if isinstance(self.change_summary, Unset):
            change_summary = UNSET
        else:
            change_summary = self.change_summary

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "config": config,
            }
        )
        if change_summary is not UNSET:
            field_dict["change_summary"] = change_summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_config_input import AgentConfigInput

        d = dict(src_dict)
        config = AgentConfigInput.from_dict(d.pop("config"))

        def _parse_change_summary(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        change_summary = _parse_change_summary(d.pop("change_summary", UNSET))

        create_agent_revision_request = cls(
            config=config,
            change_summary=change_summary,
        )

        return create_agent_revision_request
