from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="AddEnvironmentMountRequest")


@_attrs_define(repr=False)
class AddEnvironmentMountRequest:
    """
    Attributes:
        environment_id (str):
        name (str):
    """

    environment_id: str
    name: str

    def to_dict(self) -> dict[str, Any]:
        environment_id = self.environment_id

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "environment_id": environment_id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        environment_id = d.pop("environment_id")

        name = d.pop("name")

        add_environment_mount_request = cls(
            environment_id=environment_id,
            name=name,
        )

        return add_environment_mount_request
