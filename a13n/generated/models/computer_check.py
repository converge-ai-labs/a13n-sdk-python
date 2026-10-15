from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.computer_check_status import ComputerCheckStatus
from ..models.environment_action import EnvironmentAction
from ..types import UNSET, Unset

T = TypeVar("T", bound="ComputerCheck")


@_attrs_define(repr=False)
class ComputerCheck:
    """A point-in-time capability probe, not an Agent or mount permission grant.

    Attributes:
        status (ComputerCheckStatus):
        display_count (int | Unset):
        input_ready (bool | Unset):
        observe_ready (bool | Unset):
        operations (list[EnvironmentAction] | Unset):
    """

    status: ComputerCheckStatus
    display_count: int | Unset = UNSET
    input_ready: bool | Unset = UNSET
    observe_ready: bool | Unset = UNSET
    operations: list[EnvironmentAction] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        display_count = self.display_count

        input_ready = self.input_ready

        observe_ready = self.observe_ready

        operations: list[str] | Unset = UNSET
        if not isinstance(self.operations, Unset):
            operations = []
            for operations_item_data in self.operations:
                operations_item = operations_item_data.value
                operations.append(operations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if display_count is not UNSET:
            field_dict["display_count"] = display_count
        if input_ready is not UNSET:
            field_dict["input_ready"] = input_ready
        if observe_ready is not UNSET:
            field_dict["observe_ready"] = observe_ready
        if operations is not UNSET:
            field_dict["operations"] = operations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = ComputerCheckStatus(d.pop("status"))

        display_count = d.pop("display_count", UNSET)

        input_ready = d.pop("input_ready", UNSET)

        observe_ready = d.pop("observe_ready", UNSET)

        _operations = d.pop("operations", UNSET)
        operations: list[EnvironmentAction] | Unset = UNSET
        if _operations is not UNSET:
            operations = []
            for operations_item_data in _operations:
                operations_item = EnvironmentAction(operations_item_data)

                operations.append(operations_item)

        computer_check = cls(
            status=status,
            display_count=display_count,
            input_ready=input_ready,
            observe_ready=observe_ready,
            operations=operations,
        )

        computer_check.additional_properties = d
        return computer_check

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
