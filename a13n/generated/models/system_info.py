from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.operating_system import OperatingSystem
from ..types import UNSET, Unset

T = TypeVar("T", bound="SystemInfo")


@_attrs_define(repr=False)
class SystemInfo:
    """
    Attributes:
        os (OperatingSystem):
        architecture (None | str | Unset):
        cpu_model (None | str | Unset):
        kernel_version (None | str | Unset):
        os_version (None | str | Unset):
    """

    os: OperatingSystem
    architecture: str | Unset | None = UNSET
    cpu_model: str | Unset | None = UNSET
    kernel_version: str | Unset | None = UNSET
    os_version: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        os = self.os.value

        architecture: str | Unset | None
        if isinstance(self.architecture, Unset):
            architecture = UNSET
        else:
            architecture = self.architecture

        cpu_model: str | Unset | None
        if isinstance(self.cpu_model, Unset):
            cpu_model = UNSET
        else:
            cpu_model = self.cpu_model

        kernel_version: str | Unset | None
        if isinstance(self.kernel_version, Unset):
            kernel_version = UNSET
        else:
            kernel_version = self.kernel_version

        os_version: str | Unset | None
        if isinstance(self.os_version, Unset):
            os_version = UNSET
        else:
            os_version = self.os_version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "os": os,
            }
        )
        if architecture is not UNSET:
            field_dict["architecture"] = architecture
        if cpu_model is not UNSET:
            field_dict["cpu_model"] = cpu_model
        if kernel_version is not UNSET:
            field_dict["kernel_version"] = kernel_version
        if os_version is not UNSET:
            field_dict["os_version"] = os_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        os = OperatingSystem(d.pop("os"))

        def _parse_architecture(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        architecture = _parse_architecture(d.pop("architecture", UNSET))

        def _parse_cpu_model(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        cpu_model = _parse_cpu_model(d.pop("cpu_model", UNSET))

        def _parse_kernel_version(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        kernel_version = _parse_kernel_version(d.pop("kernel_version", UNSET))

        def _parse_os_version(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        os_version = _parse_os_version(d.pop("os_version", UNSET))

        system_info = cls(
            os=os,
            architecture=architecture,
            cpu_model=cpu_model,
            kernel_version=kernel_version,
            os_version=os_version,
        )

        return system_info
