from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="OpenView")


@_attrs_define(repr=False)
class OpenView:
    """
    Attributes:
        mount (str):
        reason (str):
        session_id (str):
    """

    mount: str
    reason: str
    session_id: str

    def to_dict(self) -> dict[str, Any]:
        mount = self.mount

        reason = self.reason

        session_id = self.session_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "mount": mount,
                "reason": reason,
                "session_id": session_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mount = d.pop("mount")

        reason = d.pop("reason")

        session_id = d.pop("session_id")

        open_view = cls(
            mount=mount,
            reason=reason,
            session_id=session_id,
        )

        return open_view
