from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeploymentRetry")


@_attrs_define(repr=False)
class DeploymentRetry:
    """
    Attributes:
        api_token (None | str | Unset):
    """

    api_token: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        api_token: str | Unset | None
        if isinstance(self.api_token, Unset):
            api_token = UNSET
        else:
            api_token = self.api_token

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if api_token is not UNSET:
            field_dict["api_token"] = api_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_api_token(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        api_token = _parse_api_token(d.pop("api_token", UNSET))

        deployment_retry = cls(
            api_token=api_token,
        )

        return deployment_retry
