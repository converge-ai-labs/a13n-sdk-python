from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_duplicate_labels import AgentDuplicateLabels


T = TypeVar("T", bound="AgentDuplicate")


@_attrs_define(repr=False)
class AgentDuplicate:
    """A new head whose first revision copies `revision_id`, by default the source's default revision.

    Attributes:
        name (str):
        description (str | Unset):
        labels (AgentDuplicateLabels | Unset):
        revision_id (None | str | Unset):
    """

    name: str
    description: str | Unset = UNSET
    labels: AgentDuplicateLabels | Unset = UNSET
    revision_id: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        revision_id: str | Unset | None
        if isinstance(self.revision_id, Unset):
            revision_id = UNSET
        else:
            revision_id = self.revision_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if labels is not UNSET:
            field_dict["labels"] = labels
        if revision_id is not UNSET:
            field_dict["revision_id"] = revision_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_duplicate_labels import AgentDuplicateLabels

        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: AgentDuplicateLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = AgentDuplicateLabels.from_dict(_labels)

        def _parse_revision_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        revision_id = _parse_revision_id(d.pop("revision_id", UNSET))

        agent_duplicate = cls(
            name=name,
            description=description,
            labels=labels,
            revision_id=revision_id,
        )

        return agent_duplicate
