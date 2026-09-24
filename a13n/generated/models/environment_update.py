from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="EnvironmentUpdate")


@_attrs_define(repr=False)
class EnvironmentUpdate:
    """Fields left out stay unchanged. Only an external target has an endpoint and token; a new endpoint comes with
    its token, so a stored token never reaches an endpoint it was not entered for.

        Attributes:
            endpoint (None | str | Unset):
            name (None | str | Unset):
            token (None | str | Unset):
    """

    endpoint: str | Unset | None = UNSET
    name: str | Unset | None = UNSET
    token: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        endpoint: str | Unset | None
        if isinstance(self.endpoint, Unset):
            endpoint = UNSET
        else:
            endpoint = self.endpoint

        name: str | Unset | None
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        token: str | Unset | None
        if isinstance(self.token, Unset):
            token = UNSET
        else:
            token = self.token

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if name is not UNSET:
            field_dict["name"] = name
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_endpoint(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        endpoint = _parse_endpoint(d.pop("endpoint", UNSET))

        def _parse_name(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_token(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        token = _parse_token(d.pop("token", UNSET))

        environment_update = cls(
            endpoint=endpoint,
            name=name,
            token=token,
        )

        return environment_update
