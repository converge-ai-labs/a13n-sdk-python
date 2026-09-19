from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MemorySettings")


@_attrs_define(repr=False)
class MemorySettings:
    """
    Attributes:
        provider_id (str):
        auto_organize (bool | Unset):
        save_on_request (bool | Unset):
        timezone (str | Unset):
        use_memory (bool | Unset):
    """

    provider_id: str
    auto_organize: bool | Unset = UNSET
    save_on_request: bool | Unset = UNSET
    timezone: str | Unset = UNSET
    use_memory: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        provider_id = self.provider_id

        auto_organize = self.auto_organize

        save_on_request = self.save_on_request

        timezone = self.timezone

        use_memory = self.use_memory

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "provider_id": provider_id,
            }
        )
        if auto_organize is not UNSET:
            field_dict["auto_organize"] = auto_organize
        if save_on_request is not UNSET:
            field_dict["save_on_request"] = save_on_request
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if use_memory is not UNSET:
            field_dict["use_memory"] = use_memory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider_id = d.pop("provider_id")

        auto_organize = d.pop("auto_organize", UNSET)

        save_on_request = d.pop("save_on_request", UNSET)

        timezone = d.pop("timezone", UNSET)

        use_memory = d.pop("use_memory", UNSET)

        memory_settings = cls(
            provider_id=provider_id,
            auto_organize=auto_organize,
            save_on_request=save_on_request,
            timezone=timezone,
            use_memory=use_memory,
        )

        return memory_settings
