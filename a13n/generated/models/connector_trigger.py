from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.connector_trigger_state import ConnectorTriggerState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connector_trigger_parameters import ConnectorTriggerParameters
    from ..models.event_thread_target import EventThreadTarget
    from ..models.event_type import EventType
    from ..models.store_only import StoreOnly


T = TypeVar("T", bound="ConnectorTrigger")


@_attrs_define(repr=False)
class ConnectorTrigger:
    """
    Attributes:
        connection_id (str):
        created_at (datetime.datetime):
        definition (EventType):
        event_type (str):
        failure (None | str):
        id (str):
        name (str):
        operation_kind (None | str):
        parameters (ConnectorTriggerParameters):
        provider_id (str):
        remote_id (None | str):
        state (ConnectorTriggerState):
        target (EventThreadTarget | StoreOnly):
        updated_at (datetime.datetime):
        version (int):
        workspace_id (str):
        retryable (bool | Unset):
    """

    connection_id: str
    created_at: datetime.datetime
    definition: EventType
    event_type: str
    failure: str | None
    id: str
    name: str
    operation_kind: str | None
    parameters: ConnectorTriggerParameters
    provider_id: str
    remote_id: str | None
    state: ConnectorTriggerState
    target: EventThreadTarget | StoreOnly
    updated_at: datetime.datetime
    version: int
    workspace_id: str
    retryable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.store_only import StoreOnly

        connection_id = self.connection_id

        created_at = self.created_at.isoformat()

        definition = self.definition.to_dict()

        event_type = self.event_type

        failure: str | None
        failure = self.failure

        id = self.id

        name = self.name

        operation_kind: str | None
        operation_kind = self.operation_kind

        parameters = self.parameters.to_dict()

        provider_id = self.provider_id

        remote_id: str | None
        remote_id = self.remote_id

        state = self.state.value

        target: dict[str, Any]
        if isinstance(self.target, StoreOnly):
            target = self.target.to_dict()
        else:
            target = self.target.to_dict()

        updated_at = self.updated_at.isoformat()

        version = self.version

        workspace_id = self.workspace_id

        retryable = self.retryable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connection_id": connection_id,
                "created_at": created_at,
                "definition": definition,
                "event_type": event_type,
                "failure": failure,
                "id": id,
                "name": name,
                "operation_kind": operation_kind,
                "parameters": parameters,
                "provider_id": provider_id,
                "remote_id": remote_id,
                "state": state,
                "target": target,
                "updated_at": updated_at,
                "version": version,
                "workspace_id": workspace_id,
            }
        )
        if retryable is not UNSET:
            field_dict["retryable"] = retryable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connector_trigger_parameters import ConnectorTriggerParameters
        from ..models.event_thread_target import EventThreadTarget
        from ..models.event_type import EventType
        from ..models.store_only import StoreOnly

        d = dict(src_dict)
        connection_id = d.pop("connection_id")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        definition = EventType.from_dict(d.pop("definition"))

        event_type = d.pop("event_type")

        def _parse_failure(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        failure = _parse_failure(d.pop("failure"))

        id = d.pop("id")

        name = d.pop("name")

        def _parse_operation_kind(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        operation_kind = _parse_operation_kind(d.pop("operation_kind"))

        parameters = ConnectorTriggerParameters.from_dict(d.pop("parameters"))

        provider_id = d.pop("provider_id")

        def _parse_remote_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        remote_id = _parse_remote_id(d.pop("remote_id"))

        state = ConnectorTriggerState(d.pop("state"))

        def _parse_target(data: object) -> EventThreadTarget | StoreOnly:
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

        target = _parse_target(d.pop("target"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        version = d.pop("version")

        workspace_id = d.pop("workspace_id")

        retryable = d.pop("retryable", UNSET)

        connector_trigger = cls(
            connection_id=connection_id,
            created_at=created_at,
            definition=definition,
            event_type=event_type,
            failure=failure,
            id=id,
            name=name,
            operation_kind=operation_kind,
            parameters=parameters,
            provider_id=provider_id,
            remote_id=remote_id,
            state=state,
            target=target,
            updated_at=updated_at,
            version=version,
            workspace_id=workspace_id,
            retryable=retryable,
        )

        connector_trigger.additional_properties = d
        return connector_trigger

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
