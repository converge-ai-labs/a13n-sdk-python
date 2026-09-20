from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MediaUnderstandingDefaults")


@_attrs_define(repr=False)
class MediaUnderstandingDefaults:
    """
    Attributes:
        version (int):
        workspace_id (str):
        audio (None | str | Unset):
        image (None | str | Unset):
        video (None | str | Unset):
    """

    version: int
    workspace_id: str
    audio: str | Unset | None = UNSET
    image: str | Unset | None = UNSET
    video: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        workspace_id = self.workspace_id

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

        field_dict.update(
            {
                "version": version,
                "workspace_id": workspace_id,
            }
        )
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
        version = d.pop("version")

        workspace_id = d.pop("workspace_id")

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

        media_understanding_defaults = cls(
            version=version,
            workspace_id=workspace_id,
            audio=audio,
            image=image,
            video=video,
        )

        return media_understanding_defaults
