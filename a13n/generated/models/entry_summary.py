from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.entry_status import EntryStatus
from ..models.entry_summary_delivery import EntrySummaryDelivery
from ..models.entry_summary_kind import EntrySummaryKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.failure_summary import FailureSummary
    from ..models.preview import Preview


T = TypeVar("T", bound="EntrySummary")


@_attrs_define(repr=False)
class EntrySummary:
    """
    Attributes:
        agent_id (None | str):
        agent_revision_id (None | str):
        assigned_run_id (None | str):
        child_run_id (None | str):
        created_at (datetime.datetime):
        delivery (EntrySummaryDelivery):
        failure (FailureSummary | None):
        finished_at (datetime.datetime | None):
        id (str):
        kind (EntrySummaryKind):
        origin_run_id (None | str):
        payload (Preview):
        position (int):
        principal_id (str):
        status (EntryStatus):
        thread_id (str):
        omitted_sections (list[str] | Unset):
        view (Literal['compact'] | Unset):
    """

    agent_id: str | None
    agent_revision_id: str | None
    assigned_run_id: str | None
    child_run_id: str | None
    created_at: datetime.datetime
    delivery: EntrySummaryDelivery
    failure: FailureSummary | None
    finished_at: datetime.datetime | None
    id: str
    kind: EntrySummaryKind
    origin_run_id: str | None
    payload: Preview
    position: int
    principal_id: str
    status: EntryStatus
    thread_id: str
    omitted_sections: list[str] | Unset = UNSET
    view: Literal["compact"] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.failure_summary import FailureSummary

        agent_id: str | None
        agent_id = self.agent_id

        agent_revision_id: str | None
        agent_revision_id = self.agent_revision_id

        assigned_run_id: str | None
        assigned_run_id = self.assigned_run_id

        child_run_id: str | None
        child_run_id = self.child_run_id

        created_at = self.created_at.isoformat()

        delivery = self.delivery.value

        failure: dict[str, Any] | None
        if isinstance(self.failure, FailureSummary):
            failure = self.failure.to_dict()
        else:
            failure = self.failure

        finished_at: str | None
        if isinstance(self.finished_at, datetime.datetime):
            finished_at = self.finished_at.isoformat()
        else:
            finished_at = self.finished_at

        id = self.id

        kind = self.kind.value

        origin_run_id: str | None
        origin_run_id = self.origin_run_id

        payload = self.payload.to_dict()

        position = self.position

        principal_id = self.principal_id

        status = self.status.value

        thread_id = self.thread_id

        omitted_sections: list[str] | Unset = UNSET
        if not isinstance(self.omitted_sections, Unset):
            omitted_sections = self.omitted_sections

        view = self.view

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_id": agent_id,
                "agent_revision_id": agent_revision_id,
                "assigned_run_id": assigned_run_id,
                "child_run_id": child_run_id,
                "created_at": created_at,
                "delivery": delivery,
                "failure": failure,
                "finished_at": finished_at,
                "id": id,
                "kind": kind,
                "origin_run_id": origin_run_id,
                "payload": payload,
                "position": position,
                "principal_id": principal_id,
                "status": status,
                "thread_id": thread_id,
            }
        )
        if omitted_sections is not UNSET:
            field_dict["omitted_sections"] = omitted_sections
        if view is not UNSET:
            field_dict["view"] = view

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.failure_summary import FailureSummary
        from ..models.preview import Preview

        d = dict(src_dict)

        def _parse_agent_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        agent_id = _parse_agent_id(d.pop("agent_id"))

        def _parse_agent_revision_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        agent_revision_id = _parse_agent_revision_id(d.pop("agent_revision_id"))

        def _parse_assigned_run_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        assigned_run_id = _parse_assigned_run_id(d.pop("assigned_run_id"))

        def _parse_child_run_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        child_run_id = _parse_child_run_id(d.pop("child_run_id"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        delivery = EntrySummaryDelivery(d.pop("delivery"))

        def _parse_failure(data: object) -> FailureSummary | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                failure_type_0 = FailureSummary.from_dict(data)

                return failure_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FailureSummary | None, data)

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

        id = d.pop("id")

        kind = EntrySummaryKind(d.pop("kind"))

        def _parse_origin_run_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        origin_run_id = _parse_origin_run_id(d.pop("origin_run_id"))

        payload = Preview.from_dict(d.pop("payload"))

        position = d.pop("position")

        principal_id = d.pop("principal_id")

        status = EntryStatus(d.pop("status"))

        thread_id = d.pop("thread_id")

        omitted_sections = cast(list[str], d.pop("omitted_sections", UNSET))

        view = cast(Literal["compact"] | Unset, d.pop("view", UNSET))
        if view != "compact" and not isinstance(view, Unset):
            raise ValueError(f"view must match const 'compact', got '{view}'")

        entry_summary = cls(
            agent_id=agent_id,
            agent_revision_id=agent_revision_id,
            assigned_run_id=assigned_run_id,
            child_run_id=child_run_id,
            created_at=created_at,
            delivery=delivery,
            failure=failure,
            finished_at=finished_at,
            id=id,
            kind=kind,
            origin_run_id=origin_run_id,
            payload=payload,
            position=position,
            principal_id=principal_id,
            status=status,
            thread_id=thread_id,
            omitted_sections=omitted_sections,
            view=view,
        )

        entry_summary.additional_properties = d
        return entry_summary

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
