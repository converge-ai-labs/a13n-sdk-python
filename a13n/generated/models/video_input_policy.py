from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="VideoInputPolicy")


@_attrs_define(repr=False)
class VideoInputPolicy:
    """Base64-after byte budget for both one video and all inline videos in a request.

    Attributes:
        max_video_bytes (int | Unset): Maximum Base64-encoded bytes per video and in aggregate per model request.
    """

    max_video_bytes: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        max_video_bytes = self.max_video_bytes

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if max_video_bytes is not UNSET:
            field_dict["max_video_bytes"] = max_video_bytes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_video_bytes = d.pop("max_video_bytes", UNSET)

        video_input_policy = cls(
            max_video_bytes=max_video_bytes,
        )

        return video_input_policy
