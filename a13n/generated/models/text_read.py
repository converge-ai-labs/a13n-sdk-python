from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.text_read_media_type import TextReadMediaType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TextRead")


@_attrs_define(repr=False)
class TextRead:
    """A fragment of a versioned value, not a complete JSON object or writable configuration.

    Attributes:
        has_more (bool):
        media_type (TextReadMediaType):
        next_offset (int | None):
        offset (int):
        source (str):
        text (str):
        total_chars (int):
        version (str):
        match_offset (int | None | Unset):
        query (None | str | Unset):
        representation (Literal['fragment'] | Unset):
        source_truncated (bool | Unset):
    """

    has_more: bool
    media_type: TextReadMediaType
    next_offset: int | None
    offset: int
    source: str
    text: str
    total_chars: int
    version: str
    match_offset: int | Unset | None = UNSET
    query: str | Unset | None = UNSET
    representation: Literal["fragment"] | Unset = UNSET
    source_truncated: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        has_more = self.has_more

        media_type = self.media_type.value

        next_offset: int | None
        next_offset = self.next_offset

        offset = self.offset

        source = self.source

        text = self.text

        total_chars = self.total_chars

        version = self.version

        match_offset: int | Unset | None
        if isinstance(self.match_offset, Unset):
            match_offset = UNSET
        else:
            match_offset = self.match_offset

        query: str | Unset | None
        if isinstance(self.query, Unset):
            query = UNSET
        else:
            query = self.query

        representation = self.representation

        source_truncated = self.source_truncated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "has_more": has_more,
                "media_type": media_type,
                "next_offset": next_offset,
                "offset": offset,
                "source": source,
                "text": text,
                "total_chars": total_chars,
                "version": version,
            }
        )
        if match_offset is not UNSET:
            field_dict["match_offset"] = match_offset
        if query is not UNSET:
            field_dict["query"] = query
        if representation is not UNSET:
            field_dict["representation"] = representation
        if source_truncated is not UNSET:
            field_dict["source_truncated"] = source_truncated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        has_more = d.pop("has_more")

        media_type = TextReadMediaType(d.pop("media_type"))

        def _parse_next_offset(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        next_offset = _parse_next_offset(d.pop("next_offset"))

        offset = d.pop("offset")

        source = d.pop("source")

        text = d.pop("text")

        total_chars = d.pop("total_chars")

        version = d.pop("version")

        def _parse_match_offset(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        match_offset = _parse_match_offset(d.pop("match_offset", UNSET))

        def _parse_query(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        query = _parse_query(d.pop("query", UNSET))

        representation = cast(Literal["fragment"] | Unset, d.pop("representation", UNSET))
        if representation != "fragment" and not isinstance(representation, Unset):
            raise ValueError(f"representation must match const 'fragment', got '{representation}'")

        source_truncated = d.pop("source_truncated", UNSET)

        text_read = cls(
            has_more=has_more,
            media_type=media_type,
            next_offset=next_offset,
            offset=offset,
            source=source,
            text=text,
            total_chars=total_chars,
            version=version,
            match_offset=match_offset,
            query=query,
            representation=representation,
            source_truncated=source_truncated,
        )

        text_read.additional_properties = d
        return text_read

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
