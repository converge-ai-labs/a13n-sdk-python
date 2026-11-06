from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.system_preset import SystemPreset
from ..types import UNSET, Unset

T = TypeVar("T", bound="FileMemoryGuidance")


@_attrs_define(repr=False)
class FileMemoryGuidance:
    """
    Attributes:
        custom (str | Unset):
        system_override (None | str | Unset):
        system_preset (SystemPreset | Unset):
        timezone (str | Unset):
    """

    custom: str | Unset = UNSET
    system_override: str | Unset | None = UNSET
    system_preset: SystemPreset | Unset = UNSET
    timezone: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        custom = self.custom

        system_override: str | Unset | None
        if isinstance(self.system_override, Unset):
            system_override = UNSET
        else:
            system_override = self.system_override

        system_preset: str | Unset = UNSET
        if not isinstance(self.system_preset, Unset):
            system_preset = self.system_preset.value

        timezone = self.timezone

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if custom is not UNSET:
            field_dict["custom"] = custom
        if system_override is not UNSET:
            field_dict["system_override"] = system_override
        if system_preset is not UNSET:
            field_dict["system_preset"] = system_preset
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        custom = d.pop("custom", UNSET)

        def _parse_system_override(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        system_override = _parse_system_override(d.pop("system_override", UNSET))

        _system_preset = d.pop("system_preset", UNSET)
        system_preset: SystemPreset | Unset
        if isinstance(_system_preset, Unset):
            system_preset = UNSET
        else:
            system_preset = SystemPreset(_system_preset)

        timezone = d.pop("timezone", UNSET)

        file_memory_guidance = cls(
            custom=custom,
            system_override=system_override,
            system_preset=system_preset,
            timezone=timezone,
        )

        return file_memory_guidance
