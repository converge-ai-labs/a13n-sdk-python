from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.template_duplicate_labels_type_0 import TemplateDuplicateLabelsType0


T = TypeVar("T", bound="TemplateDuplicate")


@_attrs_define(repr=False)
class TemplateDuplicate:
    """
    Attributes:
        description (None | str | Unset):
        labels (None | TemplateDuplicateLabelsType0 | Unset):
        name (None | str | Unset):
    """

    description: str | Unset | None = UNSET
    labels: TemplateDuplicateLabelsType0 | Unset | None = UNSET
    name: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.template_duplicate_labels_type_0 import TemplateDuplicateLabelsType0

        description: str | Unset | None
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        labels: dict[str, Any] | Unset | None
        if isinstance(self.labels, Unset):
            labels = UNSET
        elif isinstance(self.labels, TemplateDuplicateLabelsType0):
            labels = self.labels.to_dict()
        else:
            labels = self.labels

        name: str | Unset | None
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if labels is not UNSET:
            field_dict["labels"] = labels
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template_duplicate_labels_type_0 import TemplateDuplicateLabelsType0

        d = dict(src_dict)

        def _parse_description(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_labels(data: object) -> TemplateDuplicateLabelsType0 | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                labels_type_0 = TemplateDuplicateLabelsType0.from_dict(data)

                return labels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(TemplateDuplicateLabelsType0 | Unset | None, data)

        labels = _parse_labels(d.pop("labels", UNSET))

        def _parse_name(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        name = _parse_name(d.pop("name", UNSET))

        template_duplicate = cls(
            description=description,
            labels=labels,
            name=name,
        )

        return template_duplicate
