from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.connection_auth import ConnectionAuth
from ..models.connection_status import ConnectionStatus

if TYPE_CHECKING:
    from ..models.connection_failure import ConnectionFailure
    from ..models.connection_test_outcome import ConnectionTestOutcome
    from ..models.connector_config import ConnectorConfig
    from ..models.mcp_config import McpConfig


T = TypeVar("T", bound="Connection")


@_attrs_define(repr=False)
class Connection:
    """
    Attributes:
        auth (ConnectionAuth):
        authorization_pending (bool):
        client_secret_configured (bool):
        config (ConnectorConfig | McpConfig):
        connector_provider_id (None | str):
        created_at (datetime.datetime):
        created_by_id (str):
        credential_configured (bool):
        enabled (bool):
        failure (ConnectionFailure | None):
        id (str):
        last_test (ConnectionTestOutcome | None):
        name (str):
        organization_id (str):
        status (ConnectionStatus):
        type_ (str):
        updated_at (datetime.datetime):
        updated_by_id (str):
        version (int):
        workspace_id (str):
    """

    auth: ConnectionAuth
    authorization_pending: bool
    client_secret_configured: bool
    config: ConnectorConfig | McpConfig
    connector_provider_id: str | None
    created_at: datetime.datetime
    created_by_id: str
    credential_configured: bool
    enabled: bool
    failure: ConnectionFailure | None
    id: str
    last_test: ConnectionTestOutcome | None
    name: str
    organization_id: str
    status: ConnectionStatus
    type_: str
    updated_at: datetime.datetime
    updated_by_id: str
    version: int
    workspace_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.connection_failure import ConnectionFailure
        from ..models.connection_test_outcome import ConnectionTestOutcome
        from ..models.mcp_config import McpConfig

        auth = self.auth.value

        authorization_pending = self.authorization_pending

        client_secret_configured = self.client_secret_configured

        config: dict[str, Any]
        if isinstance(self.config, McpConfig):
            config = self.config.to_dict()
        else:
            config = self.config.to_dict()

        connector_provider_id: str | None
        connector_provider_id = self.connector_provider_id

        created_at = self.created_at.isoformat()

        created_by_id = self.created_by_id

        credential_configured = self.credential_configured

        enabled = self.enabled

        failure: dict[str, Any] | None
        if isinstance(self.failure, ConnectionFailure):
            failure = self.failure.to_dict()
        else:
            failure = self.failure

        id = self.id

        last_test: dict[str, Any] | None
        if isinstance(self.last_test, ConnectionTestOutcome):
            last_test = self.last_test.to_dict()
        else:
            last_test = self.last_test

        name = self.name

        organization_id = self.organization_id

        status = self.status.value

        type_ = self.type_

        updated_at = self.updated_at.isoformat()

        updated_by_id = self.updated_by_id

        version = self.version

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "auth": auth,
                "authorization_pending": authorization_pending,
                "client_secret_configured": client_secret_configured,
                "config": config,
                "connector_provider_id": connector_provider_id,
                "created_at": created_at,
                "created_by_id": created_by_id,
                "credential_configured": credential_configured,
                "enabled": enabled,
                "failure": failure,
                "id": id,
                "last_test": last_test,
                "name": name,
                "organization_id": organization_id,
                "status": status,
                "type": type_,
                "updated_at": updated_at,
                "updated_by_id": updated_by_id,
                "version": version,
                "workspace_id": workspace_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connection_failure import ConnectionFailure
        from ..models.connection_test_outcome import ConnectionTestOutcome
        from ..models.connector_config import ConnectorConfig
        from ..models.mcp_config import McpConfig

        d = dict(src_dict)
        auth = ConnectionAuth(d.pop("auth"))

        authorization_pending = d.pop("authorization_pending")

        client_secret_configured = d.pop("client_secret_configured")

        def _parse_config(data: object) -> ConnectorConfig | McpConfig:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_connection_config_type_0 = McpConfig.from_dict(data)

                return componentsschemas_connection_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_connection_config_type_1 = ConnectorConfig.from_dict(data)

            return componentsschemas_connection_config_type_1

        config = _parse_config(d.pop("config"))

        def _parse_connector_provider_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        connector_provider_id = _parse_connector_provider_id(d.pop("connector_provider_id"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        created_by_id = d.pop("created_by_id")

        credential_configured = d.pop("credential_configured")

        enabled = d.pop("enabled")

        def _parse_failure(data: object) -> ConnectionFailure | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                failure_type_0 = ConnectionFailure.from_dict(data)

                return failure_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConnectionFailure | None, data)

        failure = _parse_failure(d.pop("failure"))

        id = d.pop("id")

        def _parse_last_test(data: object) -> ConnectionTestOutcome | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_test_type_0 = ConnectionTestOutcome.from_dict(data)

                return last_test_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConnectionTestOutcome | None, data)

        last_test = _parse_last_test(d.pop("last_test"))

        name = d.pop("name")

        organization_id = d.pop("organization_id")

        status = ConnectionStatus(d.pop("status"))

        type_ = d.pop("type")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        updated_by_id = d.pop("updated_by_id")

        version = d.pop("version")

        workspace_id = d.pop("workspace_id")

        connection = cls(
            auth=auth,
            authorization_pending=authorization_pending,
            client_secret_configured=client_secret_configured,
            config=config,
            connector_provider_id=connector_provider_id,
            created_at=created_at,
            created_by_id=created_by_id,
            credential_configured=credential_configured,
            enabled=enabled,
            failure=failure,
            id=id,
            last_test=last_test,
            name=name,
            organization_id=organization_id,
            status=status,
            type_=type_,
            updated_at=updated_at,
            updated_by_id=updated_by_id,
            version=version,
            workspace_id=workspace_id,
        )

        connection.additional_properties = d
        return connection

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
