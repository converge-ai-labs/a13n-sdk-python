from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.preset import Preset
from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalysisCreate")


@_attrs_define(repr=False)
class AnalysisCreate:
    """
    Attributes:
        agent_id (None | str | Unset):
        max_traces (int | Unset):
        presets (list[Preset] | Unset):
        started_after (datetime.datetime | None | Unset):
        started_before (datetime.datetime | None | Unset):
        trace_id (None | str | Unset):
    """

    agent_id: str | Unset | None = UNSET
    max_traces: int | Unset = UNSET
    presets: list[Preset] | Unset = UNSET
    started_after: datetime.datetime | Unset | None = UNSET
    started_before: datetime.datetime | Unset | None = UNSET
    trace_id: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        agent_id: str | Unset | None
        if isinstance(self.agent_id, Unset):
            agent_id = UNSET
        else:
            agent_id = self.agent_id

        max_traces = self.max_traces

        presets: list[str] | Unset = UNSET
        if not isinstance(self.presets, Unset):
            presets = []
            for presets_item_data in self.presets:
                presets_item = presets_item_data.value
                presets.append(presets_item)

        started_after: str | Unset | None
        if isinstance(self.started_after, Unset):
            started_after = UNSET
        elif isinstance(self.started_after, datetime.datetime):
            started_after = self.started_after.isoformat()
        else:
            started_after = self.started_after

        started_before: str | Unset | None
        if isinstance(self.started_before, Unset):
            started_before = UNSET
        elif isinstance(self.started_before, datetime.datetime):
            started_before = self.started_before.isoformat()
        else:
            started_before = self.started_before

        trace_id: str | Unset | None
        if isinstance(self.trace_id, Unset):
            trace_id = UNSET
        else:
            trace_id = self.trace_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if agent_id is not UNSET:
            field_dict["agent_id"] = agent_id
        if max_traces is not UNSET:
            field_dict["max_traces"] = max_traces
        if presets is not UNSET:
            field_dict["presets"] = presets
        if started_after is not UNSET:
            field_dict["started_after"] = started_after
        if started_before is not UNSET:
            field_dict["started_before"] = started_before
        if trace_id is not UNSET:
            field_dict["trace_id"] = trace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_agent_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        agent_id = _parse_agent_id(d.pop("agent_id", UNSET))

        max_traces = d.pop("max_traces", UNSET)

        _presets = d.pop("presets", UNSET)
        presets: list[Preset] | Unset = UNSET
        if _presets is not UNSET:
            presets = []
            for presets_item_data in _presets:
                presets_item = Preset(presets_item_data)

                presets.append(presets_item)

        def _parse_started_after(data: object) -> datetime.datetime | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_after_type_0 = datetime.datetime.fromisoformat(data)

                return started_after_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | Unset | None, data)

        started_after = _parse_started_after(d.pop("started_after", UNSET))

        def _parse_started_before(data: object) -> datetime.datetime | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_before_type_0 = datetime.datetime.fromisoformat(data)

                return started_before_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | Unset | None, data)

        started_before = _parse_started_before(d.pop("started_before", UNSET))

        def _parse_trace_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        trace_id = _parse_trace_id(d.pop("trace_id", UNSET))

        analysis_create = cls(
            agent_id=agent_id,
            max_traces=max_traces,
            presets=presets,
            started_after=started_after,
            started_before=started_before,
            trace_id=trace_id,
        )

        return analysis_create
