from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.disk_metrics import DiskMetrics
    from ..models.limited_cpu_limit import LimitedCpuLimit
    from ..models.limited_memory_limit import LimitedMemoryLimit
    from ..models.memory_events import MemoryEvents
    from ..models.pressures import Pressures
    from ..models.unlimited_cpu_limit import UnlimitedCpuLimit
    from ..models.unlimited_memory_limit import UnlimitedMemoryLimit


T = TypeVar("T", bound="CgroupMetrics")


@_attrs_define(repr=False)
class CgroupMetrics:
    """
    Attributes:
        memory_events (MemoryEvents):
        pressure (Pressures):
        cpu_max (LimitedCpuLimit | None | UnlimitedCpuLimit | Unset):
        cpu_periods_total (int | None | Unset):
        cpu_system_usec (int | None | Unset):
        cpu_throttled_periods_total (int | None | Unset):
        cpu_throttled_usec (int | None | Unset):
        cpu_usage_usec (int | None | Unset):
        cpu_user_usec (int | None | Unset):
        io (DiskMetrics | None | Unset):
        memory_current_bytes (int | None | Unset):
        memory_max (LimitedMemoryLimit | None | UnlimitedMemoryLimit | Unset):
        pids_current (int | None | Unset):
        pids_limit (int | None | Unset):
        pids_unlimited (bool | None | Unset):
    """

    memory_events: MemoryEvents
    pressure: Pressures
    cpu_max: LimitedCpuLimit | UnlimitedCpuLimit | Unset | None = UNSET
    cpu_periods_total: int | Unset | None = UNSET
    cpu_system_usec: int | Unset | None = UNSET
    cpu_throttled_periods_total: int | Unset | None = UNSET
    cpu_throttled_usec: int | Unset | None = UNSET
    cpu_usage_usec: int | Unset | None = UNSET
    cpu_user_usec: int | Unset | None = UNSET
    io: DiskMetrics | Unset | None = UNSET
    memory_current_bytes: int | Unset | None = UNSET
    memory_max: LimitedMemoryLimit | UnlimitedMemoryLimit | Unset | None = UNSET
    pids_current: int | Unset | None = UNSET
    pids_limit: int | Unset | None = UNSET
    pids_unlimited: bool | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.disk_metrics import DiskMetrics
        from ..models.limited_cpu_limit import LimitedCpuLimit
        from ..models.limited_memory_limit import LimitedMemoryLimit
        from ..models.unlimited_cpu_limit import UnlimitedCpuLimit
        from ..models.unlimited_memory_limit import UnlimitedMemoryLimit

        memory_events = self.memory_events.to_dict()

        pressure = self.pressure.to_dict()

        cpu_max: dict[str, Any] | Unset | None
        if isinstance(self.cpu_max, Unset):
            cpu_max = UNSET
        elif isinstance(self.cpu_max, UnlimitedCpuLimit):
            cpu_max = self.cpu_max.to_dict()
        elif isinstance(self.cpu_max, LimitedCpuLimit):
            cpu_max = self.cpu_max.to_dict()
        else:
            cpu_max = self.cpu_max

        cpu_periods_total: int | Unset | None
        if isinstance(self.cpu_periods_total, Unset):
            cpu_periods_total = UNSET
        else:
            cpu_periods_total = self.cpu_periods_total

        cpu_system_usec: int | Unset | None
        if isinstance(self.cpu_system_usec, Unset):
            cpu_system_usec = UNSET
        else:
            cpu_system_usec = self.cpu_system_usec

        cpu_throttled_periods_total: int | Unset | None
        if isinstance(self.cpu_throttled_periods_total, Unset):
            cpu_throttled_periods_total = UNSET
        else:
            cpu_throttled_periods_total = self.cpu_throttled_periods_total

        cpu_throttled_usec: int | Unset | None
        if isinstance(self.cpu_throttled_usec, Unset):
            cpu_throttled_usec = UNSET
        else:
            cpu_throttled_usec = self.cpu_throttled_usec

        cpu_usage_usec: int | Unset | None
        if isinstance(self.cpu_usage_usec, Unset):
            cpu_usage_usec = UNSET
        else:
            cpu_usage_usec = self.cpu_usage_usec

        cpu_user_usec: int | Unset | None
        if isinstance(self.cpu_user_usec, Unset):
            cpu_user_usec = UNSET
        else:
            cpu_user_usec = self.cpu_user_usec

        io: dict[str, Any] | Unset | None
        if isinstance(self.io, Unset):
            io = UNSET
        elif isinstance(self.io, DiskMetrics):
            io = self.io.to_dict()
        else:
            io = self.io

        memory_current_bytes: int | Unset | None
        if isinstance(self.memory_current_bytes, Unset):
            memory_current_bytes = UNSET
        else:
            memory_current_bytes = self.memory_current_bytes

        memory_max: dict[str, Any] | Unset | None
        if isinstance(self.memory_max, Unset):
            memory_max = UNSET
        elif isinstance(self.memory_max, UnlimitedMemoryLimit):
            memory_max = self.memory_max.to_dict()
        elif isinstance(self.memory_max, LimitedMemoryLimit):
            memory_max = self.memory_max.to_dict()
        else:
            memory_max = self.memory_max

        pids_current: int | Unset | None
        if isinstance(self.pids_current, Unset):
            pids_current = UNSET
        else:
            pids_current = self.pids_current

        pids_limit: int | Unset | None
        if isinstance(self.pids_limit, Unset):
            pids_limit = UNSET
        else:
            pids_limit = self.pids_limit

        pids_unlimited: bool | Unset | None
        if isinstance(self.pids_unlimited, Unset):
            pids_unlimited = UNSET
        else:
            pids_unlimited = self.pids_unlimited

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "memory_events": memory_events,
                "pressure": pressure,
            }
        )
        if cpu_max is not UNSET:
            field_dict["cpu_max"] = cpu_max
        if cpu_periods_total is not UNSET:
            field_dict["cpu_periods_total"] = cpu_periods_total
        if cpu_system_usec is not UNSET:
            field_dict["cpu_system_usec"] = cpu_system_usec
        if cpu_throttled_periods_total is not UNSET:
            field_dict["cpu_throttled_periods_total"] = cpu_throttled_periods_total
        if cpu_throttled_usec is not UNSET:
            field_dict["cpu_throttled_usec"] = cpu_throttled_usec
        if cpu_usage_usec is not UNSET:
            field_dict["cpu_usage_usec"] = cpu_usage_usec
        if cpu_user_usec is not UNSET:
            field_dict["cpu_user_usec"] = cpu_user_usec
        if io is not UNSET:
            field_dict["io"] = io
        if memory_current_bytes is not UNSET:
            field_dict["memory_current_bytes"] = memory_current_bytes
        if memory_max is not UNSET:
            field_dict["memory_max"] = memory_max
        if pids_current is not UNSET:
            field_dict["pids_current"] = pids_current
        if pids_limit is not UNSET:
            field_dict["pids_limit"] = pids_limit
        if pids_unlimited is not UNSET:
            field_dict["pids_unlimited"] = pids_unlimited

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.disk_metrics import DiskMetrics
        from ..models.limited_cpu_limit import LimitedCpuLimit
        from ..models.limited_memory_limit import LimitedMemoryLimit
        from ..models.memory_events import MemoryEvents
        from ..models.pressures import Pressures
        from ..models.unlimited_cpu_limit import UnlimitedCpuLimit
        from ..models.unlimited_memory_limit import UnlimitedMemoryLimit

        d = dict(src_dict)
        memory_events = MemoryEvents.from_dict(d.pop("memory_events"))

        pressure = Pressures.from_dict(d.pop("pressure"))

        def _parse_cpu_max(data: object) -> LimitedCpuLimit | UnlimitedCpuLimit | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_cpu_limit_type_0 = UnlimitedCpuLimit.from_dict(data)

                return componentsschemas_cpu_limit_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_cpu_limit_type_1 = LimitedCpuLimit.from_dict(data)

                return componentsschemas_cpu_limit_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LimitedCpuLimit | UnlimitedCpuLimit | Unset | None, data)

        cpu_max = _parse_cpu_max(d.pop("cpu_max", UNSET))

        def _parse_cpu_periods_total(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        cpu_periods_total = _parse_cpu_periods_total(d.pop("cpu_periods_total", UNSET))

        def _parse_cpu_system_usec(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        cpu_system_usec = _parse_cpu_system_usec(d.pop("cpu_system_usec", UNSET))

        def _parse_cpu_throttled_periods_total(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        cpu_throttled_periods_total = _parse_cpu_throttled_periods_total(d.pop("cpu_throttled_periods_total", UNSET))

        def _parse_cpu_throttled_usec(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        cpu_throttled_usec = _parse_cpu_throttled_usec(d.pop("cpu_throttled_usec", UNSET))

        def _parse_cpu_usage_usec(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        cpu_usage_usec = _parse_cpu_usage_usec(d.pop("cpu_usage_usec", UNSET))

        def _parse_cpu_user_usec(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        cpu_user_usec = _parse_cpu_user_usec(d.pop("cpu_user_usec", UNSET))

        def _parse_io(data: object) -> DiskMetrics | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                io_type_0 = DiskMetrics.from_dict(data)

                return io_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DiskMetrics | Unset | None, data)

        io = _parse_io(d.pop("io", UNSET))

        def _parse_memory_current_bytes(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        memory_current_bytes = _parse_memory_current_bytes(d.pop("memory_current_bytes", UNSET))

        def _parse_memory_max(data: object) -> LimitedMemoryLimit | UnlimitedMemoryLimit | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_memory_limit_type_0 = UnlimitedMemoryLimit.from_dict(data)

                return componentsschemas_memory_limit_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_memory_limit_type_1 = LimitedMemoryLimit.from_dict(data)

                return componentsschemas_memory_limit_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LimitedMemoryLimit | UnlimitedMemoryLimit | Unset | None, data)

        memory_max = _parse_memory_max(d.pop("memory_max", UNSET))

        def _parse_pids_current(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        pids_current = _parse_pids_current(d.pop("pids_current", UNSET))

        def _parse_pids_limit(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        pids_limit = _parse_pids_limit(d.pop("pids_limit", UNSET))

        def _parse_pids_unlimited(data: object) -> bool | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | Unset | None, data)

        pids_unlimited = _parse_pids_unlimited(d.pop("pids_unlimited", UNSET))

        cgroup_metrics = cls(
            memory_events=memory_events,
            pressure=pressure,
            cpu_max=cpu_max,
            cpu_periods_total=cpu_periods_total,
            cpu_system_usec=cpu_system_usec,
            cpu_throttled_periods_total=cpu_throttled_periods_total,
            cpu_throttled_usec=cpu_throttled_usec,
            cpu_usage_usec=cpu_usage_usec,
            cpu_user_usec=cpu_user_usec,
            io=io,
            memory_current_bytes=memory_current_bytes,
            memory_max=memory_max,
            pids_current=pids_current,
            pids_limit=pids_limit,
            pids_unlimited=pids_unlimited,
        )

        return cgroup_metrics
