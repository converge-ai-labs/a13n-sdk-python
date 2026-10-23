from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cpu_time_seconds import CpuTimeSeconds
    from ..models.pressures import Pressures


T = TypeVar("T", bound="SystemMetrics")


@_attrs_define(repr=False)
class SystemMetrics:
    """
    Attributes:
        commit_limit_bytes (int | None | Unset):
        commit_total_bytes (int | None | Unset):
        cpu_busy_percent (float | None | Unset):
        cpu_time_seconds (CpuTimeSeconds | None | Unset):
        handle_count (int | None | Unset):
        logical_cpu_count (int | None | Unset):
        memory_available_bytes (int | None | Unset):
        memory_cache_bytes (int | None | Unset):
        memory_compressed_bytes (int | None | Unset):
        memory_total_bytes (int | None | Unset):
        memory_wired_bytes (int | None | Unset):
        pressure (None | Pressures | Unset):
        process_count (int | None | Unset):
        swap_total_bytes (int | None | Unset):
        swap_used_bytes (int | None | Unset):
        thread_count (int | None | Unset):
    """

    commit_limit_bytes: int | Unset | None = UNSET
    commit_total_bytes: int | Unset | None = UNSET
    cpu_busy_percent: float | Unset | None = UNSET
    cpu_time_seconds: CpuTimeSeconds | Unset | None = UNSET
    handle_count: int | Unset | None = UNSET
    logical_cpu_count: int | Unset | None = UNSET
    memory_available_bytes: int | Unset | None = UNSET
    memory_cache_bytes: int | Unset | None = UNSET
    memory_compressed_bytes: int | Unset | None = UNSET
    memory_total_bytes: int | Unset | None = UNSET
    memory_wired_bytes: int | Unset | None = UNSET
    pressure: Pressures | Unset | None = UNSET
    process_count: int | Unset | None = UNSET
    swap_total_bytes: int | Unset | None = UNSET
    swap_used_bytes: int | Unset | None = UNSET
    thread_count: int | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.cpu_time_seconds import CpuTimeSeconds
        from ..models.pressures import Pressures

        commit_limit_bytes: int | Unset | None
        if isinstance(self.commit_limit_bytes, Unset):
            commit_limit_bytes = UNSET
        else:
            commit_limit_bytes = self.commit_limit_bytes

        commit_total_bytes: int | Unset | None
        if isinstance(self.commit_total_bytes, Unset):
            commit_total_bytes = UNSET
        else:
            commit_total_bytes = self.commit_total_bytes

        cpu_busy_percent: float | Unset | None
        if isinstance(self.cpu_busy_percent, Unset):
            cpu_busy_percent = UNSET
        else:
            cpu_busy_percent = self.cpu_busy_percent

        cpu_time_seconds: dict[str, Any] | Unset | None
        if isinstance(self.cpu_time_seconds, Unset):
            cpu_time_seconds = UNSET
        elif isinstance(self.cpu_time_seconds, CpuTimeSeconds):
            cpu_time_seconds = self.cpu_time_seconds.to_dict()
        else:
            cpu_time_seconds = self.cpu_time_seconds

        handle_count: int | Unset | None
        if isinstance(self.handle_count, Unset):
            handle_count = UNSET
        else:
            handle_count = self.handle_count

        logical_cpu_count: int | Unset | None
        if isinstance(self.logical_cpu_count, Unset):
            logical_cpu_count = UNSET
        else:
            logical_cpu_count = self.logical_cpu_count

        memory_available_bytes: int | Unset | None
        if isinstance(self.memory_available_bytes, Unset):
            memory_available_bytes = UNSET
        else:
            memory_available_bytes = self.memory_available_bytes

        memory_cache_bytes: int | Unset | None
        if isinstance(self.memory_cache_bytes, Unset):
            memory_cache_bytes = UNSET
        else:
            memory_cache_bytes = self.memory_cache_bytes

        memory_compressed_bytes: int | Unset | None
        if isinstance(self.memory_compressed_bytes, Unset):
            memory_compressed_bytes = UNSET
        else:
            memory_compressed_bytes = self.memory_compressed_bytes

        memory_total_bytes: int | Unset | None
        if isinstance(self.memory_total_bytes, Unset):
            memory_total_bytes = UNSET
        else:
            memory_total_bytes = self.memory_total_bytes

        memory_wired_bytes: int | Unset | None
        if isinstance(self.memory_wired_bytes, Unset):
            memory_wired_bytes = UNSET
        else:
            memory_wired_bytes = self.memory_wired_bytes

        pressure: dict[str, Any] | Unset | None
        if isinstance(self.pressure, Unset):
            pressure = UNSET
        elif isinstance(self.pressure, Pressures):
            pressure = self.pressure.to_dict()
        else:
            pressure = self.pressure

        process_count: int | Unset | None
        if isinstance(self.process_count, Unset):
            process_count = UNSET
        else:
            process_count = self.process_count

        swap_total_bytes: int | Unset | None
        if isinstance(self.swap_total_bytes, Unset):
            swap_total_bytes = UNSET
        else:
            swap_total_bytes = self.swap_total_bytes

        swap_used_bytes: int | Unset | None
        if isinstance(self.swap_used_bytes, Unset):
            swap_used_bytes = UNSET
        else:
            swap_used_bytes = self.swap_used_bytes

        thread_count: int | Unset | None
        if isinstance(self.thread_count, Unset):
            thread_count = UNSET
        else:
            thread_count = self.thread_count

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if commit_limit_bytes is not UNSET:
            field_dict["commit_limit_bytes"] = commit_limit_bytes
        if commit_total_bytes is not UNSET:
            field_dict["commit_total_bytes"] = commit_total_bytes
        if cpu_busy_percent is not UNSET:
            field_dict["cpu_busy_percent"] = cpu_busy_percent
        if cpu_time_seconds is not UNSET:
            field_dict["cpu_time_seconds"] = cpu_time_seconds
        if handle_count is not UNSET:
            field_dict["handle_count"] = handle_count
        if logical_cpu_count is not UNSET:
            field_dict["logical_cpu_count"] = logical_cpu_count
        if memory_available_bytes is not UNSET:
            field_dict["memory_available_bytes"] = memory_available_bytes
        if memory_cache_bytes is not UNSET:
            field_dict["memory_cache_bytes"] = memory_cache_bytes
        if memory_compressed_bytes is not UNSET:
            field_dict["memory_compressed_bytes"] = memory_compressed_bytes
        if memory_total_bytes is not UNSET:
            field_dict["memory_total_bytes"] = memory_total_bytes
        if memory_wired_bytes is not UNSET:
            field_dict["memory_wired_bytes"] = memory_wired_bytes
        if pressure is not UNSET:
            field_dict["pressure"] = pressure
        if process_count is not UNSET:
            field_dict["process_count"] = process_count
        if swap_total_bytes is not UNSET:
            field_dict["swap_total_bytes"] = swap_total_bytes
        if swap_used_bytes is not UNSET:
            field_dict["swap_used_bytes"] = swap_used_bytes
        if thread_count is not UNSET:
            field_dict["thread_count"] = thread_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cpu_time_seconds import CpuTimeSeconds
        from ..models.pressures import Pressures

        d = dict(src_dict)

        def _parse_commit_limit_bytes(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        commit_limit_bytes = _parse_commit_limit_bytes(d.pop("commit_limit_bytes", UNSET))

        def _parse_commit_total_bytes(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        commit_total_bytes = _parse_commit_total_bytes(d.pop("commit_total_bytes", UNSET))

        def _parse_cpu_busy_percent(data: object) -> float | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | Unset | None, data)

        cpu_busy_percent = _parse_cpu_busy_percent(d.pop("cpu_busy_percent", UNSET))

        def _parse_cpu_time_seconds(data: object) -> CpuTimeSeconds | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cpu_time_seconds_type_0 = CpuTimeSeconds.from_dict(data)

                return cpu_time_seconds_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CpuTimeSeconds | Unset | None, data)

        cpu_time_seconds = _parse_cpu_time_seconds(d.pop("cpu_time_seconds", UNSET))

        def _parse_handle_count(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        handle_count = _parse_handle_count(d.pop("handle_count", UNSET))

        def _parse_logical_cpu_count(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        logical_cpu_count = _parse_logical_cpu_count(d.pop("logical_cpu_count", UNSET))

        def _parse_memory_available_bytes(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        memory_available_bytes = _parse_memory_available_bytes(d.pop("memory_available_bytes", UNSET))

        def _parse_memory_cache_bytes(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        memory_cache_bytes = _parse_memory_cache_bytes(d.pop("memory_cache_bytes", UNSET))

        def _parse_memory_compressed_bytes(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        memory_compressed_bytes = _parse_memory_compressed_bytes(d.pop("memory_compressed_bytes", UNSET))

        def _parse_memory_total_bytes(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        memory_total_bytes = _parse_memory_total_bytes(d.pop("memory_total_bytes", UNSET))

        def _parse_memory_wired_bytes(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        memory_wired_bytes = _parse_memory_wired_bytes(d.pop("memory_wired_bytes", UNSET))

        def _parse_pressure(data: object) -> Pressures | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pressure_type_0 = Pressures.from_dict(data)

                return pressure_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Pressures | Unset | None, data)

        pressure = _parse_pressure(d.pop("pressure", UNSET))

        def _parse_process_count(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        process_count = _parse_process_count(d.pop("process_count", UNSET))

        def _parse_swap_total_bytes(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        swap_total_bytes = _parse_swap_total_bytes(d.pop("swap_total_bytes", UNSET))

        def _parse_swap_used_bytes(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        swap_used_bytes = _parse_swap_used_bytes(d.pop("swap_used_bytes", UNSET))

        def _parse_thread_count(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        thread_count = _parse_thread_count(d.pop("thread_count", UNSET))

        system_metrics = cls(
            commit_limit_bytes=commit_limit_bytes,
            commit_total_bytes=commit_total_bytes,
            cpu_busy_percent=cpu_busy_percent,
            cpu_time_seconds=cpu_time_seconds,
            handle_count=handle_count,
            logical_cpu_count=logical_cpu_count,
            memory_available_bytes=memory_available_bytes,
            memory_cache_bytes=memory_cache_bytes,
            memory_compressed_bytes=memory_compressed_bytes,
            memory_total_bytes=memory_total_bytes,
            memory_wired_bytes=memory_wired_bytes,
            pressure=pressure,
            process_count=process_count,
            swap_total_bytes=swap_total_bytes,
            swap_used_bytes=swap_used_bytes,
            thread_count=thread_count,
        )

        return system_metrics
