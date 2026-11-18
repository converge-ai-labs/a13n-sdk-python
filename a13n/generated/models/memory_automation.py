from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.organization_policy import OrganizationPolicy
    from ..models.space_organization_status import SpaceOrganizationStatus


T = TypeVar("T", bound="MemoryAutomation")


@_attrs_define(repr=False)
class MemoryAutomation:
    """
    Attributes:
        id (str):
        policy (OrganizationPolicy):
        processed_history_runs (int):
        status (SpaceOrganizationStatus):
        version (int):
    """

    id: str
    policy: OrganizationPolicy
    processed_history_runs: int
    status: SpaceOrganizationStatus
    version: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        policy = self.policy.to_dict()

        processed_history_runs = self.processed_history_runs

        status = self.status.to_dict()

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "policy": policy,
                "processed_history_runs": processed_history_runs,
                "status": status,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization_policy import OrganizationPolicy
        from ..models.space_organization_status import SpaceOrganizationStatus

        d = dict(src_dict)
        id = d.pop("id")

        policy = OrganizationPolicy.from_dict(d.pop("policy"))

        processed_history_runs = d.pop("processed_history_runs")

        status = SpaceOrganizationStatus.from_dict(d.pop("status"))

        version = d.pop("version")

        memory_automation = cls(
            id=id,
            policy=policy,
            processed_history_runs=processed_history_runs,
            status=status,
            version=version,
        )

        memory_automation.additional_properties = d
        return memory_automation

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
