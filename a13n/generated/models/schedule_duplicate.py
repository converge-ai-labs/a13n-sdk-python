from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schedule_duplicate_labels_type_0 import ScheduleDuplicateLabelsType0
    from ..models.schedule_target import ScheduleTarget


T = TypeVar("T", bound="ScheduleDuplicate")


@_attrs_define(repr=False)
class ScheduleDuplicate:
    """
    Attributes:
        description (None | str | Unset):
        labels (None | ScheduleDuplicateLabelsType0 | Unset):
        name (None | str | Unset):
        target (None | ScheduleTarget | Unset):
    """

    description: str | Unset | None = UNSET
    labels: ScheduleDuplicateLabelsType0 | Unset | None = UNSET
    name: str | Unset | None = UNSET
    target: ScheduleTarget | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.schedule_duplicate_labels_type_0 import ScheduleDuplicateLabelsType0
        from ..models.schedule_target import ScheduleTarget

        description: str | Unset | None
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        labels: dict[str, Any] | Unset | None
        if isinstance(self.labels, Unset):
            labels = UNSET
        elif isinstance(self.labels, ScheduleDuplicateLabelsType0):
            labels = self.labels.to_dict()
        else:
            labels = self.labels

        name: str | Unset | None
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        target: dict[str, Any] | Unset | None
        if isinstance(self.target, Unset):
            target = UNSET
        elif isinstance(self.target, ScheduleTarget):
            target = self.target.to_dict()
        else:
            target = self.target

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if labels is not UNSET:
            field_dict["labels"] = labels
        if name is not UNSET:
            field_dict["name"] = name
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schedule_duplicate_labels_type_0 import ScheduleDuplicateLabelsType0
        from ..models.schedule_target import ScheduleTarget

        d = dict(src_dict)

        def _parse_description(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_labels(data: object) -> ScheduleDuplicateLabelsType0 | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                labels_type_0 = ScheduleDuplicateLabelsType0.from_dict(data)

                return labels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ScheduleDuplicateLabelsType0 | Unset | None, data)

        labels = _parse_labels(d.pop("labels", UNSET))

        def _parse_name(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_target(data: object) -> ScheduleTarget | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                target_type_0 = ScheduleTarget.from_dict(data)

                return target_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ScheduleTarget | Unset | None, data)

        target = _parse_target(d.pop("target", UNSET))

        schedule_duplicate = cls(
            description=description,
            labels=labels,
            name=name,
            target=target,
        )

        return schedule_duplicate
