from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UrlInputSupportOutput")


@_attrs_define(repr=False)
class UrlInputSupportOutput:
    """URL subtypes consumed natively by the selected transport.

    Attributes:
        video (list[str] | Unset):
    """

    video: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        video: list[str] | Unset = UNSET
        if not isinstance(self.video, Unset):
            video = self.video

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if video is not UNSET:
            field_dict["video"] = video

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        video = cast(list[str], d.pop("video", UNSET))

        url_input_support_output = cls(
            video=video,
        )

        return url_input_support_output
