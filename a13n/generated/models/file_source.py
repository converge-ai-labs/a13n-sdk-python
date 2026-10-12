from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileSource")


@_attrs_define(repr=False)
class FileSource:
    """
    Attributes:
        bytes_ (int):
        path (str):
        sha256 (str):
        truncated (bool | Unset):
    """

    bytes_: int
    path: str
    sha256: str
    truncated: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        bytes_ = self.bytes_

        path = self.path

        sha256 = self.sha256

        truncated = self.truncated

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "bytes": bytes_,
                "path": path,
                "sha256": sha256,
            }
        )
        if truncated is not UNSET:
            field_dict["truncated"] = truncated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bytes_ = d.pop("bytes")

        path = d.pop("path")

        sha256 = d.pop("sha256")

        truncated = d.pop("truncated", UNSET)

        file_source = cls(
            bytes_=bytes_,
            path=path,
            sha256=sha256,
            truncated=truncated,
        )

        return file_source
