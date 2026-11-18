from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="OrganizationSource")


@_attrs_define(repr=False)
class OrganizationSource:
    """
    Attributes:
        run_id (str):
        sealed_at (datetime.datetime):
        session_id (str):
        thread_id (str):
    """

    run_id: str
    sealed_at: datetime.datetime
    session_id: str
    thread_id: str

    def to_dict(self) -> dict[str, Any]:
        run_id = self.run_id

        sealed_at = self.sealed_at.isoformat()

        session_id = self.session_id

        thread_id = self.thread_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "run_id": run_id,
                "sealed_at": sealed_at,
                "session_id": session_id,
                "thread_id": thread_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        run_id = d.pop("run_id")

        sealed_at = datetime.datetime.fromisoformat(d.pop("sealed_at"))

        session_id = d.pop("session_id")

        thread_id = d.pop("thread_id")

        organization_source = cls(
            run_id=run_id,
            sealed_at=sealed_at,
            session_id=session_id,
            thread_id=thread_id,
        )

        return organization_source
