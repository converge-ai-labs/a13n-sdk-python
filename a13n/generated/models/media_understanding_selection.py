from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MediaUnderstandingSelection")


@_attrs_define(repr=False)
class MediaUnderstandingSelection:
    """The model describing each media kind a model cannot read; a kind without one is unavailable.

    Attributes:
        audio (None | str | Unset):
        image (None | str | Unset):
        video (None | str | Unset):
    """

    audio: str | Unset | None = UNSET
    image: str | Unset | None = UNSET
    video: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        audio: str | Unset | None
        if isinstance(self.audio, Unset):
            audio = UNSET
        else:
            audio = self.audio

        image: str | Unset | None
        if isinstance(self.image, Unset):
            image = UNSET
        else:
            image = self.image

        video: str | Unset | None
        if isinstance(self.video, Unset):
            video = UNSET
        else:
            video = self.video

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if audio is not UNSET:
            field_dict["audio"] = audio
        if image is not UNSET:
            field_dict["image"] = image
        if video is not UNSET:
            field_dict["video"] = video

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_audio(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        audio = _parse_audio(d.pop("audio", UNSET))

        def _parse_image(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        image = _parse_image(d.pop("image", UNSET))

        def _parse_video(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        video = _parse_video(d.pop("video", UNSET))

        media_understanding_selection = cls(
            audio=audio,
            image=image,
            video=video,
        )

        return media_understanding_selection
