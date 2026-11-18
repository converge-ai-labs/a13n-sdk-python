from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.run_agent_source import RunAgentSource

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
            definition_id (str):
            revision (AgentRevision | None):
            source (RunAgentSource):
    """

    config: AgentConfigOutput
    definition_id: str
    revision: AgentRevision | None
    source: RunAgentSource
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_revision import AgentRevision

        config = self.config.to_dict()

        definition_id = self.definition_id

        revision: dict[str, Any] | None
        if isinstance(self.revision, AgentRevision):
            revision = self.revision.to_dict()
        else:
            revision = self.revision

        source = self.source.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config": config,
                "definition_id": definition_id,
                "revision": revision,
                "source": source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_config_output import AgentConfigOutput
        from ..models.agent_revision import AgentRevision

        d = dict(src_dict)
        config = AgentConfigOutput.from_dict(d.pop("config"))

        definition_id = d.pop("definition_id")

        def _parse_revision(data: object) -> AgentRevision | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                revision_type_0 = AgentRevision.from_dict(data)

                return revision_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentRevision | None, data)

        revision = _parse_revision(d.pop("revision"))

        source = RunAgentSource(d.pop("source"))

        run_agent = cls(
            config=config,
            definition_id=definition_id,
            revision=revision,
            source=source,
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
