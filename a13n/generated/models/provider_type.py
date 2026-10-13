from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.web_operation import WebOperation
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.authentication import Authentication
    from ..models.provider_type_configuration_schema import ProviderTypeConfigurationSchema
    from ..models.provider_type_credential_schema_type_0 import ProviderTypeCredentialSchemaType0
    from ..models.provider_type_environment_schema_type_0 import ProviderTypeEnvironmentSchemaType0
    from ..models.provider_type_model_api_labels_type_0 import ProviderTypeModelApiLabelsType0
    from ..models.provider_type_settings_schemas_type_0 import ProviderTypeSettingsSchemasType0


T = TypeVar("T", bound="ProviderType")


@_attrs_define(repr=False)
class ProviderType:
    """
    Attributes:
        authentication (Authentication):
        configuration_schema (ProviderTypeConfigurationSchema):
        credential_schema (None | ProviderTypeCredentialSchemaType0):
        display_name (str):
        setup_label (None | str):
        setup_url (None | str):
        supports_test (bool):
        type_ (str):
        catalog_providers (list[str] | None | Unset):
        default_model_api (None | str | Unset):
        environment_schema (None | ProviderTypeEnvironmentSchemaType0 | Unset):
        model_api_labels (None | ProviderTypeModelApiLabelsType0 | Unset):
        model_apis (list[str] | None | Unset):
        oauth_scheme (None | str | Unset):
        operations (list[WebOperation] | None | Unset):
        settings_schemas (None | ProviderTypeSettingsSchemasType0 | Unset):
        supports_destroy (bool | None | Unset):
        supports_model_discovery (bool | Unset):
        supports_stop (bool | None | Unset):
    """

    authentication: Authentication
    configuration_schema: ProviderTypeConfigurationSchema
    credential_schema: ProviderTypeCredentialSchemaType0 | None
    display_name: str
    setup_label: str | None
    setup_url: str | None
    supports_test: bool
    type_: str
    catalog_providers: list[str] | Unset | None = UNSET
    default_model_api: str | Unset | None = UNSET
    environment_schema: ProviderTypeEnvironmentSchemaType0 | Unset | None = UNSET
    model_api_labels: ProviderTypeModelApiLabelsType0 | Unset | None = UNSET
    model_apis: list[str] | Unset | None = UNSET
    oauth_scheme: str | Unset | None = UNSET
    operations: list[WebOperation] | Unset | None = UNSET
    settings_schemas: ProviderTypeSettingsSchemasType0 | Unset | None = UNSET
    supports_destroy: bool | Unset | None = UNSET
    supports_model_discovery: bool | Unset = UNSET
    supports_stop: bool | Unset | None = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.provider_type_credential_schema_type_0 import ProviderTypeCredentialSchemaType0
        from ..models.provider_type_environment_schema_type_0 import ProviderTypeEnvironmentSchemaType0
        from ..models.provider_type_model_api_labels_type_0 import ProviderTypeModelApiLabelsType0
        from ..models.provider_type_settings_schemas_type_0 import ProviderTypeSettingsSchemasType0

        authentication = self.authentication.to_dict()

        configuration_schema = self.configuration_schema.to_dict()

        credential_schema: dict[str, Any] | None
        if isinstance(self.credential_schema, ProviderTypeCredentialSchemaType0):
            credential_schema = self.credential_schema.to_dict()
        else:
            credential_schema = self.credential_schema

        display_name = self.display_name

        setup_label: str | None
        setup_label = self.setup_label

        setup_url: str | None
        setup_url = self.setup_url

        supports_test = self.supports_test

        type_ = self.type_

        catalog_providers: list[str] | Unset | None
        if isinstance(self.catalog_providers, Unset):
            catalog_providers = UNSET
        elif isinstance(self.catalog_providers, list):
            catalog_providers = self.catalog_providers

        else:
            catalog_providers = self.catalog_providers

        default_model_api: str | Unset | None
        if isinstance(self.default_model_api, Unset):
            default_model_api = UNSET
        else:
            default_model_api = self.default_model_api

        environment_schema: dict[str, Any] | Unset | None
        if isinstance(self.environment_schema, Unset):
            environment_schema = UNSET
        elif isinstance(self.environment_schema, ProviderTypeEnvironmentSchemaType0):
            environment_schema = self.environment_schema.to_dict()
        else:
            environment_schema = self.environment_schema

        model_api_labels: dict[str, Any] | Unset | None
        if isinstance(self.model_api_labels, Unset):
            model_api_labels = UNSET
        elif isinstance(self.model_api_labels, ProviderTypeModelApiLabelsType0):
            model_api_labels = self.model_api_labels.to_dict()
        else:
            model_api_labels = self.model_api_labels

        model_apis: list[str] | Unset | None
        if isinstance(self.model_apis, Unset):
            model_apis = UNSET
        elif isinstance(self.model_apis, list):
            model_apis = self.model_apis

        else:
            model_apis = self.model_apis

        oauth_scheme: str | Unset | None
        if isinstance(self.oauth_scheme, Unset):
            oauth_scheme = UNSET
        else:
            oauth_scheme = self.oauth_scheme

        operations: list[str] | Unset | None
        if isinstance(self.operations, Unset):
            operations = UNSET
        elif isinstance(self.operations, list):
            operations = []
            for operations_type_0_item_data in self.operations:
                operations_type_0_item = operations_type_0_item_data.value
                operations.append(operations_type_0_item)

        else:
            operations = self.operations

        settings_schemas: dict[str, Any] | Unset | None
        if isinstance(self.settings_schemas, Unset):
            settings_schemas = UNSET
        elif isinstance(self.settings_schemas, ProviderTypeSettingsSchemasType0):
            settings_schemas = self.settings_schemas.to_dict()
        else:
            settings_schemas = self.settings_schemas

        supports_destroy: bool | Unset | None
        if isinstance(self.supports_destroy, Unset):
            supports_destroy = UNSET
        else:
            supports_destroy = self.supports_destroy

        supports_model_discovery = self.supports_model_discovery

        supports_stop: bool | Unset | None
        if isinstance(self.supports_stop, Unset):
            supports_stop = UNSET
        else:
            supports_stop = self.supports_stop

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "authentication": authentication,
                "configuration_schema": configuration_schema,
                "credential_schema": credential_schema,
                "display_name": display_name,
                "setup_label": setup_label,
                "setup_url": setup_url,
                "supports_test": supports_test,
                "type": type_,
            }
        )
        if catalog_providers is not UNSET:
            field_dict["catalog_providers"] = catalog_providers
        if default_model_api is not UNSET:
            field_dict["default_model_api"] = default_model_api
        if environment_schema is not UNSET:
            field_dict["environment_schema"] = environment_schema
        if model_api_labels is not UNSET:
            field_dict["model_api_labels"] = model_api_labels
        if model_apis is not UNSET:
            field_dict["model_apis"] = model_apis
        if oauth_scheme is not UNSET:
            field_dict["oauth_scheme"] = oauth_scheme
        if operations is not UNSET:
            field_dict["operations"] = operations
        if settings_schemas is not UNSET:
            field_dict["settings_schemas"] = settings_schemas
        if supports_destroy is not UNSET:
            field_dict["supports_destroy"] = supports_destroy
        if supports_model_discovery is not UNSET:
            field_dict["supports_model_discovery"] = supports_model_discovery
        if supports_stop is not UNSET:
            field_dict["supports_stop"] = supports_stop

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.authentication import Authentication
        from ..models.provider_type_configuration_schema import ProviderTypeConfigurationSchema
        from ..models.provider_type_credential_schema_type_0 import ProviderTypeCredentialSchemaType0
        from ..models.provider_type_environment_schema_type_0 import ProviderTypeEnvironmentSchemaType0
        from ..models.provider_type_model_api_labels_type_0 import ProviderTypeModelApiLabelsType0
        from ..models.provider_type_settings_schemas_type_0 import ProviderTypeSettingsSchemasType0

        d = dict(src_dict)
        authentication = Authentication.from_dict(d.pop("authentication"))

        configuration_schema = ProviderTypeConfigurationSchema.from_dict(d.pop("configuration_schema"))

        def _parse_credential_schema(data: object) -> ProviderTypeCredentialSchemaType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                credential_schema_type_0 = ProviderTypeCredentialSchemaType0.from_dict(data)

                return credential_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ProviderTypeCredentialSchemaType0 | None, data)

        credential_schema = _parse_credential_schema(d.pop("credential_schema"))

        display_name = d.pop("display_name")

        def _parse_setup_label(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        setup_label = _parse_setup_label(d.pop("setup_label"))

        def _parse_setup_url(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        setup_url = _parse_setup_url(d.pop("setup_url"))

        supports_test = d.pop("supports_test")

        type_ = d.pop("type")

        def _parse_catalog_providers(data: object) -> list[str] | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                catalog_providers_type_0 = cast(list[str], data)

                return catalog_providers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | Unset | None, data)

        catalog_providers = _parse_catalog_providers(d.pop("catalog_providers", UNSET))

        def _parse_default_model_api(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        default_model_api = _parse_default_model_api(d.pop("default_model_api", UNSET))

        def _parse_environment_schema(data: object) -> ProviderTypeEnvironmentSchemaType0 | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                environment_schema_type_0 = ProviderTypeEnvironmentSchemaType0.from_dict(data)

                return environment_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ProviderTypeEnvironmentSchemaType0 | Unset | None, data)

        environment_schema = _parse_environment_schema(d.pop("environment_schema", UNSET))

        def _parse_model_api_labels(data: object) -> ProviderTypeModelApiLabelsType0 | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_api_labels_type_0 = ProviderTypeModelApiLabelsType0.from_dict(data)

                return model_api_labels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ProviderTypeModelApiLabelsType0 | Unset | None, data)

        model_api_labels = _parse_model_api_labels(d.pop("model_api_labels", UNSET))

        def _parse_model_apis(data: object) -> list[str] | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                model_apis_type_0 = cast(list[str], data)

                return model_apis_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | Unset | None, data)

        model_apis = _parse_model_apis(d.pop("model_apis", UNSET))

        def _parse_oauth_scheme(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        oauth_scheme = _parse_oauth_scheme(d.pop("oauth_scheme", UNSET))

        def _parse_operations(data: object) -> list[WebOperation] | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                operations_type_0 = []
                _operations_type_0 = data
                for operations_type_0_item_data in _operations_type_0:
                    operations_type_0_item = WebOperation(operations_type_0_item_data)

                    operations_type_0.append(operations_type_0_item)

                return operations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[WebOperation] | Unset | None, data)

        operations = _parse_operations(d.pop("operations", UNSET))

        def _parse_settings_schemas(data: object) -> ProviderTypeSettingsSchemasType0 | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                settings_schemas_type_0 = ProviderTypeSettingsSchemasType0.from_dict(data)

                return settings_schemas_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ProviderTypeSettingsSchemasType0 | Unset | None, data)

        settings_schemas = _parse_settings_schemas(d.pop("settings_schemas", UNSET))

        def _parse_supports_destroy(data: object) -> bool | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | Unset | None, data)

        supports_destroy = _parse_supports_destroy(d.pop("supports_destroy", UNSET))

        supports_model_discovery = d.pop("supports_model_discovery", UNSET)

        def _parse_supports_stop(data: object) -> bool | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | Unset | None, data)

        supports_stop = _parse_supports_stop(d.pop("supports_stop", UNSET))

        provider_type = cls(
            authentication=authentication,
            configuration_schema=configuration_schema,
            credential_schema=credential_schema,
            display_name=display_name,
            setup_label=setup_label,
            setup_url=setup_url,
            supports_test=supports_test,
            type_=type_,
            catalog_providers=catalog_providers,
            default_model_api=default_model_api,
            environment_schema=environment_schema,
            model_api_labels=model_api_labels,
            model_apis=model_apis,
            oauth_scheme=oauth_scheme,
            operations=operations,
            settings_schemas=settings_schemas,
            supports_destroy=supports_destroy,
            supports_model_discovery=supports_model_discovery,
            supports_stop=supports_stop,
        )

        provider_type.additional_properties = d
        return provider_type

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
