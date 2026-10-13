from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="RecordSource")


@_attrs_define(repr=False)
class RecordSource:
    """
    Attributes:
        id (str):
        sha256 (str):
    """

    id: str
    sha256: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        sha256 = self.sha256

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "sha256": sha256,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        sha256 = d.pop("sha256")

        record_source = cls(
            id=id,
            sha256=sha256,
        )

        return record_source
