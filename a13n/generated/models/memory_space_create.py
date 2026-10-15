from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.memory_space_create_labels import MemorySpaceCreateLabels
    from ..models.organization_policy import OrganizationPolicy


T = TypeVar("T", bound="MemorySpaceCreate")


@_attrs_define(repr=False)
class MemorySpaceCreate:
    """
    Attributes:
        name (str):
        always_load (list[str] | Unset):
        description (None | str | Unset):
        enabled (bool | Unset):
        guide (None | str | Unset):
        labels (MemorySpaceCreateLabels | Unset):
        organization (OrganizationPolicy | Unset):
    """

    name: str
    always_load: list[str] | Unset = UNSET
    description: str | Unset | None = UNSET
    enabled: bool | Unset = UNSET
    guide: str | Unset | None = UNSET
    labels: MemorySpaceCreateLabels | Unset = UNSET
    organization: OrganizationPolicy | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        always_load: list[str] | Unset = UNSET
        if not isinstance(self.always_load, Unset):
            always_load = self.always_load

        description: str | Unset | None
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        enabled = self.enabled

        guide: str | Unset | None
        if isinstance(self.guide, Unset):
            guide = UNSET
        else:
            guide = self.guide

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        organization: dict[str, Any] | Unset = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if always_load is not UNSET:
            field_dict["always_load"] = always_load
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if guide is not UNSET:
            field_dict["guide"] = guide
        if labels is not UNSET:
            field_dict["labels"] = labels
        if organization is not UNSET:
            field_dict["organization"] = organization

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.memory_space_create_labels import MemorySpaceCreateLabels
        from ..models.organization_policy import OrganizationPolicy

        d = dict(src_dict)
        name = d.pop("name")

        always_load = cast(list[str], d.pop("always_load", UNSET))

        def _parse_description(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        description = _parse_description(d.pop("description", UNSET))

        enabled = d.pop("enabled", UNSET)

        def _parse_guide(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        guide = _parse_guide(d.pop("guide", UNSET))

        _labels = d.pop("labels", UNSET)
        labels: MemorySpaceCreateLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = MemorySpaceCreateLabels.from_dict(_labels)

        _organization = d.pop("organization", UNSET)
        organization: OrganizationPolicy | Unset
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = OrganizationPolicy.from_dict(_organization)

        memory_space_create = cls(
            name=name,
            always_load=always_load,
            description=description,
            enabled=enabled,
            guide=guide,
            labels=labels,
            organization=organization,
        )

        return memory_space_create
