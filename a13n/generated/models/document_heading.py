from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="DocumentHeading")


@_attrs_define(repr=False)
class DocumentHeading:
    """
    Attributes:
        end (int):
        level (int):
        locator (str):
        start (int):
        title (str):
    """

    end: int
    level: int
    locator: str
    start: int
    title: str

    def to_dict(self) -> dict[str, Any]:
        end = self.end

        level = self.level

        locator = self.locator

        start = self.start

        title = self.title

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "end": end,
                "level": level,
                "locator": locator,
                "start": start,
                "title": title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        end = d.pop("end")

        level = d.pop("level")

        locator = d.pop("locator")

        start = d.pop("start")

        title = d.pop("title")

        document_heading = cls(
            end=end,
            level=level,
            locator=locator,
            start=start,
            title=title,
        )

        return document_heading
