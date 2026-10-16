from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.view_cause import ViewCause

if TYPE_CHECKING:
    from ..models.view_outcome_type_0 import ViewOutcomeType0


T = TypeVar("T", bound="View")


@_attrs_define(repr=False)
class View:
    """
    Attributes:
        cause (ViewCause):
        controller_id (None | str):
        deadline (datetime.datetime):
        environment_id (str):
        epoch (int):
        failure (None | str):
        id (str):
        lease_expires_at (datetime.datetime | None):
        mount (str):
        outcome (None | ViewOutcomeType0):
        reason (str):
        run_id (str):
        state (str):
        tool_call_id (None | str):
    """

    cause: ViewCause
    controller_id: str | None
    deadline: datetime.datetime
    environment_id: str
    epoch: int
    failure: str | None
    id: str
    lease_expires_at: datetime.datetime | None
    mount: str
    outcome: ViewOutcomeType0 | None
    reason: str
    run_id: str
    state: str
    tool_call_id: str | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.view_outcome_type_0 import ViewOutcomeType0

        cause = self.cause.value

        controller_id: str | None
        controller_id = self.controller_id

        deadline = self.deadline.isoformat()

        environment_id = self.environment_id

        epoch = self.epoch

        failure: str | None
        failure = self.failure

        id = self.id

        lease_expires_at: str | None
        if isinstance(self.lease_expires_at, datetime.datetime):
            lease_expires_at = self.lease_expires_at.isoformat()
        else:
            lease_expires_at = self.lease_expires_at

        mount = self.mount

        outcome: dict[str, Any] | None
        if isinstance(self.outcome, ViewOutcomeType0):
            outcome = self.outcome.to_dict()
        else:
            outcome = self.outcome

        reason = self.reason

        run_id = self.run_id

        state = self.state

        tool_call_id: str | None
        tool_call_id = self.tool_call_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cause": cause,
                "controller_id": controller_id,
                "deadline": deadline,
                "environment_id": environment_id,
                "epoch": epoch,
                "failure": failure,
                "id": id,
                "lease_expires_at": lease_expires_at,
                "mount": mount,
                "outcome": outcome,
                "reason": reason,
                "run_id": run_id,
                "state": state,
                "tool_call_id": tool_call_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.view_outcome_type_0 import ViewOutcomeType0

        d = dict(src_dict)
        cause = ViewCause(d.pop("cause"))

        def _parse_controller_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        controller_id = _parse_controller_id(d.pop("controller_id"))

        deadline = datetime.datetime.fromisoformat(d.pop("deadline"))

        environment_id = d.pop("environment_id")

        epoch = d.pop("epoch")

        def _parse_failure(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        failure = _parse_failure(d.pop("failure"))

        id = d.pop("id")

        def _parse_lease_expires_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                lease_expires_at_type_0 = datetime.datetime.fromisoformat(data)

                return lease_expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        lease_expires_at = _parse_lease_expires_at(d.pop("lease_expires_at"))

        mount = d.pop("mount")

        def _parse_outcome(data: object) -> ViewOutcomeType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                outcome_type_0 = ViewOutcomeType0.from_dict(data)

                return outcome_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ViewOutcomeType0 | None, data)

        outcome = _parse_outcome(d.pop("outcome"))

        reason = d.pop("reason")

        run_id = d.pop("run_id")

        state = d.pop("state")

        def _parse_tool_call_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        tool_call_id = _parse_tool_call_id(d.pop("tool_call_id"))

        view = cls(
            cause=cause,
            controller_id=controller_id,
            deadline=deadline,
            environment_id=environment_id,
            epoch=epoch,
            failure=failure,
            id=id,
            lease_expires_at=lease_expires_at,
            mount=mount,
            outcome=outcome,
            reason=reason,
            run_id=run_id,
            state=state,
            tool_call_id=tool_call_id,
        )

        view.additional_properties = d
        return view

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
