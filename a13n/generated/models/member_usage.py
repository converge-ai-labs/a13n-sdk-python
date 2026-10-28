from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.member_usage_kind import MemberUsageKind
from ..models.member_usage_status import MemberUsageStatus

if TYPE_CHECKING:
    from ..models.model_metrics import ModelMetrics
    from ..models.run_metrics import RunMetrics


T = TypeVar("T", bound="MemberUsage")


@_attrs_define(repr=False)
class MemberUsage:
    """
    Attributes:
        kind (MemberUsageKind):
        name (str):
        principal_id (str):
        runs (RunMetrics):
        status (MemberUsageStatus):
        usage (ModelMetrics):
    """

    kind: MemberUsageKind
    name: str
    principal_id: str
    runs: RunMetrics
    status: MemberUsageStatus
    usage: ModelMetrics
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        name = self.name

        principal_id = self.principal_id

        runs = self.runs.to_dict()

        status = self.status.value

        usage = self.usage.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "name": name,
                "principal_id": principal_id,
                "runs": runs,
                "status": status,
                "usage": usage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_metrics import ModelMetrics
        from ..models.run_metrics import RunMetrics

        d = dict(src_dict)
        kind = MemberUsageKind(d.pop("kind"))

        name = d.pop("name")

        principal_id = d.pop("principal_id")

        runs = RunMetrics.from_dict(d.pop("runs"))

        status = MemberUsageStatus(d.pop("status"))

        usage = ModelMetrics.from_dict(d.pop("usage"))

        member_usage = cls(
            kind=kind,
            name=name,
            principal_id=principal_id,
            runs=runs,
            status=status,
            usage=usage,
        )

        member_usage.additional_properties = d
        return member_usage

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
