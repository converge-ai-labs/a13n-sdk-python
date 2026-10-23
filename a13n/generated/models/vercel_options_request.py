from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="VercelOptionsRequest")


@_attrs_define(repr=False)
class VercelOptionsRequest:
    """
    Attributes:
        api_key (str):
        cursor (int | None | Unset):
        team_id (None | str | Unset):
    """

    api_key: str
    cursor: int | Unset | None = UNSET
    team_id: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        cursor: int | Unset | None
        if isinstance(self.cursor, Unset):
            cursor = UNSET
        else:
            cursor = self.cursor

        team_id: str | Unset | None
        if isinstance(self.team_id, Unset):
            team_id = UNSET
        else:
            team_id = self.team_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "api_key": api_key,
            }
        )
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if team_id is not UNSET:
            field_dict["team_id"] = team_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("api_key")

        def _parse_cursor(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        cursor = _parse_cursor(d.pop("cursor", UNSET))

        def _parse_team_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        team_id = _parse_team_id(d.pop("team_id", UNSET))

        vercel_options_request = cls(
            api_key=api_key,
            cursor=cursor,
            team_id=team_id,
        )

        return vercel_options_request
