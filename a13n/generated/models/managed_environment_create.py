from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ManagedEnvironmentCreate")


@_attrs_define(repr=False)
class ManagedEnvironmentCreate:
    """A workspace-managed sandbox reserved from a template, for threads to mount; maintenance creates it.

    Attributes:
        template_id (str):
        name (None | str | Unset):
    """

    template_id: str
    name: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        template_id = self.template_id

        name: str | Unset | None
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "template_id": template_id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        template_id = d.pop("template_id")

        def _parse_name(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        name = _parse_name(d.pop("name", UNSET))

        managed_environment_create = cls(
            template_id=template_id,
            name=name,
        )

        return managed_environment_create
