from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_thread_target import EventThreadTarget
    from ..models.store_only import StoreOnly


T = TypeVar("T", bound="TriggerUpdate")


@_attrs_define(repr=False)
class TriggerUpdate:
    """
    Attributes:
        name (None | str | Unset):
        target (EventThreadTarget | None | StoreOnly | Unset):
    """

    name: str | Unset | None = UNSET
    target: EventThreadTarget | StoreOnly | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.event_thread_target import EventThreadTarget
        from ..models.store_only import StoreOnly

        name: str | Unset | None
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        target: dict[str, Any] | Unset | None
        if isinstance(self.target, Unset):
            target = UNSET
        elif isinstance(self.target, StoreOnly):
            target = self.target.to_dict()
        elif isinstance(self.target, EventThreadTarget):
            target = self.target.to_dict()
        else:
            target = self.target

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_thread_target import EventThreadTarget
        from ..models.store_only import StoreOnly

        d = dict(src_dict)

        def _parse_name(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_target(data: object) -> EventThreadTarget | StoreOnly | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_target_type_0 = StoreOnly.from_dict(data)

                return componentsschemas_target_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_target_type_1 = EventThreadTarget.from_dict(data)

                return componentsschemas_target_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EventThreadTarget | StoreOnly | Unset | None, data)

        target = _parse_target(d.pop("target", UNSET))

        trigger_update = cls(
            name=name,
            target=target,
        )

        return trigger_update
