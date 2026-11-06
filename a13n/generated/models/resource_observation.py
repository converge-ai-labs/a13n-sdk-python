from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.resource_observation_observation import ResourceObservationObservation
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resource import Resource
    from ..models.resource_observation_status import ResourceObservationStatus


T = TypeVar("T", bound="ResourceObservation")


@_attrs_define(repr=False)
class ResourceObservation:
    """
    Attributes:
        observation (ResourceObservationObservation):
        reference (Resource):
        created_at (None | str | Unset):
        deleting_at (None | str | Unset):
        finalizers (list[str] | Unset):
        reason (None | str | Unset):
        status (ResourceObservationStatus | Unset):
    """

    observation: ResourceObservationObservation
    reference: Resource
    created_at: str | Unset | None = UNSET
    deleting_at: str | Unset | None = UNSET
    finalizers: list[str] | Unset = UNSET
    reason: str | Unset | None = UNSET
    status: ResourceObservationStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        observation = self.observation.value

        reference = self.reference.to_dict()

        created_at: str | Unset | None
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        else:
            created_at = self.created_at

        deleting_at: str | Unset | None
        if isinstance(self.deleting_at, Unset):
            deleting_at = UNSET
        else:
            deleting_at = self.deleting_at

        finalizers: list[str] | Unset = UNSET
        if not isinstance(self.finalizers, Unset):
            finalizers = self.finalizers

        reason: str | Unset | None
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "observation": observation,
                "reference": reference,
            }
        )
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if deleting_at is not UNSET:
            field_dict["deleting_at"] = deleting_at
        if finalizers is not UNSET:
            field_dict["finalizers"] = finalizers
        if reason is not UNSET:
            field_dict["reason"] = reason
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource import Resource
        from ..models.resource_observation_status import ResourceObservationStatus

        d = dict(src_dict)
        observation = ResourceObservationObservation(d.pop("observation"))

        reference = Resource.from_dict(d.pop("reference"))

        def _parse_created_at(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        def _parse_deleting_at(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        deleting_at = _parse_deleting_at(d.pop("deleting_at", UNSET))

        finalizers = cast(list[str], d.pop("finalizers", UNSET))

        def _parse_reason(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        _status = d.pop("status", UNSET)
        status: ResourceObservationStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ResourceObservationStatus.from_dict(_status)

        resource_observation = cls(
            observation=observation,
            reference=reference,
            created_at=created_at,
            deleting_at=deleting_at,
            finalizers=finalizers,
            reason=reason,
            status=status,
        )

        resource_observation.additional_properties = d
        return resource_observation

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
