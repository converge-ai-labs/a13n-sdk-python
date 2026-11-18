from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceClaim")


@_attrs_define(repr=False)
class DeviceClaim:
    """
    Attributes:
        default_working_directory (str):
        device_id (str):
        name (str):
        computer_use (bool | Unset):
        environment_id (None | str | Unset):
        full_control (bool | Unset):
    """

    default_working_directory: str
    device_id: str
    name: str
    computer_use: bool | Unset = UNSET
    environment_id: str | Unset | None = UNSET
    full_control: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        default_working_directory = self.default_working_directory

        device_id = self.device_id

        name = self.name

        computer_use = self.computer_use

        environment_id: str | Unset | None
        if isinstance(self.environment_id, Unset):
            environment_id = UNSET
        else:
            environment_id = self.environment_id

        full_control = self.full_control

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "default_working_directory": default_working_directory,
                "device_id": device_id,
                "name": name,
            }
        )
        if computer_use is not UNSET:
            field_dict["computer_use"] = computer_use
        if environment_id is not UNSET:
            field_dict["environment_id"] = environment_id
        if full_control is not UNSET:
            field_dict["full_control"] = full_control

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        default_working_directory = d.pop("default_working_directory")

        device_id = d.pop("device_id")

        name = d.pop("name")

        computer_use = d.pop("computer_use", UNSET)

        def _parse_environment_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        environment_id = _parse_environment_id(d.pop("environment_id", UNSET))

        full_control = d.pop("full_control", UNSET)

        device_claim = cls(
            default_working_directory=default_working_directory,
            device_id=device_id,
            name=name,
            computer_use=computer_use,
            environment_id=environment_id,
            full_control=full_control,
        )

        return device_claim
