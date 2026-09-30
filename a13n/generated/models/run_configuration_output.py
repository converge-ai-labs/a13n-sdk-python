from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.run_configuration_output_extensions import RunConfigurationOutputExtensions


T = TypeVar("T", bound="RunConfigurationOutput")


@_attrs_define(repr=False)
class RunConfigurationOutput:
    """An accepted snapshot, independent of Agent definitions and Capability configuration.

    Consumers explicitly opt into namespaced extensions and own their validation.
    Extension lookups return detached values, not mutable shared state.

        Attributes:
            allowed_hosts (list[str] | None | Unset): Allowed normalized hostnames/IP literals or regex:<Python pattern>
                rules matched against the entire normalized hostname. Null is unrestricted; an empty array denies all.
            extensions (RunConfigurationOutputExtensions | Unset):
    """

    allowed_hosts: list[str] | Unset | None = UNSET
    extensions: RunConfigurationOutputExtensions | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        allowed_hosts: list[str] | Unset | None
        if isinstance(self.allowed_hosts, Unset):
            allowed_hosts = UNSET
        elif isinstance(self.allowed_hosts, list):
            allowed_hosts = self.allowed_hosts

        else:
            allowed_hosts = self.allowed_hosts

        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if allowed_hosts is not UNSET:
            field_dict["allowed_hosts"] = allowed_hosts
        if extensions is not UNSET:
            field_dict["extensions"] = extensions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_configuration_output_extensions import RunConfigurationOutputExtensions

        d = dict(src_dict)

        def _parse_allowed_hosts(data: object) -> list[str] | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allowed_hosts_type_0 = cast(list[str], data)

                return allowed_hosts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | Unset | None, data)

        allowed_hosts = _parse_allowed_hosts(d.pop("allowed_hosts", UNSET))

        _extensions = d.pop("extensions", UNSET)
        extensions: RunConfigurationOutputExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = RunConfigurationOutputExtensions.from_dict(_extensions)

        run_configuration_output = cls(
            allowed_hosts=allowed_hosts,
            extensions=extensions,
        )

        return run_configuration_output
