from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_memory_provider_request_configuration import CreateMemoryProviderRequestConfiguration
    from ..models.create_memory_provider_request_credential import CreateMemoryProviderRequestCredential


T = TypeVar("T", bound="CreateMemoryProviderRequest")


@_attrs_define(repr=False)
class CreateMemoryProviderRequest:
    """
    Attributes:
        name (str):
        type_ (str):
        configuration (CreateMemoryProviderRequestConfiguration | Unset):
        credential (CreateMemoryProviderRequestCredential | Unset):
        enabled (bool | Unset):
    """

    name: str
    type_: str
    configuration: CreateMemoryProviderRequestConfiguration | Unset = UNSET
    credential: CreateMemoryProviderRequestCredential | Unset = UNSET
    enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_

        configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = self.configuration.to_dict()

        credential: dict[str, Any] | Unset = UNSET
        if not isinstance(self.credential, Unset):
            credential = self.credential.to_dict()

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
        from ..models.create_memory_provider_request_credential import (
            CreateMemoryProviderRequestCredential,
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

        _credential = d.pop("credential", UNSET)
        credential: CreateMemoryProviderRequestCredential | Unset
        if isinstance(_credential, Unset):
            credential = UNSET
        else:
            credential = CreateMemoryProviderRequestCredential.from_dict(_credential)

        enabled = d.pop("enabled", UNSET)

        create_memory_provider_request = cls(
            name=name,
            type_=type_,
            configuration=configuration,
            credential=credential,
            enabled=enabled,
        )

        return create_memory_provider_request
