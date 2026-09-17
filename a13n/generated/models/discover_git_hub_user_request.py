from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="DiscoverGitHubUserRequest")


@_attrs_define(repr=False)
class DiscoverGitHubUserRequest:
    """
    Attributes:
        personal_access_token (str):
    """

    personal_access_token: str

    def to_dict(self) -> dict[str, Any]:
        personal_access_token = self.personal_access_token

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "personal_access_token": personal_access_token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        personal_access_token = d.pop("personal_access_token")

        discover_git_hub_user_request = cls(
            personal_access_token=personal_access_token,
        )

        return discover_git_hub_user_request
