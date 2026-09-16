from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_provider_definition_configuration_schema import ModelProviderDefinitionConfigurationSchema
    from ..models.model_provider_definition_credential_schema import ModelProviderDefinitionCredentialSchema
    from ..models.model_provider_definition_model_api_labels import ModelProviderDefinitionModelApiLabels
    from ..models.model_provider_definition_settings_schemas import ModelProviderDefinitionSettingsSchemas


T = TypeVar("T", bound="ModelProviderDefinition")


@_attrs_define(repr=False)
class ModelProviderDefinition:
    """
    Attributes:
        configuration_schema (ModelProviderDefinitionConfigurationSchema):
        credential_schema (ModelProviderDefinitionCredentialSchema):
        default_model_api (str):
        display_name (str):
        model_api_labels (ModelProviderDefinitionModelApiLabels):
        settings_schemas (ModelProviderDefinitionSettingsSchemas):
        supported_model_apis (list[str]):
        type_ (str):
        catalog_providers (list[str] | Unset):
    """

    configuration_schema: ModelProviderDefinitionConfigurationSchema
    credential_schema: ModelProviderDefinitionCredentialSchema
    default_model_api: str
    display_name: str
    model_api_labels: ModelProviderDefinitionModelApiLabels
    settings_schemas: ModelProviderDefinitionSettingsSchemas
    supported_model_apis: list[str]
    type_: str
    catalog_providers: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        configuration_schema = self.configuration_schema.to_dict()

        credential_schema = self.credential_schema.to_dict()

        default_model_api = self.default_model_api

        display_name = self.display_name

        model_api_labels = self.model_api_labels.to_dict()

        settings_schemas = self.settings_schemas.to_dict()

        supported_model_apis = self.supported_model_apis

        type_ = self.type_

        catalog_providers: list[str] | Unset = UNSET
        if not isinstance(self.catalog_providers, Unset):
            catalog_providers = self.catalog_providers

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "configuration_schema": configuration_schema,
                "credential_schema": credential_schema,
                "default_model_api": default_model_api,
                "display_name": display_name,
                "model_api_labels": model_api_labels,
                "settings_schemas": settings_schemas,
                "supported_model_apis": supported_model_apis,
                "type": type_,
            }
        )
        if catalog_providers is not UNSET:
            field_dict["catalog_providers"] = catalog_providers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_provider_definition_configuration_schema import (
            ModelProviderDefinitionConfigurationSchema,
        )
        from ..models.model_provider_definition_credential_schema import (
            ModelProviderDefinitionCredentialSchema,
        )
        from ..models.model_provider_definition_model_api_labels import (
            ModelProviderDefinitionModelApiLabels,
        )
        from ..models.model_provider_definition_settings_schemas import (
            ModelProviderDefinitionSettingsSchemas,
        )

        d = dict(src_dict)
        configuration_schema = ModelProviderDefinitionConfigurationSchema.from_dict(d.pop("configuration_schema"))

        credential_schema = ModelProviderDefinitionCredentialSchema.from_dict(d.pop("credential_schema"))

        default_model_api = d.pop("default_model_api")

        display_name = d.pop("display_name")

        model_api_labels = ModelProviderDefinitionModelApiLabels.from_dict(d.pop("model_api_labels"))

        settings_schemas = ModelProviderDefinitionSettingsSchemas.from_dict(d.pop("settings_schemas"))

        supported_model_apis = cast(list[str], d.pop("supported_model_apis"))

        type_ = d.pop("type")

        catalog_providers = cast(list[str], d.pop("catalog_providers", UNSET))

        model_provider_definition = cls(
            configuration_schema=configuration_schema,
            credential_schema=credential_schema,
            default_model_api=default_model_api,
            display_name=display_name,
            model_api_labels=model_api_labels,
            settings_schemas=settings_schemas,
            supported_model_apis=supported_model_apis,
            type_=type_,
            catalog_providers=catalog_providers,
        )

        return model_provider_definition
