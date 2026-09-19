from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.authentication import Authentication
    from ..models.model_provider_metadata_configuration_schema import ModelProviderMetadataConfigurationSchema
    from ..models.model_provider_metadata_credential_schema_type_0 import ModelProviderMetadataCredentialSchemaType0
    from ..models.model_provider_metadata_model_api_labels import ModelProviderMetadataModelApiLabels
    from ..models.model_provider_metadata_settings_schemas import ModelProviderMetadataSettingsSchemas


T = TypeVar("T", bound="ModelProviderMetadata")


@_attrs_define(repr=False)
class ModelProviderMetadata:
    """
    Attributes:
        authentication (Authentication):
        configuration_schema (ModelProviderMetadataConfigurationSchema):
        credential_schema (ModelProviderMetadataCredentialSchemaType0 | None):
        default_model_api (str):
        display_name (str):
        model_api_labels (ModelProviderMetadataModelApiLabels):
        settings_schemas (ModelProviderMetadataSettingsSchemas):
        supported_model_apis (list[str]):
        supports_connection_probe (bool):
        type_ (str):
        catalog_providers (list[str] | Unset):
        setup_label (None | str | Unset):
        setup_url (None | str | Unset):
    """

    authentication: Authentication
    configuration_schema: ModelProviderMetadataConfigurationSchema
    credential_schema: ModelProviderMetadataCredentialSchemaType0 | None
    default_model_api: str
    display_name: str
    model_api_labels: ModelProviderMetadataModelApiLabels
    settings_schemas: ModelProviderMetadataSettingsSchemas
    supported_model_apis: list[str]
    supports_connection_probe: bool
    type_: str
    catalog_providers: list[str] | Unset = UNSET
    setup_label: str | Unset | None = UNSET
    setup_url: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.model_provider_metadata_credential_schema_type_0 import ModelProviderMetadataCredentialSchemaType0

        authentication = self.authentication.to_dict()

        configuration_schema = self.configuration_schema.to_dict()

        credential_schema: dict[str, Any] | None
        if isinstance(self.credential_schema, ModelProviderMetadataCredentialSchemaType0):
            credential_schema = self.credential_schema.to_dict()
        else:
            credential_schema = self.credential_schema

        default_model_api = self.default_model_api

        display_name = self.display_name

        model_api_labels = self.model_api_labels.to_dict()

        settings_schemas = self.settings_schemas.to_dict()

        supported_model_apis = self.supported_model_apis

        supports_connection_probe = self.supports_connection_probe

        type_ = self.type_

        catalog_providers: list[str] | Unset = UNSET
        if not isinstance(self.catalog_providers, Unset):
            catalog_providers = self.catalog_providers

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

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "authentication": authentication,
                "configuration_schema": configuration_schema,
                "credential_schema": credential_schema,
                "default_model_api": default_model_api,
                "display_name": display_name,
                "model_api_labels": model_api_labels,
                "settings_schemas": settings_schemas,
                "supported_model_apis": supported_model_apis,
                "supports_connection_probe": supports_connection_probe,
                "type": type_,
            }
        )
        if catalog_providers is not UNSET:
            field_dict["catalog_providers"] = catalog_providers
        if setup_label is not UNSET:
            field_dict["setup_label"] = setup_label
        if setup_url is not UNSET:
            field_dict["setup_url"] = setup_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.authentication import Authentication
        from ..models.model_provider_metadata_configuration_schema import (
            ModelProviderMetadataConfigurationSchema,
        )
        from ..models.model_provider_metadata_credential_schema_type_0 import (
            ModelProviderMetadataCredentialSchemaType0,
        )
        from ..models.model_provider_metadata_model_api_labels import (
            ModelProviderMetadataModelApiLabels,
        )
        from ..models.model_provider_metadata_settings_schemas import (
            ModelProviderMetadataSettingsSchemas,
        )

        d = dict(src_dict)
        authentication = Authentication.from_dict(d.pop("authentication"))

        configuration_schema = ModelProviderMetadataConfigurationSchema.from_dict(d.pop("configuration_schema"))

        def _parse_credential_schema(data: object) -> ModelProviderMetadataCredentialSchemaType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                credential_schema_type_0 = ModelProviderMetadataCredentialSchemaType0.from_dict(data)

                return credential_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelProviderMetadataCredentialSchemaType0 | None, data)

        credential_schema = _parse_credential_schema(d.pop("credential_schema"))

        default_model_api = d.pop("default_model_api")

        display_name = d.pop("display_name")

        model_api_labels = ModelProviderMetadataModelApiLabels.from_dict(d.pop("model_api_labels"))

        settings_schemas = ModelProviderMetadataSettingsSchemas.from_dict(d.pop("settings_schemas"))

        supported_model_apis = cast(list[str], d.pop("supported_model_apis"))

        supports_connection_probe = d.pop("supports_connection_probe")

        type_ = d.pop("type")

        catalog_providers = cast(list[str], d.pop("catalog_providers", UNSET))

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

        model_provider_metadata = cls(
            authentication=authentication,
            configuration_schema=configuration_schema,
            credential_schema=credential_schema,
            default_model_api=default_model_api,
            display_name=display_name,
            model_api_labels=model_api_labels,
            settings_schemas=settings_schemas,
            supported_model_apis=supported_model_apis,
            supports_connection_probe=supports_connection_probe,
            type_=type_,
            catalog_providers=catalog_providers,
            setup_label=setup_label,
            setup_url=setup_url,
        )

        return model_provider_metadata
