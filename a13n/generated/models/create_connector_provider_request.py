from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_connector_provider_request_configuration import CreateConnectorProviderRequestConfiguration
    from ..models.create_connector_provider_request_credentials_type_0 import (
        CreateConnectorProviderRequestCredentialsType0,
    )


T = TypeVar("T", bound="CreateConnectorProviderRequest")


@_attrs_define(repr=False)
class CreateConnectorProviderRequest:
    """
    Attributes:
        configuration (CreateConnectorProviderRequestConfiguration):
        name (str):
        type_ (str):
        credentials (CreateConnectorProviderRequestCredentialsType0 | None | Unset):
    """

    configuration: CreateConnectorProviderRequestConfiguration
    name: str
    type_: str
    credentials: CreateConnectorProviderRequestCredentialsType0 | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_connector_provider_request_credentials_type_0 import (
            CreateConnectorProviderRequestCredentialsType0,
        )

        configuration = self.configuration.to_dict()

        name = self.name

        type_ = self.type_

        credentials: dict[str, Any] | Unset | None
        if isinstance(self.credentials, Unset):
            credentials = UNSET
        elif isinstance(self.credentials, CreateConnectorProviderRequestCredentialsType0):
            credentials = self.credentials.to_dict()
        else:
            credentials = self.credentials

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "configuration": configuration,
                "name": name,
                "type": type_,
            }
        )
        if credentials is not UNSET:
            field_dict["credentials"] = credentials

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_connector_provider_request_configuration import (
            CreateConnectorProviderRequestConfiguration,
        )
        from ..models.create_connector_provider_request_credentials_type_0 import (
            CreateConnectorProviderRequestCredentialsType0,
        )

        d = dict(src_dict)
        configuration = CreateConnectorProviderRequestConfiguration.from_dict(d.pop("configuration"))

        name = d.pop("name")

        type_ = d.pop("type")

        def _parse_credentials(data: object) -> CreateConnectorProviderRequestCredentialsType0 | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                credentials_type_0 = CreateConnectorProviderRequestCredentialsType0.from_dict(data)

                return credentials_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateConnectorProviderRequestCredentialsType0 | Unset | None, data)

        credentials = _parse_credentials(d.pop("credentials", UNSET))

        create_connector_provider_request = cls(
            configuration=configuration,
            name=name,
            type_=type_,
            credentials=credentials,
        )

        return create_connector_provider_request
