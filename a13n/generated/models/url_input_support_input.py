from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.video_url_type import VideoUrlType
from ..types import UNSET, Unset

T = TypeVar("T", bound="UrlInputSupportInput")


@_attrs_define(repr=False)
class UrlInputSupportInput:
    """URL subtypes consumed natively by the selected transport.

    Attributes:
        video (list[VideoUrlType] | Unset):
    """

    video: list[VideoUrlType] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        video: list[str] | Unset = UNSET
        if not isinstance(self.video, Unset):
            video = []
            for video_item_data in self.video:
                video_item = video_item_data.value
                video.append(video_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if video is not UNSET:
            field_dict["video"] = video

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _video = d.pop("video", UNSET)
        video: list[VideoUrlType] | Unset = UNSET
        if _video is not UNSET:
            video = []
            for video_item_data in _video:
                video_item = VideoUrlType(video_item_data)

                video.append(video_item)

        url_input_support_input = cls(
            video=video,
        )

        return url_input_support_input
