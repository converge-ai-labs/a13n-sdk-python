from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.managed_memory_document import ManagedMemoryDocument


T = TypeVar("T", bound="ManagedDocumentMutation")


@_attrs_define(repr=False)
class ManagedDocumentMutation:
    """
    Attributes:
        change_id (None | str):
        document (ManagedMemoryDocument):
    """

    change_id: str | None
    document: ManagedMemoryDocument
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        change_id: str | None
        change_id = self.change_id

        document = self.document.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "change_id": change_id,
                "document": document,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.managed_memory_document import ManagedMemoryDocument

        d = dict(src_dict)

        def _parse_change_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        change_id = _parse_change_id(d.pop("change_id"))

        document = ManagedMemoryDocument.from_dict(d.pop("document"))

        managed_document_mutation = cls(
            change_id=change_id,
            document=document,
        )

        managed_document_mutation.additional_properties = d
        return managed_document_mutation

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
