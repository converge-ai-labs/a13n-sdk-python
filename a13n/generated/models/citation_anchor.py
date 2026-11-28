from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.citation_anchor_kind import CitationAnchorKind

T = TypeVar("T", bound="CitationAnchor")


@_attrs_define(repr=False)
class CitationAnchor:
    """Half-open Unicode code-point range in the item's text.

    Attributes:
        end (int):
        kind (CitationAnchorKind):
        start (int):
    """

    end: int
    kind: CitationAnchorKind
    start: int

    def to_dict(self) -> dict[str, Any]:
        end = self.end

        kind = self.kind.value

        start = self.start

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "end": end,
                "kind": kind,
                "start": start,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        end = d.pop("end")

        kind = CitationAnchorKind(d.pop("kind"))

        start = d.pop("start")

        citation_anchor = cls(
            end=end,
            kind=kind,
            start=start,
        )

        return citation_anchor
