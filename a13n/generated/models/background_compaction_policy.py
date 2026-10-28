from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackgroundCompactionPolicy")


@_attrs_define(repr=False)
class BackgroundCompactionPolicy:
    """Host-selected overlap policy, separate from the common compaction trigger.

    Attributes:
        blocking_threshold (float | Unset):
        enabled (bool | Unset):
    """

    blocking_threshold: float | Unset = UNSET
    enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        blocking_threshold = self.blocking_threshold

        enabled = self.enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if blocking_threshold is not UNSET:
            field_dict["blocking_threshold"] = blocking_threshold
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        blocking_threshold = d.pop("blocking_threshold", UNSET)

        enabled = d.pop("enabled", UNSET)

        background_compaction_policy = cls(
            blocking_threshold=blocking_threshold,
            enabled=enabled,
        )

        return background_compaction_policy
