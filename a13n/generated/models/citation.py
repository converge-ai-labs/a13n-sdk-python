from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.citation_anchor import CitationAnchor
    from ..models.document_citation_source import DocumentCitationSource
    from ..models.web_citation_source import WebCitationSource


T = TypeVar("T", bound="Citation")


@_attrs_define(repr=False)
class Citation:
    """
    Attributes:
        sources (list[DocumentCitationSource | WebCitationSource]):
        anchor (CitationAnchor | None | Unset):
    """

    sources: list[DocumentCitationSource | WebCitationSource]
    anchor: CitationAnchor | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.citation_anchor import CitationAnchor
        from ..models.web_citation_source import WebCitationSource

        sources = []
        for sources_item_data in self.sources:
            sources_item: dict[str, Any]
            if isinstance(sources_item_data, WebCitationSource):
                sources_item = sources_item_data.to_dict()
            else:
                sources_item = sources_item_data.to_dict()

            sources.append(sources_item)

        anchor: dict[str, Any] | Unset | None
        if isinstance(self.anchor, Unset):
            anchor = UNSET
        elif isinstance(self.anchor, CitationAnchor):
            anchor = self.anchor.to_dict()
        else:
            anchor = self.anchor

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "sources": sources,
            }
        )
        if anchor is not UNSET:
            field_dict["anchor"] = anchor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.citation_anchor import CitationAnchor
        from ..models.document_citation_source import DocumentCitationSource
        from ..models.web_citation_source import WebCitationSource

        d = dict(src_dict)
        sources = []
        _sources = d.pop("sources")
        for sources_item_data in _sources:

            def _parse_sources_item(data: object) -> DocumentCitationSource | WebCitationSource:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_citation_source_type_0 = WebCitationSource.from_dict(data)

                    return componentsschemas_citation_source_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_citation_source_type_1 = DocumentCitationSource.from_dict(data)

                return componentsschemas_citation_source_type_1

            sources_item = _parse_sources_item(sources_item_data)

            sources.append(sources_item)

        def _parse_anchor(data: object) -> CitationAnchor | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                anchor_type_0 = CitationAnchor.from_dict(data)

                return anchor_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CitationAnchor | Unset | None, data)

        anchor = _parse_anchor(d.pop("anchor", UNSET))

        citation = cls(
            sources=sources,
            anchor=anchor,
        )

        return citation
