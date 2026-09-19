from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ManagedMemoryBackend")


@_attrs_define(repr=False)
class ManagedMemoryBackend:
    """
    Attributes:
        provider_id (str):
    """

    provider_id: str

    def to_dict(self) -> dict[str, Any]:
        provider_id = self.provider_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "provider_id": provider_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider_id = d.pop("provider_id")

        managed_memory_backend = cls(
            provider_id=provider_id,
        )

        return managed_memory_backend
