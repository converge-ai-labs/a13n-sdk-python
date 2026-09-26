from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.connection_status import ConnectionStatus

T = TypeVar("T", bound="CallbackOutcome")


@_attrs_define(repr=False)
class CallbackOutcome:
    """
    Attributes:
        connection_id (str):
        error (None | str):
        status (ConnectionStatus):
    """

    connection_id: str
    error: str | None
    status: ConnectionStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connection_id = self.connection_id

        error: str | None
        error = self.error

        status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connection_id": connection_id,
                "error": error,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connection_id = d.pop("connection_id")

        def _parse_error(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        error = _parse_error(d.pop("error"))

        status = ConnectionStatus(d.pop("status"))

        callback_outcome = cls(
            connection_id=connection_id,
            error=error,
            status=status,
        )

        callback_outcome.additional_properties = d
        return callback_outcome

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
