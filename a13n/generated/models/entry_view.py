from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.delivery import Delivery
from ..models.entry_status import EntryStatus
from ..models.entry_view_kind import EntryViewKind

if TYPE_CHECKING:
    from ..models.entry_view_payload import EntryViewPayload
    from ..models.failure import Failure
    from ..models.run_options_output import RunOptionsOutput


T = TypeVar("T", bound="EntryView")


@_attrs_define(repr=False)
class EntryView:
    """
    Attributes:
        agent_id (None | str):
        agent_revision_id (None | str):
        assigned_run_id (None | str):
        child_run_id (None | str):
        created_at (datetime.datetime):
        delivery (Delivery):
        failure (Failure | None):
        finished_at (datetime.datetime | None):
        id (str):
        incorporated_checkpoint_seq (int | None):
        kind (EntryViewKind):
        options (RunOptionsOutput): What a message may choose for the run it starts. A steer joins a run with the
            defaults or equal options.
        origin_run_id (None | str):
        payload (EntryViewPayload):
        position (int):
        principal_id (str):
        status (EntryStatus):
        thread_id (str):
    """

    agent_id: str | None
    agent_revision_id: str | None
    assigned_run_id: str | None
    child_run_id: str | None
    created_at: datetime.datetime
    delivery: Delivery
    failure: Failure | None
    finished_at: datetime.datetime | None
    id: str
    incorporated_checkpoint_seq: int | None
    kind: EntryViewKind
    options: RunOptionsOutput
    origin_run_id: str | None
    payload: EntryViewPayload
    position: int
    principal_id: str
    status: EntryStatus
    thread_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.failure import Failure

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
        if isinstance(self.failure, Failure):
            failure = self.failure.to_dict()
        else:
            failure = self.failure

        finished_at: str | None
        if isinstance(self.finished_at, datetime.datetime):
            finished_at = self.finished_at.isoformat()
        else:
            finished_at = self.finished_at

        id = self.id

        incorporated_checkpoint_seq: int | None
        incorporated_checkpoint_seq = self.incorporated_checkpoint_seq

        kind = self.kind.value

        options = self.options.to_dict()

        origin_run_id: str | None
        origin_run_id = self.origin_run_id

        payload = self.payload.to_dict()

        position = self.position

        principal_id = self.principal_id

        status = self.status.value

        thread_id = self.thread_id

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
                "incorporated_checkpoint_seq": incorporated_checkpoint_seq,
                "kind": kind,
                "options": options,
                "origin_run_id": origin_run_id,
                "payload": payload,
                "position": position,
                "principal_id": principal_id,
                "status": status,
                "thread_id": thread_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entry_view_payload import EntryViewPayload
        from ..models.failure import Failure
        from ..models.run_options_output import RunOptionsOutput

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

        delivery = Delivery(d.pop("delivery"))

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

        id = d.pop("id")

        def _parse_incorporated_checkpoint_seq(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        incorporated_checkpoint_seq = _parse_incorporated_checkpoint_seq(d.pop("incorporated_checkpoint_seq"))

        kind = EntryViewKind(d.pop("kind"))

        options = RunOptionsOutput.from_dict(d.pop("options"))

        def _parse_origin_run_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        origin_run_id = _parse_origin_run_id(d.pop("origin_run_id"))

        payload = EntryViewPayload.from_dict(d.pop("payload"))

        position = d.pop("position")

        principal_id = d.pop("principal_id")

        status = EntryStatus(d.pop("status"))

        thread_id = d.pop("thread_id")

        entry_view = cls(
            agent_id=agent_id,
            agent_revision_id=agent_revision_id,
            assigned_run_id=assigned_run_id,
            child_run_id=child_run_id,
            created_at=created_at,
            delivery=delivery,
            failure=failure,
            finished_at=finished_at,
            id=id,
            incorporated_checkpoint_seq=incorporated_checkpoint_seq,
            kind=kind,
            options=options,
            origin_run_id=origin_run_id,
            payload=payload,
            position=position,
            principal_id=principal_id,
            status=status,
            thread_id=thread_id,
        )

        entry_view.additional_properties = d
        return entry_view

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
