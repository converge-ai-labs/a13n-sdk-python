from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LoginSession")


@_attrs_define(repr=False)
class LoginSession:
    """
    Attributes:
        created_at (datetime.datetime):
        current (bool):
        expires_at (datetime.datetime):
        id (str):
    """

    created_at: datetime.datetime
    current: bool
    expires_at: datetime.datetime
    id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        current = self.current

        expires_at = self.expires_at.isoformat()

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "current": current,
                "expires_at": expires_at,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        current = d.pop("current")

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        id = d.pop("id")

        login_session = cls(
            created_at=created_at,
            current=current,
            expires_at=expires_at,
            id=id,
        )

        login_session.additional_properties = d
        return login_session

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
