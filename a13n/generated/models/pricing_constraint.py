from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.pricing_constraint_kind import PricingConstraintKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="PricingConstraint")


@_attrs_define(repr=False)
class PricingConstraint:
    """A stable condition selecting one ordered model price rule.

    Attributes:
        end_time (None | str | Unset):
        kind (PricingConstraintKind | Unset):
        start_date (datetime.date | None | Unset):
        start_time (None | str | Unset):
        weekdays (list[int] | Unset):
    """

    end_time: str | Unset | None = UNSET
    kind: PricingConstraintKind | Unset = UNSET
    start_date: datetime.date | Unset | None = UNSET
    start_time: str | Unset | None = UNSET
    weekdays: list[int] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        end_time: str | Unset | None
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        else:
            end_time = self.end_time

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        start_date: str | Unset | None
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        elif isinstance(self.start_date, datetime.date):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        start_time: str | Unset | None
        if isinstance(self.start_time, Unset):
            start_time = UNSET
        else:
            start_time = self.start_time

        weekdays: list[int] | Unset = UNSET
        if not isinstance(self.weekdays, Unset):
            weekdays = self.weekdays

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if kind is not UNSET:
            field_dict["kind"] = kind
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if weekdays is not UNSET:
            field_dict["weekdays"] = weekdays

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_end_time(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        end_time = _parse_end_time(d.pop("end_time", UNSET))

        _kind = d.pop("kind", UNSET)
        kind: PricingConstraintKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = PricingConstraintKind(_kind)

        def _parse_start_date(data: object) -> datetime.date | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_type_0 = datetime.date.fromisoformat(data)

                return start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | Unset | None, data)

        start_date = _parse_start_date(d.pop("start_date", UNSET))

        def _parse_start_time(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        start_time = _parse_start_time(d.pop("start_time", UNSET))

        weekdays = cast(list[int], d.pop("weekdays", UNSET))

        pricing_constraint = cls(
            end_time=end_time,
            kind=kind,
            start_date=start_date,
            start_time=start_time,
            weekdays=weekdays,
        )

        return pricing_constraint
