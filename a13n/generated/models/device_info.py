from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.device_info_path_style import DeviceInfoPathStyle

T = TypeVar("T", bound="DeviceInfo")


@_attrs_define(repr=False)
class DeviceInfo:
    """
    Attributes:
        default_working_directory (str):
        directory_discovery (bool):
        environment_id (str):
        path_style (DeviceInfoPathStyle):
    """

    default_working_directory: str
    directory_discovery: bool
    environment_id: str
    path_style: DeviceInfoPathStyle

    def to_dict(self) -> dict[str, Any]:
        default_working_directory = self.default_working_directory

        directory_discovery = self.directory_discovery

        environment_id = self.environment_id

        path_style = self.path_style.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "default_working_directory": default_working_directory,
                "directory_discovery": directory_discovery,
                "environment_id": environment_id,
                "path_style": path_style,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        default_working_directory = d.pop("default_working_directory")

        directory_discovery = d.pop("directory_discovery")

        environment_id = d.pop("environment_id")

        path_style = DeviceInfoPathStyle(d.pop("path_style"))

        device_info = cls(
            default_working_directory=default_working_directory,
            directory_discovery=directory_discovery,
            environment_id=environment_id,
            path_style=path_style,
        )

        return device_info
