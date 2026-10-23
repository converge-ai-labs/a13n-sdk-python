from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.collector import Collector
from ..models.collector_capability_reason_type_0 import CollectorCapabilityReasonType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="CollectorCapability")


@_attrs_define(repr=False)
class CollectorCapability:
    """
    Attributes:
        available (bool):
        kind (Collector):
        reason (CollectorCapabilityReasonType0 | None | Unset):
    """

    available: bool
    kind: Collector
    reason: CollectorCapabilityReasonType0 | Unset | None = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        available = self.available

        kind = self.kind.value

        reason: str | Unset | None
        if isinstance(self.reason, Unset):
            reason = UNSET
        elif isinstance(self.reason, CollectorCapabilityReasonType0):
            reason = self.reason.value
        else:
            reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "available": available,
                "kind": kind,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        available = d.pop("available")

        kind = Collector(d.pop("kind"))

        def _parse_reason(data: object) -> CollectorCapabilityReasonType0 | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reason_type_0 = CollectorCapabilityReasonType0(data)

                return reason_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CollectorCapabilityReasonType0 | Unset | None, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        collector_capability = cls(
            available=available,
            kind=kind,
            reason=reason,
        )

        collector_capability.additional_properties = d
        return collector_capability

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
