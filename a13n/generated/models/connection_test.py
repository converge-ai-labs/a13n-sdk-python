from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.connection_test_status import ConnectionTestStatus

if TYPE_CHECKING:
    from ..models.tool_info import ToolInfo


T = TypeVar("T", bound="ConnectionTest")


@_attrs_define(repr=False)
class ConnectionTest:
    """
    Attributes:
        connection_id (str):
        connection_version (int):
        message (None | str):
        status (ConnectionTestStatus):
        tested_at (datetime.datetime):
        tools (list[ToolInfo]):
    """

    connection_id: str
    connection_version: int
    message: str | None
    status: ConnectionTestStatus
    tested_at: datetime.datetime
    tools: list[ToolInfo]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connection_id = self.connection_id

        connection_version = self.connection_version

        message: str | None
        message = self.message

        status = self.status.value

        tested_at = self.tested_at.isoformat()

        tools = []
        for tools_item_data in self.tools:
            tools_item = tools_item_data.to_dict()
            tools.append(tools_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connection_id": connection_id,
                "connection_version": connection_version,
                "message": message,
                "status": status,
                "tested_at": tested_at,
                "tools": tools,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tool_info import ToolInfo

        d = dict(src_dict)
        connection_id = d.pop("connection_id")

        connection_version = d.pop("connection_version")

        def _parse_message(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        message = _parse_message(d.pop("message"))

        status = ConnectionTestStatus(d.pop("status"))

        tested_at = datetime.datetime.fromisoformat(d.pop("tested_at"))

        tools = []
        _tools = d.pop("tools")
        for tools_item_data in _tools:
            tools_item = ToolInfo.from_dict(tools_item_data)

            tools.append(tools_item)

        connection_test = cls(
            connection_id=connection_id,
            connection_version=connection_version,
            message=message,
            status=status,
            tested_at=tested_at,
            tools=tools,
        )

        connection_test.additional_properties = d
        return connection_test

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
