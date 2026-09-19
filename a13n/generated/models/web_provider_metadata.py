from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.web_provider_metadata_operations_item import WebProviderMetadataOperationsItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.authentication import Authentication
    from ..models.web_provider_metadata_configuration_schema import WebProviderMetadataConfigurationSchema
    from ..models.web_provider_metadata_credential_schema_type_0 import WebProviderMetadataCredentialSchemaType0


T = TypeVar("T", bound="WebProviderMetadata")


@_attrs_define(repr=False)
class WebProviderMetadata:
    """
    Attributes:
        authentication (Authentication):
        configuration_schema (WebProviderMetadataConfigurationSchema):
        credential_schema (None | WebProviderMetadataCredentialSchemaType0):
        display_name (str):
        operations (list[WebProviderMetadataOperationsItem]):
        type_ (str):
        setup_label (None | str | Unset):
        setup_url (None | str | Unset):
        supports_restricted_scrape (bool | Unset):
    """

    authentication: Authentication
    configuration_schema: WebProviderMetadataConfigurationSchema
    credential_schema: WebProviderMetadataCredentialSchemaType0 | None
    display_name: str
    operations: list[WebProviderMetadataOperationsItem]
    type_: str
    setup_label: str | Unset | None = UNSET
    setup_url: str | Unset | None = UNSET
    supports_restricted_scrape: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.web_provider_metadata_credential_schema_type_0 import WebProviderMetadataCredentialSchemaType0

        authentication = self.authentication.to_dict()

        configuration_schema = self.configuration_schema.to_dict()

        credential_schema: dict[str, Any] | None
        if isinstance(self.credential_schema, WebProviderMetadataCredentialSchemaType0):
            credential_schema = self.credential_schema.to_dict()
        else:
            credential_schema = self.credential_schema

        display_name = self.display_name

        operations = []
        for operations_item_data in self.operations:
            operations_item = operations_item_data.value
            operations.append(operations_item)

        type_ = self.type_

        setup_label: str | Unset | None
        if isinstance(self.setup_label, Unset):
            setup_label = UNSET
        else:
            setup_label = self.setup_label

        setup_url: str | Unset | None
        if isinstance(self.setup_url, Unset):
            setup_url = UNSET
        else:
            setup_url = self.setup_url

        supports_restricted_scrape = self.supports_restricted_scrape

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "authentication": authentication,
                "configuration_schema": configuration_schema,
                "credential_schema": credential_schema,
                "display_name": display_name,
                "operations": operations,
                "type": type_,
            }
        )
        if setup_label is not UNSET:
            field_dict["setup_label"] = setup_label
        if setup_url is not UNSET:
            field_dict["setup_url"] = setup_url
        if supports_restricted_scrape is not UNSET:
            field_dict["supports_restricted_scrape"] = supports_restricted_scrape

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.authentication import Authentication
        from ..models.web_provider_metadata_configuration_schema import (
            WebProviderMetadataConfigurationSchema,
        )
        from ..models.web_provider_metadata_credential_schema_type_0 import (
            WebProviderMetadataCredentialSchemaType0,
        )

        d = dict(src_dict)
        authentication = Authentication.from_dict(d.pop("authentication"))

        configuration_schema = WebProviderMetadataConfigurationSchema.from_dict(d.pop("configuration_schema"))

        def _parse_credential_schema(data: object) -> WebProviderMetadataCredentialSchemaType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                credential_schema_type_0 = WebProviderMetadataCredentialSchemaType0.from_dict(data)

                return credential_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(WebProviderMetadataCredentialSchemaType0 | None, data)

        credential_schema = _parse_credential_schema(d.pop("credential_schema"))

        display_name = d.pop("display_name")

        operations = []
        _operations = d.pop("operations")
        for operations_item_data in _operations:
            operations_item = WebProviderMetadataOperationsItem(operations_item_data)

            operations.append(operations_item)

        type_ = d.pop("type")

        def _parse_setup_label(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        setup_label = _parse_setup_label(d.pop("setup_label", UNSET))

        def _parse_setup_url(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        setup_url = _parse_setup_url(d.pop("setup_url", UNSET))

        supports_restricted_scrape = d.pop("supports_restricted_scrape", UNSET)

        web_provider_metadata = cls(
            authentication=authentication,
            configuration_schema=configuration_schema,
            credential_schema=credential_schema,
            display_name=display_name,
            operations=operations,
            type_=type_,
            setup_label=setup_label,
            setup_url=setup_url,
            supports_restricted_scrape=supports_restricted_scrape,
        )

        return web_provider_metadata
