from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.memory_update_labels_type_0 import MemoryUpdateLabelsType0


T = TypeVar("T", bound="MemoryUpdate")


@_attrs_define(repr=False)
class MemoryUpdate:
    """Fields left out stay unchanged; `description: null` clears it and `guide: null` inherits the default.

    Attributes:
        always_load (list[str] | None | Unset):
        description (None | str | Unset):
        guide (None | str | Unset):
        labels (MemoryUpdateLabelsType0 | None | Unset):
        name (None | str | Unset):
    """

    always_load: list[str] | Unset | None = UNSET
    description: str | Unset | None = UNSET
    guide: str | Unset | None = UNSET
    labels: MemoryUpdateLabelsType0 | Unset | None = UNSET
    name: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.memory_update_labels_type_0 import MemoryUpdateLabelsType0

        always_load: list[str] | Unset | None
        if isinstance(self.always_load, Unset):
            always_load = UNSET
        elif isinstance(self.always_load, list):
            always_load = self.always_load

        else:
            always_load = self.always_load

        description: str | Unset | None
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        guide: str | Unset | None
        if isinstance(self.guide, Unset):
            guide = UNSET
        else:
            guide = self.guide

        labels: dict[str, Any] | Unset | None
        if isinstance(self.labels, Unset):
            labels = UNSET
        elif isinstance(self.labels, MemoryUpdateLabelsType0):
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
        if always_load is not UNSET:
            field_dict["always_load"] = always_load
        if description is not UNSET:
            field_dict["description"] = description
        if guide is not UNSET:
            field_dict["guide"] = guide
        if labels is not UNSET:
            field_dict["labels"] = labels
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.memory_update_labels_type_0 import MemoryUpdateLabelsType0

        d = dict(src_dict)

        def _parse_always_load(data: object) -> list[str] | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                always_load_type_0 = cast(list[str], data)

                return always_load_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | Unset | None, data)

        always_load = _parse_always_load(d.pop("always_load", UNSET))

        def _parse_description(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_guide(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        guide = _parse_guide(d.pop("guide", UNSET))

        def _parse_labels(data: object) -> MemoryUpdateLabelsType0 | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                labels_type_0 = MemoryUpdateLabelsType0.from_dict(data)

                return labels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MemoryUpdateLabelsType0 | Unset | None, data)

        labels = _parse_labels(d.pop("labels", UNSET))

        def _parse_name(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        name = _parse_name(d.pop("name", UNSET))

        memory_update = cls(
            always_load=always_load,
            description=description,
            guide=guide,
            labels=labels,
            name=name,
        )

        return memory_update
