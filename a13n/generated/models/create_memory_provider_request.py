from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_memory_provider_request_configuration import CreateMemoryProviderRequestConfiguration
    from ..models.create_memory_provider_request_credential_type_0 import CreateMemoryProviderRequestCredentialType0


T = TypeVar("T", bound="CreateMemoryProviderRequest")


@_attrs_define(repr=False)
class CreateMemoryProviderRequest:
    """
    Attributes:
        name (str):
        type_ (str):
        configuration (CreateMemoryProviderRequestConfiguration | Unset):
        credential (CreateMemoryProviderRequestCredentialType0 | None | Unset):
        enabled (bool | Unset):
    """

    name: str
    type_: str
    configuration: CreateMemoryProviderRequestConfiguration | Unset = UNSET
    credential: CreateMemoryProviderRequestCredentialType0 | Unset | None = UNSET
    enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_memory_provider_request_credential_type_0 import CreateMemoryProviderRequestCredentialType0

        name = self.name

        type_ = self.type_

        configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = self.configuration.to_dict()

        credential: dict[str, Any] | Unset | None
        if isinstance(self.credential, Unset):
            credential = UNSET
        elif isinstance(self.credential, CreateMemoryProviderRequestCredentialType0):
            credential = self.credential.to_dict()
        else:
            credential = self.credential

        enabled = self.enabled

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "type": type_,
            }
        )
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if credential is not UNSET:
            field_dict["credential"] = credential
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_memory_provider_request_configuration import (
            CreateMemoryProviderRequestConfiguration,
        )
        from ..models.create_memory_provider_request_credential_type_0 import (
            CreateMemoryProviderRequestCredentialType0,
        )

        d = dict(src_dict)
        name = d.pop("name")

        type_ = d.pop("type")

        _configuration = d.pop("configuration", UNSET)
        configuration: CreateMemoryProviderRequestConfiguration | Unset
        if isinstance(_configuration, Unset):
            configuration = UNSET
        else:
            configuration = CreateMemoryProviderRequestConfiguration.from_dict(_configuration)

        def _parse_credential(data: object) -> CreateMemoryProviderRequestCredentialType0 | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                credential_type_0 = CreateMemoryProviderRequestCredentialType0.from_dict(data)

                return credential_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateMemoryProviderRequestCredentialType0 | Unset | None, data)

        credential = _parse_credential(d.pop("credential", UNSET))

        enabled = d.pop("enabled", UNSET)

        create_memory_provider_request = cls(
            name=name,
            type_=type_,
            configuration=configuration,
            credential=credential,
            enabled=enabled,
        )

        return create_memory_provider_request
