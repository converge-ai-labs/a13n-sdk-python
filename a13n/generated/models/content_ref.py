from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.content_ref_media_type import ContentRefMediaType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContentRef")


@_attrs_define(repr=False)
class ContentRef:
    """An immutable Host-owned value, loaded through that Host's authorized content API.

    Attributes:
        id (str):
        media_type (ContentRefMediaType):
        preview (str):
        size_bytes (int):
        truncated (bool | Unset):
    """

    id: str
    media_type: ContentRefMediaType
    preview: str
    size_bytes: int
    truncated: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        media_type = self.media_type.value

        preview = self.preview

        size_bytes = self.size_bytes

        truncated = self.truncated

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "media_type": media_type,
                "preview": preview,
                "size_bytes": size_bytes,
            }
        )
        if truncated is not UNSET:
            field_dict["truncated"] = truncated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        media_type = ContentRefMediaType(d.pop("media_type"))

        preview = d.pop("preview")

        size_bytes = d.pop("size_bytes")

        truncated = d.pop("truncated", UNSET)

        content_ref = cls(
            id=id,
            media_type=media_type,
            preview=preview,
            size_bytes=size_bytes,
            truncated=truncated,
        )

        return content_ref
