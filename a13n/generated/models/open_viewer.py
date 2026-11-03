from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.open_viewer_mode import OpenViewerMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenViewer")


@_attrs_define(repr=False)
class OpenViewer:
    """
    Attributes:
        episode (int | None | Unset):
        generation (int | None | Unset):
        mode (OpenViewerMode | Unset):
        viewer_id (None | str | Unset):
    """

    episode: int | Unset | None = UNSET
    generation: int | Unset | None = UNSET
    mode: OpenViewerMode | Unset = UNSET
    viewer_id: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        episode: int | Unset | None
        if isinstance(self.episode, Unset):
            episode = UNSET
        else:
            episode = self.episode

        generation: int | Unset | None
        if isinstance(self.generation, Unset):
            generation = UNSET
        else:
            generation = self.generation

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        viewer_id: str | Unset | None
        if isinstance(self.viewer_id, Unset):
            viewer_id = UNSET
        else:
            viewer_id = self.viewer_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if episode is not UNSET:
            field_dict["episode"] = episode
        if generation is not UNSET:
            field_dict["generation"] = generation
        if mode is not UNSET:
            field_dict["mode"] = mode
        if viewer_id is not UNSET:
            field_dict["viewer_id"] = viewer_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_episode(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        episode = _parse_episode(d.pop("episode", UNSET))

        def _parse_generation(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        generation = _parse_generation(d.pop("generation", UNSET))

        _mode = d.pop("mode", UNSET)
        mode: OpenViewerMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = OpenViewerMode(_mode)

        def _parse_viewer_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        viewer_id = _parse_viewer_id(d.pop("viewer_id", UNSET))

        open_viewer = cls(
            episode=episode,
            generation=generation,
            mode=mode,
            viewer_id=viewer_id,
        )

        return open_viewer
