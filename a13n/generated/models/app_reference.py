from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppReference")


@_attrs_define(repr=False)
class AppReference:
    """
    Attributes:
        agent_revision_id (str):
        app_id (str):
        connection_id (str):
        resource_uri (str):
        source_run_id (str):
        tool_call_id (str):
        tool_name (str):
        unavailable (bool | Unset):
    """

    agent_revision_id: str
    app_id: str
    connection_id: str
    resource_uri: str
    source_run_id: str
    tool_call_id: str
    tool_name: str
    unavailable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_revision_id = self.agent_revision_id

        app_id = self.app_id

        connection_id = self.connection_id

        resource_uri = self.resource_uri

        source_run_id = self.source_run_id

        tool_call_id = self.tool_call_id

        tool_name = self.tool_name

        unavailable = self.unavailable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_revision_id": agent_revision_id,
                "app_id": app_id,
                "connection_id": connection_id,
                "resource_uri": resource_uri,
                "source_run_id": source_run_id,
                "tool_call_id": tool_call_id,
                "tool_name": tool_name,
            }
        )
        if unavailable is not UNSET:
            field_dict["unavailable"] = unavailable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        agent_revision_id = d.pop("agent_revision_id")

        app_id = d.pop("app_id")

        connection_id = d.pop("connection_id")

        resource_uri = d.pop("resource_uri")

        source_run_id = d.pop("source_run_id")

        tool_call_id = d.pop("tool_call_id")

        tool_name = d.pop("tool_name")

        unavailable = d.pop("unavailable", UNSET)

        app_reference = cls(
            agent_revision_id=agent_revision_id,
            app_id=app_id,
            connection_id=connection_id,
            resource_uri=resource_uri,
            source_run_id=source_run_id,
            tool_call_id=tool_call_id,
            tool_name=tool_name,
            unavailable=unavailable,
        )

        app_reference.additional_properties = d
        return app_reference

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
