from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="AssetCreate")


@_attrs_define(repr=False)
class AssetCreate:
    """
    Attributes:
        name (str):
        upload_id (str):
    """

    name: str
    upload_id: str

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        upload_id = self.upload_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "upload_id": upload_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        upload_id = d.pop("upload_id")

        asset_create = cls(
            name=name,
            upload_id=upload_id,
        )

        return asset_create
