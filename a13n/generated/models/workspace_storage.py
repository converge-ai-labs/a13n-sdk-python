from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.creator_storage import CreatorStorage


T = TypeVar("T", bound="WorkspaceStorage")


@_attrs_define(repr=False)
class WorkspaceStorage:
    """
    Attributes:
        active_bytes (int):
        by_creator (list[CreatorStorage]):
        retired_bytes (int):
        staged_upload_bytes (int):
        total_bytes (int):
    """

    active_bytes: int
    by_creator: list[CreatorStorage]
    retired_bytes: int
    staged_upload_bytes: int
    total_bytes: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active_bytes = self.active_bytes

        by_creator = []
        for by_creator_item_data in self.by_creator:
            by_creator_item = by_creator_item_data.to_dict()
            by_creator.append(by_creator_item)

        retired_bytes = self.retired_bytes

        staged_upload_bytes = self.staged_upload_bytes

        total_bytes = self.total_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "active_bytes": active_bytes,
                "by_creator": by_creator,
                "retired_bytes": retired_bytes,
                "staged_upload_bytes": staged_upload_bytes,
                "total_bytes": total_bytes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.creator_storage import CreatorStorage

        d = dict(src_dict)
        active_bytes = d.pop("active_bytes")

        by_creator = []
        _by_creator = d.pop("by_creator")
        for by_creator_item_data in _by_creator:
            by_creator_item = CreatorStorage.from_dict(by_creator_item_data)

            by_creator.append(by_creator_item)

        retired_bytes = d.pop("retired_bytes")

        staged_upload_bytes = d.pop("staged_upload_bytes")

        total_bytes = d.pop("total_bytes")

        workspace_storage = cls(
            active_bytes=active_bytes,
            by_creator=by_creator,
            retired_bytes=retired_bytes,
            staged_upload_bytes=staged_upload_bytes,
            total_bytes=total_bytes,
        )

        workspace_storage.additional_properties = d
        return workspace_storage

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
