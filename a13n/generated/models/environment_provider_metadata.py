from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.authentication import Authentication
    from ..models.environment_provider_metadata_configuration_schema import (
        EnvironmentProviderMetadataConfigurationSchema,
    )
    from ..models.environment_provider_metadata_credential_schema_type_0 import (
        EnvironmentProviderMetadataCredentialSchemaType0,
    )
    from ..models.environment_provider_metadata_template_configuration_schema import (
        EnvironmentProviderMetadataTemplateConfigurationSchema,
    )


T = TypeVar("T", bound="EnvironmentProviderMetadata")


@_attrs_define(repr=False)
class EnvironmentProviderMetadata:
    """
    Attributes:
        authentication (Authentication):
        configuration_schema (EnvironmentProviderMetadataConfigurationSchema):
        credential_schema (EnvironmentProviderMetadataCredentialSchemaType0 | None):
        display_name (str):
        requires_keepalive (bool):
        supports_destroy (bool):
        supports_managed (bool):
        supports_stop (bool):
        template_configuration_schema (EnvironmentProviderMetadataTemplateConfigurationSchema):
        type_ (str):
        deployment_managed (bool | Unset):
        setup_label (None | str | Unset):
        setup_url (None | str | Unset):
    """

    authentication: Authentication
    configuration_schema: EnvironmentProviderMetadataConfigurationSchema
    credential_schema: EnvironmentProviderMetadataCredentialSchemaType0 | None
    display_name: str
    requires_keepalive: bool
    supports_destroy: bool
    supports_managed: bool
    supports_stop: bool
    template_configuration_schema: EnvironmentProviderMetadataTemplateConfigurationSchema
    type_: str
    deployment_managed: bool | Unset = UNSET
    setup_label: str | Unset | None = UNSET
    setup_url: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.environment_provider_metadata_credential_schema_type_0 import (
            EnvironmentProviderMetadataCredentialSchemaType0,
        )

        authentication = self.authentication.to_dict()

        configuration_schema = self.configuration_schema.to_dict()

        credential_schema: dict[str, Any] | None
        if isinstance(self.credential_schema, EnvironmentProviderMetadataCredentialSchemaType0):
            credential_schema = self.credential_schema.to_dict()
        else:
            credential_schema = self.credential_schema

        display_name = self.display_name

        requires_keepalive = self.requires_keepalive

        supports_destroy = self.supports_destroy

        supports_managed = self.supports_managed

        supports_stop = self.supports_stop

        template_configuration_schema = self.template_configuration_schema.to_dict()

        type_ = self.type_

        deployment_managed = self.deployment_managed

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
                "display_name": display_name,
                "requires_keepalive": requires_keepalive,
                "supports_destroy": supports_destroy,
                "supports_managed": supports_managed,
                "supports_stop": supports_stop,
                "template_configuration_schema": template_configuration_schema,
                "type": type_,
            }
        )
        if deployment_managed is not UNSET:
            field_dict["deployment_managed"] = deployment_managed
        if setup_label is not UNSET:
            field_dict["setup_label"] = setup_label
        if setup_url is not UNSET:
            field_dict["setup_url"] = setup_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.authentication import Authentication
        from ..models.environment_provider_metadata_configuration_schema import (
            EnvironmentProviderMetadataConfigurationSchema,
        )
        from ..models.environment_provider_metadata_credential_schema_type_0 import (
            EnvironmentProviderMetadataCredentialSchemaType0,
        )
        from ..models.environment_provider_metadata_template_configuration_schema import (
            EnvironmentProviderMetadataTemplateConfigurationSchema,
        )

        d = dict(src_dict)
        authentication = Authentication.from_dict(d.pop("authentication"))

        configuration_schema = EnvironmentProviderMetadataConfigurationSchema.from_dict(d.pop("configuration_schema"))

        def _parse_credential_schema(data: object) -> EnvironmentProviderMetadataCredentialSchemaType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                credential_schema_type_0 = EnvironmentProviderMetadataCredentialSchemaType0.from_dict(data)

                return credential_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnvironmentProviderMetadataCredentialSchemaType0 | None, data)

        credential_schema = _parse_credential_schema(d.pop("credential_schema"))

        display_name = d.pop("display_name")

        requires_keepalive = d.pop("requires_keepalive")

        supports_destroy = d.pop("supports_destroy")

        supports_managed = d.pop("supports_managed")

        supports_stop = d.pop("supports_stop")

        template_configuration_schema = EnvironmentProviderMetadataTemplateConfigurationSchema.from_dict(
            d.pop("template_configuration_schema")
        )

        type_ = d.pop("type")

        deployment_managed = d.pop("deployment_managed", UNSET)

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

        environment_provider_metadata = cls(
            authentication=authentication,
            configuration_schema=configuration_schema,
            credential_schema=credential_schema,
            display_name=display_name,
            requires_keepalive=requires_keepalive,
            supports_destroy=supports_destroy,
            supports_managed=supports_managed,
            supports_stop=supports_stop,
            template_configuration_schema=template_configuration_schema,
            type_=type_,
            deployment_managed=deployment_managed,
            setup_label=setup_label,
            setup_url=setup_url,
        )

        return environment_provider_metadata
