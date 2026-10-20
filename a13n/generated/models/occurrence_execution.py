from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.entry_status import EntryStatus

if TYPE_CHECKING:
    from ..models.initial_run import InitialRun


T = TypeVar("T", bound="OccurrenceExecution")


@_attrs_define(repr=False)
class OccurrenceExecution:
    """Current execution observations alongside the durable occurrence completion facts.

    Attributes:
        has_unfinished_work (bool):
        initial_entry_status (EntryStatus | None):
        initial_run (InitialRun | None):
        observed_at (datetime.datetime):
    """

    has_unfinished_work: bool
    initial_entry_status: EntryStatus | None
    initial_run: InitialRun | None
    observed_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        from ..models.initial_run import InitialRun

        has_unfinished_work = self.has_unfinished_work

        initial_entry_status: str | None
        if isinstance(self.initial_entry_status, EntryStatus):
            initial_entry_status = self.initial_entry_status.value
        else:
            initial_entry_status = self.initial_entry_status

        initial_run: dict[str, Any] | None
        if isinstance(self.initial_run, InitialRun):
            initial_run = self.initial_run.to_dict()
        else:
            initial_run = self.initial_run

        observed_at = self.observed_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "has_unfinished_work": has_unfinished_work,
                "initial_entry_status": initial_entry_status,
                "initial_run": initial_run,
                "observed_at": observed_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.initial_run import InitialRun

        d = dict(src_dict)
        has_unfinished_work = d.pop("has_unfinished_work")

        def _parse_initial_entry_status(data: object) -> EntryStatus | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                initial_entry_status_type_0 = EntryStatus(data)

                return initial_entry_status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EntryStatus | None, data)

        initial_entry_status = _parse_initial_entry_status(d.pop("initial_entry_status"))

        def _parse_initial_run(data: object) -> InitialRun | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                initial_run_type_0 = InitialRun.from_dict(data)

                return initial_run_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InitialRun | None, data)

        initial_run = _parse_initial_run(d.pop("initial_run"))

        observed_at = datetime.datetime.fromisoformat(d.pop("observed_at"))

        occurrence_execution = cls(
            has_unfinished_work=has_unfinished_work,
            initial_entry_status=initial_entry_status,
            initial_run=initial_run,
            observed_at=observed_at,
        )

        return occurrence_execution
