from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.any_change_trigger import AnyChangeTrigger
    from ..models.change_count_trigger import ChangeCountTrigger


T = TypeVar("T", bound="OrganizationPolicy")


@_attrs_define(repr=False)
class OrganizationPolicy:
    """
    Attributes:
        check_interval_seconds (int | Unset):
        cooldown_seconds (int | Unset):
        enabled (bool | Unset):
        model (None | str | Unset):
        trigger (AnyChangeTrigger | ChangeCountTrigger | Unset):
    """

    check_interval_seconds: int | Unset = UNSET
    cooldown_seconds: int | Unset = UNSET
    enabled: bool | Unset = UNSET
    model: str | Unset | None = UNSET
    trigger: AnyChangeTrigger | ChangeCountTrigger | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.any_change_trigger import AnyChangeTrigger

        check_interval_seconds = self.check_interval_seconds

        cooldown_seconds = self.cooldown_seconds

        enabled = self.enabled

        model: str | Unset | None
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        trigger: dict[str, Any] | Unset
        if isinstance(self.trigger, Unset):
            trigger = UNSET
        elif isinstance(self.trigger, AnyChangeTrigger):
            trigger = self.trigger.to_dict()
        else:
            trigger = self.trigger.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if check_interval_seconds is not UNSET:
            field_dict["check_interval_seconds"] = check_interval_seconds
        if cooldown_seconds is not UNSET:
            field_dict["cooldown_seconds"] = cooldown_seconds
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if model is not UNSET:
            field_dict["model"] = model
        if trigger is not UNSET:
            field_dict["trigger"] = trigger

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.any_change_trigger import AnyChangeTrigger
        from ..models.change_count_trigger import ChangeCountTrigger

        d = dict(src_dict)
        check_interval_seconds = d.pop("check_interval_seconds", UNSET)

        cooldown_seconds = d.pop("cooldown_seconds", UNSET)

        enabled = d.pop("enabled", UNSET)

        def _parse_model(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        model = _parse_model(d.pop("model", UNSET))

        def _parse_trigger(data: object) -> AnyChangeTrigger | ChangeCountTrigger | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                trigger_type_0 = AnyChangeTrigger.from_dict(data)

                return trigger_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            trigger_type_1 = ChangeCountTrigger.from_dict(data)

            return trigger_type_1

        trigger = _parse_trigger(d.pop("trigger", UNSET))

        organization_policy = cls(
            check_interval_seconds=check_interval_seconds,
            cooldown_seconds=cooldown_seconds,
            enabled=enabled,
            model=model,
            trigger=trigger,
        )

        return organization_policy
