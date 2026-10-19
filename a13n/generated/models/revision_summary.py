from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_summary import ConfigSummary
    from ..models.preview import Preview


T = TypeVar("T", bound="RevisionSummary")


@_attrs_define(repr=False)
class RevisionSummary:
    """
    Attributes:
        agent_id (str):
        config (ConfigSummary):
        created_at (datetime.datetime):
        digest (str):
        id (str):
        is_default (bool):
        note (Preview):
        number (int):
        omitted_sections (list[str] | Unset):
        view (Literal['compact'] | Unset):
    """

    agent_id: str
    config: ConfigSummary
    created_at: datetime.datetime
    digest: str
    id: str
    is_default: bool
    note: Preview
    number: int
    omitted_sections: list[str] | Unset = UNSET
    view: Literal["compact"] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_id = self.agent_id

        config = self.config.to_dict()

        created_at = self.created_at.isoformat()

        digest = self.digest

        id = self.id

        is_default = self.is_default

        note = self.note.to_dict()

        number = self.number

        omitted_sections: list[str] | Unset = UNSET
        if not isinstance(self.omitted_sections, Unset):
            omitted_sections = self.omitted_sections

        view = self.view

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_id": agent_id,
                "config": config,
                "created_at": created_at,
                "digest": digest,
                "id": id,
                "is_default": is_default,
                "note": note,
                "number": number,
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
        from ..models.preview import Preview

        d = dict(src_dict)
        agent_id = d.pop("agent_id")

        config = ConfigSummary.from_dict(d.pop("config"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        digest = d.pop("digest")

        id = d.pop("id")

        is_default = d.pop("is_default")

        note = Preview.from_dict(d.pop("note"))

        number = d.pop("number")

        omitted_sections = cast(list[str], d.pop("omitted_sections", UNSET))

        view = cast(Literal["compact"] | Unset, d.pop("view", UNSET))
        if view != "compact" and not isinstance(view, Unset):
            raise ValueError(f"view must match const 'compact', got '{view}'")

        revision_summary = cls(
            agent_id=agent_id,
            config=config,
            created_at=created_at,
            digest=digest,
            id=id,
            is_default=is_default,
            note=note,
            number=number,
            omitted_sections=omitted_sections,
            view=view,
        )

        revision_summary.additional_properties = d
        return revision_summary

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
