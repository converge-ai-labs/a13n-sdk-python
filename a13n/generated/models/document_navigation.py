from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="DocumentNavigation")


@_attrs_define(repr=False)
class DocumentNavigation:
    """
    Attributes:
        description (str):
        digest (str):
        id (str):
        path (str):
        title (str):
        version (int):
    """

    description: str
    digest: str
    id: str
    path: str
    title: str
    version: int

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        digest = self.digest

        id = self.id

        path = self.path

        title = self.title

        version = self.version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "description": description,
                "digest": digest,
                "id": id,
                "path": path,
                "title": title,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description")

        digest = d.pop("digest")

        id = d.pop("id")

        path = d.pop("path")

        title = d.pop("title")

        version = d.pop("version")

        document_navigation = cls(
            description=description,
            digest=digest,
            id=id,
            path=path,
            title=title,
            version=version,
        )

        return document_navigation
