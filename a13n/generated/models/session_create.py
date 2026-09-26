from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.session_create_labels import SessionCreateLabels


T = TypeVar("T", bound="SessionCreate")


@_attrs_define(repr=False)
class SessionCreate:
    """
    Attributes:
        labels (SessionCreateLabels | Unset):
    """

    labels: SessionCreateLabels | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_create_labels import SessionCreateLabels

        d = dict(src_dict)
        _labels = d.pop("labels", UNSET)
        labels: SessionCreateLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = SessionCreateLabels.from_dict(_labels)

        session_create = cls(
            labels=labels,
        )

        return session_create
