from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Upload")


@_attrs_define(repr=False)
class Upload:
    """
    Attributes:
        content_type (str):
        digest (str):
        filename (str):
        size (int):
        upload_id (str):
    """

    content_type: str
    digest: str
    filename: str
    size: int
    upload_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_type = self.content_type

        digest = self.digest

        filename = self.filename

        size = self.size

        upload_id = self.upload_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content_type": content_type,
                "digest": digest,
                "filename": filename,
                "size": size,
                "upload_id": upload_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content_type = d.pop("content_type")

        digest = d.pop("digest")

        filename = d.pop("filename")

        size = d.pop("size")

        upload_id = d.pop("upload_id")

        upload = cls(
            content_type=content_type,
            digest=digest,
            filename=filename,
            size=size,
            upload_id=upload_id,
        )

        upload.additional_properties = d
        return upload

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
