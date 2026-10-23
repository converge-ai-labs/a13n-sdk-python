from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pressure_level import PressureLevel


T = TypeVar("T", bound="Pressure")


@_attrs_define(repr=False)
class Pressure:
    """
    Attributes:
        full (None | PressureLevel | Unset):
        some (None | PressureLevel | Unset):
    """

    full: PressureLevel | Unset | None = UNSET
    some: PressureLevel | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.pressure_level import PressureLevel

        full: dict[str, Any] | Unset | None
        if isinstance(self.full, Unset):
            full = UNSET
        elif isinstance(self.full, PressureLevel):
            full = self.full.to_dict()
        else:
            full = self.full

        some: dict[str, Any] | Unset | None
        if isinstance(self.some, Unset):
            some = UNSET
        elif isinstance(self.some, PressureLevel):
            some = self.some.to_dict()
        else:
            some = self.some

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if full is not UNSET:
            field_dict["full"] = full
        if some is not UNSET:
            field_dict["some"] = some

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pressure_level import PressureLevel

        d = dict(src_dict)

        def _parse_full(data: object) -> PressureLevel | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                full_type_0 = PressureLevel.from_dict(data)

                return full_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(PressureLevel | Unset | None, data)

        full = _parse_full(d.pop("full", UNSET))

        def _parse_some(data: object) -> PressureLevel | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                some_type_0 = PressureLevel.from_dict(data)

                return some_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(PressureLevel | Unset | None, data)

        some = _parse_some(d.pop("some", UNSET))

        pressure = cls(
            full=full,
            some=some,
        )

        return pressure
