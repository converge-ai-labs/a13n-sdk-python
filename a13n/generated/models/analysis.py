from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.analysis_create import AnalysisCreate
    from ..models.selected_trace import SelectedTrace


T = TypeVar("T", bound="Analysis")


@_attrs_define(repr=False)
class Analysis:
    """
    Attributes:
        agent_id (None | str):
        cited_trace_count (int):
        created_at (datetime.datetime):
        finding_count (int):
        id (str):
        read_trace_ids (list[str]):
        run_id (str):
        run_status (str):
        selected_traces (list[SelectedTrace]):
        selection (AnalysisCreate):
        selection_truncated (bool):
        session_id (str):
        thread_id (str):
    """

    agent_id: str | None
    cited_trace_count: int
    created_at: datetime.datetime
    finding_count: int
    id: str
    read_trace_ids: list[str]
    run_id: str
    run_status: str
    selected_traces: list[SelectedTrace]
    selection: AnalysisCreate
    selection_truncated: bool
    session_id: str
    thread_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_id: str | None
        agent_id = self.agent_id

        cited_trace_count = self.cited_trace_count

        created_at = self.created_at.isoformat()

        finding_count = self.finding_count

        id = self.id

        read_trace_ids = self.read_trace_ids

        run_id = self.run_id

        run_status = self.run_status

        selected_traces = []
        for selected_traces_item_data in self.selected_traces:
            selected_traces_item = selected_traces_item_data.to_dict()
            selected_traces.append(selected_traces_item)

        selection = self.selection.to_dict()

        selection_truncated = self.selection_truncated

        session_id = self.session_id

        thread_id = self.thread_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_id": agent_id,
                "cited_trace_count": cited_trace_count,
                "created_at": created_at,
                "finding_count": finding_count,
                "id": id,
                "read_trace_ids": read_trace_ids,
                "run_id": run_id,
                "run_status": run_status,
                "selected_traces": selected_traces,
                "selection": selection,
                "selection_truncated": selection_truncated,
                "session_id": session_id,
                "thread_id": thread_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.analysis_create import AnalysisCreate
        from ..models.selected_trace import SelectedTrace

        d = dict(src_dict)

        def _parse_agent_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        agent_id = _parse_agent_id(d.pop("agent_id"))

        cited_trace_count = d.pop("cited_trace_count")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        finding_count = d.pop("finding_count")

        id = d.pop("id")

        read_trace_ids = cast(list[str], d.pop("read_trace_ids"))

        run_id = d.pop("run_id")

        run_status = d.pop("run_status")

        selected_traces = []
        _selected_traces = d.pop("selected_traces")
        for selected_traces_item_data in _selected_traces:
            selected_traces_item = SelectedTrace.from_dict(selected_traces_item_data)

            selected_traces.append(selected_traces_item)

        selection = AnalysisCreate.from_dict(d.pop("selection"))

        selection_truncated = d.pop("selection_truncated")

        session_id = d.pop("session_id")

        thread_id = d.pop("thread_id")

        analysis = cls(
            agent_id=agent_id,
            cited_trace_count=cited_trace_count,
            created_at=created_at,
            finding_count=finding_count,
            id=id,
            read_trace_ids=read_trace_ids,
            run_id=run_id,
            run_status=run_status,
            selected_traces=selected_traces,
            selection=selection,
            selection_truncated=selection_truncated,
            session_id=session_id,
            thread_id=thread_id,
        )

        analysis.additional_properties = d
        return analysis

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
