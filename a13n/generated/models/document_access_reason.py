from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.document_access_reason_kind import DocumentAccessReasonKind

T = TypeVar("T", bound="DocumentAccessReason")


@_attrs_define(repr=False)
class DocumentAccessReason:
    """
    Attributes:
        kind (DocumentAccessReasonKind):
    """

    kind: DocumentAccessReasonKind

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = DocumentAccessReasonKind(d.pop("kind"))

        document_access_reason = cls(
            kind=kind,
        )

        return document_access_reason
