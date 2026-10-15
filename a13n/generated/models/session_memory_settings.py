from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.space_binding import SpaceBinding


T = TypeVar("T", bound="SessionMemorySettings")


@_attrs_define(repr=False)
class SessionMemorySettings:
    """Participation and complete Space selection; policy belongs to each Space.

    Attributes:
        enabled (bool | Unset):
        spaces (list[SpaceBinding] | Unset):
    """

    enabled: bool | Unset = UNSET
    spaces: list[SpaceBinding] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        spaces: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.spaces, Unset):
            spaces = []
            for spaces_item_data in self.spaces:
                spaces_item = spaces_item_data.to_dict()
                spaces.append(spaces_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if spaces is not UNSET:
            field_dict["spaces"] = spaces

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.space_binding import SpaceBinding

        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        _spaces = d.pop("spaces", UNSET)
        spaces: list[SpaceBinding] | Unset = UNSET
        if _spaces is not UNSET:
            spaces = []
            for spaces_item_data in _spaces:
                spaces_item = SpaceBinding.from_dict(spaces_item_data)

                spaces.append(spaces_item)

        session_memory_settings = cls(
            enabled=enabled,
            spaces=spaces,
        )

        return session_memory_settings
