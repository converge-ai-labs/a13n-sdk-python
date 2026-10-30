from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Viewer")


@_attrs_define(repr=False)
class Viewer:
    """Sensitive, authorized control response; excluded from ordinary Browser reads.

    Attributes:
        episode (int):
        expires_at (datetime.datetime):
        url (str):
    """

    episode: int
    expires_at: datetime.datetime
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        episode = self.episode

        expires_at = self.expires_at.isoformat()

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "episode": episode,
                "expires_at": expires_at,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        episode = d.pop("episode")

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        url = d.pop("url")

        viewer = cls(
            episode=episode,
            expires_at=expires_at,
            url=url,
        )

        viewer.additional_properties = d
        return viewer

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
