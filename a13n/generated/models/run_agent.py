from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.agent_config_output import AgentConfigOutput
    from ..models.agent_revision import AgentRevision


T = TypeVar("T", bound="RunAgent")


@_attrs_define(repr=False)
class RunAgent:
    """The agent a run executes: its frozen revision, and that revision's configuration with the run's override
    applied. Models, connections and templates the configuration names stay live.

        Attributes:
            config (AgentConfigOutput):
            revision (AgentRevision):
    """

    config: AgentConfigOutput
    revision: AgentRevision
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config = self.config.to_dict()

        revision = self.revision.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config": config,
                "revision": revision,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_config_output import AgentConfigOutput
        from ..models.agent_revision import AgentRevision

        d = dict(src_dict)
        config = AgentConfigOutput.from_dict(d.pop("config"))

        revision = AgentRevision.from_dict(d.pop("revision"))

        run_agent = cls(
            config=config,
            revision=revision,
        )

        run_agent.additional_properties = d
        return run_agent

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
