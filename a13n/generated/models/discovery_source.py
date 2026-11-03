from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.discovery_source_kind import DiscoverySourceKind

T = TypeVar("T", bound="DiscoverySource")


@_attrs_define(repr=False)
class DiscoverySource:
    """
    Attributes:
        description (str):
        display_name (str):
        group_name (None | str):
        id (str):
        kind (DiscoverySourceKind):
    """

    description: str
    display_name: str
    group_name: str | None
    id: str
    kind: DiscoverySourceKind

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        display_name = self.display_name

        group_name: str | None
        group_name = self.group_name

        id = self.id

        kind = self.kind.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "description": description,
                "display_name": display_name,
                "group_name": group_name,
                "id": id,
                "kind": kind,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description")

        display_name = d.pop("display_name")

        def _parse_group_name(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        group_name = _parse_group_name(d.pop("group_name"))

        id = d.pop("id")

        kind = DiscoverySourceKind(d.pop("kind"))

        discovery_source = cls(
            description=description,
            display_name=display_name,
            group_name=group_name,
            id=id,
            kind=kind,
        )

        return discovery_source
