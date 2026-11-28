from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentCitationSource")


@_attrs_define(repr=False)
class DocumentCitationSource:
    """
    Attributes:
        document_id (None | str | Unset):
        excerpts (list[str] | Unset):
        kind (Literal['document'] | Unset):
        title (None | str | Unset):
    """

    document_id: str | Unset | None = UNSET
    excerpts: list[str] | Unset = UNSET
    kind: Literal["document"] | Unset = UNSET
    title: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        document_id: str | Unset | None
        if isinstance(self.document_id, Unset):
            document_id = UNSET
        else:
            document_id = self.document_id

        excerpts: list[str] | Unset = UNSET
        if not isinstance(self.excerpts, Unset):
            excerpts = self.excerpts

        kind = self.kind

        title: str | Unset | None
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if document_id is not UNSET:
            field_dict["document_id"] = document_id
        if excerpts is not UNSET:
            field_dict["excerpts"] = excerpts
        if kind is not UNSET:
            field_dict["kind"] = kind
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_document_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        document_id = _parse_document_id(d.pop("document_id", UNSET))

        excerpts = cast(list[str], d.pop("excerpts", UNSET))

        kind = cast(Literal["document"] | Unset, d.pop("kind", UNSET))
        if kind != "document" and not isinstance(kind, Unset):
            raise ValueError(f"kind must match const 'document', got '{kind}'")

        def _parse_title(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        title = _parse_title(d.pop("title", UNSET))

        document_citation_source = cls(
            document_id=document_id,
            excerpts=excerpts,
            kind=kind,
            title=title,
        )

        return document_citation_source
