from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.run_labels_labels import RunLabelsLabels


T = TypeVar("T", bound="RunLabels")


@_attrs_define(repr=False)
class RunLabels:
    """
    Attributes:
        labels (RunLabelsLabels):
    """

    labels: RunLabelsLabels

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
        from ..models.run_labels_labels import RunLabelsLabels

        d = dict(src_dict)
        labels = RunLabelsLabels.from_dict(d.pop("labels"))

        run_labels = cls(
            labels=labels,
        )

        return run_labels
