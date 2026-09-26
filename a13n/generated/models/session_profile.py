from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.profile import Profile


T = TypeVar("T", bound="SessionProfile")


@_attrs_define(repr=False)
class SessionProfile:
    """What a browser restores from its HttpOnly cookie: the account and the token it sends on mutations.

    Attributes:
        csrf_token (str):
        user (Profile):
    """

    csrf_token: str
    user: Profile
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        csrf_token = self.csrf_token

        user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "csrf_token": csrf_token,
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.profile import Profile

        d = dict(src_dict)
        csrf_token = d.pop("csrf_token")

        user = Profile.from_dict(d.pop("user"))

        session_profile = cls(
            csrf_token=csrf_token,
            user=user,
        )

        session_profile.additional_properties = d
        return session_profile

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
