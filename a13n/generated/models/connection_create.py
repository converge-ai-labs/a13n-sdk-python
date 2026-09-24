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


T = TypeVar("T", bound="ConnectionCreate")


@_attrs_define(repr=False)
class ConnectionCreate:
    """
    Attributes:
        config (ConnectorConfig | McpConfig):
        name (str):
        type_ (str):
        auth (ConnectionAuth | Unset):
        client_secret (None | str | Unset):
        connector_provider_id (None | str | Unset):
        credential (BearerCredential | HeadersCredential | None | Unset):
    """

    config: ConnectorConfig | McpConfig
    name: str
    type_: str
    auth: ConnectionAuth | Unset = UNSET
    client_secret: str | Unset | None = UNSET
    connector_provider_id: str | Unset | None = UNSET
    credential: BearerCredential | HeadersCredential | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.bearer_credential import BearerCredential
        from ..models.headers_credential import HeadersCredential
        from ..models.mcp_config import McpConfig

        config: dict[str, Any]
        if isinstance(self.config, McpConfig):
            config = self.config.to_dict()
        else:
            config = self.config.to_dict()

        name = self.name

        type_ = self.type_

        auth: str | Unset = UNSET
        if not isinstance(self.auth, Unset):
            auth = self.auth.value

        client_secret: str | Unset | None
        if isinstance(self.client_secret, Unset):
            client_secret = UNSET
        else:
            client_secret = self.client_secret

        connector_provider_id: str | Unset | None
        if isinstance(self.connector_provider_id, Unset):
            connector_provider_id = UNSET
        else:
            connector_provider_id = self.connector_provider_id

        credential: dict[str, Any] | Unset | None
        if isinstance(self.credential, Unset):
            credential = UNSET
        elif isinstance(self.credential, BearerCredential):
            credential = self.credential.to_dict()
        elif isinstance(self.credential, HeadersCredential):
            credential = self.credential.to_dict()
        else:
            credential = self.credential

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "config": config,
                "name": name,
                "type": type_,
            }
        )
        if auth is not UNSET:
            field_dict["auth"] = auth
        if client_secret is not UNSET:
            field_dict["client_secret"] = client_secret
        if connector_provider_id is not UNSET:
            field_dict["connector_provider_id"] = connector_provider_id
        if credential is not UNSET:
            field_dict["credential"] = credential

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bearer_credential import BearerCredential
        from ..models.connector_config import ConnectorConfig
        from ..models.headers_credential import HeadersCredential
        from ..models.mcp_config import McpConfig

        d = dict(src_dict)

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

        name = d.pop("name")

        type_ = d.pop("type")

        _auth = d.pop("auth", UNSET)
        auth: ConnectionAuth | Unset
        if isinstance(_auth, Unset):
            auth = UNSET
        else:
            auth = ConnectionAuth(_auth)

        def _parse_client_secret(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        client_secret = _parse_client_secret(d.pop("client_secret", UNSET))

        def _parse_connector_provider_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        connector_provider_id = _parse_connector_provider_id(d.pop("connector_provider_id", UNSET))

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

        connection_create = cls(
            config=config,
            name=name,
            type_=type_,
            auth=auth,
            client_secret=client_secret,
            connector_provider_id=connector_provider_id,
            credential=credential,
        )

        return connection_create
