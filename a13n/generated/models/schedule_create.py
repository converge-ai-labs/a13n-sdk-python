from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.schedule_create_state import ScheduleCreateState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cron_schedule import CronSchedule
    from ..models.once_schedule import OnceSchedule
    from ..models.schedule_create_labels import ScheduleCreateLabels
    from ..models.schedule_invocation_input import ScheduleInvocationInput


T = TypeVar("T", bound="ScheduleCreate")


@_attrs_define(repr=False)
class ScheduleCreate:
    """
    Attributes:
        invocation (ScheduleInvocationInput):
        name (str):
        schedule (CronSchedule | OnceSchedule):
        description (None | str | Unset):
        labels (ScheduleCreateLabels | Unset):
        max_lateness_seconds (int | Unset):
        state (ScheduleCreateState | Unset):
    """

    invocation: ScheduleInvocationInput
    name: str
    schedule: CronSchedule | OnceSchedule
    description: str | Unset | None = UNSET
    labels: ScheduleCreateLabels | Unset = UNSET
    max_lateness_seconds: int | Unset = UNSET
    state: ScheduleCreateState | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.cron_schedule import CronSchedule

        invocation = self.invocation.to_dict()

        name = self.name

        schedule: dict[str, Any]
        if isinstance(self.schedule, CronSchedule):
            schedule = self.schedule.to_dict()
        else:
            schedule = self.schedule.to_dict()

        description: str | Unset | None
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        max_lateness_seconds = self.max_lateness_seconds

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "invocation": invocation,
                "name": name,
                "schedule": schedule,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if labels is not UNSET:
            field_dict["labels"] = labels
        if max_lateness_seconds is not UNSET:
            field_dict["max_lateness_seconds"] = max_lateness_seconds
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cron_schedule import CronSchedule
        from ..models.once_schedule import OnceSchedule
        from ..models.schedule_create_labels import ScheduleCreateLabels
        from ..models.schedule_invocation_input import ScheduleInvocationInput

        d = dict(src_dict)
        invocation = ScheduleInvocationInput.from_dict(d.pop("invocation"))

        name = d.pop("name")

        def _parse_schedule(data: object) -> CronSchedule | OnceSchedule:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_schedule_rule_type_0 = CronSchedule.from_dict(data)

                return componentsschemas_schedule_rule_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_schedule_rule_type_1 = OnceSchedule.from_dict(data)

            return componentsschemas_schedule_rule_type_1

        schedule = _parse_schedule(d.pop("schedule"))

        def _parse_description(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        description = _parse_description(d.pop("description", UNSET))

        _labels = d.pop("labels", UNSET)
        labels: ScheduleCreateLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = ScheduleCreateLabels.from_dict(_labels)

        max_lateness_seconds = d.pop("max_lateness_seconds", UNSET)

        _state = d.pop("state", UNSET)
        state: ScheduleCreateState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = ScheduleCreateState(_state)

        schedule_create = cls(
            invocation=invocation,
            name=name,
            schedule=schedule,
            description=description,
            labels=labels,
            max_lateness_seconds=max_lateness_seconds,
            state=state,
        )

        return schedule_create
