from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.error_code import ErrorCode

if TYPE_CHECKING:
    from ..models.error_body_details import ErrorBodyDetails


T = TypeVar("T", bound="ErrorBody")


@_attrs_define(repr=False)
class ErrorBody:
    """
    Attributes:
        code (ErrorCode):
        details (ErrorBodyDetails):
        message (str):
        request_id (None | str):
    """

    code: ErrorCode
    details: ErrorBodyDetails
    message: str
    request_id: str | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code.value

        details = self.details.to_dict()

        message = self.message

        request_id: str | None
        request_id = self.request_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "details": details,
                "message": message,
                "request_id": request_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_body_details import ErrorBodyDetails

        d = dict(src_dict)
        code = ErrorCode(d.pop("code"))

        details = ErrorBodyDetails.from_dict(d.pop("details"))

        message = d.pop("message")

        def _parse_request_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        request_id = _parse_request_id(d.pop("request_id"))

        error_body = cls(
            code=code,
            details=details,
            message=message,
            request_id=request_id,
        )

        error_body.additional_properties = d
        return error_body

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
