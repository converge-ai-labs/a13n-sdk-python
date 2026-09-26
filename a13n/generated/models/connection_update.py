from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.connection_auth import ConnectionAuth
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bearer_credential import BearerCredential
    from ..models.connector_config import ConnectorConfig
    from ..models.headers_credential import HeadersCredential
    from ..models.mcp_config import McpConfig


T = TypeVar("T", bound="ConnectionUpdate")


@_attrs_define(repr=False)
class ConnectionUpdate:
    """
    Attributes:
        auth (ConnectionAuth | None | Unset):
        client_secret (None | str | Unset):
        config (ConnectorConfig | McpConfig | None | Unset):
        credential (BearerCredential | HeadersCredential | None | Unset):
        enabled (bool | None | Unset):
        name (None | str | Unset):
    """

    auth: ConnectionAuth | Unset | None = UNSET
    client_secret: str | Unset | None = UNSET
    config: ConnectorConfig | McpConfig | Unset | None = UNSET
    credential: BearerCredential | HeadersCredential | Unset | None = UNSET
    enabled: bool | Unset | None = UNSET
    name: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.bearer_credential import BearerCredential
        from ..models.connector_config import ConnectorConfig
        from ..models.headers_credential import HeadersCredential
        from ..models.mcp_config import McpConfig

        auth: str | Unset | None
        if isinstance(self.auth, Unset):
            auth = UNSET
        elif isinstance(self.auth, ConnectionAuth):
            auth = self.auth.value
        else:
            auth = self.auth

        client_secret: str | Unset | None
        if isinstance(self.client_secret, Unset):
            client_secret = UNSET
        else:
            client_secret = self.client_secret

        config: dict[str, Any] | Unset | None
        if isinstance(self.config, Unset):
            config = UNSET
        elif isinstance(self.config, McpConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, ConnectorConfig):
            config = self.config.to_dict()
        else:
            config = self.config

        credential: dict[str, Any] | Unset | None
        if isinstance(self.credential, Unset):
            credential = UNSET
        elif isinstance(self.credential, BearerCredential):
            credential = self.credential.to_dict()
        elif isinstance(self.credential, HeadersCredential):
            credential = self.credential.to_dict()
        else:
            credential = self.credential

        enabled: bool | Unset | None
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        name: str | Unset | None
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if auth is not UNSET:
            field_dict["auth"] = auth
        if client_secret is not UNSET:
            field_dict["client_secret"] = client_secret
        if config is not UNSET:
            field_dict["config"] = config
        if credential is not UNSET:
            field_dict["credential"] = credential
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bearer_credential import BearerCredential
        from ..models.connector_config import ConnectorConfig
        from ..models.headers_credential import HeadersCredential
        from ..models.mcp_config import McpConfig

        d = dict(src_dict)

        def _parse_auth(data: object) -> ConnectionAuth | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                auth_type_0 = ConnectionAuth(data)

                return auth_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConnectionAuth | Unset | None, data)

        auth = _parse_auth(d.pop("auth", UNSET))

        def _parse_client_secret(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        client_secret = _parse_client_secret(d.pop("client_secret", UNSET))

        def _parse_config(data: object) -> ConnectorConfig | McpConfig | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_connection_config_type_0 = McpConfig.from_dict(data)

                return componentsschemas_connection_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_connection_config_type_1 = ConnectorConfig.from_dict(data)

                return componentsschemas_connection_config_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConnectorConfig | McpConfig | Unset | None, data)

        config = _parse_config(d.pop("config", UNSET))

        def _parse_credential(data: object) -> BearerCredential | HeadersCredential | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_entered_credential_type_0 = BearerCredential.from_dict(data)

                return componentsschemas_entered_credential_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_entered_credential_type_1 = HeadersCredential.from_dict(data)

                return componentsschemas_entered_credential_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BearerCredential | HeadersCredential | Unset | None, data)

        credential = _parse_credential(d.pop("credential", UNSET))

        def _parse_enabled(data: object) -> bool | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | Unset | None, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        def _parse_name(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        name = _parse_name(d.pop("name", UNSET))

        connection_update = cls(
            auth=auth,
            client_secret=client_secret,
            config=config,
            credential=credential,
            enabled=enabled,
            name=name,
        )

        return connection_update
