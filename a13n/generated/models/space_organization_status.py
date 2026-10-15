from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.failure import Failure


T = TypeVar("T", bound="SpaceOrganizationStatus")


@_attrs_define(repr=False)
class SpaceOrganizationStatus:
    """
    Attributes:
        active_run_id (None | str | Unset):
        due_at (datetime.datetime | None | Unset):
        failure (Failure | None | Unset):
        history_gap (bool | Unset):
        last_run_id (None | str | Unset):
        pending (bool | Unset):
        processed_seq (int | Unset):
        session_id (None | str | Unset):
    """

    active_run_id: str | Unset | None = UNSET
    due_at: datetime.datetime | Unset | None = UNSET
    failure: Failure | Unset | None = UNSET
    history_gap: bool | Unset = UNSET
    last_run_id: str | Unset | None = UNSET
    pending: bool | Unset = UNSET
    processed_seq: int | Unset = UNSET
    session_id: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.failure import Failure

        active_run_id: str | Unset | None
        if isinstance(self.active_run_id, Unset):
            active_run_id = UNSET
        else:
            active_run_id = self.active_run_id

        due_at: str | Unset | None
        if isinstance(self.due_at, Unset):
            due_at = UNSET
        elif isinstance(self.due_at, datetime.datetime):
            due_at = self.due_at.isoformat()
        else:
            due_at = self.due_at

        failure: dict[str, Any] | Unset | None
        if isinstance(self.failure, Unset):
            failure = UNSET
        elif isinstance(self.failure, Failure):
            failure = self.failure.to_dict()
        else:
            failure = self.failure

        history_gap = self.history_gap

        last_run_id: str | Unset | None
        if isinstance(self.last_run_id, Unset):
            last_run_id = UNSET
        else:
            last_run_id = self.last_run_id

        pending = self.pending

        processed_seq = self.processed_seq

        session_id: str | Unset | None
        if isinstance(self.session_id, Unset):
            session_id = UNSET
        else:
            session_id = self.session_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if active_run_id is not UNSET:
            field_dict["active_run_id"] = active_run_id
        if due_at is not UNSET:
            field_dict["due_at"] = due_at
        if failure is not UNSET:
            field_dict["failure"] = failure
        if history_gap is not UNSET:
            field_dict["history_gap"] = history_gap
        if last_run_id is not UNSET:
            field_dict["last_run_id"] = last_run_id
        if pending is not UNSET:
            field_dict["pending"] = pending
        if processed_seq is not UNSET:
            field_dict["processed_seq"] = processed_seq
        if session_id is not UNSET:
            field_dict["session_id"] = session_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.failure import Failure

        d = dict(src_dict)

        def _parse_active_run_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        active_run_id = _parse_active_run_id(d.pop("active_run_id", UNSET))

        def _parse_due_at(data: object) -> datetime.datetime | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                due_at_type_0 = datetime.datetime.fromisoformat(data)

                return due_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | Unset | None, data)

        due_at = _parse_due_at(d.pop("due_at", UNSET))

        def _parse_failure(data: object) -> Failure | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                failure_type_0 = Failure.from_dict(data)

                return failure_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Failure | Unset | None, data)

        failure = _parse_failure(d.pop("failure", UNSET))

        history_gap = d.pop("history_gap", UNSET)

        def _parse_last_run_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        last_run_id = _parse_last_run_id(d.pop("last_run_id", UNSET))

        pending = d.pop("pending", UNSET)

        processed_seq = d.pop("processed_seq", UNSET)

        def _parse_session_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        session_id = _parse_session_id(d.pop("session_id", UNSET))

        space_organization_status = cls(
            active_run_id=active_run_id,
            due_at=due_at,
            failure=failure,
            history_gap=history_gap,
            last_run_id=last_run_id,
            pending=pending,
            processed_seq=processed_seq,
            session_id=session_id,
        )

        return space_organization_status
