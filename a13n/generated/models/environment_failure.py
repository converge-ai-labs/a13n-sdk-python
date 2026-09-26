from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.certainty import Certainty

T = TypeVar("T", bound="EnvironmentFailure")


@_attrs_define(repr=False)
class EnvironmentFailure:
    """The last error of the outstanding operation or, on a ready instance, of its last renewal.

    `unknown` means the call may have taken effect: only the same operation may continue. `permanent` failures
    refuse new mounts and acceptance until the cause is fixed or the instance is deleted; `environment_lost` means
    the provider no longer has the sandbox.

        Attributes:
            at (datetime.datetime):
            certainty (Certainty):
            code (str):
            message (str):
            operation_id (None | str):
            permanent (bool):
    """

    at: datetime.datetime
    certainty: Certainty
    code: str
    message: str
    operation_id: str | None
    permanent: bool

    def to_dict(self) -> dict[str, Any]:
        at = self.at.isoformat()

        certainty = self.certainty.value

        code = self.code

        message = self.message

        operation_id: str | None
        operation_id = self.operation_id

        permanent = self.permanent

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "at": at,
                "certainty": certainty,
                "code": code,
                "message": message,
                "operation_id": operation_id,
                "permanent": permanent,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        at = datetime.datetime.fromisoformat(d.pop("at"))

        certainty = Certainty(d.pop("certainty"))

        code = d.pop("code")

        message = d.pop("message")

        def _parse_operation_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        operation_id = _parse_operation_id(d.pop("operation_id"))

        permanent = d.pop("permanent")

        environment_failure = cls(
            at=at,
            certainty=certainty,
            code=code,
            message=message,
            operation_id=operation_id,
            permanent=permanent,
        )

        return environment_failure
