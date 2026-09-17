from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.client_connection_status_error_type_0 import ClientConnectionStatusErrorType0
from ..models.client_connection_status_status import ClientConnectionStatusStatus

T = TypeVar("T", bound="ClientConnectionStatus")


@_attrs_define(repr=False)
class ClientConnectionStatus:
    """
    Attributes:
        connection_id (None | str):
        error (ClientConnectionStatusErrorType0 | None):
        observed_at (datetime.datetime):
        status (ClientConnectionStatusStatus):
    """

    connection_id: str | None
    error: ClientConnectionStatusErrorType0 | None
    observed_at: datetime.datetime
    status: ClientConnectionStatusStatus

    def to_dict(self) -> dict[str, Any]:
        connection_id: str | None
        connection_id = self.connection_id

        error: str | None
        if isinstance(self.error, ClientConnectionStatusErrorType0):
            error = self.error.value
        else:
            error = self.error

        observed_at = self.observed_at.isoformat()

        status = self.status.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "connection_id": connection_id,
                "error": error,
                "observed_at": observed_at,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_connection_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        connection_id = _parse_connection_id(d.pop("connection_id"))

        def _parse_error(data: object) -> ClientConnectionStatusErrorType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                error_type_0 = ClientConnectionStatusErrorType0(data)

                return error_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ClientConnectionStatusErrorType0 | None, data)

        error = _parse_error(d.pop("error"))

        observed_at = datetime.datetime.fromisoformat(d.pop("observed_at"))

        status = ClientConnectionStatusStatus(d.pop("status"))

        client_connection_status = cls(
            connection_id=connection_id,
            error=error,
            observed_at=observed_at,
            status=status,
        )

        return client_connection_status
