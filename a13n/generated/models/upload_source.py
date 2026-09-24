from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="UploadSource")


@_attrs_define(repr=False)
class UploadSource:
    """A package archive staged through `/uploads`.

    Attributes:
        kind (Literal['upload']):
        upload_id (str):
    """

    kind: Literal["upload"]
    upload_id: str

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        upload_id = self.upload_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
                "upload_id": upload_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = cast(Literal["upload"], d.pop("kind"))
        if kind != "upload":
            raise ValueError(f"kind must match const 'upload', got '{kind}'")

        upload_id = d.pop("upload_id")

        upload_source = cls(
            kind=kind,
            upload_id=upload_id,
        )

        return upload_source
