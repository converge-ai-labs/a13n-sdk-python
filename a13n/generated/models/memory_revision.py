from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.memory_revision_op import MemoryRevisionOp

T = TypeVar("T", bound="MemoryRevision")


@_attrs_define(repr=False)
class MemoryRevision:
    """One change to one path. A move is two: `move_out` at the source and `move_in` at the destination.

    Attributes:
        created_at (datetime.datetime):
        moved_path (None | str):
        op (MemoryRevisionOp):
        path (str):
        principal_id (None | str):
        run_id (None | str):
        seq (int):
        tool_call_id (None | str):
    """

    created_at: datetime.datetime
    moved_path: str | None
    op: MemoryRevisionOp
    path: str
    principal_id: str | None
    run_id: str | None
    seq: int
    tool_call_id: str | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        moved_path: str | None
        moved_path = self.moved_path

        op = self.op.value

        path = self.path

        principal_id: str | None
        principal_id = self.principal_id

        run_id: str | None
        run_id = self.run_id

        seq = self.seq

        tool_call_id: str | None
        tool_call_id = self.tool_call_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "moved_path": moved_path,
                "op": op,
                "path": path,
                "principal_id": principal_id,
                "run_id": run_id,
                "seq": seq,
                "tool_call_id": tool_call_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_moved_path(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        moved_path = _parse_moved_path(d.pop("moved_path"))

        op = MemoryRevisionOp(d.pop("op"))

        path = d.pop("path")

        def _parse_principal_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        principal_id = _parse_principal_id(d.pop("principal_id"))

        def _parse_run_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        run_id = _parse_run_id(d.pop("run_id"))

        seq = d.pop("seq")

        def _parse_tool_call_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        tool_call_id = _parse_tool_call_id(d.pop("tool_call_id"))

        memory_revision = cls(
            created_at=created_at,
            moved_path=moved_path,
            op=op,
            path=path,
            principal_id=principal_id,
            run_id=run_id,
            seq=seq,
            tool_call_id=tool_call_id,
        )

        memory_revision.additional_properties = d
        return memory_revision

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
