from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.run_status import RunStatus
from ..models.trigger import Trigger

T = TypeVar("T", bound="SessionPreview")


@_attrs_define(repr=False)
class SessionPreview:
    """The session's latest run, summarized for a list row.

    Attributes:
        agent_id (str):
        agent_name (str):
        input_text (None | str):
        output_text (None | str):
        run_id (str):
        status (RunStatus):
        thread_id (str):
        trigger (Trigger):
    """

    agent_id: str
    agent_name: str
    input_text: str | None
    output_text: str | None
    run_id: str
    status: RunStatus
    thread_id: str
    trigger: Trigger
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_id = self.agent_id

        agent_name = self.agent_name

        input_text: str | None
        input_text = self.input_text

        output_text: str | None
        output_text = self.output_text

        run_id = self.run_id

        status = self.status.value

        thread_id = self.thread_id

        trigger = self.trigger.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_id": agent_id,
                "agent_name": agent_name,
                "input_text": input_text,
                "output_text": output_text,
                "run_id": run_id,
                "status": status,
                "thread_id": thread_id,
                "trigger": trigger,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        agent_id = d.pop("agent_id")

        agent_name = d.pop("agent_name")

        def _parse_input_text(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        input_text = _parse_input_text(d.pop("input_text"))

        def _parse_output_text(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        output_text = _parse_output_text(d.pop("output_text"))

        run_id = d.pop("run_id")

        status = RunStatus(d.pop("status"))

        thread_id = d.pop("thread_id")

        trigger = Trigger(d.pop("trigger"))

        session_preview = cls(
            agent_id=agent_id,
            agent_name=agent_name,
            input_text=input_text,
            output_text=output_text,
            run_id=run_id,
            status=status,
            thread_id=thread_id,
            trigger=trigger,
        )

        session_preview.additional_properties = d
        return session_preview

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
