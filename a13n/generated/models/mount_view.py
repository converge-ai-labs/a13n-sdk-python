from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MountView")


@_attrs_define(repr=False)
class MountView:
    """
    Attributes:
        environment_id (str):
        name (str):
        working_directory (None | str):
    """

    environment_id: str
    name: str
    working_directory: str | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        environment_id = self.environment_id

        name = self.name

        working_directory: str | None
        working_directory = self.working_directory

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "environment_id": environment_id,
                "name": name,
                "working_directory": working_directory,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        environment_id = d.pop("environment_id")

        name = d.pop("name")

        def _parse_working_directory(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        working_directory = _parse_working_directory(d.pop("working_directory"))

        mount_view = cls(
            environment_id=environment_id,
            name=name,
            working_directory=working_directory,
        )

        mount_view.additional_properties = d
        return mount_view

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
