from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.observer_state_children import ObserverStateChildren
    from ..models.observer_state_parts import ObserverStateParts
    from ..models.observer_state_threads import ObserverStateThreads


T = TypeVar("T", bound="ObserverState")


@_attrs_define(repr=False)
class ObserverState:
    """
    Attributes:
        children (ObserverStateChildren | Unset):
        parts (ObserverStateParts | Unset):
        request_index (int | Unset):
        threads (ObserverStateThreads | Unset):
    """

    children: ObserverStateChildren | Unset = UNSET
    parts: ObserverStateParts | Unset = UNSET
    request_index: int | Unset = UNSET
    threads: ObserverStateThreads | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        children: dict[str, Any] | Unset = UNSET
        if not isinstance(self.children, Unset):
            children = self.children.to_dict()

        parts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parts, Unset):
            parts = self.parts.to_dict()

        request_index = self.request_index

        threads: dict[str, Any] | Unset = UNSET
        if not isinstance(self.threads, Unset):
            threads = self.threads.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if children is not UNSET:
            field_dict["children"] = children
        if parts is not UNSET:
            field_dict["parts"] = parts
        if request_index is not UNSET:
            field_dict["request_index"] = request_index
        if threads is not UNSET:
            field_dict["threads"] = threads

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.observer_state_children import ObserverStateChildren
        from ..models.observer_state_parts import ObserverStateParts
        from ..models.observer_state_threads import ObserverStateThreads

        d = dict(src_dict)
        _children = d.pop("children", UNSET)
        children: ObserverStateChildren | Unset
        if isinstance(_children, Unset):
            children = UNSET
        else:
            children = ObserverStateChildren.from_dict(_children)

        _parts = d.pop("parts", UNSET)
        parts: ObserverStateParts | Unset
        if isinstance(_parts, Unset):
            parts = UNSET
        else:
            parts = ObserverStateParts.from_dict(_parts)

        request_index = d.pop("request_index", UNSET)

        _threads = d.pop("threads", UNSET)
        threads: ObserverStateThreads | Unset
        if isinstance(_threads, Unset):
            threads = UNSET
        else:
            threads = ObserverStateThreads.from_dict(_threads)

        observer_state = cls(
            children=children,
            parts=parts,
            request_index=request_index,
            threads=threads,
        )

        observer_state.additional_properties = d
        return observer_state

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
