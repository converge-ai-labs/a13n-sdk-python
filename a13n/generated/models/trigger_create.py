from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_thread_target import EventThreadTarget
    from ..models.store_only import StoreOnly
    from ..models.trigger_create_parameters import TriggerCreateParameters


T = TypeVar("T", bound="TriggerCreate")


@_attrs_define(repr=False)
class TriggerCreate:
    """
    Attributes:
        connection_id (str):
        event_type (str):
        name (str):
        parameters (TriggerCreateParameters | Unset):
        target (EventThreadTarget | StoreOnly | Unset):
    """

    connection_id: str
    event_type: str
    name: str
    parameters: TriggerCreateParameters | Unset = UNSET
    target: EventThreadTarget | StoreOnly | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.store_only import StoreOnly

        connection_id = self.connection_id

        event_type = self.event_type

        name = self.name

        parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        target: dict[str, Any] | Unset
        if isinstance(self.target, Unset):
            target = UNSET
        elif isinstance(self.target, StoreOnly):
            target = self.target.to_dict()
        else:
            target = self.target.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "connection_id": connection_id,
                "event_type": event_type,
                "name": name,
            }
        )
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_thread_target import EventThreadTarget
        from ..models.store_only import StoreOnly
        from ..models.trigger_create_parameters import TriggerCreateParameters

        d = dict(src_dict)
        connection_id = d.pop("connection_id")

        event_type = d.pop("event_type")

        name = d.pop("name")

        _parameters = d.pop("parameters", UNSET)
        parameters: TriggerCreateParameters | Unset
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = TriggerCreateParameters.from_dict(_parameters)

        def _parse_target(data: object) -> EventThreadTarget | StoreOnly | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_target_type_0 = StoreOnly.from_dict(data)

                return componentsschemas_target_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_target_type_1 = EventThreadTarget.from_dict(data)

            return componentsschemas_target_type_1

        target = _parse_target(d.pop("target", UNSET))

        trigger_create = cls(
            connection_id=connection_id,
            event_type=event_type,
            name=name,
            parameters=parameters,
            target=target,
        )

        return trigger_create
