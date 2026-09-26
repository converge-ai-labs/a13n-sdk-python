from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.connection_test_outcome_status import ConnectionTestOutcomeStatus

T = TypeVar("T", bound="ConnectionTestOutcome")


@_attrs_define(repr=False)
class ConnectionTestOutcome:
    """What a test found for the connection version it tested.

    Attributes:
        connection_version (int):
        message (None | str):
        status (ConnectionTestOutcomeStatus):
        tested_at (datetime.datetime):
    """

    connection_version: int
    message: str | None
    status: ConnectionTestOutcomeStatus
    tested_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connection_version = self.connection_version

        message: str | None
        message = self.message

        status = self.status.value

        tested_at = self.tested_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connection_version": connection_version,
                "message": message,
                "status": status,
                "tested_at": tested_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connection_version = d.pop("connection_version")

        def _parse_message(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        message = _parse_message(d.pop("message"))

        status = ConnectionTestOutcomeStatus(d.pop("status"))

        tested_at = datetime.datetime.fromisoformat(d.pop("tested_at"))

        connection_test_outcome = cls(
            connection_version=connection_version,
            message=message,
            status=status,
            tested_at=tested_at,
        )

        connection_test_outcome.additional_properties = d
        return connection_test_outcome

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
