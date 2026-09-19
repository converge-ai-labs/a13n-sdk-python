from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.memory_entry_selection_mode import MemoryEntrySelectionMode
from ..models.memory_scope import MemoryScope
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inline_memory_backend import InlineMemoryBackend
    from ..models.managed_memory_backend import ManagedMemoryBackend


T = TypeVar("T", bound="MemoryEntrySelection")


@_attrs_define(repr=False)
class MemoryEntrySelection:
    """
    Attributes:
        backend (InlineMemoryBackend | ManagedMemoryBackend):
        description (str):
        mode (MemoryEntrySelectionMode):
        name (str):
        auto_organize (bool | Unset):
        auto_recall (bool | Unset):
        recall_limit (int | Unset):
        recall_required (bool | Unset):
        recall_threshold (float | None | Unset):
        recall_timeout (float | Unset):
        scope (MemoryScope | None | Unset):
        toolset (bool | Unset):
    """

    backend: InlineMemoryBackend | ManagedMemoryBackend
    description: str
    mode: MemoryEntrySelectionMode
    name: str
    auto_organize: bool | Unset = UNSET
    auto_recall: bool | Unset = UNSET
    recall_limit: int | Unset = UNSET
    recall_required: bool | Unset = UNSET
    recall_threshold: float | Unset | None = UNSET
    recall_timeout: float | Unset = UNSET
    scope: MemoryScope | Unset | None = UNSET
    toolset: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.managed_memory_backend import ManagedMemoryBackend

        backend: dict[str, Any]
        if isinstance(self.backend, ManagedMemoryBackend):
            backend = self.backend.to_dict()
        else:
            backend = self.backend.to_dict()

        description = self.description

        mode = self.mode.value

        name = self.name

        auto_organize = self.auto_organize

        auto_recall = self.auto_recall

        recall_limit = self.recall_limit

        recall_required = self.recall_required

        recall_threshold: float | Unset | None
        if isinstance(self.recall_threshold, Unset):
            recall_threshold = UNSET
        else:
            recall_threshold = self.recall_threshold

        recall_timeout = self.recall_timeout

        scope: str | Unset | None
        if isinstance(self.scope, Unset):
            scope = UNSET
        elif isinstance(self.scope, MemoryScope):
            scope = self.scope.value
        else:
            scope = self.scope

        toolset = self.toolset

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "backend": backend,
                "description": description,
                "mode": mode,
                "name": name,
            }
        )
        if auto_organize is not UNSET:
            field_dict["auto_organize"] = auto_organize
        if auto_recall is not UNSET:
            field_dict["auto_recall"] = auto_recall
        if recall_limit is not UNSET:
            field_dict["recall_limit"] = recall_limit
        if recall_required is not UNSET:
            field_dict["recall_required"] = recall_required
        if recall_threshold is not UNSET:
            field_dict["recall_threshold"] = recall_threshold
        if recall_timeout is not UNSET:
            field_dict["recall_timeout"] = recall_timeout
        if scope is not UNSET:
            field_dict["scope"] = scope
        if toolset is not UNSET:
            field_dict["toolset"] = toolset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inline_memory_backend import InlineMemoryBackend
        from ..models.managed_memory_backend import ManagedMemoryBackend

        d = dict(src_dict)

        def _parse_backend(data: object) -> InlineMemoryBackend | ManagedMemoryBackend:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                backend_type_0 = ManagedMemoryBackend.from_dict(data)

                return backend_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            backend_type_1 = InlineMemoryBackend.from_dict(data)

            return backend_type_1

        backend = _parse_backend(d.pop("backend"))

        description = d.pop("description")

        mode = MemoryEntrySelectionMode(d.pop("mode"))

        name = d.pop("name")

        auto_organize = d.pop("auto_organize", UNSET)

        auto_recall = d.pop("auto_recall", UNSET)

        recall_limit = d.pop("recall_limit", UNSET)

        recall_required = d.pop("recall_required", UNSET)

        def _parse_recall_threshold(data: object) -> float | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | Unset | None, data)

        recall_threshold = _parse_recall_threshold(d.pop("recall_threshold", UNSET))

        recall_timeout = d.pop("recall_timeout", UNSET)

        def _parse_scope(data: object) -> MemoryScope | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scope_type_0 = MemoryScope(data)

                return scope_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MemoryScope | Unset | None, data)

        scope = _parse_scope(d.pop("scope", UNSET))

        toolset = d.pop("toolset", UNSET)

        memory_entry_selection = cls(
            backend=backend,
            description=description,
            mode=mode,
            name=name,
            auto_organize=auto_organize,
            auto_recall=auto_recall,
            recall_limit=recall_limit,
            recall_required=recall_required,
            recall_threshold=recall_threshold,
            recall_timeout=recall_timeout,
            scope=scope,
            toolset=toolset,
        )

        return memory_entry_selection
