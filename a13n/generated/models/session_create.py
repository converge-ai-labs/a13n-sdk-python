from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.session_create_labels import SessionCreateLabels
    from ..models.session_memory_settings import SessionMemorySettings
    from ..models.session_origin import SessionOrigin


T = TypeVar("T", bound="SessionCreate")


@_attrs_define(repr=False)
class SessionCreate:
    """
    Attributes:
        labels (SessionCreateLabels | Unset):
        memory (None | SessionMemorySettings | Unset):
        origin (None | SessionOrigin | Unset):
        title (None | str | Unset):
    """

    labels: SessionCreateLabels | Unset = UNSET
    memory: SessionMemorySettings | Unset | None = UNSET
    origin: SessionOrigin | Unset | None = UNSET
    title: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.session_memory_settings import SessionMemorySettings
        from ..models.session_origin import SessionOrigin

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

        origin: dict[str, Any] | Unset | None
        if isinstance(self.origin, Unset):
            origin = UNSET
        elif isinstance(self.origin, SessionOrigin):
            origin = self.origin.to_dict()
        else:
            origin = self.origin

        title: str | Unset | None
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if labels is not UNSET:
            field_dict["labels"] = labels
        if memory is not UNSET:
            field_dict["memory"] = memory
        if origin is not UNSET:
            field_dict["origin"] = origin
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_create_labels import SessionCreateLabels
        from ..models.session_memory_settings import SessionMemorySettings
        from ..models.session_origin import SessionOrigin

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

        def _parse_origin(data: object) -> SessionOrigin | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                origin_type_0 = SessionOrigin.from_dict(data)

                return origin_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(SessionOrigin | Unset | None, data)

        origin = _parse_origin(d.pop("origin", UNSET))

        def _parse_title(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        title = _parse_title(d.pop("title", UNSET))

        session_create = cls(
            labels=labels,
            memory=memory,
            origin=origin,
            title=title,
        )

        return session_create
