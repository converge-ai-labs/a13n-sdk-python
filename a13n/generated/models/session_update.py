from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.session_update_labels import SessionUpdateLabels


T = TypeVar("T", bound="SessionUpdate")


@_attrs_define(repr=False)
class SessionUpdate:
    """
    Attributes:
        labels (SessionUpdateLabels):
    """

    labels: SessionUpdateLabels

    def to_dict(self) -> dict[str, Any]:
        labels = self.labels.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "labels": labels,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_update_labels import SessionUpdateLabels

        d = dict(src_dict)
        labels = SessionUpdateLabels.from_dict(d.pop("labels"))

        session_update = cls(
            labels=labels,
        )

        return session_update
