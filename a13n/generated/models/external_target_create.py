from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalTargetCreate")


@_attrs_define(repr=False)
class ExternalTargetCreate:
    """An envd daemon someone runs, registered by its endpoint and the token it accepts.

    Attributes:
        endpoint (str):
        token (str):
        name (None | str | Unset):
    """

    endpoint: str
    token: str
    name: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        endpoint = self.endpoint

        token = self.token

        name: str | Unset | None
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "endpoint": endpoint,
                "token": token,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        endpoint = d.pop("endpoint")

        token = d.pop("token")

        def _parse_name(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        name = _parse_name(d.pop("name", UNSET))

        external_target_create = cls(
            endpoint=endpoint,
            token=token,
            name=name,
        )

        return external_target_create
