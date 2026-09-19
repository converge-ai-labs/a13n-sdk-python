from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddEnvironmentMountRequest")


@_attrs_define(repr=False)
class AddEnvironmentMountRequest:
    """
    Attributes:
        environment_id (str):
        name (str):
        working_directory (None | str | Unset):
    """

    environment_id: str
    name: str
    working_directory: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        environment_id = self.environment_id

        name = self.name

        working_directory: str | Unset | None
        if isinstance(self.working_directory, Unset):
            working_directory = UNSET
        else:
            working_directory = self.working_directory

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "environment_id": environment_id,
                "name": name,
            }
        )
        if working_directory is not UNSET:
            field_dict["working_directory"] = working_directory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        environment_id = d.pop("environment_id")

        name = d.pop("name")

        def _parse_working_directory(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        working_directory = _parse_working_directory(d.pop("working_directory", UNSET))

        add_environment_mount_request = cls(
            environment_id=environment_id,
            name=name,
            working_directory=working_directory,
        )

        return add_environment_mount_request
