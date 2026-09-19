from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StoredMemoryScope")


@_attrs_define(repr=False)
class StoredMemoryScope:
    """
    Attributes:
        environment_id (str):
        id (str):
        provider_identity (str):
        scope (str):
        subject_id (str):
        availability (Literal['unresolved'] | Unset):
        supports_changes (bool | Unset):
        supports_revisions (bool | Unset):
    """

    environment_id: str
    id: str
    provider_identity: str
    scope: str
    subject_id: str
    availability: Literal["unresolved"] | Unset = UNSET
    supports_changes: bool | Unset = UNSET
    supports_revisions: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        environment_id = self.environment_id

        id = self.id

        provider_identity = self.provider_identity

        scope = self.scope

        subject_id = self.subject_id

        availability = self.availability

        supports_changes = self.supports_changes

        supports_revisions = self.supports_revisions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "environment_id": environment_id,
                "id": id,
                "provider_identity": provider_identity,
                "scope": scope,
                "subject_id": subject_id,
            }
        )
        if availability is not UNSET:
            field_dict["availability"] = availability
        if supports_changes is not UNSET:
            field_dict["supports_changes"] = supports_changes
        if supports_revisions is not UNSET:
            field_dict["supports_revisions"] = supports_revisions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        environment_id = d.pop("environment_id")

        id = d.pop("id")

        provider_identity = d.pop("provider_identity")

        scope = d.pop("scope")

        subject_id = d.pop("subject_id")

        availability = cast(Literal["unresolved"] | Unset, d.pop("availability", UNSET))
        if availability != "unresolved" and not isinstance(availability, Unset):
            raise ValueError(f"availability must match const 'unresolved', got '{availability}'")

        supports_changes = d.pop("supports_changes", UNSET)

        supports_revisions = d.pop("supports_revisions", UNSET)

        stored_memory_scope = cls(
            environment_id=environment_id,
            id=id,
            provider_identity=provider_identity,
            scope=scope,
            subject_id=subject_id,
            availability=availability,
            supports_changes=supports_changes,
            supports_revisions=supports_revisions,
        )

        stored_memory_scope.additional_properties = d
        return stored_memory_scope

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
