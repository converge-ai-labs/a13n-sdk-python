from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_config_input import AgentConfigInput


T = TypeVar("T", bound="AgentRevisionCreate")


@_attrs_define(repr=False)
class AgentRevisionCreate:
    """
    Attributes:
        config (AgentConfigInput):
        make_default (bool | Unset):
        note (None | str | Unset):
    """

    config: AgentConfigInput
    make_default: bool | Unset = UNSET
    note: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        config = self.config.to_dict()

        make_default = self.make_default

        note: str | Unset | None
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "config": config,
            }
        )
        if make_default is not UNSET:
            field_dict["make_default"] = make_default
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_config_input import AgentConfigInput

        d = dict(src_dict)
        config = AgentConfigInput.from_dict(d.pop("config"))

        make_default = d.pop("make_default", UNSET)

        def _parse_note(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        note = _parse_note(d.pop("note", UNSET))

        agent_revision_create = cls(
            config=config,
            make_default=make_default,
            note=note,
        )

        return agent_revision_create
