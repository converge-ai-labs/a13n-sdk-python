from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_model_characteristics import AgentModelCharacteristics
    from ..models.agent_override_output_model_settings_type_0 import AgentOverrideOutputModelSettingsType0
    from ..models.agent_override_output_subagents_type_0 import AgentOverrideOutputSubagentsType0
    from ..models.agent_override_output_toolsets_type_0 import AgentOverrideOutputToolsetsType0
    from ..models.agent_reviewer import AgentReviewer
    from ..models.client_tool_definition import ClientToolDefinition
    from ..models.connection_selection import ConnectionSelection
    from ..models.media_understanding_selection import MediaUnderstandingSelection
    from ..models.output_spec import OutputSpec
    from ..models.plugin_selection import PluginSelection
    from ..models.retry_override import RetryOverride
    from ..models.skill_selection import SkillSelection


T = TypeVar("T", bound="AgentOverrideOutput")


@_attrs_define(repr=False)
class AgentOverrideOutput:
    """What one run changes of its revision's configuration; an omitted or null field keeps the revision's.

    `toolsets` replaces whole toolsets; `retries` and each subagent edge replace the fields they set, and a null
    edge removes it; every other field replaces the revision's value.

        Attributes:
            client_tools (list[ClientToolDefinition] | None | Unset):
            connection_tools (list[ConnectionSelection] | None | Unset):
            instructions (None | str | Unset):
            media_understanding (MediaUnderstandingSelection | None | Unset):
            model (None | str | Unset):
            model_characteristics (AgentModelCharacteristics | None | Unset):
            model_settings (AgentOverrideOutputModelSettingsType0 | None | Unset):
            output_spec (None | OutputSpec | Unset):
            plugins (list[PluginSelection] | None | Unset):
            retries (None | RetryOverride | Unset):
            reviewer (AgentReviewer | None | Unset):
            skills (list[SkillSelection] | None | Unset):
            subagents (AgentOverrideOutputSubagentsType0 | None | Unset):
            toolsets (AgentOverrideOutputToolsetsType0 | None | Unset):
    """

    client_tools: list[ClientToolDefinition] | Unset | None = UNSET
    connection_tools: list[ConnectionSelection] | Unset | None = UNSET
    instructions: str | Unset | None = UNSET
    media_understanding: MediaUnderstandingSelection | Unset | None = UNSET
    model: str | Unset | None = UNSET
    model_characteristics: AgentModelCharacteristics | Unset | None = UNSET
    model_settings: AgentOverrideOutputModelSettingsType0 | Unset | None = UNSET
    output_spec: OutputSpec | Unset | None = UNSET
    plugins: list[PluginSelection] | Unset | None = UNSET
    retries: RetryOverride | Unset | None = UNSET
    reviewer: AgentReviewer | Unset | None = UNSET
    skills: list[SkillSelection] | Unset | None = UNSET
    subagents: AgentOverrideOutputSubagentsType0 | Unset | None = UNSET
    toolsets: AgentOverrideOutputToolsetsType0 | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_model_characteristics import AgentModelCharacteristics
        from ..models.agent_override_output_model_settings_type_0 import (
            AgentOverrideOutputModelSettingsType0,
        )
        from ..models.agent_override_output_subagents_type_0 import AgentOverrideOutputSubagentsType0
        from ..models.agent_override_output_toolsets_type_0 import AgentOverrideOutputToolsetsType0
        from ..models.agent_reviewer import AgentReviewer
        from ..models.media_understanding_selection import MediaUnderstandingSelection
        from ..models.output_spec import OutputSpec
        from ..models.retry_override import RetryOverride

        client_tools: list[dict[str, Any]] | Unset | None
        if isinstance(self.client_tools, Unset):
            client_tools = UNSET
        elif isinstance(self.client_tools, list):
            client_tools = []
            for client_tools_type_0_item_data in self.client_tools:
                client_tools_type_0_item = client_tools_type_0_item_data.to_dict()
                client_tools.append(client_tools_type_0_item)

        else:
            client_tools = self.client_tools

        connection_tools: list[dict[str, Any]] | Unset | None
        if isinstance(self.connection_tools, Unset):
            connection_tools = UNSET
        elif isinstance(self.connection_tools, list):
            connection_tools = []
            for connection_tools_type_0_item_data in self.connection_tools:
                connection_tools_type_0_item = connection_tools_type_0_item_data.to_dict()
                connection_tools.append(connection_tools_type_0_item)

        else:
            connection_tools = self.connection_tools

        instructions: str | Unset | None
        if isinstance(self.instructions, Unset):
            instructions = UNSET
        else:
            instructions = self.instructions

        media_understanding: dict[str, Any] | Unset | None
        if isinstance(self.media_understanding, Unset):
            media_understanding = UNSET
        elif isinstance(self.media_understanding, MediaUnderstandingSelection):
            media_understanding = self.media_understanding.to_dict()
        else:
            media_understanding = self.media_understanding

        model: str | Unset | None
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        model_characteristics: dict[str, Any] | Unset | None
        if isinstance(self.model_characteristics, Unset):
            model_characteristics = UNSET
        elif isinstance(self.model_characteristics, AgentModelCharacteristics):
            model_characteristics = self.model_characteristics.to_dict()
        else:
            model_characteristics = self.model_characteristics

        model_settings: dict[str, Any] | Unset | None
        if isinstance(self.model_settings, Unset):
            model_settings = UNSET
        elif isinstance(self.model_settings, AgentOverrideOutputModelSettingsType0):
            model_settings = self.model_settings.to_dict()
        else:
            model_settings = self.model_settings

        output_spec: dict[str, Any] | Unset | None
        if isinstance(self.output_spec, Unset):
            output_spec = UNSET
        elif isinstance(self.output_spec, OutputSpec):
            output_spec = self.output_spec.to_dict()
        else:
            output_spec = self.output_spec

        plugins: list[dict[str, Any]] | Unset | None
        if isinstance(self.plugins, Unset):
            plugins = UNSET
        elif isinstance(self.plugins, list):
            plugins = []
            for plugins_type_0_item_data in self.plugins:
                plugins_type_0_item = plugins_type_0_item_data.to_dict()
                plugins.append(plugins_type_0_item)

        else:
            plugins = self.plugins

        retries: dict[str, Any] | Unset | None
        if isinstance(self.retries, Unset):
            retries = UNSET
        elif isinstance(self.retries, RetryOverride):
            retries = self.retries.to_dict()
        else:
            retries = self.retries

        reviewer: dict[str, Any] | Unset | None
        if isinstance(self.reviewer, Unset):
            reviewer = UNSET
        elif isinstance(self.reviewer, AgentReviewer):
            reviewer = self.reviewer.to_dict()
        else:
            reviewer = self.reviewer

        skills: list[dict[str, Any]] | Unset | None
        if isinstance(self.skills, Unset):
            skills = UNSET
        elif isinstance(self.skills, list):
            skills = []
            for skills_type_0_item_data in self.skills:
                skills_type_0_item = skills_type_0_item_data.to_dict()
                skills.append(skills_type_0_item)

        else:
            skills = self.skills

        subagents: dict[str, Any] | Unset | None
        if isinstance(self.subagents, Unset):
            subagents = UNSET
        elif isinstance(self.subagents, AgentOverrideOutputSubagentsType0):
            subagents = self.subagents.to_dict()
        else:
            subagents = self.subagents

        toolsets: dict[str, Any] | Unset | None
        if isinstance(self.toolsets, Unset):
            toolsets = UNSET
        elif isinstance(self.toolsets, AgentOverrideOutputToolsetsType0):
            toolsets = self.toolsets.to_dict()
        else:
            toolsets = self.toolsets

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if client_tools is not UNSET:
            field_dict["client_tools"] = client_tools
        if connection_tools is not UNSET:
            field_dict["connection_tools"] = connection_tools
        if instructions is not UNSET:
            field_dict["instructions"] = instructions
        if media_understanding is not UNSET:
            field_dict["media_understanding"] = media_understanding
        if model is not UNSET:
            field_dict["model"] = model
        if model_characteristics is not UNSET:
            field_dict["model_characteristics"] = model_characteristics
        if model_settings is not UNSET:
            field_dict["model_settings"] = model_settings
        if output_spec is not UNSET:
            field_dict["output_spec"] = output_spec
        if plugins is not UNSET:
            field_dict["plugins"] = plugins
        if retries is not UNSET:
            field_dict["retries"] = retries
        if reviewer is not UNSET:
            field_dict["reviewer"] = reviewer
        if skills is not UNSET:
            field_dict["skills"] = skills
        if subagents is not UNSET:
            field_dict["subagents"] = subagents
        if toolsets is not UNSET:
            field_dict["toolsets"] = toolsets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_model_characteristics import AgentModelCharacteristics
        from ..models.agent_override_output_model_settings_type_0 import (
            AgentOverrideOutputModelSettingsType0,
        )
        from ..models.agent_override_output_subagents_type_0 import AgentOverrideOutputSubagentsType0
        from ..models.agent_override_output_toolsets_type_0 import AgentOverrideOutputToolsetsType0
        from ..models.agent_reviewer import AgentReviewer
        from ..models.client_tool_definition import ClientToolDefinition
        from ..models.connection_selection import ConnectionSelection
        from ..models.media_understanding_selection import MediaUnderstandingSelection
        from ..models.output_spec import OutputSpec
        from ..models.plugin_selection import PluginSelection
        from ..models.retry_override import RetryOverride
        from ..models.skill_selection import SkillSelection

        d = dict(src_dict)

        def _parse_client_tools(data: object) -> list[ClientToolDefinition] | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                client_tools_type_0 = []
                _client_tools_type_0 = data
                for client_tools_type_0_item_data in _client_tools_type_0:
                    client_tools_type_0_item = ClientToolDefinition.from_dict(client_tools_type_0_item_data)

                    client_tools_type_0.append(client_tools_type_0_item)

                return client_tools_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ClientToolDefinition] | Unset | None, data)

        client_tools = _parse_client_tools(d.pop("client_tools", UNSET))

        def _parse_connection_tools(data: object) -> list[ConnectionSelection] | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                connection_tools_type_0 = []
                _connection_tools_type_0 = data
                for connection_tools_type_0_item_data in _connection_tools_type_0:
                    connection_tools_type_0_item = ConnectionSelection.from_dict(connection_tools_type_0_item_data)

                    connection_tools_type_0.append(connection_tools_type_0_item)

                return connection_tools_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ConnectionSelection] | Unset | None, data)

        connection_tools = _parse_connection_tools(d.pop("connection_tools", UNSET))

        def _parse_instructions(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        instructions = _parse_instructions(d.pop("instructions", UNSET))

        def _parse_media_understanding(data: object) -> MediaUnderstandingSelection | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                media_understanding_type_0 = MediaUnderstandingSelection.from_dict(data)

                return media_understanding_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MediaUnderstandingSelection | Unset | None, data)

        media_understanding = _parse_media_understanding(d.pop("media_understanding", UNSET))

        def _parse_model(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        model = _parse_model(d.pop("model", UNSET))

        def _parse_model_characteristics(data: object) -> AgentModelCharacteristics | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_characteristics_type_0 = AgentModelCharacteristics.from_dict(data)

                return model_characteristics_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentModelCharacteristics | Unset | None, data)

        model_characteristics = _parse_model_characteristics(d.pop("model_characteristics", UNSET))

        def _parse_model_settings(data: object) -> AgentOverrideOutputModelSettingsType0 | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_settings_type_0 = AgentOverrideOutputModelSettingsType0.from_dict(data)

                return model_settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentOverrideOutputModelSettingsType0 | Unset | None, data)

        model_settings = _parse_model_settings(d.pop("model_settings", UNSET))

        def _parse_output_spec(data: object) -> OutputSpec | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                output_spec_type_0 = OutputSpec.from_dict(data)

                return output_spec_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(OutputSpec | Unset | None, data)

        output_spec = _parse_output_spec(d.pop("output_spec", UNSET))

        def _parse_plugins(data: object) -> list[PluginSelection] | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                plugins_type_0 = []
                _plugins_type_0 = data
                for plugins_type_0_item_data in _plugins_type_0:
                    plugins_type_0_item = PluginSelection.from_dict(plugins_type_0_item_data)

                    plugins_type_0.append(plugins_type_0_item)

                return plugins_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PluginSelection] | Unset | None, data)

        plugins = _parse_plugins(d.pop("plugins", UNSET))

        def _parse_retries(data: object) -> RetryOverride | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                retries_type_0 = RetryOverride.from_dict(data)

                return retries_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(RetryOverride | Unset | None, data)

        retries = _parse_retries(d.pop("retries", UNSET))

        def _parse_reviewer(data: object) -> AgentReviewer | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                reviewer_type_0 = AgentReviewer.from_dict(data)

                return reviewer_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentReviewer | Unset | None, data)

        reviewer = _parse_reviewer(d.pop("reviewer", UNSET))

        def _parse_skills(data: object) -> list[SkillSelection] | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                skills_type_0 = []
                _skills_type_0 = data
                for skills_type_0_item_data in _skills_type_0:
                    skills_type_0_item = SkillSelection.from_dict(skills_type_0_item_data)

                    skills_type_0.append(skills_type_0_item)

                return skills_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SkillSelection] | Unset | None, data)

        skills = _parse_skills(d.pop("skills", UNSET))

        def _parse_subagents(data: object) -> AgentOverrideOutputSubagentsType0 | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                subagents_type_0 = AgentOverrideOutputSubagentsType0.from_dict(data)

                return subagents_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentOverrideOutputSubagentsType0 | Unset | None, data)

        subagents = _parse_subagents(d.pop("subagents", UNSET))

        def _parse_toolsets(data: object) -> AgentOverrideOutputToolsetsType0 | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                toolsets_type_0 = AgentOverrideOutputToolsetsType0.from_dict(data)

                return toolsets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentOverrideOutputToolsetsType0 | Unset | None, data)

        toolsets = _parse_toolsets(d.pop("toolsets", UNSET))

        agent_override_output = cls(
            client_tools=client_tools,
            connection_tools=connection_tools,
            instructions=instructions,
            media_understanding=media_understanding,
            model=model,
            model_characteristics=model_characteristics,
            model_settings=model_settings,
            output_spec=output_spec,
            plugins=plugins,
            retries=retries,
            reviewer=reviewer,
            skills=skills,
            subagents=subagents,
            toolsets=toolsets,
        )

        return agent_override_output
