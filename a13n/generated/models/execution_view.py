from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.execution_view_status import ExecutionViewStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecutionView")


@_attrs_define(repr=False)
class ExecutionView:
    """Run identity is the Service Run; attempt and worker identify the retained owner.

    Attributes:
        attempt_id (str):
        cancel_requested_at (datetime.datetime | None):
        execution_id (str):
        expires_at (datetime.datetime | None):
        first_delivered_at (datetime.datetime | None):
        run_id (str):
        thread_id (str):
        tool_call_id (str):
        tool_name (str):
        worker_id (str):
        completed_at (datetime.datetime | None | Unset):
        created_at (datetime.datetime | Unset):
        delivery_acknowledged (bool | Unset):
        error (None | str | Unset):
        foreground_released (bool | Unset):
        result_available (bool | Unset):
        status (ExecutionViewStatus | Unset):
    """

    attempt_id: str
    cancel_requested_at: datetime.datetime | None
    execution_id: str
    expires_at: datetime.datetime | None
    first_delivered_at: datetime.datetime | None
    run_id: str
    thread_id: str
    tool_call_id: str
    tool_name: str
    worker_id: str
    completed_at: datetime.datetime | Unset | None = UNSET
    created_at: datetime.datetime | Unset = UNSET
    delivery_acknowledged: bool | Unset = UNSET
    error: str | Unset | None = UNSET
    foreground_released: bool | Unset = UNSET
    result_available: bool | Unset = UNSET
    status: ExecutionViewStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attempt_id = self.attempt_id

        cancel_requested_at: str | None
        if isinstance(self.cancel_requested_at, datetime.datetime):
            cancel_requested_at = self.cancel_requested_at.isoformat()
        else:
            cancel_requested_at = self.cancel_requested_at

        execution_id = self.execution_id

        expires_at: str | None
        if isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        first_delivered_at: str | None
        if isinstance(self.first_delivered_at, datetime.datetime):
            first_delivered_at = self.first_delivered_at.isoformat()
        else:
            first_delivered_at = self.first_delivered_at

        run_id = self.run_id

        thread_id = self.thread_id

        tool_call_id = self.tool_call_id

        tool_name = self.tool_name

        worker_id = self.worker_id

        completed_at: str | Unset | None
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        delivery_acknowledged = self.delivery_acknowledged

        error: str | Unset | None
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        foreground_released = self.foreground_released

        result_available = self.result_available

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attempt_id": attempt_id,
                "cancel_requested_at": cancel_requested_at,
                "execution_id": execution_id,
                "expires_at": expires_at,
                "first_delivered_at": first_delivered_at,
                "run_id": run_id,
                "thread_id": thread_id,
                "tool_call_id": tool_call_id,
                "tool_name": tool_name,
                "worker_id": worker_id,
            }
        )
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if delivery_acknowledged is not UNSET:
            field_dict["delivery_acknowledged"] = delivery_acknowledged
        if error is not UNSET:
            field_dict["error"] = error
        if foreground_released is not UNSET:
            field_dict["foreground_released"] = foreground_released
        if result_available is not UNSET:
            field_dict["result_available"] = result_available
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attempt_id = d.pop("attempt_id")

        def _parse_cancel_requested_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cancel_requested_at_type_0 = datetime.datetime.fromisoformat(data)

                return cancel_requested_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        cancel_requested_at = _parse_cancel_requested_at(d.pop("cancel_requested_at"))

        execution_id = d.pop("execution_id")

        def _parse_expires_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = datetime.datetime.fromisoformat(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        expires_at = _parse_expires_at(d.pop("expires_at"))

        def _parse_first_delivered_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                first_delivered_at_type_0 = datetime.datetime.fromisoformat(data)

                return first_delivered_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        first_delivered_at = _parse_first_delivered_at(d.pop("first_delivered_at"))

        run_id = d.pop("run_id")

        thread_id = d.pop("thread_id")

        tool_call_id = d.pop("tool_call_id")

        tool_name = d.pop("tool_name")

        worker_id = d.pop("worker_id")

        def _parse_completed_at(data: object) -> datetime.datetime | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = datetime.datetime.fromisoformat(data)

                return completed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | Unset | None, data)

        completed_at = _parse_completed_at(d.pop("completed_at", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        delivery_acknowledged = d.pop("delivery_acknowledged", UNSET)

        def _parse_error(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        error = _parse_error(d.pop("error", UNSET))

        foreground_released = d.pop("foreground_released", UNSET)

        result_available = d.pop("result_available", UNSET)

        _status = d.pop("status", UNSET)
        status: ExecutionViewStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ExecutionViewStatus(_status)

        execution_view = cls(
            attempt_id=attempt_id,
            cancel_requested_at=cancel_requested_at,
            execution_id=execution_id,
            expires_at=expires_at,
            first_delivered_at=first_delivered_at,
            run_id=run_id,
            thread_id=thread_id,
            tool_call_id=tool_call_id,
            tool_name=tool_name,
            worker_id=worker_id,
            completed_at=completed_at,
            created_at=created_at,
            delivery_acknowledged=delivery_acknowledged,
            error=error,
            foreground_released=foreground_released,
            result_available=result_available,
            status=status,
        )

        execution_view.additional_properties = d
        return execution_view

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
