from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.session_memory_settings import SessionMemorySettings
    from ..models.session_update_labels_type_0 import SessionUpdateLabelsType0


T = TypeVar("T", bound="SessionUpdate")


@_attrs_define(repr=False)
class SessionUpdate:
    """
    Attributes:
        labels (None | SessionUpdateLabelsType0 | Unset):
        memory (None | SessionMemorySettings | Unset):
    """

    labels: SessionUpdateLabelsType0 | Unset | None = UNSET
    memory: SessionMemorySettings | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.session_memory_settings import SessionMemorySettings
        from ..models.session_update_labels_type_0 import SessionUpdateLabelsType0

        labels: dict[str, Any] | Unset | None
        if isinstance(self.labels, Unset):
            labels = UNSET
        elif isinstance(self.labels, SessionUpdateLabelsType0):
            labels = self.labels.to_dict()
        else:
            labels = self.labels

        memory: dict[str, Any] | Unset | None
        if isinstance(self.memory, Unset):
            memory = UNSET
        elif isinstance(self.memory, SessionMemorySettings):
            memory = self.memory.to_dict()
        else:
            memory = self.memory

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if labels is not UNSET:
            field_dict["labels"] = labels
        if memory is not UNSET:
            field_dict["memory"] = memory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_memory_settings import SessionMemorySettings
        from ..models.session_update_labels_type_0 import SessionUpdateLabelsType0

        d = dict(src_dict)

        def _parse_labels(data: object) -> SessionUpdateLabelsType0 | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                labels_type_0 = SessionUpdateLabelsType0.from_dict(data)

                return labels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(SessionUpdateLabelsType0 | Unset | None, data)

        labels = _parse_labels(d.pop("labels", UNSET))

        def _parse_memory(data: object) -> SessionMemorySettings | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                memory_type_0 = SessionMemorySettings.from_dict(data)

                return memory_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(SessionMemorySettings | Unset | None, data)

        memory = _parse_memory(d.pop("memory", UNSET))

        session_update = cls(
            labels=labels,
            memory=memory,
        )

        return session_update
