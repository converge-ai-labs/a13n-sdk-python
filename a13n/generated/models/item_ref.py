from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.item_kind import ItemKind
from ..models.item_state import ItemState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_ref_failure_type_0 import ItemRefFailureType0
    from ..models.memory_source import MemorySource


T = TypeVar("T", bound="ItemRef")


@_attrs_define(repr=False)
class ItemRef:
    """The item a live event changed, and its state after the event.

    Attributes:
        id (str):
        kind (ItemKind):
        state (ItemState):
        failure (ItemRefFailureType0 | None | Unset):
        memory_sources (list[MemorySource] | None | Unset):
        ordinal (int | None | Unset):
        response_group (None | str | Unset):
    """

    id: str
    kind: ItemKind
    state: ItemState
    failure: ItemRefFailureType0 | Unset | None = UNSET
    memory_sources: list[MemorySource] | Unset | None = UNSET
    ordinal: int | Unset | None = UNSET
    response_group: str | Unset | None = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.item_ref_failure_type_0 import ItemRefFailureType0

        id = self.id

        kind = self.kind.value

        state = self.state.value

        failure: dict[str, Any] | Unset | None
        if isinstance(self.failure, Unset):
            failure = UNSET
        elif isinstance(self.failure, ItemRefFailureType0):
            failure = self.failure.to_dict()
        else:
            failure = self.failure

        memory_sources: list[dict[str, Any]] | Unset | None
        if isinstance(self.memory_sources, Unset):
            memory_sources = UNSET
        elif isinstance(self.memory_sources, list):
            memory_sources = []
            for memory_sources_type_0_item_data in self.memory_sources:
                memory_sources_type_0_item = memory_sources_type_0_item_data.to_dict()
                memory_sources.append(memory_sources_type_0_item)

        else:
            memory_sources = self.memory_sources

        ordinal: int | Unset | None
        if isinstance(self.ordinal, Unset):
            ordinal = UNSET
        else:
            ordinal = self.ordinal

        response_group: str | Unset | None
        if isinstance(self.response_group, Unset):
            response_group = UNSET
        else:
            response_group = self.response_group

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "kind": kind,
                "state": state,
            }
        )
        if failure is not UNSET:
            field_dict["failure"] = failure
        if memory_sources is not UNSET:
            field_dict["memory_sources"] = memory_sources
        if ordinal is not UNSET:
            field_dict["ordinal"] = ordinal
        if response_group is not UNSET:
            field_dict["response_group"] = response_group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.item_ref_failure_type_0 import ItemRefFailureType0
        from ..models.memory_source import MemorySource

        d = dict(src_dict)
        id = d.pop("id")

        kind = ItemKind(d.pop("kind"))

        state = ItemState(d.pop("state"))

        def _parse_failure(data: object) -> ItemRefFailureType0 | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                failure_type_0 = ItemRefFailureType0.from_dict(data)

                return failure_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ItemRefFailureType0 | Unset | None, data)

        failure = _parse_failure(d.pop("failure", UNSET))

        def _parse_memory_sources(data: object) -> list[MemorySource] | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                memory_sources_type_0 = []
                _memory_sources_type_0 = data
                for memory_sources_type_0_item_data in _memory_sources_type_0:
                    memory_sources_type_0_item = MemorySource.from_dict(memory_sources_type_0_item_data)

                    memory_sources_type_0.append(memory_sources_type_0_item)

                return memory_sources_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MemorySource] | Unset | None, data)

        memory_sources = _parse_memory_sources(d.pop("memory_sources", UNSET))

        def _parse_ordinal(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        ordinal = _parse_ordinal(d.pop("ordinal", UNSET))

        def _parse_response_group(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        response_group = _parse_response_group(d.pop("response_group", UNSET))

        item_ref = cls(
            id=id,
            kind=kind,
            state=state,
            failure=failure,
            memory_sources=memory_sources,
            ordinal=ordinal,
            response_group=response_group,
        )

        item_ref.additional_properties = d
        return item_ref

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
