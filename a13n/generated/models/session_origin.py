from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SessionOrigin")


@_attrs_define(repr=False)
class SessionOrigin:
    """Caller-supplied display context, not execution provenance or an authorization boundary.

    Attributes:
        application (str):
        external_id (None | str | Unset):
        name (None | str | Unset):
    """

    application: str
    external_id: str | Unset | None = UNSET
    name: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        application = self.application

        external_id: str | Unset | None
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        name: str | Unset | None
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "application": application,
            }
        )
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        application = d.pop("application")

        def _parse_external_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        def _parse_name(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        name = _parse_name(d.pop("name", UNSET))

        session_origin = cls(
            application=application,
            external_id=external_id,
            name=name,
        )

        return session_origin
