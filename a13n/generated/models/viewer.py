from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.viewer_protocol import ViewerProtocol
from ..types import UNSET, Unset

T = TypeVar("T", bound="Viewer")


@_attrs_define(repr=False)
class Viewer:
    """Sensitive, authorized control response; excluded from ordinary Browser reads.

    Attributes:
        episode (int):
        expires_at (datetime.datetime):
        url (str):
        generation (int | None | Unset):
        password (None | str | Unset):
        protocol (ViewerProtocol | Unset):
        token (None | str | Unset):
    """

    episode: int
    expires_at: datetime.datetime
    url: str
    generation: int | Unset | None = UNSET
    password: str | Unset | None = UNSET
    protocol: ViewerProtocol | Unset = UNSET
    token: str | Unset | None = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        episode = self.episode

        expires_at = self.expires_at.isoformat()

        url = self.url

        generation: int | Unset | None
        if isinstance(self.generation, Unset):
            generation = UNSET
        else:
            generation = self.generation

        password: str | Unset | None
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        protocol: str | Unset = UNSET
        if not isinstance(self.protocol, Unset):
            protocol = self.protocol.value

        token: str | Unset | None
        if isinstance(self.token, Unset):
            token = UNSET
        else:
            token = self.token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "episode": episode,
                "expires_at": expires_at,
                "url": url,
            }
        )
        if generation is not UNSET:
            field_dict["generation"] = generation
        if password is not UNSET:
            field_dict["password"] = password
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        episode = d.pop("episode")

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        url = d.pop("url")

        def _parse_generation(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        generation = _parse_generation(d.pop("generation", UNSET))

        def _parse_password(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        password = _parse_password(d.pop("password", UNSET))

        _protocol = d.pop("protocol", UNSET)
        protocol: ViewerProtocol | Unset
        if isinstance(_protocol, Unset):
            protocol = UNSET
        else:
            protocol = ViewerProtocol(_protocol)

        def _parse_token(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        token = _parse_token(d.pop("token", UNSET))

        viewer = cls(
            episode=episode,
            expires_at=expires_at,
            url=url,
            generation=generation,
            password=password,
            protocol=protocol,
            token=token,
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
