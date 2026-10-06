from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.part_cursor_kind import PartCursorKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="PartCursor")


@_attrs_define(repr=False)
class PartCursor:
    """
    Attributes:
        kind (PartCursorKind):
        part_id (str):
        emitted_content (bool | Unset):
        emitted_signature (bool | Unset):
        tool_name (None | str | Unset):
    """

    kind: PartCursorKind
    part_id: str
    emitted_content: bool | Unset = UNSET
    emitted_signature: bool | Unset = UNSET
    tool_name: str | Unset | None = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        part_id = self.part_id

        emitted_content = self.emitted_content

        emitted_signature = self.emitted_signature

        tool_name: str | Unset | None
        if isinstance(self.tool_name, Unset):
            tool_name = UNSET
        else:
            tool_name = self.tool_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "part_id": part_id,
            }
        )
        if emitted_content is not UNSET:
            field_dict["emitted_content"] = emitted_content
        if emitted_signature is not UNSET:
            field_dict["emitted_signature"] = emitted_signature
        if tool_name is not UNSET:
            field_dict["tool_name"] = tool_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = PartCursorKind(d.pop("kind"))

        part_id = d.pop("part_id")

        emitted_content = d.pop("emitted_content", UNSET)

        emitted_signature = d.pop("emitted_signature", UNSET)

        def _parse_tool_name(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        tool_name = _parse_tool_name(d.pop("tool_name", UNSET))

        part_cursor = cls(
            kind=kind,
            part_id=part_id,
            emitted_content=emitted_content,
            emitted_signature=emitted_signature,
            tool_name=tool_name,
        )

        part_cursor.additional_properties = d
        return part_cursor

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
