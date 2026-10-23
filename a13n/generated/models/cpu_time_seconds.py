from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CpuTimeSeconds")


@_attrs_define(repr=False)
class CpuTimeSeconds:
    """
    Attributes:
        idle (float | None | Unset):
        iowait (float | None | Unset):
        irq (float | None | Unset):
        nice (float | None | Unset):
        softirq (float | None | Unset):
        steal (float | None | Unset):
        system (float | None | Unset):
        user (float | None | Unset):
    """

    idle: float | Unset | None = UNSET
    iowait: float | Unset | None = UNSET
    irq: float | Unset | None = UNSET
    nice: float | Unset | None = UNSET
    softirq: float | Unset | None = UNSET
    steal: float | Unset | None = UNSET
    system: float | Unset | None = UNSET
    user: float | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        idle: float | Unset | None
        if isinstance(self.idle, Unset):
            idle = UNSET
        else:
            idle = self.idle

        iowait: float | Unset | None
        if isinstance(self.iowait, Unset):
            iowait = UNSET
        else:
            iowait = self.iowait

        irq: float | Unset | None
        if isinstance(self.irq, Unset):
            irq = UNSET
        else:
            irq = self.irq

        nice: float | Unset | None
        if isinstance(self.nice, Unset):
            nice = UNSET
        else:
            nice = self.nice

        softirq: float | Unset | None
        if isinstance(self.softirq, Unset):
            softirq = UNSET
        else:
            softirq = self.softirq

        steal: float | Unset | None
        if isinstance(self.steal, Unset):
            steal = UNSET
        else:
            steal = self.steal

        system: float | Unset | None
        if isinstance(self.system, Unset):
            system = UNSET
        else:
            system = self.system

        user: float | Unset | None
        if isinstance(self.user, Unset):
            user = UNSET
        else:
            user = self.user

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if idle is not UNSET:
            field_dict["idle"] = idle
        if iowait is not UNSET:
            field_dict["iowait"] = iowait
        if irq is not UNSET:
            field_dict["irq"] = irq
        if nice is not UNSET:
            field_dict["nice"] = nice
        if softirq is not UNSET:
            field_dict["softirq"] = softirq
        if steal is not UNSET:
            field_dict["steal"] = steal
        if system is not UNSET:
            field_dict["system"] = system
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_idle(data: object) -> float | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | Unset | None, data)

        idle = _parse_idle(d.pop("idle", UNSET))

        def _parse_iowait(data: object) -> float | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | Unset | None, data)

        iowait = _parse_iowait(d.pop("iowait", UNSET))

        def _parse_irq(data: object) -> float | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | Unset | None, data)

        irq = _parse_irq(d.pop("irq", UNSET))

        def _parse_nice(data: object) -> float | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | Unset | None, data)

        nice = _parse_nice(d.pop("nice", UNSET))

        def _parse_softirq(data: object) -> float | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | Unset | None, data)

        softirq = _parse_softirq(d.pop("softirq", UNSET))

        def _parse_steal(data: object) -> float | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | Unset | None, data)

        steal = _parse_steal(d.pop("steal", UNSET))

        def _parse_system(data: object) -> float | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | Unset | None, data)

        system = _parse_system(d.pop("system", UNSET))

        def _parse_user(data: object) -> float | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | Unset | None, data)

        user = _parse_user(d.pop("user", UNSET))

        cpu_time_seconds = cls(
            idle=idle,
            iowait=iowait,
            irq=irq,
            nice=nice,
            softirq=softirq,
            steal=steal,
            system=system,
            user=user,
        )

        return cpu_time_seconds
