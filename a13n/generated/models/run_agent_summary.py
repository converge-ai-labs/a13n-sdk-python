from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_summary import ConfigSummary


T = TypeVar("T", bound="RunAgentSummary")


@_attrs_define(repr=False)
class RunAgentSummary:
    """
    Attributes:
        config (ConfigSummary):
        connection_ids (list[str]):
        overridden_paths (list[str]):
        references_truncated (bool):
        revision_id (str):
        skill_ids (list[str]):
        subagent_ids (list[str]):
        omitted_sections (list[str] | Unset):
        view (Literal['compact'] | Unset):
    """

    config: ConfigSummary
    connection_ids: list[str]
    overridden_paths: list[str]
    references_truncated: bool
    revision_id: str
    skill_ids: list[str]
    subagent_ids: list[str]
    omitted_sections: list[str] | Unset = UNSET
    view: Literal["compact"] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config = self.config.to_dict()

        connection_ids = self.connection_ids

        overridden_paths = self.overridden_paths

        references_truncated = self.references_truncated

        revision_id = self.revision_id

        skill_ids = self.skill_ids

        subagent_ids = self.subagent_ids

        omitted_sections: list[str] | Unset = UNSET
        if not isinstance(self.omitted_sections, Unset):
            omitted_sections = self.omitted_sections

        view = self.view

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config": config,
                "connection_ids": connection_ids,
                "overridden_paths": overridden_paths,
                "references_truncated": references_truncated,
                "revision_id": revision_id,
                "skill_ids": skill_ids,
                "subagent_ids": subagent_ids,
            }
        )
        if omitted_sections is not UNSET:
            field_dict["omitted_sections"] = omitted_sections
        if view is not UNSET:
            field_dict["view"] = view

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_summary import ConfigSummary

        d = dict(src_dict)
        config = ConfigSummary.from_dict(d.pop("config"))

        connection_ids = cast(list[str], d.pop("connection_ids"))

        overridden_paths = cast(list[str], d.pop("overridden_paths"))

        references_truncated = d.pop("references_truncated")

        revision_id = d.pop("revision_id")

        skill_ids = cast(list[str], d.pop("skill_ids"))

        subagent_ids = cast(list[str], d.pop("subagent_ids"))

        omitted_sections = cast(list[str], d.pop("omitted_sections", UNSET))

        view = cast(Literal["compact"] | Unset, d.pop("view", UNSET))
        if view != "compact" and not isinstance(view, Unset):
            raise ValueError(f"view must match const 'compact', got '{view}'")

        run_agent_summary = cls(
            config=config,
            connection_ids=connection_ids,
            overridden_paths=overridden_paths,
            references_truncated=references_truncated,
            revision_id=revision_id,
            skill_ids=skill_ids,
            subagent_ids=subagent_ids,
            omitted_sections=omitted_sections,
            view=view,
        )

        run_agent_summary.additional_properties = d
        return run_agent_summary

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
