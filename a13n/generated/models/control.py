from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="Control")


@_attrs_define(repr=False)
class Control:
    """
    Attributes:
        epoch (int):
        session_id (str):
    """

    epoch: int
    session_id: str

    def to_dict(self) -> dict[str, Any]:
        epoch = self.epoch

        session_id = self.session_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "epoch": epoch,
                "session_id": session_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        epoch = d.pop("epoch")

        session_id = d.pop("session_id")

        control = cls(
            epoch=epoch,
            session_id=session_id,
        )

        return control
