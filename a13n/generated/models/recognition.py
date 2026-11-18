from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="Recognition")


@_attrs_define(repr=False)
class Recognition:
    """
    Attributes:
        device_id (str):
        environment_id (str):
    """

    device_id: str
    environment_id: str

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        environment_id = self.environment_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "device_id": device_id,
                "environment_id": environment_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        device_id = d.pop("device_id")

        environment_id = d.pop("environment_id")

        recognition = cls(
            device_id=device_id,
            environment_id=environment_id,
        )

        return recognition
