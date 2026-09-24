from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attempt_view_start_reason import AttemptViewStartReason
from ..models.attempt_view_status import AttemptViewStatus

if TYPE_CHECKING:
    from ..models.failure import Failure


T = TypeVar("T", bound="AttemptView")


@_attrs_define(repr=False)
class AttemptView:
    """
    Attributes:
        created_at (datetime.datetime):
        failure (Failure | None):
        finished_at (datetime.datetime | None):
        harness_run_id (None | str):
        id (str):
        number (int):
        replaces_attempt_id (None | str):
        run_id (str):
        start_reason (AttemptViewStartReason):
        started_at (datetime.datetime | None):
        status (AttemptViewStatus):
        worker_build (str):
        yield_reason (None | str):
    """

    created_at: datetime.datetime
    failure: Failure | None
    finished_at: datetime.datetime | None
    harness_run_id: str | None
    id: str
    number: int
    replaces_attempt_id: str | None
    run_id: str
    start_reason: AttemptViewStartReason
    started_at: datetime.datetime | None
    status: AttemptViewStatus
    worker_build: str
    yield_reason: str | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.failure import Failure

        created_at = self.created_at.isoformat()

        failure: dict[str, Any] | None
        if isinstance(self.failure, Failure):
            failure = self.failure.to_dict()
        else:
            failure = self.failure

        finished_at: str | None
        if isinstance(self.finished_at, datetime.datetime):
            finished_at = self.finished_at.isoformat()
        else:
            finished_at = self.finished_at

        harness_run_id: str | None
        harness_run_id = self.harness_run_id

        id = self.id

        number = self.number

        replaces_attempt_id: str | None
        replaces_attempt_id = self.replaces_attempt_id

        run_id = self.run_id

        start_reason = self.start_reason.value

        started_at: str | None
        if isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        status = self.status.value

        worker_build = self.worker_build

        yield_reason: str | None
        yield_reason = self.yield_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "failure": failure,
                "finished_at": finished_at,
                "harness_run_id": harness_run_id,
                "id": id,
                "number": number,
                "replaces_attempt_id": replaces_attempt_id,
                "run_id": run_id,
                "start_reason": start_reason,
                "started_at": started_at,
                "status": status,
                "worker_build": worker_build,
                "yield_reason": yield_reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.failure import Failure

        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_failure(data: object) -> Failure | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                failure_type_0 = Failure.from_dict(data)

                return failure_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Failure | None, data)

        failure = _parse_failure(d.pop("failure"))

        def _parse_finished_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                finished_at_type_0 = datetime.datetime.fromisoformat(data)

                return finished_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        finished_at = _parse_finished_at(d.pop("finished_at"))

        def _parse_harness_run_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        harness_run_id = _parse_harness_run_id(d.pop("harness_run_id"))

        id = d.pop("id")

        number = d.pop("number")

        def _parse_replaces_attempt_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        replaces_attempt_id = _parse_replaces_attempt_id(d.pop("replaces_attempt_id"))

        run_id = d.pop("run_id")

        start_reason = AttemptViewStartReason(d.pop("start_reason"))

        def _parse_started_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_at_type_0 = datetime.datetime.fromisoformat(data)

                return started_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        started_at = _parse_started_at(d.pop("started_at"))

        status = AttemptViewStatus(d.pop("status"))

        worker_build = d.pop("worker_build")

        def _parse_yield_reason(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        yield_reason = _parse_yield_reason(d.pop("yield_reason"))

        attempt_view = cls(
            created_at=created_at,
            failure=failure,
            finished_at=finished_at,
            harness_run_id=harness_run_id,
            id=id,
            number=number,
            replaces_attempt_id=replaces_attempt_id,
            run_id=run_id,
            start_reason=start_reason,
            started_at=started_at,
            status=status,
            worker_build=worker_build,
            yield_reason=yield_reason,
        )

        attempt_view.additional_properties = d
        return attempt_view

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
