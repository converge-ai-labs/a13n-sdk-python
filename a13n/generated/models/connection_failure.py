from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.connection_failure_reason import ConnectionFailureReason
from ..models.operation_kind import OperationKind

T = TypeVar("T", bound="ConnectionFailure")


@_attrs_define(repr=False)
class ConnectionFailure:
    """Why the last remote operation failed; `outcome_unknown` means it may have taken effect.

    Attributes:
        code (None | str):
        operation_id (str):
        operation_kind (OperationKind):
        reason (ConnectionFailureReason):
    """

    code: str | None
    operation_id: str
    operation_kind: OperationKind
    reason: ConnectionFailureReason
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code: str | None
        code = self.code

        operation_id = self.operation_id

        operation_kind = self.operation_kind.value

        reason = self.reason.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "operation_id": operation_id,
                "operation_kind": operation_kind,
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_code(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        code = _parse_code(d.pop("code"))

        operation_id = d.pop("operation_id")

        operation_kind = OperationKind(d.pop("operation_kind"))

        reason = ConnectionFailureReason(d.pop("reason"))

        connection_failure = cls(
            code=code,
            operation_id=operation_id,
            operation_kind=operation_kind,
            reason=reason,
        )

        connection_failure.additional_properties = d
        return connection_failure

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
