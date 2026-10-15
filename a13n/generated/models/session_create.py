from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.session_create_labels import SessionCreateLabels
    from ..models.session_memory_settings import SessionMemorySettings


T = TypeVar("T", bound="SessionCreate")


@_attrs_define(repr=False)
class SessionCreate:
    """
    Attributes:
        labels (SessionCreateLabels | Unset):
        memory (None | SessionMemorySettings | Unset):
    """

    labels: SessionCreateLabels | Unset = UNSET
    memory: SessionMemorySettings | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.session_memory_settings import SessionMemorySettings

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

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
        from ..models.session_create_labels import SessionCreateLabels
        from ..models.session_memory_settings import SessionMemorySettings

        d = dict(src_dict)
        _labels = d.pop("labels", UNSET)
        labels: SessionCreateLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = SessionCreateLabels.from_dict(_labels)

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

        session_create = cls(
            labels=labels,
            memory=memory,
        )

        return session_create
