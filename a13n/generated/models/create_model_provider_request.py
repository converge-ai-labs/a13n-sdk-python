from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_model_provider_request_configuration import CreateModelProviderRequestConfiguration
    from ..models.create_model_provider_request_credential_type_0 import CreateModelProviderRequestCredentialType0
    from ..models.create_model_provider_request_extra_headers import CreateModelProviderRequestExtraHeaders


T = TypeVar("T", bound="CreateModelProviderRequest")


@_attrs_define(repr=False)
class CreateModelProviderRequest:
    """
    Attributes:
        name (str):
        type_ (str):
        configuration (CreateModelProviderRequestConfiguration | Unset):
        credential (CreateModelProviderRequestCredentialType0 | None | Unset):
        enabled (bool | Unset):
        extra_headers (CreateModelProviderRequestExtraHeaders | Unset):
    """

    name: str
    type_: str
    configuration: CreateModelProviderRequestConfiguration | Unset = UNSET
    credential: CreateModelProviderRequestCredentialType0 | Unset | None = UNSET
    enabled: bool | Unset = UNSET
    extra_headers: CreateModelProviderRequestExtraHeaders | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_model_provider_request_credential_type_0 import CreateModelProviderRequestCredentialType0

        name = self.name

        type_ = self.type_

        configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = self.configuration.to_dict()

        credential: dict[str, Any] | Unset | None
        if isinstance(self.credential, Unset):
            credential = UNSET
        elif isinstance(self.credential, CreateModelProviderRequestCredentialType0):
            credential = self.credential.to_dict()
        else:
            credential = self.credential

        enabled = self.enabled

        extra_headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extra_headers, Unset):
            extra_headers = self.extra_headers.to_dict()

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
        if extra_headers is not UNSET:
            field_dict["extra_headers"] = extra_headers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_model_provider_request_configuration import (
            CreateModelProviderRequestConfiguration,
        )
        from ..models.create_model_provider_request_credential_type_0 import (
            CreateModelProviderRequestCredentialType0,
        )
        from ..models.create_model_provider_request_extra_headers import (
            CreateModelProviderRequestExtraHeaders,
        )

        d = dict(src_dict)
        name = d.pop("name")

        type_ = d.pop("type")

        _configuration = d.pop("configuration", UNSET)
        configuration: CreateModelProviderRequestConfiguration | Unset
        if isinstance(_configuration, Unset):
            configuration = UNSET
        else:
            configuration = CreateModelProviderRequestConfiguration.from_dict(_configuration)

        def _parse_credential(data: object) -> CreateModelProviderRequestCredentialType0 | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                credential_type_0 = CreateModelProviderRequestCredentialType0.from_dict(data)

                return credential_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateModelProviderRequestCredentialType0 | Unset | None, data)

        credential = _parse_credential(d.pop("credential", UNSET))

        enabled = d.pop("enabled", UNSET)

        _extra_headers = d.pop("extra_headers", UNSET)
        extra_headers: CreateModelProviderRequestExtraHeaders | Unset
        if isinstance(_extra_headers, Unset):
            extra_headers = UNSET
        else:
            extra_headers = CreateModelProviderRequestExtraHeaders.from_dict(_extra_headers)

        create_model_provider_request = cls(
            name=name,
            type_=type_,
            configuration=configuration,
            credential=credential,
            enabled=enabled,
            extra_headers=extra_headers,
        )

        return create_model_provider_request
