from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.item_kind import ItemKind
from ..models.item_state import ItemState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.preview import Preview


T = TypeVar("T", bound="ItemSummary")


@_attrs_define(repr=False)
class ItemSummary:
    """
    Attributes:
        arguments (Preview):
        ended_at (datetime.datetime | None):
        id (str):
        kind (ItemKind):
        ordinal (int):
        result (Preview):
        source_truncated (bool):
        source_truncated_fields (list[str]):
        started_at (datetime.datetime):
        state (ItemState):
        text (Preview):
        tool_call_id (None | str):
        tool_name (None | str):
        omitted_sections (list[str] | Unset):
    """

    arguments: Preview
    ended_at: datetime.datetime | None
    id: str
    kind: ItemKind
    ordinal: int
    result: Preview
    source_truncated: bool
    source_truncated_fields: list[str]
    started_at: datetime.datetime
    state: ItemState
    text: Preview
    tool_call_id: str | None
    tool_name: str | None
    omitted_sections: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        arguments = self.arguments.to_dict()

        ended_at: str | None
        if isinstance(self.ended_at, datetime.datetime):
            ended_at = self.ended_at.isoformat()
        else:
            ended_at = self.ended_at

        id = self.id

        kind = self.kind.value

        ordinal = self.ordinal

        result = self.result.to_dict()

        source_truncated = self.source_truncated

        source_truncated_fields = self.source_truncated_fields

        started_at = self.started_at.isoformat()

        state = self.state.value

        text = self.text.to_dict()

        tool_call_id: str | None
        tool_call_id = self.tool_call_id

        tool_name: str | None
        tool_name = self.tool_name

        omitted_sections: list[str] | Unset = UNSET
        if not isinstance(self.omitted_sections, Unset):
            omitted_sections = self.omitted_sections

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "arguments": arguments,
                "ended_at": ended_at,
                "id": id,
                "kind": kind,
                "ordinal": ordinal,
                "result": result,
                "source_truncated": source_truncated,
                "source_truncated_fields": source_truncated_fields,
                "started_at": started_at,
                "state": state,
                "text": text,
                "tool_call_id": tool_call_id,
                "tool_name": tool_name,
            }
        )
        if omitted_sections is not UNSET:
            field_dict["omitted_sections"] = omitted_sections

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.preview import Preview

        d = dict(src_dict)
        arguments = Preview.from_dict(d.pop("arguments"))

        def _parse_ended_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ended_at_type_0 = datetime.datetime.fromisoformat(data)

                return ended_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        ended_at = _parse_ended_at(d.pop("ended_at"))

        id = d.pop("id")

        kind = ItemKind(d.pop("kind"))

        ordinal = d.pop("ordinal")

        result = Preview.from_dict(d.pop("result"))

        source_truncated = d.pop("source_truncated")

        source_truncated_fields = cast(list[str], d.pop("source_truncated_fields"))

        started_at = datetime.datetime.fromisoformat(d.pop("started_at"))

        state = ItemState(d.pop("state"))

        text = Preview.from_dict(d.pop("text"))

        def _parse_tool_call_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        tool_call_id = _parse_tool_call_id(d.pop("tool_call_id"))

        def _parse_tool_name(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        tool_name = _parse_tool_name(d.pop("tool_name"))

        omitted_sections = cast(list[str], d.pop("omitted_sections", UNSET))

        item_summary = cls(
            arguments=arguments,
            ended_at=ended_at,
            id=id,
            kind=kind,
            ordinal=ordinal,
            result=result,
            source_truncated=source_truncated,
            source_truncated_fields=source_truncated_fields,
            started_at=started_at,
            state=state,
            text=text,
            tool_call_id=tool_call_id,
            tool_name=tool_name,
            omitted_sections=omitted_sections,
        )

        item_summary.additional_properties = d
        return item_summary

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
