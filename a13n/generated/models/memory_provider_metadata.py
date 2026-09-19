from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.authentication import Authentication
    from ..models.memory_provider_metadata_configuration_schema import MemoryProviderMetadataConfigurationSchema
    from ..models.memory_provider_metadata_credential_schema_type_0 import MemoryProviderMetadataCredentialSchemaType0


T = TypeVar("T", bound="MemoryProviderMetadata")


@_attrs_define(repr=False)
class MemoryProviderMetadata:
    """
    Attributes:
        authentication (Authentication):
        configuration_schema (MemoryProviderMetadataConfigurationSchema):
        credential_schema (MemoryProviderMetadataCredentialSchemaType0 | None):
        display_name (str):
        type_ (str):
        setup_label (None | str | Unset):
        setup_url (None | str | Unset):
        supports_changes (bool | Unset):
        supports_documents (bool | Unset):
        supports_records (bool | Unset):
        supports_revisions (bool | Unset):
    """

    authentication: Authentication
    configuration_schema: MemoryProviderMetadataConfigurationSchema
    credential_schema: MemoryProviderMetadataCredentialSchemaType0 | None
    display_name: str
    type_: str
    setup_label: str | Unset | None = UNSET
    setup_url: str | Unset | None = UNSET
    supports_changes: bool | Unset = UNSET
    supports_documents: bool | Unset = UNSET
    supports_records: bool | Unset = UNSET
    supports_revisions: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.memory_provider_metadata_credential_schema_type_0 import (
            MemoryProviderMetadataCredentialSchemaType0,
        )

        authentication = self.authentication.to_dict()

        configuration_schema = self.configuration_schema.to_dict()

        credential_schema: dict[str, Any] | None
        if isinstance(self.credential_schema, MemoryProviderMetadataCredentialSchemaType0):
            credential_schema = self.credential_schema.to_dict()
        else:
            credential_schema = self.credential_schema

        display_name = self.display_name

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

        supports_changes = self.supports_changes

        supports_documents = self.supports_documents

        supports_records = self.supports_records

        supports_revisions = self.supports_revisions

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "authentication": authentication,
                "configuration_schema": configuration_schema,
                "credential_schema": credential_schema,
                "display_name": display_name,
                "type": type_,
            }
        )
        if setup_label is not UNSET:
            field_dict["setup_label"] = setup_label
        if setup_url is not UNSET:
            field_dict["setup_url"] = setup_url
        if supports_changes is not UNSET:
            field_dict["supports_changes"] = supports_changes
        if supports_documents is not UNSET:
            field_dict["supports_documents"] = supports_documents
        if supports_records is not UNSET:
            field_dict["supports_records"] = supports_records
        if supports_revisions is not UNSET:
            field_dict["supports_revisions"] = supports_revisions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.authentication import Authentication
        from ..models.memory_provider_metadata_configuration_schema import (
            MemoryProviderMetadataConfigurationSchema,
        )
        from ..models.memory_provider_metadata_credential_schema_type_0 import (
            MemoryProviderMetadataCredentialSchemaType0,
        )

        d = dict(src_dict)
        authentication = Authentication.from_dict(d.pop("authentication"))

        configuration_schema = MemoryProviderMetadataConfigurationSchema.from_dict(d.pop("configuration_schema"))

        def _parse_credential_schema(data: object) -> MemoryProviderMetadataCredentialSchemaType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                credential_schema_type_0 = MemoryProviderMetadataCredentialSchemaType0.from_dict(data)

                return credential_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MemoryProviderMetadataCredentialSchemaType0 | None, data)

        credential_schema = _parse_credential_schema(d.pop("credential_schema"))

        display_name = d.pop("display_name")

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

        supports_changes = d.pop("supports_changes", UNSET)

        supports_documents = d.pop("supports_documents", UNSET)

        supports_records = d.pop("supports_records", UNSET)

        supports_revisions = d.pop("supports_revisions", UNSET)

        memory_provider_metadata = cls(
            authentication=authentication,
            configuration_schema=configuration_schema,
            credential_schema=credential_schema,
            display_name=display_name,
            type_=type_,
            setup_label=setup_label,
            setup_url=setup_url,
            supports_changes=supports_changes,
            supports_documents=supports_documents,
            supports_records=supports_records,
            supports_revisions=supports_revisions,
        )

        return memory_provider_metadata
