from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_config_input import AgentConfigInput
    from ..models.create_agent_request_labels import CreateAgentRequestLabels


T = TypeVar("T", bound="CreateAgentRequest")


@_attrs_define(repr=False)
class CreateAgentRequest:
    """
    Attributes:
        config (AgentConfigInput):
        name (str):
        description (None | str | Unset):
        key (None | str | Unset):
        labels (CreateAgentRequestLabels | Unset):
    """

    config: AgentConfigInput
    name: str
    description: str | Unset | None = UNSET
    key: str | Unset | None = UNSET
    labels: CreateAgentRequestLabels | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        config = self.config.to_dict()

        name = self.name

        description: str | Unset | None
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        key: str | Unset | None
        if isinstance(self.key, Unset):
            key = UNSET
        else:
            key = self.key

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "config": config,
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if key is not UNSET:
            field_dict["key"] = key
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_config_input import AgentConfigInput
        from ..models.create_agent_request_labels import CreateAgentRequestLabels

        d = dict(src_dict)
        config = AgentConfigInput.from_dict(d.pop("config"))

        name = d.pop("name")

        def _parse_description(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_key(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        key = _parse_key(d.pop("key", UNSET))

        _labels = d.pop("labels", UNSET)
        labels: CreateAgentRequestLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = CreateAgentRequestLabels.from_dict(_labels)

        create_agent_request = cls(
            config=config,
            name=name,
            description=description,
            key=key,
            labels=labels,
        )

        return create_agent_request
