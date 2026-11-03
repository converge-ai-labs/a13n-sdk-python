from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.desktop_viewer_mode import DesktopViewerMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="DesktopViewer")


@_attrs_define(repr=False)
class DesktopViewer:
    """
    Attributes:
        episode (int):
        expires_at (datetime.datetime):
        generation (int):
        mode (DesktopViewerMode):
        password (str):
        websocket_url (str):
        viewer_id (None | str | Unset):
    """

    episode: int
    expires_at: datetime.datetime
    generation: int
    mode: DesktopViewerMode
    password: str
    websocket_url: str
    viewer_id: str | Unset | None = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        episode = self.episode

        expires_at = self.expires_at.isoformat()

        generation = self.generation

        mode = self.mode.value

        password = self.password

        websocket_url = self.websocket_url

        viewer_id: str | Unset | None
        if isinstance(self.viewer_id, Unset):
            viewer_id = UNSET
        else:
            viewer_id = self.viewer_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "episode": episode,
                "expires_at": expires_at,
                "generation": generation,
                "mode": mode,
                "password": password,
                "websocket_url": websocket_url,
            }
        )
        if viewer_id is not UNSET:
            field_dict["viewer_id"] = viewer_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        episode = d.pop("episode")

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        generation = d.pop("generation")

        mode = DesktopViewerMode(d.pop("mode"))

        password = d.pop("password")

        websocket_url = d.pop("websocket_url")

        def _parse_viewer_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        viewer_id = _parse_viewer_id(d.pop("viewer_id", UNSET))

        desktop_viewer = cls(
            episode=episode,
            expires_at=expires_at,
            generation=generation,
            mode=mode,
            password=password,
            websocket_url=websocket_url,
            viewer_id=viewer_id,
        )

        desktop_viewer.additional_properties = d
        return desktop_viewer

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
