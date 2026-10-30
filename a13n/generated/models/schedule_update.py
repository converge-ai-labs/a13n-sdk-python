from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cron_schedule import CronSchedule
    from ..models.once_schedule import OnceSchedule
    from ..models.schedule_invocation_input import ScheduleInvocationInput
    from ..models.schedule_target import ScheduleTarget
    from ..models.schedule_update_labels_type_0 import ScheduleUpdateLabelsType0


T = TypeVar("T", bound="ScheduleUpdate")


@_attrs_define(repr=False)
class ScheduleUpdate:
    """
    Attributes:
        description (None | str | Unset):
        invocation (None | ScheduleInvocationInput | Unset):
        labels (None | ScheduleUpdateLabelsType0 | Unset):
        max_lateness_seconds (int | None | Unset):
        name (None | str | Unset):
        schedule (CronSchedule | None | OnceSchedule | Unset):
        target (None | ScheduleTarget | Unset):
    """

    description: str | Unset | None = UNSET
    invocation: ScheduleInvocationInput | Unset | None = UNSET
    labels: ScheduleUpdateLabelsType0 | Unset | None = UNSET
    max_lateness_seconds: int | Unset | None = UNSET
    name: str | Unset | None = UNSET
    schedule: CronSchedule | OnceSchedule | Unset | None = UNSET
    target: ScheduleTarget | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.cron_schedule import CronSchedule
        from ..models.once_schedule import OnceSchedule
        from ..models.schedule_invocation_input import ScheduleInvocationInput
        from ..models.schedule_target import ScheduleTarget
        from ..models.schedule_update_labels_type_0 import ScheduleUpdateLabelsType0

        description: str | Unset | None
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        invocation: dict[str, Any] | Unset | None
        if isinstance(self.invocation, Unset):
            invocation = UNSET
        elif isinstance(self.invocation, ScheduleInvocationInput):
            invocation = self.invocation.to_dict()
        else:
            invocation = self.invocation

        labels: dict[str, Any] | Unset | None
        if isinstance(self.labels, Unset):
            labels = UNSET
        elif isinstance(self.labels, ScheduleUpdateLabelsType0):
            labels = self.labels.to_dict()
        else:
            labels = self.labels

        max_lateness_seconds: int | Unset | None
        if isinstance(self.max_lateness_seconds, Unset):
            max_lateness_seconds = UNSET
        else:
            max_lateness_seconds = self.max_lateness_seconds

        name: str | Unset | None
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        schedule: dict[str, Any] | Unset | None
        if isinstance(self.schedule, Unset):
            schedule = UNSET
        elif isinstance(self.schedule, CronSchedule):
            schedule = self.schedule.to_dict()
        elif isinstance(self.schedule, OnceSchedule):
            schedule = self.schedule.to_dict()
        else:
            schedule = self.schedule

        target: dict[str, Any] | Unset | None
        if isinstance(self.target, Unset):
            target = UNSET
        elif isinstance(self.target, ScheduleTarget):
            target = self.target.to_dict()
        else:
            target = self.target

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if invocation is not UNSET:
            field_dict["invocation"] = invocation
        if labels is not UNSET:
            field_dict["labels"] = labels
        if max_lateness_seconds is not UNSET:
            field_dict["max_lateness_seconds"] = max_lateness_seconds
        if name is not UNSET:
            field_dict["name"] = name
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cron_schedule import CronSchedule
        from ..models.once_schedule import OnceSchedule
        from ..models.schedule_invocation_input import ScheduleInvocationInput
        from ..models.schedule_target import ScheduleTarget
        from ..models.schedule_update_labels_type_0 import ScheduleUpdateLabelsType0

        d = dict(src_dict)

        def _parse_description(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_invocation(data: object) -> ScheduleInvocationInput | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_0 = ScheduleInvocationInput.from_dict(data)

                return invocation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ScheduleInvocationInput | Unset | None, data)

        invocation = _parse_invocation(d.pop("invocation", UNSET))

        def _parse_labels(data: object) -> ScheduleUpdateLabelsType0 | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                labels_type_0 = ScheduleUpdateLabelsType0.from_dict(data)

                return labels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ScheduleUpdateLabelsType0 | Unset | None, data)

        labels = _parse_labels(d.pop("labels", UNSET))

        def _parse_max_lateness_seconds(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        max_lateness_seconds = _parse_max_lateness_seconds(d.pop("max_lateness_seconds", UNSET))

        def _parse_name(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_schedule(data: object) -> CronSchedule | OnceSchedule | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_schedule_rule_type_0 = CronSchedule.from_dict(data)

                return componentsschemas_schedule_rule_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_schedule_rule_type_1 = OnceSchedule.from_dict(data)

                return componentsschemas_schedule_rule_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CronSchedule | OnceSchedule | Unset | None, data)

        schedule = _parse_schedule(d.pop("schedule", UNSET))

        def _parse_target(data: object) -> ScheduleTarget | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                target_type_0 = ScheduleTarget.from_dict(data)

                return target_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ScheduleTarget | Unset | None, data)

        target = _parse_target(d.pop("target", UNSET))

        schedule_update = cls(
            description=description,
            invocation=invocation,
            labels=labels,
            max_lateness_seconds=max_lateness_seconds,
            name=name,
            schedule=schedule,
            target=target,
        )

        return schedule_update
