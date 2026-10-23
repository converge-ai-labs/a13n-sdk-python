from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pressure import Pressure


T = TypeVar("T", bound="Pressures")


@_attrs_define(repr=False)
class Pressures:
    """
    Attributes:
        cpu (None | Pressure | Unset):
        io (None | Pressure | Unset):
        memory (None | Pressure | Unset):
    """

    cpu: Pressure | Unset | None = UNSET
    io: Pressure | Unset | None = UNSET
    memory: Pressure | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.pressure import Pressure

        cpu: dict[str, Any] | Unset | None
        if isinstance(self.cpu, Unset):
            cpu = UNSET
        elif isinstance(self.cpu, Pressure):
            cpu = self.cpu.to_dict()
        else:
            cpu = self.cpu

        io: dict[str, Any] | Unset | None
        if isinstance(self.io, Unset):
            io = UNSET
        elif isinstance(self.io, Pressure):
            io = self.io.to_dict()
        else:
            io = self.io

        memory: dict[str, Any] | Unset | None
        if isinstance(self.memory, Unset):
            memory = UNSET
        elif isinstance(self.memory, Pressure):
            memory = self.memory.to_dict()
        else:
            memory = self.memory

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if cpu is not UNSET:
            field_dict["cpu"] = cpu
        if io is not UNSET:
            field_dict["io"] = io
        if memory is not UNSET:
            field_dict["memory"] = memory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pressure import Pressure

        d = dict(src_dict)

        def _parse_cpu(data: object) -> Pressure | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cpu_type_0 = Pressure.from_dict(data)

                return cpu_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Pressure | Unset | None, data)

        cpu = _parse_cpu(d.pop("cpu", UNSET))

        def _parse_io(data: object) -> Pressure | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                io_type_0 = Pressure.from_dict(data)

                return io_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Pressure | Unset | None, data)

        io = _parse_io(d.pop("io", UNSET))

        def _parse_memory(data: object) -> Pressure | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                memory_type_0 = Pressure.from_dict(data)

                return memory_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Pressure | Unset | None, data)

        memory = _parse_memory(d.pop("memory", UNSET))

        pressures = cls(
            cpu=cpu,
            io=io,
            memory=memory,
        )

        return pressures
