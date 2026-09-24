from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_config_input import AgentConfigInput
    from ..models.agent_create_labels import AgentCreateLabels


T = TypeVar("T", bound="AgentCreate")


@_attrs_define(repr=False)
class AgentCreate:
    """
    Attributes:
        config (AgentConfigInput):
        key (str):
        name (str):
        description (str | Unset):
        labels (AgentCreateLabels | Unset):
    """

    config: AgentConfigInput
    key: str
    name: str
    description: str | Unset = UNSET
    labels: AgentCreateLabels | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        config = self.config.to_dict()

        key = self.key

        name = self.name

        description = self.description

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "config": config,
                "key": key,
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_config_input import AgentConfigInput
        from ..models.agent_create_labels import AgentCreateLabels

        d = dict(src_dict)
        config = AgentConfigInput.from_dict(d.pop("config"))

        key = d.pop("key")

        name = d.pop("name")

        description = d.pop("description", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: AgentCreateLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = AgentCreateLabels.from_dict(_labels)

        agent_create = cls(
            config=config,
            key=key,
            name=name,
            description=description,
            labels=labels,
        )

        return agent_create
