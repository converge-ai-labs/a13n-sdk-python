from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.collector import Collector
from ..models.collector_status_state_type_1 import CollectorStatusStateType1
from ..models.state import State
from ..types import UNSET, Unset

T = TypeVar("T", bound="CollectorStatus")


@_attrs_define(repr=False)
class CollectorStatus:
    """
    Attributes:
        state (CollectorStatusStateType1 | State):
        checked_at (float | None | Unset):
        collector (Collector | None | Unset):
    """

    state: CollectorStatusStateType1 | State
    checked_at: float | Unset | None = UNSET
    collector: Collector | Unset | None = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state: str
        if isinstance(self.state, State):
            state = self.state.value
        else:
            state = self.state.value

        checked_at: float | Unset | None
        if isinstance(self.checked_at, Unset):
            checked_at = UNSET
        else:
            checked_at = self.checked_at

        collector: str | Unset | None
        if isinstance(self.collector, Unset):
            collector = UNSET
        elif isinstance(self.collector, Collector):
            collector = self.collector.value
        else:
            collector = self.collector

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
            }
        )
        if checked_at is not UNSET:
            field_dict["checked_at"] = checked_at
        if collector is not UNSET:
            field_dict["collector"] = collector

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_state(data: object) -> CollectorStatusStateType1 | State:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                state_type_0 = State(data)

                return state_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, str):
                raise TypeError()
            state_type_1 = CollectorStatusStateType1(data)

            return state_type_1

        state = _parse_state(d.pop("state"))

        def _parse_checked_at(data: object) -> float | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | Unset | None, data)

        checked_at = _parse_checked_at(d.pop("checked_at", UNSET))

        def _parse_collector(data: object) -> Collector | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                collector_type_0 = Collector(data)

                return collector_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Collector | Unset | None, data)

        collector = _parse_collector(d.pop("collector", UNSET))

        collector_status = cls(
            state=state,
            checked_at=checked_at,
            collector=collector,
        )

        collector_status.additional_properties = d
        return collector_status

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
