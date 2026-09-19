from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.memory_provider_definition_configuration_schema import MemoryProviderDefinitionConfigurationSchema
    from ..models.memory_provider_definition_credential_schema import MemoryProviderDefinitionCredentialSchema


T = TypeVar("T", bound="MemoryProviderDefinition")


@_attrs_define(repr=False)
class MemoryProviderDefinition:
    """
    Attributes:
        configuration_schema (MemoryProviderDefinitionConfigurationSchema):
        credential_schema (MemoryProviderDefinitionCredentialSchema):
        display_name (str):
        type_ (str):
        requires_credential (bool | Unset):
        supports_changes (bool | Unset):
        supports_documents (bool | Unset):
        supports_records (bool | Unset):
        supports_revisions (bool | Unset):
    """

    configuration_schema: MemoryProviderDefinitionConfigurationSchema
    credential_schema: MemoryProviderDefinitionCredentialSchema
    display_name: str
    type_: str
    requires_credential: bool | Unset = UNSET
    supports_changes: bool | Unset = UNSET
    supports_documents: bool | Unset = UNSET
    supports_records: bool | Unset = UNSET
    supports_revisions: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        configuration_schema = self.configuration_schema.to_dict()

        credential_schema = self.credential_schema.to_dict()

        display_name = self.display_name

        type_ = self.type_

        requires_credential = self.requires_credential

        supports_changes = self.supports_changes

        supports_documents = self.supports_documents

        supports_records = self.supports_records

        supports_revisions = self.supports_revisions

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "configuration_schema": configuration_schema,
                "credential_schema": credential_schema,
                "display_name": display_name,
                "type": type_,
            }
        )
        if requires_credential is not UNSET:
            field_dict["requires_credential"] = requires_credential
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
        from ..models.memory_provider_definition_configuration_schema import (
            MemoryProviderDefinitionConfigurationSchema,
        )
        from ..models.memory_provider_definition_credential_schema import (
            MemoryProviderDefinitionCredentialSchema,
        )

        d = dict(src_dict)
        configuration_schema = MemoryProviderDefinitionConfigurationSchema.from_dict(d.pop("configuration_schema"))

        credential_schema = MemoryProviderDefinitionCredentialSchema.from_dict(d.pop("credential_schema"))

        display_name = d.pop("display_name")

        type_ = d.pop("type")

        requires_credential = d.pop("requires_credential", UNSET)

        supports_changes = d.pop("supports_changes", UNSET)

        supports_documents = d.pop("supports_documents", UNSET)

        supports_records = d.pop("supports_records", UNSET)

        supports_revisions = d.pop("supports_revisions", UNSET)

        memory_provider_definition = cls(
            configuration_schema=configuration_schema,
            credential_schema=credential_schema,
            display_name=display_name,
            type_=type_,
            requires_credential=requires_credential,
            supports_changes=supports_changes,
            supports_documents=supports_documents,
            supports_records=supports_records,
            supports_revisions=supports_revisions,
        )

        return memory_provider_definition
