from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.part_cursor_kind import PartCursorKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.citation import Citation


T = TypeVar("T", bound="PartCursor")


@_attrs_define(repr=False)
class PartCursor:
    """
    Attributes:
        kind (PartCursorKind):
        part_id (str):
        citations (list[Citation] | Unset):
        emitted_content (bool | Unset):
        emitted_signature (bool | Unset):
        tool_name (None | str | Unset):
    """

    kind: PartCursorKind
    part_id: str
    citations: list[Citation] | Unset = UNSET
    emitted_content: bool | Unset = UNSET
    emitted_signature: bool | Unset = UNSET
    tool_name: str | Unset | None = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        part_id = self.part_id

        citations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.citations, Unset):
            citations = []
            for citations_item_data in self.citations:
                citations_item = citations_item_data.to_dict()
                citations.append(citations_item)

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
        if citations is not UNSET:
            field_dict["citations"] = citations
        if emitted_content is not UNSET:
            field_dict["emitted_content"] = emitted_content
        if emitted_signature is not UNSET:
            field_dict["emitted_signature"] = emitted_signature
        if tool_name is not UNSET:
            field_dict["tool_name"] = tool_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.citation import Citation

        d = dict(src_dict)
        kind = PartCursorKind(d.pop("kind"))

        part_id = d.pop("part_id")

        _citations = d.pop("citations", UNSET)
        citations: list[Citation] | Unset = UNSET
        if _citations is not UNSET:
            citations = []
            for citations_item_data in _citations:
                citations_item = Citation.from_dict(citations_item_data)

                citations.append(citations_item)

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
            citations=citations,
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
